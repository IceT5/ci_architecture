#!/usr/bin/env python3
"""
CI Data Extractor - Extract comprehensive raw CI/CD data without classification

This module extracts detailed raw data from CI/CD configurations.
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
class StepData:
    """Detailed step data."""
    name: str = ""
    id: str = ""
    uses: str = ""
    run: str = ""
    with_params: Dict[str, Any] = field(default_factory=dict)
    env: Dict[str, str] = field(default_factory=dict)
    if_condition: str = ""
    continue_on_error: bool = False
    timeout_minutes: int = 0


@dataclass
class JobData:
    """Detailed job data extracted from workflow."""
    name: str
    display_name: str = ""
    runs_on: str = ""
    needs: List[str] = field(default_factory=list)
    uses: str = ""  # For reusable workflow calls
    with_params: Dict[str, Any] = field(default_factory=dict)  # Inputs for reusable workflow
    steps: List[StepData] = field(default_factory=list)
    if_condition: str = ""
    matrix: Optional[Dict] = None
    matrix_configs: List[Dict[str, Any]] = field(default_factory=list)  # Expanded matrix configs
    env_vars: Dict[str, str] = field(default_factory=dict)
    outputs: Dict[str, str] = field(default_factory=dict)
    timeout_minutes: int = 0
    # Extracted relationships
    calls_workflows: List[str] = field(default_factory=list)
    calls_actions: List[str] = field(default_factory=list)


@dataclass
class WorkflowData:
    """Detailed workflow data without classification."""
    filename: str
    name: str
    path: str
    triggers: List[str] = field(default_factory=list)
    trigger_details: Dict[str, Any] = field(default_factory=dict)  # Detailed trigger config
    jobs: Dict[str, JobData] = field(default_factory=dict)
    env_vars: Dict[str, str] = field(default_factory=dict)
    concurrency: Dict[str, str] = field(default_factory=dict)
    raw_content: str = ""  # Full content for LLM context
    # Relationships
    callers: List[str] = field(default_factory=list)  # Who calls this workflow


@dataclass
class ActionData:
    """Detailed composite action data."""
    name: str
    path: str
    description: str = ""
    inputs: Dict[str, Dict] = field(default_factory=dict)  # name -> {description, required, default}
    outputs: Dict[str, Dict] = field(default_factory=dict)
    runs_steps: List[StepData] = field(default_factory=list)
    runs_using: str = ""  # composite, docker, node
    called_actions: List[str] = field(default_factory=list)
    used_by: List[str] = field(default_factory=list)


@dataclass
class ScriptData:
    """Detailed script data."""
    name: str
    path: str
    type: str  # .py, .sh, .ps1, .bat
    content: str = ""  # Full content for LLM analysis
    functions: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    called_by: List[str] = field(default_factory=list)  # Which workflows use this


@dataclass
class PreCommitHookData:
    """Pre-commit hook configuration."""
    id: str = ""
    repo: str = ""
    rev: str = ""
    additional_dependencies: List[str] = field(default_factory=list)
    args: List[str] = field(default_factory=list)
    files: str = ""
    exclude: str = ""
    language: str = ""
    description: str = ""


@dataclass
class PreCommitConfigData:
    """Complete pre-commit configuration."""
    path: str = ""
    default_stages: List[str] = field(default_factory=list)
    default_language_version: Dict[str, str] = field(default_factory=dict)
    ci: Dict[str, Any] = field(default_factory=dict)  # CI-specific settings like autofix_prs
    repos: List[PreCommitHookData] = field(default_factory=list)
    local_hooks: List[PreCommitHookData] = field(default_factory=list)  # Local repo hooks


@dataclass
class CIData:
    """Complete CI/CD raw data for LLM analysis."""
    repo_name: str
    repo_path: str
    workflows: Dict[str, WorkflowData] = field(default_factory=dict)
    actions: List[ActionData] = field(default_factory=list)
    scripts: List[ScriptData] = field(default_factory=list)
    pre_commit_configs: List[PreCommitConfigData] = field(default_factory=list)  # pre-commit configs
    # Raw relationship data
    workflow_call_graph: Dict[str, List[str]] = field(default_factory=dict)
    job_dependency_graph: Dict[str, List[str]] = field(default_factory=dict)
    action_usage_graph: Dict[str, List[str]] = field(default_factory=dict)
    # Metadata
    ci_directories: List[str] = field(default_factory=list)
    # Scripts directory mapping
    scripts_by_directory: Dict[str, List[str]] = field(default_factory=dict)


class CIDataExtractor:
    """Extract comprehensive raw CI/CD data without making classification decisions."""
    
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
        
        # Extract scripts with directory mapping
        data.scripts, data.scripts_by_directory = self._extract_scripts(ci_dirs)
        
        # Extract pre-commit configurations
        data.pre_commit_configs = self._extract_pre_commit_configs()
        
        # Build relationship graphs
        self._build_relationships(data)
        
        return data
    
    def _find_ci_directories(self) -> Dict[str, Path]:
        """Find all CI-related directories."""
        patterns = [
            (".github/workflows", "github_workflows"),
            (".github/actions", "github_actions"),
            (".github/scripts", "github_scripts"),
            (".ci", "ci_dir"),
            (".circleci", "circleci"),
            ("ci", "ci_root"),
            ("scripts", "scripts"),
            ("test", "test"),
            ("tests", "tests"),
        ]
        
        found = {}
        for pattern, key in patterns:
            path = self.repo_path / pattern
            if path.exists():
                found[key] = path
        
        return found
    
    def _extract_workflow(self, filepath: Path) -> Optional[WorkflowData]:
        """Extract detailed workflow data from YAML file."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            wf_data = yaml.safe_load(content)
            if not wf_data:
                return None
            
            # Handle 'on' as True (YAML keyword)
            if True in wf_data and "on" not in wf_data:
                wf_data["on"] = wf_data.pop(True)
            
            # Extract triggers with details
            triggers, trigger_details = self._extract_triggers(wf_data)
            
            # Extract jobs with full details
            jobs = self._extract_jobs(wf_data, filepath.name)
            
            # Extract workflow-level env
            env_vars = wf_data.get("env", {}) or {}
            
            # Extract concurrency config
            concurrency = wf_data.get("concurrency", {}) or {}
            if isinstance(concurrency, str):
                concurrency = {"group": concurrency}
            
            return WorkflowData(
                filename=filepath.name,
                name=wf_data.get("name", filepath.stem),
                path=str(filepath.relative_to(self.repo_path)),
                triggers=triggers,
                trigger_details=trigger_details,
                jobs=jobs,
                env_vars=env_vars if isinstance(env_vars, dict) else {},
                concurrency=concurrency if isinstance(concurrency, dict) else {},
                raw_content=content
            )
        except Exception as e:
            print(f"Error parsing {filepath}: {e}", file=sys.stderr)
            return None
    
    def _extract_triggers(self, wf_data: Dict) -> Tuple[List[str], Dict]:
        """Extract trigger events with details."""
        triggers = []
        trigger_details = {}
        on_config = wf_data.get("on", {})
        
        if isinstance(on_config, str):
            triggers = [on_config]
        elif isinstance(on_config, list):
            triggers = on_config
        elif isinstance(on_config, dict):
            triggers = list(on_config.keys())
            trigger_details = on_config
        
        return triggers, trigger_details
    
    def _extract_jobs(self, wf_data: Dict, workflow_name: str) -> Dict[str, JobData]:
        """Extract detailed job data."""
        jobs = {}
        
        for job_name, job_data in (wf_data.get("jobs", {}) or {}).items():
            if not isinstance(job_data, dict):
                continue
            
            # Extract steps with full details
            steps = self._extract_steps(job_data.get("steps", []))
            
            # Extract matrix with expanded configs
            matrix = None
            matrix_configs = []
            strategy = job_data.get("strategy", {})
            if isinstance(strategy, dict):
                matrix = strategy.get("matrix")
                if matrix:
                    matrix_configs = self._expand_matrix(matrix)
            
            # Extract environment variables
            env = job_data.get("env", {}) or {}
            env_vars = env if isinstance(env, dict) else {}
            
            # Extract outputs
            outputs = job_data.get("outputs", {}) or {}
            
            # Extract needs (dependencies)
            needs = job_data.get("needs", [])
            if isinstance(needs, str):
                needs = [needs]
            
            # Extract uses (for reusable workflows) with parameters
            uses = job_data.get("uses", "")
            with_params = job_data.get("with", {}) or {}
            
            # Find calls in this job
            calls_workflows = []
            calls_actions = []
            
            if uses:
                calls_workflows.append(uses)
            
            for step in steps:
                step_uses = step.uses
                if step_uses:
                    if step_uses.startswith("./.github/actions/"):
                        action_name = step_uses.replace("./.github/actions/", "").split("/")[0]
                        calls_actions.append(f"local:{action_name}")
                    elif step_uses.startswith("./.github/workflows/"):
                        calls_workflows.append(step_uses)
                    elif "/" in step_uses and not step_uses.startswith("./"):
                        calls_actions.append(step_uses)
            
            # Extract display name
            display_name = job_data.get("name", job_name)
            
            jobs[job_name] = JobData(
                name=job_name,
                display_name=display_name,
                runs_on=job_data.get("runs-on", ""),
                needs=needs,
                uses=uses,
                with_params=with_params if isinstance(with_params, dict) else {},
                steps=steps,
                if_condition=str(job_data.get("if", "")),
                matrix=matrix,
                matrix_configs=matrix_configs,
                env_vars=env_vars,
                outputs=outputs if isinstance(outputs, dict) else {},
                timeout_minutes=job_data.get("timeout-minutes", 0),
                calls_workflows=calls_workflows,
                calls_actions=calls_actions
            )
        
        return jobs
    
    def _extract_steps(self, steps_data: List) -> List[StepData]:
        """Extract detailed step data."""
        steps = []
        for step in steps_data:
            if not isinstance(step, dict):
                continue
            
            with_params = step.get("with", {}) or {}
            env = step.get("env", {}) or {}
            
            steps.append(StepData(
                name=step.get("name", ""),
                id=step.get("id", ""),
                uses=step.get("uses", ""),
                run=step.get("run", ""),
                with_params=with_params if isinstance(with_params, dict) else {},
                env=env if isinstance(env, dict) else {},
                if_condition=str(step.get("if", "")),
                continue_on_error=step.get("continue-on-error", False),
                timeout_minutes=step.get("timeout-minutes", 0)
            ))
        
        return steps
    
    def _expand_matrix(self, matrix: Dict) -> List[Dict[str, Any]]:
        """Expand matrix to list of configurations."""
        configs = []
        
        if not isinstance(matrix, dict):
            return configs
        
        # Handle include
        includes = matrix.get("include", [])
        if includes:
            for item in includes:
                if isinstance(item, dict):
                    configs.append(item)
        
        # Simple matrix expansion (limited)
        exclude = matrix.get("exclude", [])
        
        # Get all dimension keys
        dimension_keys = [k for k in matrix.keys() if k not in ["include", "exclude"]]
        
        if dimension_keys:
            # For simple cases, just record the dimensions
            for key in dimension_keys:
                values = matrix.get(key, [])
                if isinstance(values, list):
                    for val in values:
                        configs.append({key: val})
        
        return configs[:50]  # Limit number of configs
    
    def _extract_action(self, action_dir: Path) -> Optional[ActionData]:
        """Extract detailed action data."""
        action_file = action_dir / "action.yml"
        if not action_file.exists():
            action_file = action_dir / "action.yaml"
        
        if not action_file.exists():
            return None
        
        try:
            with open(action_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            
            # Extract inputs with details
            inputs = {}
            for name, inp in (data.get("inputs", {}) or {}).items():
                if isinstance(inp, dict):
                    inputs[name] = {
                        "description": inp.get("description", ""),
                        "required": inp.get("required", False),
                        "default": inp.get("default", "")
                    }
            
            # Extract outputs
            outputs = {}
            for name, out in (data.get("outputs", {}) or {}).items():
                if isinstance(out, dict):
                    outputs[name] = {
                        "description": out.get("description", ""),
                        "value": out.get("value", "")
                    }
            
            # Extract steps
            runs = data.get("runs", {})
            steps = []
            called_actions = []
            
            if isinstance(runs, dict):
                steps = self._extract_steps(runs.get("steps", []))
                for step in steps:
                    if step.uses:
                        called_actions.append(step.uses)
            
            return ActionData(
                name=action_dir.name,
                path=str(action_dir.relative_to(self.repo_path)),
                description=data.get("description", ""),
                inputs=inputs,
                outputs=outputs,
                runs_steps=steps,
                runs_using=runs.get("using", "") if isinstance(runs, dict) else "",
                called_actions=called_actions
            )
        except Exception as e:
            print(f"Error parsing action {action_dir}: {e}", file=sys.stderr)
            return None
    
    def _extract_scripts(self, ci_dirs: Dict[str, Path]) -> Tuple[List[ScriptData], Dict[str, List[str]]]:
        """Extract script information with directory mapping."""
        scripts = []
        scripts_by_dir = defaultdict(list)
        seen = set()
        
        for dir_key, path in ci_dirs.items():
            if not isinstance(path, Path) or not path.exists():
                continue
            
            for ext in ["*.sh", "*.py", "*.ps1", "*.bat"]:
                for f in path.rglob(ext):
                    if f.name not in seen:
                        seen.add(f.name)
                        try:
                            with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                                content = fp.read()
                            
                            # Extract functions (for Python and Shell)
                            functions = []
                            imports = []
                            if f.suffix == ".py":
                                func_pattern = r'^def\s+(\w+)\s*\('
                                functions = re.findall(func_pattern, content, re.MULTILINE)
                                import_pattern = r'^(?:import|from)\s+(\S+)'
                                imports = re.findall(import_pattern, content, re.MULTILINE)
                            elif f.suffix == ".sh":
                                func_pattern = r'^(?:function\s+)?(\w+)\s*\(\s*\)\s*\{'
                                functions = re.findall(func_pattern, content, re.MULTILINE)
                            
                            script = ScriptData(
                                name=f.name,
                                path=str(f.relative_to(self.repo_path)),
                                type=f.suffix,
                                content=content[:5000],  # Limit content
                                functions=functions,
                                imports=imports
                            )
                            scripts.append(script)
                            
                            # Map to directory
                            rel_dir = str(f.parent.relative_to(self.repo_path))
                            scripts_by_dir[rel_dir].append(f.name)
                            
                        except Exception as e:
                            pass
        
        return scripts[:100], dict(scripts_by_dir)  # Limit
    
    def _extract_pre_commit_configs(self) -> List[PreCommitConfigData]:
        """Extract pre-commit configuration from .pre-commit-config.yaml files."""
        configs = []
        
        # Common pre-commit config file locations
        config_paths = [
            self.repo_path / ".pre-commit-config.yaml",
            self.repo_path / ".pre-commit-config.yml",
            self.repo_path / ".pre-commit-config" / "config.yaml",
        ]
        
        for config_path in config_paths:
            if not config_path.exists():
                continue
            
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
                
                config = PreCommitConfigData(
                    path=str(config_path.relative_to(self.repo_path))
                )
                
                # Extract default stages
                config.default_stages = data.get("default_stages", [])
                
                # Extract default language version
                config.default_language_version = data.get("default_language_version", {})
                
                # Extract CI settings
                config.ci = data.get("ci", {})
                
                # Extract repos and hooks
                repos = data.get("repos", [])
                for repo_data in repos:
                    if not isinstance(repo_data, dict):
                        continue
                    
                    repo_url = repo_data.get("repo", "")
                    rev = repo_data.get("rev", "")
                    hooks = repo_data.get("hooks", [])
                    
                    for hook in hooks:
                        if not isinstance(hook, dict):
                            continue
                        
                        hook_data = PreCommitHookData(
                            id=hook.get("id", ""),
                            repo=repo_url,
                            rev=rev,
                            additional_dependencies=hook.get("additional_dependencies", []),
                            args=hook.get("args", []),
                            files=hook.get("files", ""),
                            exclude=hook.get("exclude", ""),
                            language=hook.get("language", ""),
                            description=hook.get("description", "")
                        )
                        
                        # Check if it's a local hook (repo == "local")
                        if repo_url == "local":
                            config.local_hooks.append(hook_data)
                        else:
                            config.repos.append(hook_data)
                
                configs.append(config)
                
            except Exception as e:
                print(f"Error parsing pre-commit config {config_path}: {e}", file=sys.stderr)
        
        return configs
    
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
        
        # Track script usage in workflows
        script_names = {s.name: s for s in data.scripts}
        for wf_name, wf in data.workflows.items():
            for job_name, job in wf.jobs.items():
                for step in job.steps:
                    run_script = step.run
                    if run_script:
                        for script_name, script in script_names.items():
                            if script_name in run_script:
                                script.called_by.append(f"{wf_name}::{job_name}")


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
        "scripts_by_directory": data.scripts_by_directory,
        "relationships": {
            "workflow_calls": data.workflow_call_graph,
            "job_dependencies": data.job_dependency_graph,
            "action_usages": data.action_usage_graph,
        }
    }
    
    # Convert workflows with full details
    for wf_name, wf in data.workflows.items():
        result["workflows"][wf_name] = {
            "name": wf.name,
            "filename": wf.filename,
            "path": wf.path,
            "triggers": wf.triggers,
            "trigger_details": wf.trigger_details,
            "env_vars": wf.env_vars,
            "concurrency": wf.concurrency,
            "jobs": {
                job_name: {
                    "display_name": job.display_name,
                    "runs_on": job.runs_on,
                    "needs": job.needs,
                    "uses": job.uses,
                    "with_params": job.with_params,
                    "if_condition": job.if_condition,
                    "matrix": job.matrix,
                    "matrix_configs": job.matrix_configs,
                    "env_vars": job.env_vars,
                    "outputs": job.outputs,
                    "timeout_minutes": job.timeout_minutes,
                    "steps": [
                        {
                            "name": step.name,
                            "id": step.id,
                            "uses": step.uses,
                            "run": step.run[:500] if step.run else "",  # Limit
                            "with_params": step.with_params,
                            "env": step.env,
                        }
                        for step in job.steps
                    ],
                    "calls_workflows": job.calls_workflows,
                    "calls_actions": job.calls_actions,
                }
                for job_name, job in wf.jobs.items()
            },
            "callers": wf.callers,
        }
    
    # Convert actions
    for action in data.actions:
        result["actions"].append({
            "name": action.name,
            "path": action.path,
            "description": action.description,
            "inputs": action.inputs,
            "outputs": action.outputs,
            "runs_using": action.runs_using,
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
            "imports": script.imports,
            "content_preview": script.content[:1500],  # Limit
            "called_by": script.called_by,
        })
    
    # Convert pre-commit configs
    result["pre_commit_configs"] = []
    for pc_config in data.pre_commit_configs:
        config_dict = {
            "path": pc_config.path,
            "default_stages": pc_config.default_stages,
            "default_language_version": pc_config.default_language_version,
            "ci": pc_config.ci,
            "repos": [],
            "local_hooks": [],
        }
        
        # External repo hooks
        for hook in pc_config.repos:
            config_dict["repos"].append({
                "id": hook.id,
                "repo": hook.repo,
                "rev": hook.rev,
                "additional_dependencies": hook.additional_dependencies,
                "args": hook.args,
                "files": hook.files,
                "exclude": hook.exclude,
                "language": hook.language,
                "description": hook.description,
            })
        
        # Local hooks
        for hook in pc_config.local_hooks:
            config_dict["local_hooks"].append({
                "id": hook.id,
                "additional_dependencies": hook.additional_dependencies,
                "args": hook.args,
                "files": hook.files,
                "exclude": hook.exclude,
                "language": hook.language,
                "description": hook.description,
            })
        
        result["pre_commit_configs"].append(config_dict)
    
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