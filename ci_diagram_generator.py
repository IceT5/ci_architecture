#!/usr/bin/env python3
"""
CI Architecture Diagram Generator - Generate architecture diagrams from LLM analysis results

This module receives LLM analysis results and generates architecture diagrams.
The LLM is responsible for classification and understanding.
"""

import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class CategoryInfo:
    """Category defined by LLM."""
    id: str  # Category identifier (e.g., "pull_ci", "integration_tests")
    name: str  # Human readable name (e.g., "Pull Request CI")
    description: str  # LLM-provided description
    icon: str = "📄"  # Emoji icon for the category
    directory: str = ""  # Related script directory


@dataclass
class WorkflowClassification:
    """LLM's classification of a workflow."""
    filename: str
    category: str  # Reference to CategoryInfo.id
    purpose: str  # What this workflow does
    importance: str  # "primary", "secondary", "auxiliary"
    jobs_summary: str = ""  # Summary of jobs
    key_configs: List[str] = field(default_factory=list)  # Key configurations
    notes: str = ""


@dataclass
class JobClassification:
    """LLM's classification of a job."""
    name: str
    workflow: str
    category: str
    purpose: str
    runs_on: str = ""
    key_steps: List[str] = field(default_factory=list)
    config_params: Dict[str, Any] = field(default_factory=dict)
    notes: str = ""


@dataclass
class ActionClassification:
    """LLM's classification of an action."""
    name: str
    category: str
    purpose: str
    used_by_workflows: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class ScriptClassification:
    """LLM's classification of a script."""
    name: str
    path: str
    purpose: str
    category: str
    related_workflows: List[str] = field(default_factory=list)
    key_functions: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class LLMAnalysisResult:
    """Complete LLM analysis result structure."""
    # LLM-defined categories
    categories: List[Dict] = field(default_factory=list)
    
    # Classifications
    workflow_classifications: Dict[str, Dict] = field(default_factory=dict)
    job_classifications: Dict[str, Dict] = field(default_factory=dict)
    action_classifications: Dict[str, Dict] = field(default_factory=dict)
    script_classifications: Dict[str, Dict] = field(default_factory=dict)
    
    # LLM's understanding of the project
    project_type: str = ""
    ci_philosophy: str = ""
    key_patterns: List[str] = field(default_factory=list)
    
    # Architecture description
    architecture_summary: str = ""
    recommendations: List[str] = field(default_factory=list)


def generate_llm_prompt(raw_data: Dict) -> str:
    """Generate a detailed prompt for LLM to analyze the CI data."""
    
    prompt = """# CI/CD Architecture Analysis Request

You are analyzing the CI/CD infrastructure of a software project. Your task is to:
1. Understand the project's CI/CD architecture
2. Create meaningful categories for organizing workflows and jobs
3. Classify each workflow, job, action, and script
4. Provide detailed information for generating an architecture diagram

## Important Guidelines for Categories

Create categories based on the **functional purpose** of workflows/jobs, not just their names. Common CI/CD categories include:

1. **Pull Request CI** - Workflows triggered on PRs for validation
2. **Post-Merge/Trunk CI** - Workflows that run after merging to main
3. **Scheduled/Periodic CI** - Cron-based workflows
4. **Build Pipelines** - Compilation and artifact generation
5. **Testing** - Various test suites (unit, integration, e2e)
6. **Linting/Code Quality** - Static analysis and formatting
7. **Binary/Release** - Artifact and release builds
8. **Documentation** - Doc generation and validation
9. **Utility/Maintenance** - Helper workflows (merge, rebase, cleanup)

## Output Format Requirements

For each category, you must identify:
- **Script Directory**: Where related scripts are located
- **Workflow List**: Which workflows belong to this category
- **Job List**: Key jobs within each workflow
- **Config Parameters**: Important matrix configs, inputs, environment variables
- **Summary**: A brief description of what this category does

---

## Raw Data

"""
    
    # Add repository info
    prompt += f"### Repository: {raw_data.get('repo_name', 'Unknown')}\n\n"
    
    # Add CI directories
    ci_dirs = raw_data.get("ci_directories", [])
    if ci_dirs:
        prompt += "### CI Directories Found\n"
        for d in ci_dirs:
            prompt += f"- `{d}`\n"
        prompt += "\n"
    
    # Add scripts by directory
    scripts_by_dir = raw_data.get("scripts_by_directory", {})
    if scripts_by_dir:
        prompt += "### Scripts by Directory\n"
        for dir_path, scripts in scripts_by_dir.items():
            prompt += f"- `{dir_path}/`: {', '.join(scripts[:10])}"
            if len(scripts) > 10:
                prompt += f" (+{len(scripts)-10} more)"
            prompt += "\n"
        prompt += "\n"
    
    # Add workflows with detailed info
    workflows = raw_data.get("workflows", {})
    if workflows:
        prompt += "### Workflows\n\n"
        for wf_name, wf in list(workflows.items())[:30]:  # Limit to 30 workflows
            prompt += f"#### {wf_name}\n"
            prompt += f"- **Name**: {wf.get('name', 'N/A')}\n"
            prompt += f"- **Path**: `{wf.get('path', 'N/A')}`\n"
            prompt += f"- **Triggers**: {', '.join(wf.get('triggers', []))}\n"
            
            # Jobs info
            jobs = wf.get("jobs", {})
            if jobs:
                prompt += f"- **Jobs** ({len(jobs)}):\n"
                for job_name, job in list(jobs.items())[:15]:  # Limit jobs per workflow
                    prompt += f"  - `{job_name}`"
                    
                    # Add uses if reusable workflow
                    if job.get("uses"):
                        uses = job.get("uses", "")
                        prompt += f" → uses `{uses}`"
                    
                    # Add runs-on
                    runs_on = job.get("runs_on", "")
                    if runs_on:
                        prompt += f" (runs-on: {runs_on})"
                    
                    prompt += "\n"
                    
                    # Add key steps
                    steps = job.get("steps", [])
                    if steps:
                        key_steps = [s.get("name", "") or s.get("uses", "") or s.get("id", "") for s in steps[:5]]
                        key_steps = [s for s in key_steps if s]
                        if key_steps:
                            prompt += f"    - Steps: {', '.join(key_steps[:5])}"
                            if len(steps) > 5:
                                prompt += f" (+{len(steps)-5})"
                            prompt += "\n"
                    
                    # Add matrix config if present
                    matrix = job.get("matrix", {})
                    if matrix and matrix.get("include"):
                        configs = matrix.get("include", [])
                        prompt += f"    - Matrix configs: {len(configs)} configurations\n"
                        # Show sample configs
                        for i, cfg in enumerate(configs[:3]):
                            if isinstance(cfg, dict):
                                cfg_str = ", ".join(f"{k}={v}" for k, v in list(cfg.items())[:4])
                                prompt += f"      - {cfg_str}\n"
                    
                    # Add with_params for reusable workflows
                    with_params = job.get("with_params", {})
                    if with_params:
                        params_str = ", ".join(f"{k}={str(v)[:50]}" for k, v in list(with_params.items())[:4])
                        prompt += f"    - Parameters: {params_str}\n"
            
            prompt += "\n"
    
    # Add actions
    actions = raw_data.get("actions", [])
    if actions:
        prompt += "### Composite Actions\n\n"
        for action in actions[:20]:
            prompt += f"- **{action.get('name')}** (`{action.get('path')}`)\n"
            desc = action.get("description", "")
            if desc:
                prompt += f"  - {desc[:100]}\n"
            inputs = action.get("inputs", {})
            if inputs:
                prompt += f"  - Inputs: {', '.join(list(inputs.keys())[:5])}\n"
            used_by = action.get("used_by", [])
            if used_by:
                prompt += f"  - Used by: {len(used_by)} workflows/jobs\n"
        prompt += "\n"
    
    # Add scripts
    scripts = raw_data.get("scripts", [])
    if scripts:
        prompt += "### CI Scripts\n\n"
        for script in scripts[:20]:
            prompt += f"- **{script.get('name')}** (`{script.get('path')}`)\n"
            funcs = script.get("functions", [])
            if funcs:
                prompt += f"  - Functions: {', '.join(funcs[:5])}\n"
            called_by = script.get("called_by", [])
            if called_by:
                prompt += f"  - Called by: {len(called_by)} jobs\n"
        prompt += "\n"
    
    # Add relationships
    relationships = raw_data.get("relationships", {})
    workflow_calls = relationships.get("workflow_calls", {})
    if workflow_calls:
        prompt += "### Workflow Call Graph\n"
        for callee, callers in list(workflow_calls.items())[:10]:
            prompt += f"- `{callee}` ← called by: {', '.join(callers[:3])}\n"
        prompt += "\n"
    
    action_usages = relationships.get("action_usages", {})
    if action_usages:
        prompt += "### Action Usage Graph\n"
        for action, users in list(action_usages.items())[:10]:
            prompt += f"- `{action}` ← used by: {len(users)} jobs\n"
        prompt += "\n"
    
    # Add expected output format
    prompt += """
---

## Expected Output Format

Please provide your analysis in the following JSON format. Be comprehensive and include ALL workflows, jobs, and scripts.

```json
{
  "categories": [
    {
      "id": "category_id",
      "name": "Human Readable Name",
      "description": "Detailed description of what this category is for",
      "icon": "📄",
      "directory": ".github/scripts or relevant directory",
      "workflows": ["workflow1.yml", "workflow2.yml"],
      "summary": "Brief summary of what this category accomplishes"
    }
  ],
  "workflow_classifications": {
    "workflow_file.yml": {
      "category": "category_id",
      "purpose": "What this workflow does",
      "importance": "primary|secondary|auxiliary",
      "jobs_summary": "Brief summary of main jobs",
      "key_configs": ["config1", "config2"],
      "key_jobs": ["job1", "job2"],
      "notes": "Additional observations"
    }
  },
  "job_classifications": {
    "workflow_file.yml::job_name": {
      "category": "category_id",
      "purpose": "What this job does",
      "runs_on": "runner type",
      "key_steps": ["step1", "step2"],
      "config_params": {
        "param1": "value1",
        "matrix_configs": 5
      },
      "notes": ""
    }
  },
  "action_classifications": {
    "action_name": {
      "category": "category_id",
      "purpose": "What this action does",
      "used_by_workflows": ["workflow1.yml"],
      "notes": ""
    }
  },
  "script_classifications": {
    "script_name.sh": {
      "path": ".github/scripts/script_name.sh",
      "purpose": "What this script does",
      "category": "category_id",
      "related_workflows": ["workflow1.yml"],
      "key_functions": ["func1", "func2"],
      "notes": ""
    }
  },
  "project_type": "Type of project (e.g., Python Library, Web Application, Mobile App)",
  "ci_philosophy": "Analysis of the CI/CD approach used",
  "key_patterns": ["Pattern 1", "Pattern 2", "Pattern 3"],
  "architecture_summary": "Brief summary of the CI architecture",
  "recommendations": ["Recommendation 1", "Recommendation 2"]
}
```

**IMPORTANT**: 
1. Make sure every workflow is classified
2. Include ALL jobs for each workflow
3. For each category, specify which script directory it relates to
4. Provide meaningful purposes and summaries
5. Include key config parameters (matrix configs, with_params, etc.)
"""

    return prompt


def parse_llm_response(llm_response: str) -> LLMAnalysisResult:
    """Parse LLM's JSON response into LLMAnalysisResult."""
    
    # Extract JSON from response
    json_str = llm_response
    
    # Try to find JSON block
    if "```json" in llm_response:
        start = llm_response.find("```json") + 7
        end = llm_response.find("```", start)
        json_str = llm_response[start:end].strip()
    elif "```" in llm_response:
        start = llm_response.find("```") + 3
        end = llm_response.find("```", start)
        json_str = llm_response[start:end].strip()
    
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        # Return empty result if parsing fails
        return LLMAnalysisResult()
    
    return LLMAnalysisResult(
        categories=data.get("categories", []),
        workflow_classifications=data.get("workflow_classifications", {}),
        job_classifications=data.get("job_classifications", {}),
        action_classifications=data.get("action_classifications", {}),
        script_classifications=data.get("script_classifications", {}),
        project_type=data.get("project_type", ""),
        ci_philosophy=data.get("ci_philosophy", ""),
        key_patterns=data.get("key_patterns", []),
        architecture_summary=data.get("architecture_summary", ""),
        recommendations=data.get("recommendations", [])
    )


def generate_architecture_diagram(
    raw_data: Dict,
    llm_analysis: LLMAnalysisResult,
    output_file: str
) -> str:
    """Generate comprehensive architecture diagram from raw data + LLM analysis."""
    
    lines = []
    
    # Title
    repo_name = raw_data.get("repo_name", "Unknown").upper()
    lines.append(f"# {repo_name} CI/CD Architecture Analysis")
    lines.append("")
    
    # Project Overview
    if llm_analysis.project_type or llm_analysis.architecture_summary:
        lines.append("## Project Overview")
        lines.append("")
        if llm_analysis.project_type:
            lines.append(f"**Project Type**: {llm_analysis.project_type}")
            lines.append("")
        if llm_analysis.architecture_summary:
            lines.append("**Architecture Summary**:")
            lines.append(llm_analysis.architecture_summary)
            lines.append("")
        if llm_analysis.ci_philosophy:
            lines.append(f"**CI Philosophy**: {llm_analysis.ci_philosophy}")
            lines.append("")
        lines.append("---")
        lines.append("")
    
    # Build category lookup
    category_lookup = {cat.get("id"): cat for cat in llm_analysis.categories}
    
    # Group workflows by category
    workflows_by_category = defaultdict(list)
    for wf_name, wf_data in raw_data.get("workflows", {}).items():
        classification = llm_analysis.workflow_classifications.get(wf_name, {})
        category_id = classification.get("category", "uncategorized")
        workflows_by_category[category_id].append((wf_name, wf_data, classification))
    
    # Generate sections for each category
    for category in llm_analysis.categories:
        cat_id = category.get("id")
        cat_name = category.get("name", cat_id)
        cat_desc = category.get("description", "")
        cat_icon = category.get("icon", "📄")
        cat_dir = category.get("directory", "")
        cat_summary = category.get("summary", "")
        
        lines.append(f"## {cat_icon} {cat_name}")
        lines.append("")
        
        if cat_desc:
            lines.append(f"**Description**: {cat_desc}")
            lines.append("")
        
        if cat_dir:
            lines.append(f"**Script Directory**: `{cat_dir}`")
            lines.append("")
        
        if cat_summary:
            lines.append(f"**Summary**: {cat_summary}")
            lines.append("")
        
        # List workflows in this category
        wf_list = workflows_by_category.get(cat_id, [])
        if wf_list:
            lines.append("### Workflows")
            lines.append("")
            
            for wf_name, wf_data, classification in wf_list:
                purpose = classification.get("purpose", "")
                importance = classification.get("importance", "secondary")
                key_jobs = classification.get("key_jobs", [])
                notes = classification.get("notes", "")
                
                lines.append(f"#### `{wf_name}`")
                lines.append("")
                
                if purpose:
                    lines.append(f"- **Purpose**: {purpose}")
                
                lines.append(f"- **Importance**: {importance}")
                lines.append(f"- **Triggers**: {', '.join(wf_data.get('triggers', []))}")
                
                # Jobs list
                jobs = wf_data.get("jobs", {})
                if jobs:
                    lines.append(f"- **Jobs** ({len(jobs)}):")
                    for job_name, job_data in jobs.items():
                        job_display = job_data.get("display_name", job_name)
                        runs_on = job_data.get("runs_on", "")
                        uses = job_data.get("uses", "")
                        
                        job_line = f"  - `{job_name}`"
                        if job_display and job_display != job_name:
                            job_line += f" ({job_display})"
                        if runs_on:
                            job_line += f" → {runs_on}"
                        if uses:
                            job_line += f" [uses: `{uses}`]"
                        lines.append(job_line)
                        
                        # Key steps
                        steps = job_data.get("steps", [])
                        if steps:
                            step_names = [s.get("name", "") or s.get("uses", "") for s in steps[:5]]
                            step_names = [s for s in step_names if s]
                            if step_names:
                                lines.append(f"    - Key steps: {', '.join(step_names[:5])}")
                        
                        # Config params
                        matrix = job_data.get("matrix", {})
                        if matrix and matrix.get("include"):
                            configs = matrix.get("include", [])
                            lines.append(f"    - Matrix configs: {len(configs)} variants")
                            # Show sample
                            for cfg in configs[:2]:
                                if isinstance(cfg, dict):
                                    cfg_items = list(cfg.items())[:3]
                                    cfg_str = ", ".join(f"{k}={v}" for k, v in cfg_items)
                                    lines.append(f"      - `{cfg_str}`")
                        
                        with_params = job_data.get("with_params", {})
                        if with_params:
                            params_list = list(with_params.items())[:4]
                            params_str = ", ".join(f"{k}={str(v)[:30]}..." if len(str(v)) > 30 else f"{k}={v}" for k, v in params_list)
                            lines.append(f"    - Config: {params_str}")
                
                if notes:
                    lines.append(f"- **Notes**: {notes}")
                
                lines.append("")
        
        else:
            lines.append("*No workflows in this category.*")
            lines.append("")
        
        # List related scripts
        cat_scripts = [s for s in raw_data.get("scripts", []) 
                       if llm_analysis.script_classifications.get(s.get("name", ""), {}).get("category") == cat_id]
        if cat_scripts:
            lines.append("### Related Scripts")
            lines.append("")
            for script in cat_scripts:
                script_name = script.get("name", "")
                script_path = script.get("path", "")
                script_classification = llm_analysis.script_classifications.get(script_name, {})
                purpose = script_classification.get("purpose", "")
                funcs = script.get("functions", [])
                
                lines.append(f"- `{script_path}`")
                if purpose:
                    lines.append(f"  - {purpose}")
                if funcs:
                    lines.append(f"  - Functions: {', '.join(funcs[:5])}")
            lines.append("")
        
        # List related actions
        cat_actions = [a for a in raw_data.get("actions", [])
                       if llm_analysis.action_classifications.get(a.get("name", ""), {}).get("category") == cat_id]
        if cat_actions:
            lines.append("### Related Actions")
            lines.append("")
            for action in cat_actions:
                action_name = action.get("name", "")
                action_desc = action.get("description", "")
                action_classification = llm_analysis.action_classifications.get(action_name, {})
                purpose = action_classification.get("purpose", action_desc)
                
                lines.append(f"- `{action_name}`")
                if purpose:
                    lines.append(f"  - {purpose}")
            lines.append("")
        
        lines.append("---")
        lines.append("")
    
    # Uncategorized workflows
    uncategorized = workflows_by_category.get("uncategorized", [])
    if uncategorized:
        lines.append("## 📄 Uncategorized Workflows")
        lines.append("")
        for wf_name, wf_data, _ in uncategorized:
            lines.append(f"- `{wf_name}` - {wf_data.get('name', 'No name')}")
        lines.append("")
    
    # Summary section
    lines.append("## Summary Statistics")
    lines.append("")
    
    total_workflows = len(raw_data.get("workflows", {}))
    total_jobs = sum(len(wf.get("jobs", {})) for wf in raw_data.get("workflows", {}).values())
    total_actions = len(raw_data.get("actions", []))
    total_scripts = len(raw_data.get("scripts", []))
    
    lines.append(f"| Item | Count |")
    lines.append(f"|------|-------|")
    lines.append(f"| Workflows | {total_workflows} |")
    lines.append(f"| Jobs | {total_jobs} |")
    lines.append(f"| Composite Actions | {total_actions} |")
    lines.append(f"| CI Scripts | {total_scripts} |")
    lines.append(f"| Categories | {len(llm_analysis.categories)} |")
    lines.append("")
    
    if llm_analysis.key_patterns:
        lines.append("### Key Patterns")
        lines.append("")
        for pattern in llm_analysis.key_patterns:
            lines.append(f"- {pattern}")
        lines.append("")
    
    if llm_analysis.recommendations:
        lines.append("### Recommendations")
        lines.append("")
        for rec in llm_analysis.recommendations:
            lines.append(f"- {rec}")
        lines.append("")
    
    # Write to file
    content = "\n".join(lines)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
    
    return content


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python ci_diagram_generator.py prompt <raw_data.json> - Generate LLM prompt")
        print("  python ci_diagram_generator.py diagram <raw_data.json> <llm_response.json> [output_file] - Generate diagram")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "prompt":
        # Generate LLM prompt from raw data
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        prompt = generate_llm_prompt(raw_data)
        print(prompt)
    
    elif command == "diagram":
        # Generate diagram from raw data + LLM analysis
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        with open(sys.argv[3], "r", encoding="utf-8") as f:
            llm_response_str = f.read()
        
        llm_analysis = parse_llm_response(llm_response_str)
        output_file = sys.argv[4] if len(sys.argv) > 4 else "CI_ARCHITECTURE.md"
        
        diagram = generate_architecture_diagram(raw_data, llm_analysis, output_file)
        print(f"Architecture diagram saved to: {output_file}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)