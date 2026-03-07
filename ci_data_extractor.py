#!/usr/bin/env python3
"""
CI Data Extractor - Extract raw CI/CD data without classification

This module only extracts raw data from CI/CD configurations.
All classification and understanding should be done by LLM.
"""

import os
import re
import yaml
import json
from pathlib import Path
from typing import Dict, List, Set, Any, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass, field, asdict
import sys


@dataclass
class JobData:
    """Raw job data extracted from workflow."""
    name: str
    runs_on: str = ""
    needs: List[str] = field(default_factory=list)
    uses: str = ""
    steps: List[Dict] = field(default_factory=list)
    if_condition: str = ""
    matrix: Optional[Dict] = None
    env_vars: List[str] = field(default_factory=list)
    # Extracted relationships
    calls_workflows: List[str] = field(default_factory=list)
    calls_actions: List[str] = field(default_factory=list)


@dataclass
class WorkflowData:
    """Raw workflow data without classification."""
    filename: str
    name: str
    triggers: List[str] = field(default_factory=list)
    jobs: Dict[str, JobData] = field(default_factory=dict)
    raw_content_summary: str = ""  # First N lines for LLM context
    # Relationships
    callers: List[str] = field(default_factory=list)  # Who calls this workflow


@dataclass
class ActionData:
    """Raw composite action data."""
    name: str
    path: str
    description: str = ""
    inputs: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    runs_steps: List[Dict] = field(default_factory=list)
    called_actions: List[str] = field(default_factory=list)
    used_by: List[str] = field(default_factory=list)


@dataclass
class ScriptData:
    """Raw script data."""
    name: str
    path: str
    type: str  # .py, .sh, .ps1, .bat
    content_preview: str = ""  # First 50 lines for LLM analysis
    functions: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)


@dataclass
class CIData:
    """Complete CI/CD raw data for LLM analysis."""
    repo_name: str
    repo_path: str
    workflows: Dict[str, WorkflowData] = field(default_factory=dict)
    actions: List[ActionData] = field(default_factory=list)
    scripts: List[ScriptData] = field(default_factory=list)
    # Raw relationship data
    workflow_call_graph: Dict[str, List[str]] = field(default_factory=dict)
    job_dependency_graph: Dict[str, List[str]] = field(default_factory=dict)
    action_usage_graph: Dict[str, List[str]] = field(default_factory=dict)
    # Metadata
    ci_directories: List[str] = field(default_factory=list)


class CIDataExtractor:
    """Extract raw CI/CD data without making classification decisions."""
    
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path).resolve()
        self.repo_name = self.repo_path.name
        
    def extract_all(self) -> CIData:
        """Extract all CI/CD data from repository."""
        data = CIData(
            repo_name=self.repo_name,
            repo_path=str(self.repo_path)
        )
        
        # Find CI directories
        ci_dirs = self._find_ci_directories()
        data.ci_directories = list(ci_dirs.keys())
        
        # Extract workflows
        workflows_dir = ci_dirs.get("github_workflows")
        if workflows_dir and workflows_dir.exists():
            for wf_file in workflows_dir.glob("*.yml"):
                wf_data = self._extract_workflow(wf_file)
                if wf_data:
                    data.workflows[wf_file.name] = wf_data
            for wf_file in workflows_dir.glob("*.yaml"):
                wf_data = self._extract_workflow(wf_file)
                if wf_data:
                    data.workflows[wf_file.name] = wf_data
        
        # Extract actions
        actions_dir = ci_dirs.get("github_actions")
        if actions_dir and actions_dir.exists():
            for action_dir in actions_dir.iterdir():
                if action_dir.is_dir():
                    action_data = self._extract_action(action_dir)
                    if action_data:
                        data.actions.append(action_data)
        
        # Extract scripts
        data.scripts = self._extract_scripts(ci_dirs)
        
        # Build relationship graphs
        self._build_relationships(data)
        
        return data
    
    def _find_ci_directories(self) -> Dict[str, Path]:
        """Find all CI-related directories."""
        patterns = [
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
        for pattern in patterns:
            path = self.repo_path / pattern
            if path.exists():
                found[pattern.replace("/", "_").replace(".", "")] = path
        
        return found
    
    def _extract_workflow(self, filepath: Path) -> Optional[WorkflowData]:
        """Extract raw workflow data from YAML file."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            wf_data = yaml.safe_load(content)
            if not wf_data:
                return None
            
            # Handle 'on' as True (YAML keyword)
            if True in wf_data and "on" not in wf_data:
                wf_data["on"] = wf_data.pop(True)
            
            # Extract triggers
            triggers = self._extract_triggers(wf_data)
            
            # Extract jobs
            jobs = self._extract_jobs(wf_data, filepath.name)
            
            # Get content summary (first 100 lines for context)
            lines = content.split("\n")[:100]
            content_summary = "\n".join(lines)
            
            return WorkflowData(
                filename=filepath.name,
                name=wf_data.get("name", filepath.stem),
                triggers=triggers,
                jobs=jobs,
                raw_content_summary=content_summary
            )
        except Exception as e:
            print(f"Error parsing {filepath}: {e}", file=sys.stderr)
            return None
    
    def _extract_triggers(self, wf_data: Dict) -> List[str]:
        """Extract trigger events."""
        triggers = []
        on_config = wf_data.get("on", {})
        
        if isinstance(on_config, str):
            triggers = [on_config]
        elif isinstance(on_config, list):
            triggers = on_config
        elif isinstance(on_config, dict):
            triggers = list(on_config.keys())
        
        return triggers
    
    def _extract_jobs(self, wf_data: Dict, workflow_name: str) -> Dict[str, JobData]:
        """Extract raw job data."""
        jobs = {}
        
        for job_name, job_data in (wf_data.get("jobs", {}) or {}).items():
            if not isinstance(job_data, dict):
                continue
            
            # Extract steps
            steps = []
            for step in job_data.get("steps", []):
                if isinstance(step, dict):
                    steps.append({
                        "name": step.get("name", ""),
                        "uses": step.get("uses", ""),
                        "run": step.get("run", ""),
                        "with": step.get("with", {}),
                        "env": step.get("env", {}),
                    })
            
            # Extract matrix
            matrix = None
            strategy = job_data.get("strategy", {})
            if isinstance(strategy, dict):
                matrix = strategy.get("matrix")
            
            # Extract environment variables
            env = job_data.get("env", {})
            env_vars = list(env.keys()) if isinstance(env, dict) else []
            
            # Extract needs (dependencies)
            needs = job_data.get("needs", [])
            if isinstance(needs, str):
                needs = [needs]
            
            # Extract uses (for reusable workflows)
            uses = job_data.get("uses", "")
            
            # Find calls in this job
            calls_workflows = []
            calls_actions = []
            
            if uses:
                if "./.github/workflows/" in uses or "uses" in uses:
                    calls_workflows.append(uses)
            
            for step in steps:
                step_uses = step.get("uses", "")
                if step_uses:
                    if step_uses.startswith("./.github/actions/"):
                        action_name = step_uses.replace("./.github/actions/", "").split("/")[0]
                        calls_actions.append(f"local:{action_name}")
                    elif step_uses.startswith("./.github/workflows/"):
                        calls_workflows.append(step_uses)
                    elif "/" in step_uses and not step_uses.startswith("./"):
                        calls_actions.append(step_uses)
            
            jobs[job_name] = JobData(
                name=job_name,
                runs_on=job_data.get("runs-on", ""),
                needs=needs,
                uses=uses,
                steps=steps,
                if_condition=job_data.get("if", ""),
                matrix=matrix,
                env_vars=env_vars,
                calls_workflows=calls_workflows,
                calls_actions=calls_actions
            )
        
        return jobs
    
    def _extract_action(self, action_dir: Path) -> Optional[ActionData]:
        """Extract raw action data."""
        action_file = action_dir / "action.yml"
        if not action_file.exists():
            action_file = action_dir / "action.yaml"
        
        if not action_file.exists():
            return None
        
        try:
            with open(action_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            
            # Extract steps
            runs = data.get("runs", {})
            steps = runs.get("steps", []) if isinstance(runs, dict) else []
            
            # Extract called actions
            called_actions = []
            for step in steps:
                if isinstance(step, dict):
                    step_uses = step.get("uses", "")
                    if step_uses:
                        called_actions.append(step_uses)
            
            return ActionData(
                name=action_dir.name,
                path=str(action_dir.relative_to(self.repo_path)),
                description=data.get("description", ""),
                inputs=list((data.get("inputs", {}) or {}).keys()),
                outputs=list((data.get("outputs", {}) or {}).keys()),
                runs_steps=steps,
                called_actions=called_actions
            )
        except Exception as e:
            print(f"Error parsing action {action_dir}: {e}", file=sys.stderr)
            return None
    
    def _extract_scripts(self, ci_dirs: Dict[str, Path]) -> List[ScriptData]:
        """Extract script information."""
        scripts = []
        seen = set()
        
        for key, path in ci_dirs.items():
            if not isinstance(path, Path) or not path.exists():
                continue
            
            for ext in ["*.sh", "*.py", "*.ps1", "*.bat"]:
                for f in path.rglob(ext):
                    if f.name not in seen:
                        seen.add(f.name)
                        try:
                            with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                                content = fp.read()
                            
                            # Get preview
                            lines = content.split("\n")[:50]
                            preview = "\n".join(lines)
                            
                            # Extract functions (for Python and Shell)
                            functions = []
                            if f.suffix == ".py":
                                func_pattern = r'^def\s+(\w+)\s*\('
                                functions = re.findall(func_pattern, content, re.MULTILINE)
                            elif f.suffix == ".sh":
                                func_pattern = r'^(?:function\s+)?(\w+)\s*\(\s*\)\s*\{'
                                functions = re.findall(func_pattern, content, re.MULTILINE)
                            
                            scripts.append(ScriptData(
                                name=f.name,
                                path=str(f.relative_to(self.repo_path)),
                                type=f.suffix,
                                content_preview=preview,
                                functions=functions
                            ))
                        except Exception as e:
                            pass
        
        return scripts[:100]  # Limit
    
    def _build_relationships(self, data: CIData):
        """Build relationship graphs from extracted data."""
        # Workflow call graph
        for wf_name, wf in data.workflows.items():
            callers = []
            for job_name, job in wf.jobs.items():
                for called_wf in job.calls_workflows:
                    if called_wf not in data.workflow_call_graph:
                        data.workflow_call_graph[called_wf] = []
                    data.workflow_call_graph[called_wf].append(f"{wf_name}::{job_name}")
        
        # Job dependency graph
        for wf_name, wf in data.workflows.items():
            for job_name, job in wf.jobs.items():
                key = f"{wf_name}::{job_name}"
                if job.needs:
                    data.job_dependency_graph[key] = job.needs
        
        # Action usage graph
        action_map = {f"local:{a.name}": a for a in data.actions}
        for wf_name, wf in data.workflows.items():
            for job_name, job in wf.jobs.items():
                for called_action in job.calls_actions:
                    if called_action not in data.action_usage_graph:
                        data.action_usage_graph[called_action] = []
                    data.action_usage_graph[called_action].append(f"{wf_name}::{job_name}")
                    
                    # Track local action usage
                    if called_action.startswith("local:") and called_action in action_map:
                        action_map[called_action].used_by.append(f"{wf_name}::{job_name}")


def extract_to_json(repo_path: str, output_file: str = None) -> str:
    """Extract CI/CD data and output as JSON for LLM analysis."""
    extractor = CIDataExtractor(repo_path)
    data = extractor.extract_all()
    
    # Convert to dict for JSON serialization
    result = {
        "repo_name": data.repo_name,
        "repo_path": data.repo_path,
        "ci_directories": data.ci_directories,
        "workflows": {},
        "actions": [],
        "scripts": [],
        "relationships": {
            "workflow_calls": data.workflow_call_graph,
            "job_dependencies": data.job_dependency_graph,
            "action_usages": data.action_usage_graph,
        }
    }
    
    # Convert workflows
    for wf_name, wf in data.workflows.items():
        result["workflows"][wf_name] = {
            "name": wf.name,
            "filename": wf.filename,
            "triggers": wf.triggers,
            "jobs": {
                job_name: {
                    "runs_on": job.runs_on,
                    "needs": job.needs,
                    "steps": job.steps,
                    "calls_workflows": job.calls_workflows,
                    "calls_actions": job.calls_actions,
                }
                for job_name, job in wf.jobs.items()
            },
            "callers": wf.callers,
            "content_summary": wf.raw_content_summary[:2000],  # Limit for JSON
        }
    
    # Convert actions
    for action in data.actions:
        result["actions"].append({
            "name": action.name,
            "path": action.path,
            "description": action.description,
            "inputs": action.inputs,
            "outputs": action.outputs,
            "called_actions": action.called_actions,
            "used_by": action.used_by,
        })
    
    # Convert scripts
    for script in data.scripts:
        result["scripts"].append({
            "name": script.name,
            "path": script.path,
            "type": script.type,
            "functions": script.functions,
            "content_preview": script.content_preview[:1000],  # Limit
        })
    
    # Output JSON
    json_str = json.dumps(result, indent=2, ensure_ascii=False)
    
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(json_str)
        print(f"CI data extracted to: {output_file}")
    
    return json_str


if __name__ == "__main__":
    import sys
    
    repo_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else "ci_data.json"
    
    if repo_path:
        extract_to_json(repo_path, output_file)
    else:
        print("Usage: python ci_data_extractor.py <repo_path> [output_file]")