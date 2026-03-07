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


@dataclass
class CategoryInfo:
    """Category defined by LLM."""
    name: str  # Category identifier (e.g., "pull_ci", "integration_tests")
    display_name: str  # Human readable name (e.g., "Pull Request CI", "Integration Tests")
    description: str  # LLM-provided description
    icon: str = "📄"  # Emoji icon for the category


@dataclass
class WorkflowClassification:
    """LLM's classification of a workflow."""
    filename: str
    category: str  # Reference to CategoryInfo.name
    purpose: str  # What this workflow does (LLM analyzed)
    importance: str  # "primary", "secondary", "auxiliary"
    notes: str = ""  # Additional notes from LLM


@dataclass  
class ActionClassification:
    """LLM's classification of an action."""
    name: str
    category: str
    purpose: str
    importance: str
    notes: str = ""


@dataclass
class ScriptClassification:
    """LLM's classification of a script."""
    name: str
    purpose: str
    related_workflows: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class LLMAnalysisResult:
    """Complete LLM analysis result structure."""
    # LLM-defined categories
    workflow_categories: List[Dict] = field(default_factory=list)
    action_categories: List[Dict] = field(default_factory=list)
    
    # Classifications
    workflow_classifications: Dict[str, Dict] = field(default_factory=dict)  # filename -> classification
    action_classifications: Dict[str, Dict] = field(default_factory=dict)  # name -> classification
    script_classifications: Dict[str, Dict] = field(default_factory=dict)  # name -> classification
    
    # LLM's understanding of the project
    project_type: str = ""  # e.g., "Python Library", "Web Application", "Mobile App"
    ci_philosophy: str = ""  # LLM's analysis of CI approach
    key_patterns: List[str] = field(default_factory=list)  # Notable patterns discovered
    
    # Architecture description (LLM generated)
    architecture_summary: str = ""
    recommendations: List[str] = field(default_factory=list)


def generate_architecture_diagram(
    raw_data: Dict,  # From ci_data_extractor
    llm_analysis: LLMAnalysisResult,  # From LLM
    output_file: str
) -> str:
    """Generate architecture diagram from raw data + LLM analysis."""
    
    lines = []
    
    # Header
    lines.append("```")
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + f" {raw_data['repo_name'].upper()} CI/CD ARCHITECTURE".center(97) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("")
    
    # LLM Summary
    if llm_analysis.architecture_summary:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " ARCHITECTURE SUMMARY".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        for line in llm_analysis.architecture_summary.split("\n")[:10]:
            lines.append(f"│  {line:<95}│")
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # Project Type
    if llm_analysis.project_type:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " PROJECT TYPE".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        lines.append(f"│  {llm_analysis.project_type:<95}│")
        if llm_analysis.ci_philosophy:
            lines.append("│".ljust(98) + "│")
            lines.append(f"│  CI Philosophy: {llm_analysis.ci_philosophy[:78]}".ljust(98) + "│")
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # Triggers
    all_triggers = set()
    for wf_name, wf in raw_data.get("workflows", {}).items():
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
    
    # Workflows by LLM-defined categories
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " WORKFLOWS (by LLM categories)".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    # Group workflows by LLM-defined categories
    categorized_workflows = {}
    for wf_name, wf in raw_data.get("workflows", {}).items():
        classification = llm_analysis.workflow_classifications.get(wf_name, {})
        category = classification.get("category", "other")
        if category not in categorized_workflows:
            categorized_workflows[category] = []
        categorized_workflows[category].append((wf_name, wf, classification))
    
    # Get category display info
    category_info = {cat["name"]: cat for cat in llm_analysis.workflow_categories}
    
    for category in llm_analysis.workflow_categories:
        cat_name = category["name"]
        display_name = category.get("display_name", cat_name)
        icon = category.get("icon", "📄")
        
        wfs = categorized_workflows.get(cat_name, [])
        if wfs:
            lines.append(f"│  {icon} [{display_name}] ({len(wfs)} workflows)".ljust(98) + "│")
            for wf_name, wf_data, classification in wfs[:5]:
                jobs_count = len(wf_data.get("jobs", {}))
                purpose = classification.get("purpose", "")[:50] if classification.get("purpose") else ""
                callers_count = len(wf_data.get("callers", []))
                caller_info = f", {callers_count} callers" if callers_count else ""
                lines.append(f"│      • {wf_name:<30} ({jobs_count} jobs{caller_info})"[:97] + "│")
                if purpose:
                    lines.append(f"│        └─ {purpose}".ljust(98) + "│")
            lines.append("│" + " " * 97 + "│")
    
    # Uncategorized workflows
    uncategorized = categorized_workflows.get("other", [])
    if uncategorized:
        lines.append("│  📄 [Other]".ljust(98) + "│")
        for wf_name, wf_data, _ in uncategorized[:5]:
            jobs_count = len(wf_data.get("jobs", {}))
            lines.append(f"│      • {wf_name:<30} ({jobs_count} jobs)".ljust(98) + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # Workflow Call Relationships (raw data)
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " WORKFLOW CALL RELATIONSHIPS".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    relationships = raw_data.get("relationships", {})
    workflow_calls = relationships.get("workflow_calls", {})
    
    if workflow_calls:
        for callee, callers in list(workflow_calls.items())[:8]:
            callee_short = Path(callee).name if "/" in callee else callee
            callers_str = ", ".join([c.split("::")[0] for c in callers[:3]])
            if len(callers) > 3:
                callers_str += f" (+{len(callers)-3})"
            lines.append(f"│  📦 {callee_short:<30} ← {callers_str}".ljust(98) + "│")
    else:
        lines.append("│  No workflow calls detected.".ljust(98) + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")
    
    # Actions by LLM-defined categories
    if raw_data.get("actions"):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " COMPOSITE ACTIONS (by LLM categories)".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        # Group actions by LLM categories
        action_categories = {}
        for action in raw_data.get("actions", []):
            name = action.get("name", "")
            classification = llm_analysis.action_classifications.get(name, {})
            category = classification.get("category", "utility")
            if category not in action_categories:
                action_categories[category] = []
            action_categories[category].append(action)
        
        # Get action category info
        action_cat_info = {cat["name"]: cat for cat in llm_analysis.action_categories}
        
        for category in llm_analysis.action_categories:
            cat_name = category["name"]
            display_name = category.get("display_name", cat_name)
            icon = category.get("icon", "📦")
            
            actions = action_categories.get(cat_name, [])
            if actions:
                lines.append(f"│  {icon} {display_name}:".ljust(98) + "│")
                for action in actions[:5]:
                    name = action.get("name", "")
                    used_by = action.get("used_by", [])
                    usage_info = f" ({len(used_by)} uses)" if used_by else ""
                    lines.append(f"│    • {name:<50}{usage_info}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # CI Scripts (with LLM classification)
    if raw_data.get("scripts"):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " CI SCRIPTS (analyzed by LLM)".center(97) + "│")
        lines.append("├" + "─" * 97 + "┤")
        
        for script in raw_data.get("scripts", [])[:10]:
            name = script.get("name", "")
            classification = llm_analysis.script_classifications.get(name, {})
            purpose = classification.get("purpose", "")[:60] if classification else ""
            type_icon = "🐍" if script.get("type") == ".py" else "🐚" if script.get("type") == ".sh" else "📄"
            lines.append(f"│  {type_icon} {name:<25} - {purpose}".ljust(98) + "│")
        
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")
    
    # Summary
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " SUMMARY".center(97) + "│")
    lines.append("├" + "─" * 97 + "┤")
    
    total_workflows = len(raw_data.get("workflows", {}))
    total_jobs = sum(len(wf.get("jobs", {})) for wf in raw_data.get("workflows", {}).values())
    total_actions = len(raw_data.get("actions", []))
    total_scripts = len(raw_data.get("scripts", []))
    
    lines.append(f"│  Total Workflows: {total_workflows:<78}│")
    lines.append(f"│  Total Jobs: {total_jobs:<82}│")
    lines.append(f"│  Composite Actions: {total_actions:<71}│")
    lines.append(f"│  CI Scripts: {total_scripts:<77}│")
    
    if llm_analysis.key_patterns:
        lines.append("│".ljust(98) + "│")
        lines.append("│  🔑 Key Patterns Discovered:".ljust(98) + "│")
        for pattern in llm_analysis.key_patterns[:5]:
            lines.append(f"│    • {pattern[:80]}".ljust(98) + "│")
    
    if llm_analysis.recommendations:
        lines.append("│".ljust(98) + "│")
        lines.append("│  💡 Recommendations:".ljust(98) + "│")
        for rec in llm_analysis.recommendations[:3]:
            lines.append(f"│    • {rec[:80]}".ljust(98) + "│")
    
    lines.append("└" + "─" * 97 + "┘")
    lines.append("```")
    
    # Write to file
    content = "\n".join(lines)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
    
    return content


def generate_llm_prompt(raw_data: Dict) -> str:
    """Generate a prompt for LLM to analyze the CI data."""
    
    prompt = """# CI/CD Architecture Analysis Request

I have extracted the following CI/CD data from a repository. Please analyze it and provide:
1. Workflow classifications and categories
2. Action classifications
3. Script purposes
4. Project type and CI philosophy
5. Architecture summary

## Raw Data

### Workflows
"""
    
    # Add workflow info
    for wf_name, wf in list(raw_data.get("workflows", {}).items())[:20]:
        prompt += f"\n**{wf_name}**:\n"
        prompt += f"- Name: {wf.get('name', 'N/A')}\n"
        prompt += f"- Triggers: {', '.join(wf.get('triggers', []))}\n"
        prompt += f"- Jobs: {list(wf.get('jobs', {}).keys())[:10]}\n"
        
        # Add content summary (truncated)
        summary = wf.get('content_summary', '')[:500]
        if summary:
            prompt += f"- Content Preview:\n```\n{summary}\n```\n"
    
    # Add actions info
    if raw_data.get('actions'):
        prompt += "\n### Composite Actions\n"
        for action in raw_data.get('actions', [])[:20]:
            prompt += f"- {action.get('name')}: {action.get('description', 'No description')[:100]}\n"
    
    # Add scripts info
    if raw_data.get('scripts'):
        prompt += "\n### CI Scripts\n"
        for script in raw_data.get('scripts', [])[:20]:
            prompt += f"- {script.get('name')} ({script.get('type')}): {script.get('content_preview', '')[:200]}\n"
    
    # Add relationships
    relationships = raw_data.get('relationships', {})
    if relationships.get('workflow_calls'):
        prompt += "\n### Workflow Calls\n"
        for callee, callers in list(relationships['workflow_calls'].items())[:10]:
            prompt += f"- {callee} <- {callers}\n"
    
    # Add expected output format
    prompt += """

## Expected Output Format

Please provide your analysis in the following JSON format:

```json
{
  "workflow_categories": [
    {
      "name": "category_id",
      "display_name": "Human Readable Name",
      "description": "What this category is for",
      "icon": "📄"
    }
  ],
  "action_categories": [
    {
      "name": "category_id",
      "display_name": "Human Readable Name",
      "description": "What this category is for",
      "icon": "📦"
    }
  ],
  "workflow_classifications": {
    "workflow_file.yml": {
      "category": "category_id",
      "purpose": "What this workflow does",
      "importance": "primary|secondary|auxiliary",
      "notes": "Additional observations"
    }
  },
  "action_classifications": {
    "action_name": {
      "category": "category_id",
      "purpose": "What this action does",
      "importance": "primary|secondary|auxiliary"
    }
  },
  "script_classifications": {
    "script_name.sh": {
      "purpose": "What this script does",
      "related_workflows": ["workflow1.yml"],
      "notes": "Additional observations"
    }
  },
  "project_type": "Type of project (e.g., Python Library, Web Application)",
  "ci_philosophy": "Analysis of the CI/CD approach used",
  "key_patterns": ["Pattern 1", "Pattern 2"],
  "architecture_summary": "Brief summary of the CI architecture",
  "recommendations": ["Recommendation 1", "Recommendation 2"]
}
```
"""
    
    return prompt


def parse_llm_response(llm_response: str) -> LLMAnalysisResult:
    """Parse LLM's JSON response into LLMAnalysisResult."""
    
    # Extract JSON from response
    json_match = None
    if "```json" in llm_response:
        start = llm_response.find("```json") + 7
        end = llm_response.find("```", start)
        json_str = llm_response[start:end].strip()
    elif "```" in llm_response:
        start = llm_response.find("```") + 3
        end = llm_response.find("```", start)
        json_str = llm_response[start:end].strip()
    else:
        json_str = llm_response
    
    try:
        data = json.loads(json_str)
    except json.JSONDecodeError:
        # Return empty result if parsing fails
        return LLMAnalysisResult()
    
    return LLMAnalysisResult(
        workflow_categories=data.get("workflow_categories", []),
        action_categories=data.get("action_categories", []),
        workflow_classifications=data.get("workflow_classifications", {}),
        action_classifications=data.get("action_classifications", {}),
        script_classifications=data.get("script_classifications", {}),
        project_type=data.get("project_type", ""),
        ci_philosophy=data.get("ci_philosophy", ""),
        key_patterns=data.get("key_patterns", []),
        architecture_summary=data.get("architecture_summary", ""),
        recommendations=data.get("recommendations", [])
    )


def merge_data_and_analysis(raw_data: Dict, llm_analysis: LLMAnalysisResult) -> Dict:
    """Merge raw data with LLM analysis for diagram generation."""
    return {
        "raw_data": raw_data,
        "llm_analysis": llm_analysis
    }


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python ci_diagram_generator.py prompt <raw_data.json> - Generate LLM prompt")
        print("  python ci_diagram_generator.py diagram <raw_data.json> <llm_response.json> - Generate diagram")
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