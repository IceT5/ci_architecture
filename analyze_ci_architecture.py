#!/usr/bin/env python3
"""
CI Architecture Analyzer - Generic GitHub Actions CI/CD Analysis Tool

Analyzes GitHub Actions workflows and generates comprehensive ASCII architecture diagrams
for any project using GitHub Actions.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Any
from collections import defaultdict


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


def extract_jobs(wf_data: Dict) -> Dict[str, Dict]:
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
        
        jobs[job_name] = job_info
    
    return jobs


def analyze_workflow(filepath: Path) -> Dict:
    """Analyze a single workflow file."""
    wf_data = parse_workflow_file(filepath)
    
    if not wf_data:
        return {}
    
    name = wf_data.get("name", filepath.stem)
    triggers = extract_triggers(wf_data)
    jobs = extract_jobs(wf_data)
    
    # Determine workflow type
    filename = filepath.name.lower()
    is_reusable = filename.startswith("_")
    is_generated = "generated" in filename
    
    # Categorize workflow
    category = categorize_workflow(name, filename, triggers)
    
    return {
        "filename": filepath.name,
        "name": name,
        "triggers": triggers,
        "jobs": jobs,
        "is_reusable": is_reusable,
        "is_generated": is_generated,
        "category": category,
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
        
        return {
            "name": action_dir.name,
            "description": data.get("description", ""),
            "category": category,
            "inputs": list((data.get("inputs", {}) or {}).keys()),
            "outputs": list((data.get("outputs", {}) or {}).keys()),
        }
    except:
        return {}


def find_ci_scripts(ci_dirs: Dict[str, Path]) -> List[Dict]:
    """Find CI-related scripts."""
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
                    scripts.append({
                        "name": f.name,
                        "path": str(f.relative_to(path.parent)) if f.parent != path else f.name,
                        "type": f.suffix,
                    })
    
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


def generate_architecture_diagram(
    repo_name: str,
    workflows: Dict,
    actions: List[Dict],
    scripts: List[Dict],
    runners: Dict[str, int],
    test_configs: List[Dict],
    output_file: str,
) -> str:
    """Generate ASCII architecture diagram."""
    
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
                lines.append(f"│      • {wf_name:<30} ({jobs_count} jobs, triggers: {triggers})"[:97] + "│")
            lines.append("│" + " " * 97 + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # 3. REUSABLE WORKFLOWS
    reusable = [(n, d) for n, d in workflows.items() if d.get("is_reusable")]
    
    if reusable:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " REUSABLE WORKFLOWS".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        for wf_name, wf_data in reusable[:8]:
            jobs_count = len(wf_data.get("jobs", {}))
            jobs = list(wf_data.get("jobs", {}).keys())[:3]
            lines.append(f"│  📦 {wf_name:<40} ({jobs_count} jobs)".ljust(98) + "│")
            for job in jobs:
                lines.append(f"│      └─ {job:<50}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 4. COMPOSITE ACTIONS
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
                lines.append(f"│    • {a['name']:<50}".ljust(98) + "│")
        
        # Artifact actions
        artifact_actions = action_categories.get("artifacts", [])
        if artifact_actions:
            lines.append("│  Artifact Actions:".ljust(98) + "│")
            for a in artifact_actions[:5]:
                lines.append(f"│    • {a['name']:<50}".ljust(98) + "│")
        
        # Testing actions
        testing_actions = action_categories.get("testing", [])
        if testing_actions:
            lines.append("│  Testing Actions:".ljust(98) + "│")
            for a in testing_actions[:5]:
                lines.append(f"│    • {a['name']:<50}".ljust(98) + "│")
        
        # Other actions
        other_actions = [a for cat, acts in action_categories.items() 
                        for a in acts if cat not in ["setup", "artifacts", "testing"]]
        if other_actions:
            lines.append("│  Other Actions:".ljust(98) + "│")
            for a in other_actions[:5]:
                lines.append(f"│    • {a['name']:<50}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 5. TEST CONFIGURATIONS
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
    
    # 6. CI SCRIPTS
    if scripts:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " CI EXECUTION SCRIPTS".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        for script in scripts[:10]:
            lines.append(f"│    • {script['name']:<50}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # 7. RUNNER TYPES
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
    
    lines.append(f"│  Total Workflows: {len(workflows):<78}│")
    lines.append(f"│    • Entry Workflows: {len([w for w in workflows.values() if not w.get('is_reusable')]):<64}│")
    lines.append(f"│    • Reusable Workflows: {len([w for w in workflows.values() if w.get('is_reusable')]):<62}│")
    lines.append(f"│  Total Jobs: {total_jobs:<82}│")
    lines.append(f"│  Composite Actions: {len(actions):<71}│")
    lines.append(f"│  CI Scripts: {len(scripts):<77}│")
    lines.append(f"│  Test Configurations: {len(test_configs):<68}│")
    lines.append(f"│  Runner Types: {len(runners):<73}│")
    
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
    
    # Find CI directories
    ci_dirs = find_ci_directories(str(repo_path))
    
    # Analyze workflows
    workflows_dir = ci_dirs.get("github_workflows")
    workflows = {}
    
    if workflows_dir and workflows_dir.exists():
        print(f"Found workflows directory: {workflows_dir}")
        for wf_file in workflows_dir.glob("*.yml"):
            wf_data = analyze_workflow(wf_file)
            if wf_data:
                workflows[wf_file.name] = wf_data
        for wf_file in workflows_dir.glob("*.yaml"):
            wf_data = analyze_workflow(wf_file)
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
    
    # Find CI scripts
    scripts = find_ci_scripts(ci_dirs)
    print(f"Found {len(scripts)} CI scripts")
    
    # Extract runner types
    runners = extract_runner_types(workflows)
    print(f"Found {len(runners)} runner types")
    
    # Extract test configurations
    test_configs = extract_test_configs(workflows)
    print(f"Found {len(test_configs)} test configurations")
    
    # Generate architecture diagram
    content = generate_architecture_diagram(
        repo_name=repo_name,
        workflows=workflows,
        actions=actions,
        scripts=scripts,
        runners=runners,
        test_configs=test_configs,
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