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
│  • Extracts workflow/job/step details                                   │
│  • Builds relationship graphs                                           │
│  • Maps scripts to directories                                          │
│  • Outputs comprehensive JSON                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ JSON (raw_data.json)
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    LLM ANALYSIS                                         │
│  • Receives detailed prompt with all extracted data                     │
│  • Creates functional categories (PR CI, Build, Test, etc.)            │
│  • Classifies workflows by purpose                                      │
│  • Identifies key configs and parameters                                │
│  • Maps scripts to categories                                           │
│  • Returns structured JSON analysis                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ JSON (llm_response.json)
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    DIAGRAM GENERATION (Python)                          │
│  ci_diagram_generator.py                                                │
│  • Merges raw data with LLM analysis                                    │
│  • Generates Markdown architecture document                             │
│  • Shows categories with scripts, jobs, configs                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## Files

| File | Purpose |
|------|---------|
| `ci_data_extractor.py` | Comprehensive data extraction - workflows, jobs, steps, actions, scripts |
| `ci_diagram_generator.py` | Generates LLM prompts and architecture diagrams |
| `analyze_ci_architecture.py` | Legacy: standalone analyzer with hardcoded rules |

## Usage

### Step 1: Extract Raw Data

```bash
python ci_data_extractor.py /path/to/repo ci_data.json
```

This outputs `ci_data.json` containing:
- All workflow configurations with full job/step details
- Matrix configurations and parameters
- All composite actions with inputs/outputs
- All CI scripts with function analysis
- Relationship graphs (workflow calls, action usages)
- Scripts organized by directory

### Step 2: Generate LLM Prompt

```bash
python ci_diagram_generator.py prompt ci_data.json
```

This generates a detailed prompt for the LLM including:
- Repository structure
- All workflows with jobs, steps, triggers
- Matrix configurations
- Actions and their relationships
- Scripts and their functions

### Step 3: Send Prompt to LLM

Copy the prompt and send to the LLM. The LLM will return a JSON analysis with:
- **Categories**: Functional groupings (PR CI, Build, Test, etc.)
- **Workflow Classifications**: Purpose, importance, key jobs
- **Job Classifications**: Key steps, config params
- **Script Classifications**: Purpose, related workflows
- **Architecture Summary**: Project type, CI philosophy, patterns

Save the LLM response as `llm_response.json`.

### Step 4: Generate Architecture Diagram

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.json CI_ARCHITECTURE.md
```

## Output Format

The generated architecture document includes:

### For Each Category:
- **Description**: What this category accomplishes
- **Script Directory**: Where related scripts are located
- **Workflows**: List of workflows with:
  - Purpose and importance
  - Triggers
  - Jobs with key steps
  - Config parameters (matrix, with_params)
- **Related Scripts**: Scripts in this category
- **Related Actions**: Composite actions used

### Summary Statistics:
- Total workflows, jobs, actions, scripts
- Key patterns identified
- Recommendations

## LLM Prompt Guidelines

The prompt instructs the LLM to:

1. **Create functional categories** based on purpose, not names
2. **Classify everything**: Every workflow, job, action, script
3. **Include directory mappings**: Link categories to script directories
4. **Show config details**: Matrix configs, parameters, inputs
5. **Provide summaries**: Purpose and description for each item

## Common Categories

| Category | Description | Typical Workflows |
|----------|-------------|-------------------|
| Pull Request CI | PR validation | `pull.yml`, `lint.yml` |
| Trunk/Post-Merge | After merge testing | `trunk.yml` |
| Scheduled CI | Periodic testing | `periodic.yml`, `nightly.yml` |
| Build Pipelines | Compilation | `*-build.yml` |
| Testing | Test suites | `*-test.yml`, `inductor.yml` |
| Binary/Release | Artifacts | `generated-*-binary-*.yml` |
| Linting | Code quality | `lint.yml` |
| Documentation | Docs | `docs.yml` |
| Utility | Helpers | `trymerge.yml`, `revert.yml` |

## Example Workflow

```bash
# 1. Extract data from a project
python ci_data_extractor.py /path/to/pytorch ci_data.json

# 2. Generate prompt
python ci_diagram_generator.py prompt ci_data.json > prompt.txt

# 3. Send prompt.txt to LLM, save response as analysis.json

# 4. Generate diagram
python ci_diagram_generator.py diagram ci_data.json analysis.json CI_ARCHITECTURE.md

# 5. View the result
cat CI_ARCHITECTURE.md
```

## Requirements

- Python 3.8+
- PyYAML

```bash
pip install pyyaml
```

## What Gets Extracted

### Workflows
- Name, path, triggers
- Environment variables
- Concurrency settings
- All jobs with:
  - runs-on, needs, if conditions
  - Steps with name, uses, run, with_params
  - Matrix configurations (expanded)
  - with_params for reusable workflows
  - Outputs

### Actions
- Description
- Inputs (name, description, required, default)
- Outputs
- Steps called
- Used by which workflows

### Scripts
- Path and type (.py, .sh, etc.)
- Functions (extracted)
- Imports (for Python)
- Called by which jobs

### Relationships
- Workflow call graph (who calls whom)
- Job dependency graph
- Action usage graph

## Benefits of This Architecture

1. **Comprehensive**: Extracts all details - steps, configs, parameters
2. **Directory Mapping**: Shows which scripts relate to which categories
3. **Config Details**: Displays matrix configs, with_params, etc.
4. **Flexible Categories**: LLM creates categories based on actual project
5. **Intelligent Analysis**: LLM understands purpose and relationships
6. **Maintainable**: No hardcoded patterns - LLM adapts automatically