#!/usr/bin/env python3
"""
CI Architecture Analyzer - Generic GitHub Actions CI/CD Analysis Tool

Analyzes GitHub Actions workflows and generates comprehensive ASCII architecture diagrams
for any project using GitHub Actions.

Enhanced with:
- Dependency graph building
- Call chain tracking (workflow -> workflow -> action)
- Script content analysis
- Nested relationship visualization
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Any, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass, field


@dataclass
class CallRelationship:
    """Represents a call relationship between components."""
    caller: str  # Caller component (workflow/job)
    callee: str  # Called component (workflow/action)
    call_type: str  # 'workflow_call', 'uses', 'action'
    job_name: Optional[str] = None  # Job name if caller is a workflow


@dataclass
class DependencyGraph:
    """Dependency graph for CI/CD components."""
    workflow_calls: Dict[str, List[CallRelationship]] = field(default_factory=dict)
    job_dependencies: Dict[str, List[str]] = field(default_factory=dict)
    action_usages: Dict[str, List[str]] = field(default_factory=dict)
    
    def add_workflow_call(self, workflow: str, relationship: CallRelationship):
        if workflow not in self.workflow_calls:
            self.workflow_calls[workflow] = []
        self.workflow_calls[workflow].append(relationship)
    
    def add_job_dependency(self, workflow: str, job: str, depends_on: List[str]):
        key = f"{workflow}::{job}"
        self.job_dependencies[key] = depends_on
    
    def add_action_usage(self, action: str, used_by: str):
        if action not in self.action_usages:
            self.action_usages[action] = []
        if used_by not in self.action_usages[action]:
            self.action_usages[action].append(used_by)


@dataclass
class ScriptAnalysis:
    """Analysis result for a script file."""
    name: str
    path: str
    script_type: str
    functions: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    called_scripts: List[str] = field(default_factory=list)
    ci_keywords: List[str] = field(default_factory=list)
    description: str = ""


def find_ci_directories(repo_path: str) -> Dict[str, Path]:
    """Find all CI-related directories in the repository."""
    repo = Path(repo_path)
    
    # Common CI directory patterns
    ci_dir_patterns = [
        ".github/workflows",
        ".github/actions", 
        ".ci",
        ".circleci",
        "ci",
        "scripts",
        "test",
        "tests",
    ]
    
    found = {}
    for pattern in ci_dir_patterns:
        path = repo / pattern
        if path.exists():
            found[pattern.replace("/", "_").replace(".", "")] = path
    
    found["repo_name"] = repo.name
    found["repo_path"] = repo
    return found


def parse_workflow_file(filepath: Path) -> Dict:
    """Parse a GitHub Actions workflow file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Parse YAML
        wf_data = yaml.safe_load(content)
        if not wf_data:
            return {}
        
        # Handle 'on' as True (YAML keyword)
        if True in wf_data and "on" not in wf_data:
            wf_data["on"] = wf_data.pop(True)
        
        return wf_data
    except Exception as e:
        return {}


def extract_triggers(wf_data: Dict) -> List[str]:
    """Extract trigger events from workflow data."""
    triggers = []
    on_config = wf_data.get("on", {})
    
    if isinstance(on_config, str):
        triggers = [on_config]
    elif isinstance(on_config, list):
        triggers = on_config
    elif isinstance(on_config, dict):
        triggers = list(on_config.keys())
    
    return triggers


def extract_jobs(wf_data: Dict, workflow_name: str = "", dep_graph: DependencyGraph = None) -> Dict[str, Dict]:
    """Extract job information from workflow data."""
    jobs = {}
    
    for job_name, job_data in (wf_data.get("jobs", {}) or {}).items():
        if not isinstance(job_data, dict):
            continue
            
        job_info = {
            "name": job_name,
            "runs_on": job_data.get("runs-on", ""),
            "needs": job_data.get("needs", []),
            "uses": job_data.get("uses", ""),
            "steps_count": len(job_data.get("steps", [])),
            "if_condition": job_data.get("if", ""),
            "matrix": None,
            "calls_workflows": [],
            "calls_actions": [],
        }
        
        # Extract matrix strategy
        strategy = job_data.get("strategy", {})
        if isinstance(strategy, dict):
            matrix = strategy.get("matrix", {})
            if matrix:
                job_info["matrix"] = matrix
        
        # Extract environment variables
        env = job_data.get("env", {})
        if env:
            job_info["env_vars"] = list(env.keys()) if isinstance(env, dict) else []
        
        # Extract workflow calls (uses: ./.github/workflows/xxx.yml)
        uses = job_data.get("uses", "")
        if uses:
            if uses.startswith("./.github/workflows/") or uses.startswith(".github/workflows/"):
                # Local workflow call
                called_wf = Path(uses).name
                job_info["calls_workflows"].append(called_wf)
                if dep_graph:
                    rel = CallRelationship(
                        caller=workflow_name,
                        callee=called_wf,
                        call_type="workflow_call",
                        job_name=job_name
                    )
                    dep_graph.add_workflow_call(workflow_name, rel)
            elif "/" in uses and not uses.startswith("./"):
                # External action or reusable workflow
                if ".yml" in uses or ".yaml" in uses:
                    # External reusable workflow
                    job_info["calls_workflows"].append(uses)
                else:
                    # External action
                    job_info["calls_actions"].append(uses)
                    if dep_graph:
                        dep_graph.add_action_usage(uses, f"{workflow_name}::{job_name}")
        
        # Extract action calls from steps
        steps = job_data.get("steps", [])
        for step in steps:
            if isinstance(step, dict):
                step_uses = step.get("uses", "")
                if step_uses:
                    if step_uses.startswith("./.github/actions/"):
                        # Local composite action
                        action_name = step_uses.replace("./.github/actions/", "").split("/")[0]
                        job_info["calls_actions"].append(f"local:{action_name}")
                        if dep_graph:
                            dep_graph.add_action_usage(f"local:{action_name}", f"{workflow_name}::{job_name}")
                    elif step_uses.startswith("pytorch/pytorch/.github/actions/"):
                        # PyTorch local action reference
                        action_name = step_uses.split("/.github/actions/")[1].split("/")[0]
                        job_info["calls_actions"].append(f"pytorch:{action_name}")
                    elif "/" in step_uses and not step_uses.startswith("./"):
                        # External action
                        job_info["calls_actions"].append(step_uses)
                        if dep_graph:
                            dep_graph.add_action_usage(step_uses, f"{workflow_name}::{job_name}")
        
        # Record job dependencies
        if dep_graph and job_info["needs"]:
            needs_list = job_info["needs"] if isinstance(job_info["needs"], list) else [job_info["needs"]]
            dep_graph.add_job_dependency(workflow_name, job_name, needs_list)
        
        jobs[job_name] = job_info
    
    return jobs


def analyze_workflow(filepath: Path, dep_graph: DependencyGraph = None) -> Dict:
    """Analyze a single workflow file."""
    wf_data = parse_workflow_file(filepath)
    
    if not wf_data:
        return {}
    
    name = wf_data.get("name", filepath.stem)
    triggers = extract_triggers(wf_data)
    jobs = extract_jobs(wf_data, filepath.name, dep_graph)
    
    # Determine workflow type
    filename = filepath.name.lower()
    is_reusable = filename.startswith("_")
    is_generated = "generated" in filename
    
    # Categorize workflow
    category = categorize_workflow(name, filename, triggers)
    
    # Check if this is a reusable workflow (has workflow_call trigger)
    is_reusable_by_trigger = "workflow_call" in triggers
    
    return {
        "filename": filepath.name,
        "name": name,
        "triggers": triggers,
        "jobs": jobs,
        "is_reusable": is_reusable or is_reusable_by_trigger,
        "is_generated": is_generated,
        "category": category,
        "callers": [],  # Will be populated by build_call_relationships
    }


def categorize_workflow(name: str, filename: str, triggers: List[str]) -> str:
    """Categorize workflow by its purpose."""
    name_lower = name.lower()
    filename_lower = filename.lower()
    
    # Check by filename/name patterns
    if "pull" in filename_lower or "pr" in filename_lower:
        return "pull_ci"
    if "trunk" in filename_lower or "main" in filename_lower:
        return "trunk_ci"
    if any(x in filename_lower for x in ["periodic", "nightly", "daily", "weekly", "cron"]):
        return "periodic"
    if "lint" in filename_lower or "format" in filename_lower:
        return "lint"
    if "test" in filename_lower:
        return "test"
    if "build" in filename_lower:
        return "build"
    if any(x in filename_lower for x in ["release", "publish", "deploy"]):
        return "release"
    if any(x in filename_lower for x in ["docker", "container", "image"]):
        return "container"
    if any(x in filename_lower for x in ["benchmark", "perf"]):
        return "performance"
    if any(x in filename_lower for x in ["security", "scan", "sast"]):
        return "security"
    
    # Check by triggers
    if "schedule" in triggers and "pull_request" not in triggers:
        return "periodic"
    if "workflow_call" in triggers:
        return "reusable"
    if "workflow_dispatch" in triggers and len(triggers) == 1:
        return "manual"
    
    return "other"


def analyze_composite_action(action_dir: Path) -> Dict:
    """Analyze a composite action directory."""
    action_file = action_dir / "action.yml"
    if not action_file.exists():
        action_file = action_dir / "action.yaml"
    
    if not action_file.exists():
        return {}
    
    try:
        with open(action_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        
        # Categorize action
        name = action_dir.name.lower()
        if "setup" in name:
            category = "setup"
        elif "teardown" in name or "cleanup" in name:
            category = "teardown"
        elif "download" in name or "upload" in name or "artifact" in name:
            category = "artifacts"
        elif "test" in name:
            category = "testing"
        elif "build" in name:
            category = "build"
        elif "cache" in name:
            category = "caching"
        else:
            category = "utility"
        
        # Extract called actions from steps
        called_actions = []
        runs = data.get("runs", {})
        if isinstance(runs, dict):
            steps = runs.get("steps", [])
            for step in steps:
                if isinstance(step, dict):
                    step_uses = step.get("uses", "")
                    if step_uses:
                        called_actions.append(step_uses)
        
        return {
            "name": action_dir.name,
            "description": data.get("description", ""),
            "category": category,
            "inputs": list((data.get("inputs", {}) or {}).keys()),
            "outputs": list((data.get("outputs", {}) or {}).keys()),
            "called_actions": called_actions,
            "used_by": [],  # Will be populated by build_call_relationships
        }
    except:
        return {}


def analyze_script_content(filepath: Path) -> ScriptAnalysis:
    """Analyze a script file to extract its functionality."""
    analysis = ScriptAnalysis(
        name=filepath.name,
        path=str(filepath),
        script_type=filepath.suffix
    )
    
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        if filepath.suffix == ".py":
            # Python script analysis
            # Extract function definitions
            func_pattern = r'^def\s+(\w+)\s*\('
            analysis.functions = re.findall(func_pattern, content, re.MULTILINE)
            
            # Extract imports
            import_pattern = r'^(?:from\s+(\S+)\s+import|import\s+(\S+))'
            imports = re.findall(import_pattern, content, re.MULTILINE)
            analysis.imports = [imp[0] or imp[1] for imp in imports]
            
            # Extract script calls
            call_pattern = r'(?:subprocess|os\.system|os\.popen)\s*[\(\[].*?["\']([^"\']+)["\']'
            analysis.called_scripts = re.findall(call_pattern, content)
            
            # CI keywords
            ci_keywords = ["build", "test", "deploy", "docker", "pytest", "unittest", 
                          "cmake", "ninja", "pip", "conda", "aws", "s3", "artifact",
                          "coverage", "lint", "format", "benchmark"]
            found_keywords = []
            content_lower = content.lower()
            for kw in ci_keywords:
                if kw in content_lower:
                    found_keywords.append(kw)
            analysis.ci_keywords = found_keywords
            
            # Generate description
            if analysis.functions:
                analysis.description = f"Python script with functions: {', '.join(analysis.functions[:5])}"
            else:
                analysis.description = "Python script"
                
        elif filepath.suffix == ".sh":
            # Shell script analysis
            # Extract function definitions
            func_pattern = r'^(?:function\s+)?(\w+)\s*\(\s*\)\s*\{'
            analysis.functions = re.findall(func_pattern, content, re.MULTILINE)
            
            # Extract script calls
            call_pattern = r'(?:source|\.)\s+([^\s;&|]+)|(?:bash|sh|python)\s+([^\s;&|]+)'
            calls = re.findall(call_pattern, content)
            analysis.called_scripts = [c[0] or c[1] for c in calls if c[0] or c[1]]
            
            # CI keywords
            ci_keywords = ["build", "test", "deploy", "docker", "cmake", "ninja",
                          "pip", "conda", "aws", "s3", "artifact", "coverage"]
            found_keywords = []
            content_lower = content.lower()
            for kw in ci_keywords:
                if kw in content_lower:
                    found_keywords.append(kw)
            analysis.ci_keywords = found_keywords
            
            # Generate description
            if analysis.functions:
                analysis.description = f"Shell script with functions: {', '.join(analysis.functions[:5])}"
            else:
                analysis.description = "Shell script"
        
        elif filepath.suffix in [".ps1", ".bat"]:
            # Windows script
            ci_keywords = ["build", "test", "deploy", "docker", "cmake"]
            found_keywords = []
            content_lower = content.lower()
            for kw in ci_keywords:
                if kw in content_lower:
                    found_keywords.append(kw)
            analysis.ci_keywords = found_keywords
            analysis.description = f"Windows {filepath.suffix} script"
    
    except Exception as e:
        analysis.description = f"Could not analyze: {str(e)}"
    
    return analysis


def find_ci_scripts(ci_dirs: Dict[str, Path]) -> List[ScriptAnalysis]:
    """Find and analyze CI-related scripts."""
    scripts = []
    seen = set()
    
    for key, path in ci_dirs.items():
        if not isinstance(path, Path) or not path.exists():
            continue
        
        # Find shell scripts
        for ext in ["*.sh", "*.py", "*.ps1", "*.bat"]:
            for f in path.rglob(ext):
                if f.name not in seen:
                    seen.add(f.name)
                    analysis = analyze_script_content(f)
                    scripts.append(analysis)
    
    return scripts[:50]  # Limit to 50 scripts


def extract_runner_types(workflows: Dict[str, Dict]) -> Dict[str, int]:
    """Extract runner types used across workflows."""
    runners = defaultdict(int)
    
    for wf_name, wf_data in workflows.items():
        for job_name, job_data in wf_data.get("jobs", {}).items():
            runs_on = job_data.get("runs_on", "")
            if runs_on:
                if isinstance(runs_on, str):
                    runners[runs_on] += 1
                elif isinstance(runs_on, list):
                    for r in runs_on:
                        runners[str(r)] += 1
    
    return dict(runners)


def extract_test_configs(workflows: Dict[str, Dict]) -> List[Dict]:
    """Extract test configurations from workflow matrices."""
    configs = []
    seen = set()
    
    for wf_name, wf_data in workflows.items():
        for job_name, job_data in wf_data.get("jobs", {}).items():
            matrix = job_data.get("matrix", {})
            if not matrix:
                continue
            
            # Extract config names from matrix
            include = matrix.get("include", [])
            if isinstance(include, list):
                for item in include:
                    if isinstance(item, dict):
                        # Look for common config keys
                        for key in ["config", "test_config", "test_type", "suite", "category"]:
                            if key in item:
                                config_val = str(item[key])
                                if config_val not in seen:
                                    seen.add(config_val)
                                    configs.append({
                                        "name": config_val,
                                        "workflow": wf_name,
                                        "job": job_name,
                                    })
    
    return configs


def build_call_relationships(workflows: Dict, actions: List[Dict], dep_graph: DependencyGraph) -> None:
    """Build call relationships between workflows and actions."""
    # Build a map of callers for each workflow
    for wf_name, wf_data in workflows.items():
        for job_name, job_data in wf_data.get("jobs", {}).items():
            # Check for workflow calls
            for called_wf in job_data.get("calls_workflows", []):
                # Find the actual workflow file name
                target_wf = called_wf if called_wf in workflows else None
                if target_wf and target_wf not in workflows[wf_name].get("callers", []):
                    if "callers" not in workflows[target_wf]:
                        workflows[target_wf]["callers"] = []
                    workflows[target_wf]["callers"].append(f"{wf_name}::{job_name}")
    
    # Build used_by relationships for actions
    action_map = {f"local:{a['name']}": a for a in actions}
    
    for wf_name, wf_data in workflows.items():
        for job_name, job_data in wf_data.get("jobs", {}).items():
            for called_action in job_data.get("calls_actions", []):
                if called_action.startswith("local:"):
                    action_name = called_action
                    if action_name in action_map:
                        if "used_by" not in action_map[action_name]:
                            action_map[action_name]["used_by"] = []
                        action_map[action_name]["used_by"].append(f"{wf_name}::{job_name}")


def build_nested_call_chain(workflows: Dict, start_wf: str, visited: Set[str] = None, depth: int = 0) -> List[List[str]]:
    """Build nested call chains starting from a workflow."""
    if visited is None:
        visited = set()
    
    if start_wf not in workflows or start_wf in visited or depth > 5:
        return []
    
    visited.add(start_wf)
    chains = []
    wf_data = workflows[start_wf]
    
    for job_name, job_data in wf_data.get("jobs", {}).items():
        # Workflow calls
        for called_wf in job_data.get("calls_workflows", []):
            target_wf = called_wf if called_wf in workflows else None
            if target_wf:
                chain = [f"{start_wf}::{job_name}", target_wf]
                sub_chains = build_nested_call_chain(workflows, target_wf, visited.copy(), depth + 1)
                if sub_chains:
                    for sub_chain in sub_chains:
                        chains.append(chain + sub_chain[1:])
                else:
                    chains.append(chain)
    
    return chains


def generate_dependency_diagram(workflows: Dict, actions: List[Dict], dep_graph: DependencyGraph) -> List[str]:
    """Generate dependency diagram showing call relationships."""
    lines = []
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " WORKFLOW CALL RELATIONSHIPS (Nested)".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    # Find entry workflows (not called by other workflows)
    entry_workflows = []
    for wf_name, wf_data in workflows.items():
        if not wf_data.get("callers") and not wf_data.get("is_reusable"):
            entry_workflows.append(wf_name)
    
    # Build call chains for entry workflows
    for wf_name in sorted(entry_workflows)[:10]:
        chains = build_nested_call_chain(workflows, wf_name)
        if chains:
            lines.append(f"│  📌 {wf_name}:".ljust(98) + "│")
            for chain in chains[:3]:  # Limit chains per workflow
                chain_str = " → ".join(chain[:5])  # Limit chain depth display
                if len(chain_str) > 80:
                    chain_str = chain_str[:77] + "..."
                lines.append(f"│      {chain_str}".ljust(98) + "│")
    
    # Show reusable workflows and their callers
    reusable_workflows = [(n, d) for n, d in workflows.items() if d.get("is_reusable")]
    if reusable_workflows:
        lines.append("│".ljust(98) + "│")
        lines.append("│  🔄 Reusable Workflows:".ljust(98) + "│")
        for wf_name, wf_data in reusable_workflows[:8]:
            callers = wf_data.get("callers", [])
            if callers:
                callers_str = ", ".join(callers[:3])
                if len(callers) > 3:
                    callers_str += f" (+{len(callers)-3} more)"
                line = f"│    • {wf_name:<30} ← called by: {callers_str}"
                lines.append(line[:97] + "│")
            else:
                lines.append(f"│    • {wf_name:<30} (no callers found)".ljust(98) + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    
    return lines


def generate_action_usage_diagram(workflows: Dict, actions: List[Dict], dep_graph: DependencyGraph) -> List[str]:
    """Generate diagram showing action usage relationships."""
    lines = []
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " ACTION USAGE RELATIONSHIPS".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    # Local actions
    local_actions = [a for a in actions if a.get("used_by")]
    if local_actions:
        lines.append("│  📦 Local Composite Actions:".ljust(98) + "│")
        for action in local_actions[:8]:
            used_by = action.get("used_by", [])
            if used_by:
                used_by_str = ", ".join(used_by[:2])
                if len(used_by) > 2:
                    used_by_str += f" (+{len(used_by)-2} more)"
                line = f"│    • {action['name']:<25} → used by: {used_by_str}"
                lines.append(line[:97] + "│")
    
    # External actions
    external_actions = defaultdict(list)
    for wf_name, wf_data in workflows.items():
        for job_name, job_data in wf_data.get("jobs", {}).items():
            for called_action in job_data.get("calls_actions", []):
                if not called_action.startswith("local:") and not called_action.startswith("pytorch:"):
                    external_actions[called_action].append(f"{wf_name}::{job_name}")
    
    if external_actions:
        lines.append("│".ljust(98) + "│")
        lines.append("│  🌐 External Actions:".ljust(98) + "│")
        # Sort by usage count
        sorted_actions = sorted(external_actions.items(), key=lambda x: -len(x[1]))[:10]
        for action, users in sorted_actions:
            action_short = action.split("@")[0] if "@" in action else action
            if len(action_short) > 35:
                action_short = action_short[:32] + "..."
            users_count = len(users)
            line = f"│    • {action_short:<35} ({users_count} uses)"
            lines.append(line[:97] + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    
    return lines


def generate_job_dependency_diagram(workflows: Dict, dep_graph: DependencyGraph) -> List[str]:
    """Generate job dependency diagram."""
    lines = []
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " JOB DEPENDENCIES (needs)".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    # Group by workflow
    wf_job_deps = defaultdict(list)
    for key, deps in dep_graph.job_dependencies.items():
        wf_name = key.split("::")[0]
        job_name = key.split("::")[1] if "::" in key else ""
        wf_job_deps[wf_name].append((job_name, deps))
    
    for wf_name in sorted(wf_job_deps.keys())[:8]:
        jobs = wf_job_deps[wf_name]
        lines.append(f"│  📋 {wf_name}:".ljust(98) + "│")
        for job_name, deps in jobs[:5]:
            deps_str = " → ".join(deps) if isinstance(deps, list) else str(deps)
            line = f"│      {job_name:<25} depends on: {deps_str}"
            lines.append(line[:97] + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    
    return lines


def generate_script_analysis_diagram(scripts: List[ScriptAnalysis]) -> List[str]:
    """Generate script analysis diagram."""
    lines = []
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " CI SCRIPTS ANALYSIS".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    # Group by script type
    py_scripts = [s for s in scripts if s.script_type == ".py"]
    sh_scripts = [s for s in scripts if s.script_type == ".sh"]
    other_scripts = [s for s in scripts if s.script_type not in [".py", ".sh"]]
    
    if py_scripts:
        lines.append("│  🐍 Python Scripts:".ljust(98) + "│")
        for script in py_scripts[:5]:
            desc = script.description[:60] if script.description else script.name
            kw = f" [{', '.join(script.ci_keywords[:3])}]" if script.ci_keywords else ""
            line = f"│    • {script.name:<25} - {desc}{kw}"
            lines.append(line[:97] + "│")
    
    if sh_scripts:
        lines.append("│".ljust(98) + "│")
        lines.append("│  🐚 Shell Scripts:".ljust(98) + "│")
        for script in sh_scripts[:5]:
            desc = script.description[:60] if script.description else script.name
            kw = f" [{', '.join(script.ci_keywords[:3])}]" if script.ci_keywords else ""
            line = f"│    • {script.name:<25} - {desc}{kw}"
            lines.append(line[:97] + "│")
    
    if other_scripts:
        lines.append("│".ljust(98) + "│")
        lines.append("│  📄 Other Scripts:".ljust(98) + "│")
        for script in other_scripts[:5]:
            line = f"│    • {script.name:<25} - {script.description[:50]}"
            lines.append(line[:97] + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    
    return lines


def generate_architecture_diagram(
    repo_name: str,
    workflows: Dict,
    actions: List[Dict],
    scripts: List[ScriptAnalysis],
    runners: Dict[str, int],
    test_configs: List[Dict],
    dep_graph: DependencyGraph,
    output_file: str,
) -> str:
    """Generate ASCII architecture diagram with enhanced relationships."""
    
    lines = []
    
    # Helper to create box lines
    def box_line(content="", width=97):
        return f"│ {content:<{width-2}}│"
    
    # Header
    lines.append("```")
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + f" {repo_name.upper()} CI/CD ARCHITECTURE".center(97) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("")
    
    # 1. TRIGGER SOURCES
    all_triggers = set()
    for wf in workflows.values():
        all_triggers.update(wf.get("triggers", []))
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " TRIGGER SOURCES".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    trigger_descriptions = {
        "pull_request": "Triggered on pull request events",
        "push": "Triggered on push events",
        "schedule": "Triggered on schedule (cron)",
        "workflow_dispatch": "Manual trigger",
        "workflow_call": "Called by other workflows",
        "release": "Triggered on release events",
        "workflow_run": "Triggered by another workflow run",
    }
    
    for t in sorted(all_triggers):
        desc = trigger_descriptions.get(t, "")
        if desc:
            lines.append(f"│  • {t:<18} - {desc:<62}│")
        else:
            lines.append(f"│  • {t:<83}│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 2. WORKFLOW CATEGORIES
    categorized = defaultdict(list)
    for wf_name, wf_data in workflows.items():
        if not wf_data.get("is_reusable"):
            categorized[wf_data.get("category", "other")].append((wf_name, wf_data))
    
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " MAIN WORKFLOWS".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    category_icons = {
        "pull_ci": "🔄",
        "trunk_ci": "📦",
        "periodic": "⏰",
        "lint": "🔍",
        "test": "🧪",
        "build": "🔨",
        "release": "🚀",
        "container": "🐳",
        "performance": "📊",
        "security": "🔒",
        "reusable": "♻️",
        "manual": "👆",
        "other": "📄",
    }
    
    for cat, wfs in categorized.items():
        if wfs:
            icon = category_icons.get(cat, "📄")
            lines.append(f"│  {icon} [{cat.upper()}] ({len(wfs)} workflows)".ljust(98) + "│")
            for wf_name, wf_data in wfs[:4]:
                triggers = ", ".join(wf_data.get("triggers", []))[:40]
                jobs_count = len(wf_data.get("jobs", {}))
                callers_count = len(wf_data.get("callers", []))
                caller_info = f", called by {callers_count}" if callers_count else ""
                lines.append(f"│      • {wf_name:<30} ({jobs_count} jobs{caller_info})"[:97] + "│")
            lines.append("│" + " " * 97 + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 3. WORKFLOW CALL RELATIONSHIPS (NEW)
    dep_lines = generate_dependency_diagram(workflows, actions, dep_graph)
    lines.extend(dep_lines)
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 4. REUSABLE WORKFLOWS
    reusable = [(n, d) for n, d in workflows.items() if d.get("is_reusable")]
    
    if reusable:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " REUSABLE WORKFLOWS".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        for wf_name, wf_data in reusable[:8]:
            jobs_count = len(wf_data.get("jobs", {}))
            jobs = list(wf_data.get("jobs", {}).keys())[:3]
            callers = wf_data.get("callers", [])
            callers_info = f" ← {len(callers)} callers" if callers else ""
            lines.append(f"│  📦 {wf_name:<40} ({jobs_count} jobs){callers_info}".ljust(98) + "│")
            for job in jobs:
                job_data = wf_data.get("jobs", {}).get(job, {})
                calls_wf = job_data.get("calls_workflows", [])
                calls_info = f" → {calls_wf[0]}" if calls_wf else ""
                lines.append(f"│      └─ {job:<50}{calls_info}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 5. JOB DEPENDENCIES (NEW)
    job_dep_lines = generate_job_dependency_diagram(workflows, dep_graph)
    lines.extend(job_dep_lines)
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 6. ACTION USAGE RELATIONSHIPS (NEW)
    action_lines = generate_action_usage_diagram(workflows, actions, dep_graph)
    lines.extend(action_lines)
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 7. COMPOSITE ACTIONS
    if actions:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " COMPOSITE ACTIONS".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        action_categories = defaultdict(list)
        for action in actions:
            action_categories[action.get("category", "utility")].append(action)
        
        # Setup actions
        setup_actions = action_categories.get("setup", [])
        if setup_actions:
            lines.append("│  Setup Actions:".ljust(98) + "│")
            for a in setup_actions[:5]:
                used_by = a.get("used_by", [])
                usage = f" ({len(used_by)} uses)" if used_by else ""
                lines.append(f"│    • {a['name']:<50}{usage}".ljust(98) + "│")
        
        # Artifact actions
        artifact_actions = action_categories.get("artifacts", [])
        if artifact_actions:
            lines.append("│  Artifact Actions:".ljust(98) + "│")
            for a in artifact_actions[:5]:
                used_by = a.get("used_by", [])
                usage = f" ({len(used_by)} uses)" if used_by else ""
                lines.append(f"│    • {a['name']:<50}{usage}".ljust(98) + "│")
        
        # Testing actions
        testing_actions = action_categories.get("testing", [])
        if testing_actions:
            lines.append("│  Testing Actions:".ljust(98) + "│")
            for a in testing_actions[:5]:
                used_by = a.get("used_by", [])
                usage = f" ({len(used_by)} uses)" if used_by else ""
                lines.append(f"│    • {a['name']:<50}{usage}".ljust(98) + "│")
        
        # Other actions
        other_actions = [a for cat, acts in action_categories.items() 
                        for a in acts if cat not in ["setup", "artifacts", "testing"]]
        if other_actions:
            lines.append("│  Other Actions:".ljust(98) + "│")
            for a in other_actions[:5]:
                used_by = a.get("used_by", [])
                usage = f" ({len(used_by)} uses)" if used_by else ""
                lines.append(f"│    • {a['name']:<50}{usage}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 8. TEST CONFIGURATIONS
    if test_configs:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " TEST CONFIGURATIONS".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        for config in test_configs[:15]:
            lines.append(f"│    • {config['name']:<50} ({config['workflow']})".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 9. CI SCRIPTS ANALYSIS (ENHANCED)
    script_lines = generate_script_analysis_diagram(scripts)
    lines.extend(script_lines)
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 10. RUNNER TYPES
    if runners:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " RUNNER TYPES".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        sorted_runners = sorted(runners.items(), key=lambda x: -x[1])[:15]
        
        for runner, count in sorted_runners:
            # Clean up runner name
            r = runner.replace("${{", "").replace("}}", "").strip()
            
            # Determine runner type
            r_lower = r.lower()
            if "ubuntu" in r_lower or "linux" in r_lower:
                r_type = "Linux"
            elif "macos" in r_lower or "mac" in r_lower:
                r_type = "macOS"
            elif "windows" in r_lower or "win" in r_lower:
                r_type = "Windows"
            else:
                r_type = "Self-hosted"
            
            lines.append(f"│  • {r[:50]:<50} [{r_type}] ({count} jobs)".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("")
    
    # SUMMARY
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " SUMMARY".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    total_jobs = sum(len(w.get("jobs", {})) for w in workflows.values())
    total_wf_calls = sum(len(v) for v in dep_graph.workflow_calls.values())
    total_action_usages = sum(len(v) for v in dep_graph.action_usages.values())
    total_job_deps = len(dep_graph.job_dependencies)
    
    lines.append(f"│  Total Workflows: {len(workflows):<78}│")
    lines.append(f"│    • Entry Workflows: {len([w for w in workflows.values() if not w.get('is_reusable')]):<64}│")
    lines.append(f"│    • Reusable Workflows: {len([w for w in workflows.values() if w.get('is_reusable')]):<62}│")
    lines.append(f"│  Total Jobs: {total_jobs:<82}│")
    lines.append(f"│  Composite Actions: {len(actions):<71}│")
    lines.append(f"│  CI Scripts: {len(scripts):<77}│")
    lines.append(f"│  Test Configurations: {len(test_configs):<68}│")
    lines.append(f"│  Runner Types: {len(runners):<73}│")
    lines.append("│".ljust(98) + "│")
    lines.append(f"│  📊 Relationship Statistics:".ljust(98) + "│")
    lines.append(f"│    • Workflow-to-Workflow Calls: {total_wf_calls:<56}│")
    lines.append(f"│    • Action Usages: {total_action_usages:<64}│")
    lines.append(f"│    • Job Dependencies: {total_job_deps:<61}│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("```")
    
    # Write to file
    content = "\n".join(lines)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    return content


def analyze_ci_architecture(repo_path: str = None, output_file: str = None):
    """Main analysis function."""
    
    if repo_path is None:
        repo_path = os.getcwd()
    
    if output_file is None:
        output_file = "CI_ARCHITECTURE.md"
    
    repo_path = Path(repo_path).resolve()
    repo_name = repo_path.name
    
    print(f"Analyzing CI/CD architecture for: {repo_name}")
    print("=" * 60)
    
    # Initialize dependency graph
    dep_graph = DependencyGraph()
    
    # Find CI directories
    ci_dirs = find_ci_directories(str(repo_path))
    
    # Analyze workflows
    workflows_dir = ci_dirs.get("github_workflows")
    workflows = {}
    
    if workflows_dir and workflows_dir.exists():
        print(f"Found workflows directory: {workflows_dir}")
        for wf_file in workflows_dir.glob("*.yml"):
            wf_data = analyze_workflow(wf_file, dep_graph)
            if wf_data:
                workflows[wf_file.name] = wf_data
        for wf_file in workflows_dir.glob("*.yaml"):
            wf_data = analyze_workflow(wf_file, dep_graph)
            if wf_data:
                workflows[wf_file.name] = wf_data
    
    print(f"Found {len(workflows)} workflows")
    
    # Analyze composite actions
    actions_dir = ci_dirs.get("github_actions")
    actions = []
    
    if actions_dir and actions_dir.exists():
        print(f"Found actions directory: {actions_dir}")
        for action_dir in actions_dir.iterdir():
            if action_dir.is_dir():
                action_data = analyze_composite_action(action_dir)
                if action_data:
                    actions.append(action_data)
    
    print(f"Found {len(actions)} composite actions")
    
    # Build call relationships
    print("Building call relationships...")
    build_call_relationships(workflows, actions, dep_graph)
    
    # Find and analyze CI scripts
    scripts = find_ci_scripts(ci_dirs)
    print(f"Found {len(scripts)} CI scripts")
    
    # Extract runner types
    runners = extract_runner_types(workflows)
    print(f"Found {len(runners)} runner types")
    
    # Extract test configurations
    test_configs = extract_test_configs(workflows)
    print(f"Found {len(test_configs)} test configurations")
    
    # Print relationship statistics
    print(f"\nRelationship Statistics:")
    print(f"  Workflow calls: {sum(len(v) for v in dep_graph.workflow_calls.values())}")
    print(f"  Action usages: {sum(len(v) for v in dep_graph.action_usages.values())}")
    print(f"  Job dependencies: {len(dep_graph.job_dependencies)}")
    
    # Generate architecture diagram
    content = generate_architecture_diagram(
        repo_name=repo_name,
        workflows=workflows,
        actions=actions,
        scripts=scripts,
        runners=runners,
        test_configs=test_configs,
        dep_graph=dep_graph,
        output_file=output_file,
    )
    
    print(f"\nArchitecture diagram saved to: {output_file}")
    print(f"Total lines: {len(content.splitlines())}")
    
    return content


if __name__ == "__main__":
    import sys
    
    repo_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    analyze_ci_architecture(repo_path, output_file)