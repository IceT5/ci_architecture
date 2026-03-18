# CI Architecture Analyzer

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A powerful tool for analyzing GitHub Actions CI/CD architecture with LLM-powered intelligent classification and understanding.

## Features

- **Comprehensive Data Extraction**: Extracts all CI/CD components including workflows, jobs, steps, composite actions, and scripts
- **LLM-Powered Analysis**: Uses LLM for intelligent classification and understanding, no hardcoded rules
- **Reusable Workflow Support**: Full support for GitHub Actions reusable workflows (`workflow_call`)
- **Matrix Job Expansion**: Complete expansion of matrix configurations for all job variants
- **Script Analysis**: Analyzes Python, Shell, PowerShell, and Batch scripts with function extraction
- **Relationship Mapping**: Builds workflow call graphs, job dependency graphs, and action usage graphs
- **Pre-commit Integration**: Extracts and documents pre-commit hook configurations
- **Multi-CI Support**: Supports CircleCI, GitLab CI, Azure Pipelines, and other CI systems

## Design Philosophy

**Minimal code automation, maximum LLM intelligence:**

- **Code only extracts data**: Python scripts extract raw data from workflows, jobs, steps, actions, and scripts
- **LLM does all understanding**: Classification, organization, relationships, and summaries are all handled by LLM
- **No hardcoded categories**: LLM dynamically defines stages and categories based on actual project content
- **Logical organization**: LLM organizes documentation according to CI/CD execution flow

## Installation

### Prerequisites

- Python 3.8+
- PyYAML

### Install Dependencies

```bash
pip install pyyaml
```

## Quick Start

### Step 1: Extract Data

```bash
python ci_data_extractor.py /path/to/repo ci_data.json
```

This outputs `ci_data.json` containing:
- All workflows with job and step details
- Matrix configurations and with_params
- Composite actions with inputs/outputs
- CI scripts with function lists
- Workflow call relationship graph
- Action usage statistics
- Pre-commit configurations

### Step 2: Generate Prompt

**For small/medium projects (≤30 workflows):**

```bash
python ci_diagram_generator.py prompt ci_data.json prompt.txt
```

**For large projects (>30 workflows):**

```bash
python ci_diagram_generator.py split ci_data.json ./prompts/ 10
```

This generates multiple prompt files for parallel processing.

### Step 3: Send to LLM

Read the prompt file and send to your LLM for analysis. Save the response as `llm_response.md`.

### Step 4: Generate Final Document

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.md CI_ARCHITECTURE.md
```

## Project Structure

```
ci_architecture/
├── ci_data_extractor.py      # Core data extraction module
├── ci_diagram_generator.py   # Prompt generation and result processing
├── analyze_ci_architecture.py # Legacy analyzer (deprecated)
├── SKILL.md                   # Skill documentation for LLM agents
├── README.md                  # This file
└── LICENSE                    # Apache 2.0 License
```

## Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Data Extraction (Python)                             │
│  ci_data_extractor.py                                                   │
│  • Scans .github/workflows, .github/actions, script directories         │
│  • Extracts all workflows, jobs, steps, configuration parameters        │
│  • Extracts script functions and call relationships                     │
│  • Outputs complete JSON data                                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ ci_data.json
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    Generate LLM Prompt (Python)                         │
│  ci_diagram_generator.py                                                │
│  • Formats raw data into detailed prompt                                │
│  • Includes all workflows, jobs, configurations, relationships          │
│  • Guides LLM to organize content by execution logic                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Prompt
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    LLM Analysis                                         │
│                                                                         │
│  LLM responsibilities:                                                  │
│  • Analyze CI/CD process stages                                         │
│  • Determine execution order                                            │
│  • Show call relationships and dependencies                             │
│  • Organize as readable architecture documentation                      │
│  • Provide key findings and recommendations                             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Markdown document
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    Save Result (Python)                                 │
│  ci_diagram_generator.py                                                │
│  • Clean up format                                                      │
│  • Save as CI_ARCHITECTURE.md                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

## Output Document Structure

The generated architecture document includes:

1. **Project Overview** - Project type and CI/CD overall architecture
2. **CI/CD Flow Diagram** - ASCII diagram showing the overall architecture
3. **Stage-based Content** - Workflows organized by execution stage
4. **Workflow Details** - Complete job lists, dependencies, key configurations
5. **Matrix Job Expansion** - All matrix variants fully listed
6. **Script and Action Index** - Organized by directory/purpose
7. **Pre-commit Configuration** - External and local hooks
8. **Key Findings and Recommendations**
9. **Appendix** - Workflow call relationship tree

## Supported CI Systems

- **GitHub Actions** (primary focus)
  - Workflows (.github/workflows/*.yml)
  - Composite Actions (.github/actions/*/action.yml)
  - Reusable Workflows (workflow_call trigger)
- **CircleCI** (.circleci/config.yml)
- **GitLab CI** (.gitlab-ci.yml)
- **Azure Pipelines** (azure-pipelines.yml)
- **Jenkins** (Jenkinsfile)
- **Travis CI** (.travis.yml)
- **Drone CI** (.drone.yml)
- **Buildkite** (buildkite.yml)
- **Pre-commit** (.pre-commit-config.yaml)

## Script Analysis

Supports analysis of:
- **Python** (.py) - Function definitions, imports, subprocess calls
- **Shell** (.sh) - Functions, source commands, script executions
- **PowerShell** (.ps1) - Dot-sourcing, script calls
- **Batch** (.bat) - Call commands, script references

## Key Classes

### CIDataExtractor

Main extraction class that:
- Finds CI-related directories
- Extracts workflow data with full details
- Parses composite actions
- Analyzes scripts with nested call tracking
- Builds relationship graphs

### Data Classes

- `WorkflowData` - Complete workflow information
- `JobData` - Job details with matrix expansion
- `StepData` - Step execution details
- `ActionData` - Composite action information
- `ScriptData` - Script analysis results
- `PreCommitConfigData` - Pre-commit configuration
- `WorkflowCallInput` / `WorkflowCallOutput` - Reusable workflow I/O

## Requirements

- Python 3.8+
- PyYAML

```bash
pip install pyyaml
```

## License

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.

## Copyright

Copyright (c) 2026 IceT5. All rights reserved.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**IceT5**

---

*This tool is designed to work with LLM agents for maximum flexibility and intelligence in CI/CD architecture analysis.*