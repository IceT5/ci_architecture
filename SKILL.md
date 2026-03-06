# CI Architecture Analysis Skill

Analyzes GitHub Actions CI/CD architecture and generates comprehensive diagrams.

## Overview

This skill discovers all CI/CD-related code from a repository and generates detailed ASCII architecture diagrams showing the complete workflow stages.

## What This Skill Does

### 1. Data Collection
Discovers CI code from multiple directories:
- `.github/workflows/*.yml` - GitHub Actions workflows
- `.github/actions/*/action.yml` - Composite actions  
- `.ci/` or similar - CI execution scripts
- `test/` - Test categories

### 2. Architecture Diagram Generation

Generates ASCII diagram with workflow stages:

1. **TRIGGER SOURCES** - What starts CI/CD (pull_request, push, schedule, etc.)
2. **MAIN ENTRY WORKFLOWS** - Core CI workflows (pull, trunk, periodic, lint)
3. **PRE-BUILD PHASE** - Orchestration (runner determination, target selection)
4. **BUILD JOBS** - Platform-specific builds (Linux, macOS, Windows, CUDA, etc.)
5. **TEST CONFIGURATIONS** - Test types and categories
6. **TEST WORKFLOWS** - Reusable test workflows
7. **COMPOSITE ACTIONS** - Setup, teardown, artifacts actions
8. **TEST EXECUTION** - CI scripts and environment variables
9. **BINARY BUILD WORKFLOWS** - Package/wheel generation
10. **RUNNER TYPES** - Compute resources

## Usage

```bash
python explore.py <repo_path> <output_dir>
```

Example:
```bash
python explore.py /path/to/repo /path/to/output
```

## Output

Generates `CI_ARCHITECTURE.md` containing:
- ASCII architecture diagram with all stages
- Detailed workflow information
- Job configurations
- Test categories and counts
- Runner types

## Requirements

- Python 3.8+
- PyYAML

## Notes

- Works with any GitHub Actions repository
- Automatically categorizes workflows by type
- Generic - analyzes whatever exists in the repository
- No hardcoded project-specific logic
