---
name: ci_architecture
description: |
  Analyzes GitHub Actions CI/CD architecture with LLM-powered classification and understanding.
  
  TRIGGERS: "Analyze ci/cd", "Analyze workflow", "CI architecture", "Test infrastructure", "CI/CD diagram"
---

# CI Architecture Analysis Skill

Analyzes GitHub Actions CI/CD architecture with a **separation of concerns**:
- **Python scripts** handle data extraction and diagram generation
- **LLM** handles classification and understanding

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    DATA EXTRACTION (Python)                             │
│  ci_data_extractor.py                                                   │
│  • Scans CI directories                                                 │
│  • Extracts raw workflow/action/script data                            │
│  • Builds relationship graphs                                           │
│  • Outputs JSON (no classification decisions)                          │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ JSON
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    LLM ANALYSIS                                         │
│  • Understands project context                                          │
│  • Creates categories based on project patterns                         │
│  • Classifies workflows by actual purpose                              │
│  • Analyzes scripts semantics                                           │
│  • Returns structured JSON analysis                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ JSON
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    DIAGRAM GENERATION (Python)                          │
│  ci_diagram_generator.py                                                │
│  • Receives raw data + LLM analysis                                    │
│  • Generates ASCII architecture diagram                                │
│  • Categories are LLM-defined, dynamic                                 │
└─────────────────────────────────────────────────────────────────────────┘
```

## Files

| File | Purpose |
|------|---------|
| `ci_data_extractor.py` | Pure data extraction - no classification logic |
| `ci_diagram_generator.py` | Generates diagrams from raw data + LLM analysis |
| `analyze_ci_architecture.py` | Legacy: standalone analyzer with hardcoded rules |

## Usage

### Step 1: Extract Raw Data

```bash
python ci_data_extractor.py /path/to/repo ci_data.json
```

This outputs `ci_data.json` containing:
- All workflow configurations (triggers, jobs, steps)
- All composite actions
- All CI scripts with previews
- Relationship graphs (workflow calls, job dependencies, action usages)

### Step 2: Generate LLM Prompt

```bash
python ci_diagram_generator.py prompt ci_data.json
```

This generates a prompt for the LLM. Send this prompt to the LLM and save the response.

### Step 3: Generate Architecture Diagram

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.json CI_ARCHITECTURE.md
```

## What Gets Extracted vs Analyzed

### Extracted by Python (no understanding required)
- File listings and directory structure
- YAML parsing results (triggers, jobs, steps)
- Raw relationships (which workflow calls which)
- Job dependency graphs
- Script content previews

### Analyzed by LLM (requires understanding)
- **Workflow categories**: LLM creates categories based on what workflows actually do
- **Workflow purposes**: What each workflow is for
- **Action classifications**: How to group actions
- **Script purposes**: What scripts do
- **Project type**: What kind of project this is
- **CI philosophy**: The approach/patterns used
- **Recommendations**: Improvement suggestions

## LLM Response Format

The LLM should return JSON in this format:

```json
{
  "workflow_categories": [
    {
      "name": "pull_validation",
      "display_name": "Pull Request Validation",
      "description": "Validates PRs before merge",
      "icon": "🔄"
    }
  ],
  "workflow_classifications": {
    "pull.yml": {
      "category": "pull_validation",
      "purpose": "Runs tests and checks on pull requests",
      "importance": "primary"
    }
  },
  "project_type": "Python Library",
  "ci_philosophy": "GitHub Flow with comprehensive PR validation",
  "architecture_summary": "This project uses...",
  "key_patterns": ["Reusable workflows for DRY", "Matrix for multi-platform"],
  "recommendations": ["Consider adding caching"]
}
```

## Benefits of This Architecture

1. **Truly Generic**: No hardcoded patterns that fail on different naming conventions
2. **Adaptive**: LLM creates categories based on what exists in the project
3. **Intelligent Understanding**: LLM explains what workflows do, not just their names
4. **Project Context**: LLM understands the type of project and its CI philosophy
5. **Maintainable**: No need to update code for new patterns - LLM adapts automatically

## Example Workflow

```bash
# 1. Extract data
python ci_data_extractor.py /path/to/pytorch ci_data.json

# 2. Generate prompt
python ci_diagram_generator.py prompt ci_data.json > prompt.txt

# 3. Send prompt.txt to LLM, save response as analysis.json

# 4. Generate diagram
python ci_diagram_generator.py diagram ci_data.json analysis.json CI_ARCHITECTURE.md
```

## Legacy Mode

The original `analyze_ci_architecture.py` still works as a standalone tool:

```bash
python analyze_ci_architecture.py /path/to/repo
```

This uses hardcoded classification rules and works well for projects following common conventions.

## Requirements

- Python 3.8+
- PyYAML

```bash
pip install pyyaml