---
name: ci_architecture
description: |
  Analyzes GitHub Actions CI/CD architecture and generates comprehensive ASCII architecture diagrams.
  
  TRIGGERS: "Analyze ci/cd", "Analyze workflow", "CI architecture", "Test infrastructure", "CI/CD diagram"
---

# CI Architecture Analysis Skill

Analyzes GitHub Actions CI/CD architecture and generates comprehensive ASCII architecture diagrams for any project.

## Overview

This skill performs deep analysis of a project's CI/CD infrastructure by examining workflow files, composite actions, test scripts, and related configurations. It produces a detailed architecture diagram that helps understand:

- **Trigger Sources** - What events start CI/CD pipelines
- **Main Workflows** - Core CI workflows categorized by purpose
- **Reusable Workflows** - Shared workflow templates
- **Composite Actions** - Reusable action components
- **Test Configurations** - Test types and matrix configurations
- **CI Scripts** - Execution scripts and utilities
- **Runner Types** - Compute resources used

## What This Skill Does

### 1. Data Collection
Discovers CI code from multiple directories:
- `.github/workflows/*.yml` / `*.yaml` - GitHub Actions workflows
- `.github/actions/*/action.yml` - Composite actions  
- `.ci/` - CI execution scripts
- `ci/` - Alternative CI scripts location
- `scripts/` - Build and utility scripts
- `test/` or `tests/` - Test directories

### 2. Analysis Components

#### Workflow Analysis
- Identifies entry workflows vs reusable workflows (prefixed with `_`)
- Extracts trigger types (pull_request, push, schedule, workflow_dispatch, etc.)
- Maps job dependencies and relationships
- Categorizes workflows by purpose:
  - **pull_ci** - Pull request validation
  - **trunk_ci** - Main branch/post-merge CI
  - **periodic** - Scheduled/cron jobs
  - **lint** - Code quality checks
  - **test** - Test workflows
  - **build** - Build workflows
  - **release** - Release/publish workflows
  - **container** - Docker/container workflows
  - **performance** - Benchmark workflows
  - **security** - Security scanning
  - **reusable** - Called by other workflows
  - **manual** - Manual trigger only

#### Job Analysis
- Extracts job names and configurations
- Identifies runner requirements
- Parses matrix strategies for parallel execution
- Maps job dependencies (needs)

#### Test Configuration Analysis
- Extracts test configurations from workflow matrices
- Identifies common config keys: config, test_config, test_type, suite, category
- Groups configurations by workflow

#### Infrastructure Analysis
- Composite actions categorized by purpose:
  - **setup** - Environment setup actions
  - **teardown** - Cleanup actions
  - **artifacts** - Upload/download actions
  - **testing** - Test-related actions
  - **build** - Build actions
  - **caching** - Cache actions
  - **utility** - General purpose actions

### 3. Architecture Diagram Generation

Generates comprehensive ASCII diagram with sections:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    [REPO_NAME] CI/CD ARCHITECTURE                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           TRIGGER SOURCES                                │
│  • pull_request  • push  • schedule  • workflow_dispatch  ...           │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           MAIN WORKFLOWS                                 │
│  🔄 [PULL_CI]  📦 [TRUNK_CI]  ⏰ [PERIODIC]  🔍 [LINT]  ...             │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                              [Reusable Workflows]
                                    │
                                    ▼
                              [Composite Actions]
                                    │
                                    ▼
                              [CI Scripts]
                                    │
                                    ▼
                              [Runner Types]
```

## Usage

### Command Line
```bash
python analyze_ci_architecture.py [repo_path] [output_file]
```

**Parameters:**
- `repo_path` - Path to the repository root (default: current directory)
- `output_file` - Output file path (default: `CI_ARCHITECTURE.md`)

**Examples:**
```bash
# Analyze current directory
python analyze_ci_architecture.py

# Analyze specific repository
python analyze_ci_architecture.py /path/to/project

# Specify output file
python analyze_ci_architecture.py /path/to/repo output.md
```

### As an AI Skill
When invoked by an AI agent, this skill will:
1. Analyze the target repository's CI/CD infrastructure
2. Generate a comprehensive architecture document
3. Provide workflow categorization and job details
4. Include runner types and test configurations

## Output

Generates `CI_ARCHITECTURE.md` containing:

### 1. ASCII Architecture Diagram
Visual representation of the entire CI/CD pipeline with:
- Trigger sources with descriptions
- Main workflows categorized by purpose
- Reusable workflows with job counts
- Composite actions grouped by category
- Test configurations extracted from matrices
- CI execution scripts
- Runner types with usage counts

### 2. Summary Statistics
- Total workflows count
- Entry vs reusable workflow breakdown
- Total jobs across all workflows
- Composite actions count
- CI scripts count
- Test configurations count
- Runner types count

## Features

### Generic Design
- Works with **any** GitHub Actions repository
- No hardcoded project-specific logic
- Automatically discovers CI infrastructure
- Handles various naming conventions

### Smart Categorization
- Pattern-based workflow categorization
- Trigger-based fallback categorization
- Action grouping by functionality

### Comprehensive Analysis
- Parses complex matrix strategies
- Extracts job dependencies
- Identifies self-hosted vs GitHub-hosted runners
- Discovers scripts across multiple directories

## Requirements

- Python 3.8+
- PyYAML

## Installation

```bash
pip install pyyaml
```

## File Structure

```
ci_architecture/
├── SKILL.md                    # This file - skill description
├── example.md                  # Example output (PyTorch case study)
└── analyze_ci_architecture.py  # Main analysis script
```

## How It Works

1. **Directory Discovery**: Scans common CI directories for workflows and actions
2. **Workflow Parsing**: Parses YAML files and handles GitHub Actions specifics
3. **Trigger Extraction**: Identifies all trigger types for each workflow
4. **Job Analysis**: Extracts job configurations, matrices, and dependencies
5. **Categorization**: Classifies workflows by purpose using patterns
6. **Action Discovery**: Finds and categorizes composite actions
7. **Script Discovery**: Locates CI-related scripts in common locations
8. **Runner Extraction**: Identifies runner types from job configurations
9. **Diagram Generation**: Produces formatted ASCII architecture diagram

## Common Use Cases

1. **Project Onboarding**: Quickly understand a new project's CI/CD infrastructure
2. **CI Migration**: Document existing CI before migrating to a new system
3. **Documentation**: Generate CI architecture documentation automatically
4. **Auditing**: Review and audit CI/CD configurations
5. **Optimization**: Identify opportunities to parallelize or optimize workflows

## Supported CI Systems

- **GitHub Actions** (primary support)
- Future support planned for:
  - GitLab CI
  - CircleCI
  - Azure Pipelines

## Limitations

- Currently focuses on GitHub Actions only
- Complex conditional logic may not be fully represented
- Generated/templated workflows may need manual review
- Self-hosted runner detection depends on naming conventions