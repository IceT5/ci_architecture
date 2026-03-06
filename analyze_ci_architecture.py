#!/usr/bin/env python3
"""
High-Quality CI Architecture Analyzer - Produces very detailed and comprehensive architecture diagrams.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set
from collections import defaultdict


def analyze_workflows_deep(repo_path: str) -> Dict:
    """Deep analysis of GitHub Actions workflows."""
    workflows = {}
    workflows_dir = os.path.join(repo_path, ".github", "workflows")

    if not os.path.exists(workflows_dir):
        return workflows

    for file in os.listdir(workflows_dir):
        if file.endswith((".yml", ".yaml")):
            filepath = os.path.join(workflows_dir, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                wf_data = yaml.safe_load(content)
                if not wf_data:
                    continue

                triggers = []
                on_data = wf_data.get("on") or wf_data.get(True)
                if on_data:
                    if isinstance(on_data, dict):
                        triggers = list(on_data.keys())
                    elif isinstance(on_data, list):
                        triggers = on_data

                jobs = wf_data.get("jobs", {})
                job_names = list(jobs.keys())

                is_entry = len(triggers) > 0 and not file.startswith("_")
                is_reusable = file.startswith("_")

                workflows[file] = {
                    "triggers": triggers,
                    "jobs": job_names,
                    "is_entry": is_entry,
                    "is_reusable": is_reusable,
                    "job_details": jobs,
                    "filepath": filepath,
                }
            except Exception as e:
                pass

    return workflows


def find_orchestration_workflows(workflows: Dict) -> Dict:
    """Find orchestration/pre-build workflows."""
    orchestration = {
        "runner_determinator": [],
        "test_selection": [],
        "target_determination": [],
    }

    for wf_name in workflows.keys():
        wf_lower = wf_name.lower()
        if "runner" in wf_lower and "determinator" in wf_lower:
            orchestration["runner_determinator"].append(wf_name)
        elif "llm" in wf_lower and "td" in wf_lower:
            orchestration["test_selection"].append(wf_name)
        elif "target" in wf_lower and "determination" in wf_lower:
            orchestration["target_determination"].append(wf_name)

    return orchestration


def parse_job_name_detailed(job_name: str) -> Dict:
    """Parse job name to extract very detailed information."""
    jn = job_name.lower()
    result = {
        "name": job_name,
        "os": "",
        "os_version": "",
        "python": "",
        "compiler": "",
        "compiler_version": "",
        "variant": "",
        "cuda": "",
        "cudnn": "",
        "arch": "",
        "special": "",
        "description": "",
        "category": "other",
    }

    if "linux" in jn or "ubuntu" in jn or "focal" in jn or "jammy" in jn:
        result["os"] = "Linux"
        if "focal" in jn:
            result["os_version"] = "Ubuntu 20.04"
        elif "jammy" in jn:
            result["os_version"] = "Ubuntu 22.04"
    elif "macos" in jn or "mac-os" in jn:
        result["os"] = "macOS"
    elif "windows" in jn or "win-" in jn:
        result["os"] = "Windows"
        if "vs2019" in jn:
            result["os_version"] = "Windows Server 2019, VS2019"

    cuda_match = re.search(r"cuda([0-9_]+)", jn)
    if cuda_match:
        result["cuda"] = cuda_match.group(1).replace("_", ".")
        result["variant"] = "CUDA"

    cudnn_match = re.search(r"cudnn([0-9]+)", jn)
    if cudnn_match:
        result["cudnn"] = cudnn_match.group(1)

    if "rocm" in jn:
        rocm_match = re.search(r"rocm([0-9_.]+)", jn)
        if rocm_match:
            result["cuda"] = rocm_match.group(1).replace("_", ".")
        result["variant"] = "ROCm"
        result["category"] = "rocm"

    if "xpu" in jn:
        result["variant"] = "XPU"
        result["category"] = "xpu"

    if "mps" in jn:
        result["variant"] = "MPS"
        result["category"] = "mps"

    py_match = re.search(r"py([0-9_]+)", jn)
    if py_match:
        result["python"] = py_match.group(1).replace("_", ".")

    gcc_match = re.search(r"gcc([0-9]+)", jn)
    if gcc_match:
        result["compiler"] = "GCC"
        result["compiler_version"] = gcc_match.group(1)

    clang_match = re.search(r"clang([0-9]+)", jn)
    if clang_match:
        result["compiler"] = "Clang"
        result["compiler_version"] = clang_match.group(1)

    sm_match = re.search(r"sm([0-9]+)", jn)
    if sm_match:
        arch_map = {"80": "A100", "86": "RTX 30xx", "89": "Ada (RTX 40xx)", "90": "Hopper"}
        result["arch"] = f"SM{sm_match.group(1)} ({arch_map.get(sm_match.group(1), '')})"

    if "bazel" in jn:
        result["special"] = "Bazel"
        result["category"] = "bazel"
    elif "asan" in jn:
        result["special"] = "Address Sanitizer"
    elif "onnx" in jn:
        result["special"] = "ONNX variant"
    elif "mobile" in jn:
        result["special"] = "Mobile build"
    elif "inductor" in jn:
        result["special"] = "Inductor"
        result["category"] = "inductor"
    elif "no-ops" in jn or "no_ops" in jn:
        result["special"] = "No operators"
    elif "pch" in jn:
        result["special"] = "Precompiled headers"
    elif "executorch" in jn:
        result["special"] = "ExecuTorch"
    elif "xla" in jn:
        result["special"] = "XLA/TPU"
    elif "libtorch" in jn:
        result["special"] = "Libtorch"
    elif "aarch64" in jn or "arm64" in jn:
        result["special"] = "ARM64"

    if not result["category"] or result["category"] == "other":
        if result["variant"] == "CUDA" or result["cuda"]:
            result["category"] = "cuda"
        elif result["os"] == "Linux" and not result["variant"]:
            result["category"] = "linux_cpu"

    return result


def get_job_description(parsed: Dict) -> str:
    """Generate human-readable job description."""
    parts = []

    if parsed["special"]:
        return parsed["special"]

    if parsed["cuda"]:
        parts.append(f"CUDA {parsed['cuda']}")
    if parsed["cudnn"]:
        parts.append(f"cuDNN {parsed['cudnn']}")
    if parsed["arch"]:
        parts.append(parsed["arch"])

    if parsed["os"] == "Linux" and not parsed["cuda"]:
        if parsed["os_version"]:
            parts.append(parsed["os_version"].replace("Ubuntu ", ""))
        if parsed["python"]:
            parts.append(f"Py {parsed['python']}")
        if parsed["compiler"]:
            parts.append(f"{parsed['compiler']} {parsed['compiler_version']}")

    if parsed["os"] == "macOS":
        parts.append("ARM64")

    if parsed["os"] == "Windows":
        if parsed["os_version"]:
            parts.append("CPU")

    return ", ".join(parts) if parts else "-"


def extract_job_details_by_workflow(workflows: Dict) -> Dict:
    """Extract job details organized by workflow."""
    jobs_by_wf = defaultdict(list)

    entry_workflows = {k: v for k, v in workflows.items() if v.get("is_entry")}

    for wf_name, wf_data in entry_workflows.items():
        for job_name in wf_data.get("jobs", []):
            job_info = wf_data.get("job_details", {}).get(job_name, {})

            parsed = parse_job_name_detailed(job_name)
            parsed["workflow"] = wf_name
            parsed["uses"] = job_info.get("uses", "")
            parsed["description"] = get_job_description(parsed)

            jobs_by_wf[wf_name].append(parsed)

    return dict(jobs_by_wf)


def extract_test_configs(workflows: Dict) -> Dict:
    """Extract test configurations organized by category."""
    configs = {"core": [], "inductor": [], "specialized": [], "all": []}

    core_patterns = [
        "default",
        "distributed",
        "jit_legacy",
        "crossref",
        "dynamo_wrapped",
        "docs_test",
        "backwards_compat",
        "slow",
        "nogpu",
        "multigpu",
        "numpy_2_x",
    ]
    inductor_patterns = ["inductor", "aot_", "cpu_inductor", "dynamic_"]
    specialized_patterns = [
        "mps",
        "xla",
        "executorch",
        "onnx",
        "functorch",
        "benchmark",
        "mem_leak",
    ]

    config_descriptions = {
        "default": "Standard PyTorch tests (sharded 5 ways)",
        "distributed": "Distributed training tests (sharded 2-3 ways)",
        "jit_legacy": "Legacy JIT compiler tests",
        "crossref": "Cross-reference tests",
        "dynamo_wrapped": "TorchDynamo wrapped tests (sharded 3 ways)",
        "docs_test": "Documentation building tests",
        "backwards_compat": "Backward compatibility tests",
        "slow": "Slow-running tests (periodic only)",
        "nogpu_AVX512": "CPU-only AVX512 tests",
        "nogpu_NO_AVX2": "CPU-only non-AVX2 tests",
        "multigpu": "Multi-GPU tests",
        "numpy_2_x": "NumPy 2.x compatibility tests",
        "inductor": "Core inductor unit tests",
        "inductor_distributed": "Inductor distributed tests",
        "inductor_cpp_wrapper": "C++ wrapper tests",
        "inductor_huggingface": "HuggingFace model benchmarks",
        "inductor_timm": "Timm model benchmarks",
        "inductor_torchbench": "TorchBench benchmarks",
        "inductor_amx": "AMX SIMD tests",
        "inductor_avx2": "AVX2 SIMD tests",
        "inductor-halide": "Halide backend tests",
        "inductor-triton-cpu": "Triton CPU tests",
        "cpu_inductor_huggingface": "CPU inductor HuggingFace",
        "cpu_inductor_timm": "CPU inductor Timm",
        "cpu_inductor_torchbench": "CPU inductor TorchBench",
        "dynamic_cpu_inductor_huggingface": "Dynamic CPU inductor HF",
        "dynamic_cpu_inductor_timm": "Dynamic CPU inductor Timm",
        "dynamic_cpu_inductor_torchbench": "Dynamic CPU inductor TorchBench",
        "mem_leak_check": "Memory leak detection tests",
        "rerun_disabled_tests": "Re-run previously disabled tests",
        "pr_time_benchmarks": "PR timing benchmarks",
        "xla": "XLA/TPU tests",
        "executorch": "ExecuTorch tests",
        "mps": "Metal Performance Shaders (macOS)",
    }

    for wf_name, wf_data in workflows.items():
        if not wf_data.get("is_entry"):
            continue

        job_details = wf_data.get("job_details", {})
        for job_name, job_info in job_details.items():
            with_config = job_info.get("with", {})
            test_matrix = with_config.get("test-matrix") or with_config.get("test_matrix", "")

            if test_matrix and isinstance(test_matrix, str):
                config_matches = re.findall(r'config:\s*"([^"]+)"', test_matrix)
                for config in config_matches:
                    desc = config_descriptions.get(config, "")
                    config_entry = {
                        "config": config,
                        "description": desc,
                        "job": job_name,
                        "workflow": wf_name,
                    }
                    configs["all"].append(config_entry)

                    is_core = any(p in config for p in core_patterns)
                    is_inductor = any(p in config for p in inductor_patterns)
                    is_specialized = any(p in config for p in specialized_patterns)

                    if is_core and not is_inductor:
                        configs["core"].append(config_entry)
                    elif is_inductor:
                        configs["inductor"].append(config_entry)
                    elif is_specialized:
                        configs["specialized"].append(config_entry)

    configs["core"] = configs["core"][:20]
    configs["inductor"] = configs["inductor"][:25]
    configs["specialized"] = configs["specialized"][:20]

    return configs


def find_binary_workflows(workflows: Dict) -> Dict:
    """Find binary build workflows (generated from templates)."""
    binary = {"linux": [], "macos": [], "windows": [], "templates": []}

    templates_dir = os.path.join(".github", "templates")
    if os.path.exists(templates_dir):
        for f in os.listdir(templates_dir):
            if f.endswith(".j2"):
                binary["templates"].append(f)

    for wf_name in workflows.keys():
        if "generated" in wf_name:
            if "linux" in wf_name or "manywheel" in wf_name or "libtorch" in wf_name:
                binary["linux"].append(wf_name)
            elif "macos" in wf_name:
                binary["macos"].append(wf_name)
            elif "windows" in wf_name:
                binary["windows"].append(wf_name)

    return binary


def find_test_structure(repo_path: str) -> Dict:
    """Find test structure."""
    tests = {"found": False, "structure": {}, "all_tests": []}

    test_dirs = ["test", "Test", "tests", "TEST"]
    test_path = None

    for d in test_dirs:
        p = os.path.join(repo_path, d)
        if os.path.exists(p):
            test_path = p
            break

    if not test_path:
        return tests

    tests["found"] = True

    try:
        for item in sorted(os.listdir(test_path)):
            item_path = os.path.join(test_path, item)
            if os.path.isdir(item_path):
                try:
                    files = os.listdir(item_path)
                    py_files = [f for f in files if f.startswith("test_") and f.endswith(".py")]

                    all_test_funcs = []
                    for pf in py_files:
                        try:
                            with open(os.path.join(item_path, pf), "r", encoding="utf-8") as f:
                                content = f.read()
                                test_funcs = re.findall(r"def (test_[a-z0-9_]+)", content)
                                all_test_funcs.extend(test_funcs[:30])
                        except:
                            pass

                    if all_test_funcs:
                        tests["structure"][item] = {
                            "test_files": len(py_files),
                            "sample_tests": all_test_funcs[:5],
                            "total_tests": len(all_test_funcs),
                        }
                        tests["all_tests"].extend(all_test_funcs)
                except:
                    pass
    except:
        pass

    return tests


def find_lint_tools(repo_path: str) -> List[str]:
    """Find linting and code quality tools."""
    tools = []

    lintrunner_file = os.path.join(repo_path, ".lintrunner.toml")
    if os.path.exists(lintrunner_file):
        try:
            with open(lintrunner_file, "r", encoding="utf-8") as f:
                content = f.read()

            linters = re.findall(r"code\s*=\s*['\"](\w+)['\"]", content)
            tools = list(set(linters))
        except:
            pass

    return tools


def find_composite_actions(repo_path: str) -> Dict:
    """Find composite actions in .github/actions/"""
    actions = {"setup": [], "teardown": [], "artifacts": [], "testing": [], "utilities": []}

    actions_dir = os.path.join(repo_path, ".github", "actions")
    if not os.path.exists(actions_dir):
        return actions

    try:
        for item in os.listdir(actions_dir):
            item_path = os.path.join(actions_dir, item)
            if os.path.isdir(item_path):
                action_name = item.lower()
                if "setup" in action_name:
                    actions["setup"].append(item)
                elif "teardown" in action_name:
                    actions["teardown"].append(item)
                elif "download" in action_name or "upload" in action_name:
                    actions["artifacts"].append(item)
                elif "test" in action_name:
                    actions["testing"].append(item)
                else:
                    actions["utilities"].append(item)
    except:
        pass

    return actions


def find_test_scripts(repo_path: str) -> List[Dict]:
    """Find test execution scripts with descriptions."""
    scripts = []

    script_descriptions = {
        "build.sh": ["cmake config", "ninja build", "wheel create"],
        "test.sh": ["pytest run", "sharding", "TD selection"],
        "multigpu-test.sh": ["multi-GPU", "distributed", "NCCL tests"],
        "docs-test.sh": ["Sphinx build", "Doc validation"],
    }

    for ci_dir in [
        os.path.join(repo_path, ".ci", "pytorch"),
        os.path.join(repo_path, "ci"),
        os.path.join(repo_path, ".ci"),
    ]:
        if os.path.exists(ci_dir):
            try:
                for item in os.listdir(ci_dir):
                    if item.endswith(".sh"):
                        scripts.append(
                            {
                                "name": item.replace(".sh", ""),
                                "description": script_descriptions.get(item, []),
                            }
                        )
            except:
                pass

    return scripts


def generate_architecture_doc(
    repo_name: str,
    workflows: Dict,
    job_configs_by_wf: Dict,
    test_configs: Dict,
    tests: Dict,
    lint_tools: List[str],
    actions: Dict,
    scripts: List[Dict],
    orchestration: Dict,
    binary_wfs: Dict,
    output_file: str,
) -> str:
    """Generate very comprehensive architecture documentation."""

    lines = []

    # Header
    lines.append("```")
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 18 + f"{repo_name.upper()} CI/CD ARCHITECTURE" + " " * 20 + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("")

    # Trigger Sources - Fixed alignment
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 35 + "TRIGGER SOURCES" + " " * 41 + "│")
    lines.append("├" + "─" * 97 + "┤")

    all_triggers = set()
    for wf, data in workflows.items():
        all_triggers.update(data.get("triggers", []))

    trigger_descriptions = {
        "pull_request": "PRs to main, release/*, landchecks/*",
        "push": "Commits to main, release/*, nightly",
        "schedule": "Cron jobs (periodic, nightly, slow tests)",
        "workflow_dispatch": "Manual triggers",
        "tag": "ciflow/trunk/*, ciflow/periodic/*, etc.",
    }

    # Sort triggers with descriptions first
    sorted_triggers = sorted(all_triggers, key=lambda x: (x not in trigger_descriptions, x))
    for t in sorted_triggers:
        desc = trigger_descriptions.get(t, "")
        if desc:
            lines.append(f"│  • {t:<18} → {desc:<73}│")
        else:
            lines.append(f"│  • {t:<18} │")

    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")

    # Main Entry Workflows
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 32 + "MAIN ENTRY WORKFLOWS" + " " * 34 + "│")
    lines.append("├" + "─" * 97 + "┤")
    lines.append(
        "│                                                                                          │"
    )

    entry_workflows = {k: v for k, v in workflows.items() if v.get("is_entry")}

    priority_workflows = ["pull.yml", "trunk.yml", "periodic.yml", "lint.yml"]
    main_wfs = [wf for wf in priority_workflows if wf in entry_workflows]

    # Simple list format for main entry workflows
    if main_wfs:
        for wf in main_wfs:
            wf_type = (
                "PR validation"
                if "pull" in wf
                else (
                    "post-merge"
                    if "trunk" in wf
                    else ("scheduled" if "periodic" in wf else "code lint")
                )
            )
            trigger = (
                "PR/push"
                if "pull" in wf
                else ("push" if "trunk" in wf else ("cron" if "periodic" in wf else "PR"))
            )
            wf_short = wf.replace(".yml", "")
            lines.append(
                f"│  • {wf_short:<12} ({wf_type:<12}) - Triggers: {trigger:<15}                                        │"
            )

    # Additional workflows
    additional_wfs = ["slow.yml", "inductor.yml", "torchbench.yml", "nightly.yml"]
    second_row = [wf for wf in additional_wfs if wf in entry_workflows]

    if second_row:
        for wf in second_row:
            wf_type = (
                "slow tests"
                if "slow" in wf
                else (
                    "inductor bench"
                    if "inductor" in wf
                    else ("benchmark" if "torchbench" in wf else "nightly")
                )
            )
            wf_short = wf.replace(".yml", "")
            lines.append(
                f"│  • {wf_short:<12} ({wf_type:<12})                                                  │"
            )

    lines.append(
        "│                                                                                          │"
    )
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")

    # Pre-Build Phase (Orchestration)
    if (
        orchestration["runner_determinator"]
        or orchestration["test_selection"]
        or orchestration["target_determination"]
    ):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " " * 24 + "PRE-BUILD PHASE (Orchestration)" + " " * 28 + "│")
        lines.append("├" + "─" * 97 + "┤")
        lines.append(
            "│                                                                                          │"
        )

        if orchestration["runner_determinator"]:
            lines.append(
                "│  ┌──────────────────────────────────┐    ┌───────────────────────────────────────┐  │"
            )
            for wf in orchestration["runner_determinator"]:
                lines.append(f"│  │ {wf:<32} │    │" + " " * 37 + "│  │")
            lines.append(
                "│  │                                  │    │  Determines runner fleet:           │  │"
            )
            lines.append(
                "│  │  Determines runner type:        │    │  • Meta runners (default)           │  │"
            )
            lines.append(
                "│  │  • Empty (Meta)                  │    │  • Linux Foundation (lf.*)          │  │"
            )
            lines.append(
                "│  │  • lf.* (Linux Foundation)      │    │  • LF Canary (lf.c.*)              │  │"
            )
            lines.append(
                "│  └──────────────────────────────────┘    └───────────────────────────────────────┘  │"
            )

        if orchestration["test_selection"]:
            lines.append(
                "│                                                                                          │"
            )
            for wf in orchestration["test_selection"]:
                lines.append(f"│  • {wf} - LLM-based test selection")

        if orchestration["target_determination"]:
            lines.append(
                "│                                                                                          │"
            )
            for wf in orchestration["target_determination"]:
                lines.append(f"│  • {wf} - Calculates which tests to run based on code changes")

        lines.append(
            "│                                                                                          │"
        )
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")

    # Test Configurations
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 24 + "TEST CONFIGURATIONS (Sharded)" + " " * 32 + "│")
    lines.append("├" + "─" * 97 + "┤")
    lines.append(
        "│                                                                                          │"
    )

    if test_configs.get("core"):
        lines.append("│  ┌" + "─" * 93 + "┐  │")
        lines.append("│  │" + " " * 35 + "CORE TEST CONFIGS" + " " * 48 + "│  │")
        lines.append("│  ├" + "─" * 93 + "┤  │")

        unique_core = {}
        for c in test_configs["core"]:
            if c["config"] not in unique_core:
                unique_core[c["config"]] = c.get("description", "")

        for cfg, desc in sorted(unique_core.items())[:12]:
            if desc:
                lines.append(f'│  │ config: "{cfg:<15}" - {desc:<58}│  │')
            else:
                lines.append(
                    f'│  │ config: "{cfg:<15}"                                              │  │'
                )

        lines.append("│  └" + "─" * 93 + "┘  │")
        lines.append(
            "│                                                                                          │"
        )

    if test_configs.get("inductor"):
        lines.append("│  ┌" + "─" * 93 + "┐  │")
        lines.append("│  │" + " " * 33 + "INDUCTOR TEST CONFIGS" + " " * 47 + "│  │")
        lines.append("│  ├" + "─" * 93 + "┤  │")

        unique_inductor = {}
        for c in test_configs["inductor"]:
            if c["config"] not in unique_inductor:
                unique_inductor[c["config"]] = c.get("description", "")

        for cfg, desc in sorted(unique_inductor.items())[:12]:
            if desc:
                lines.append(f'│  │ config: "{cfg:<25}" - {desc:<45}│  │')
            else:
                lines.append(
                    f'│  │ config: "{cfg:<25}"                                             │  │'
                )

        lines.append("│  └" + "─" * 93 + "┘  │")
        lines.append(
            "│                                                                                          │"
        )

    if test_configs.get("specialized"):
        lines.append("│  ┌" + "─" * 93 + "┐  │")
        lines.append("│  │" + " " * 31 + "SPECIALIZED TEST CONFIGS" + " " * 47 + "│  │")
        lines.append("│  ├" + "─" * 93 + "┤  │")

        unique_spec = {}
        for c in test_configs["specialized"]:
            if c["config"] not in unique_spec:
                unique_spec[c["config"]] = c.get("description", "")

        for cfg, desc in sorted(unique_spec.items())[:12]:
            if desc:
                lines.append(f'│  │ config: "{cfg:<20}" - {desc:<50}│  │')
            else:
                lines.append(
                    f'│  │ config: "{cfg:<20}"                                             │  │'
                )

        lines.append("│  └" + "─" * 93 + "┘  │")
        lines.append(
            "│                                                                                          │"
        )

    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")
    lines.append("")

    # Test Workflows (Reusable)
    reusable_workflows = {k: v for k, v in workflows.items() if v.get("is_reusable")}
    test_wfs = [wf for wf in reusable_workflows.keys() if "test" in wf.lower()]

    if test_wfs:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " " * 24 + "TEST WORKFLOWS (Reusable)" + " " * 38 + "│")
        lines.append("├" + "─" * 97 + "┤")
        lines.append(
            "│                                                                                          │"
        )
        lines.append(
            "│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌─────────────────┐  │"
        )

        test_wf_details = {
            "_linux-test.yml": ("Matrix testing", "Docker-based", "GPU/CPU runners"),
            "_mac-test.yml": ("macOS testing", "ARM64 native", ""),
            "_win-test.yml": ("Windows tests", "VS2019 env", ""),
            "_rocm-test.yml": ("AMD GPU tests", "ROCm stack", ""),
            "_mac-test-mps.yml": ("Metal shaders", "macOS 13/14", ""),
            "_xpu-test.yml": ("Intel XPU", "Intel GPUs", ""),
            "_docs.yml": ("Doc building", "Sphinx", ""),
            "_bazel-build-test.yml": ("Bazel testing", "Build system", ""),
        }

        wf_groups = [test_wfs[i : i + 4] for i in range(0, len(test_wfs), 4)]

        for wf_group in wf_groups:
            row1 = "│"
            row2 = "│"
            row3 = "│"
            row4 = "│"

            for wf in wf_group:
                wf_name = wf.replace(".yml", "")
                details = test_wf_details.get(wf, ("", "", ""))

                row1 += f" {wf_name:<14} │"
                row2 += f"                  │"
                row3 += f" • {details[0]:<12} │"
                row4 += f" • {details[1]:<12} │"

            while len(wf_group) < 4:
                row1 += " " * 16 + "│"
                row2 += " " * 16 + "│"
                row3 += " " * 16 + "│"
                row4 += " " * 16 + "│"

            row1 += " " * (97 - len(row1) - 1) + "│"
            row2 += " " * (97 - len(row2) - 1) + "│"
            row3 += " " * (97 - len(row3) - 1) + "│"
            row4 += " " * (97 - len(row4) - 1) + "│"

            lines.append(row1)
            lines.append(row2)
            lines.append(row3)
            lines.append(row4)

        lines.append(
            "│  └────────────────┘  └────────────────┘  └────────────────┘  └─────────────────┘  │"
        )
        lines.append(
            "│                                                                                          │"
        )
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")

    # Composite Actions - Improved layout
    if any(actions.values()):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " " * 24 + "COMPOSITE ACTIONS (.github/actions/)" + " " * 24 + "│")
        lines.append("├" + "─" * 97 + "┤")
        lines.append(
            "│                                                                                          │"
        )

        all_setup = actions.get("setup", []) + actions.get("teardown", [])
        all_artifacts = actions.get("artifacts", [])
        all_testing = actions.get("testing", []) + actions.get("utilities", [])

        # Column headers
        lines.append(
            "│  SETUP/TEARDOWN                   ARTIFACTS                           TESTING                       │"
        )
        lines.append("│  " + "─" * 27 + "  " + "─" * 29 + "  " + "─" * 27 + "  │")

        # Data rows
        max_len = max(len(all_setup), len(all_artifacts), len(all_testing), 5)

        for i in range(max_len):
            setup = all_setup[i] if i < len(all_setup) else ""
            artifacts = all_artifacts[i] if i < len(all_artifacts) else ""
            testing = all_testing[i] if i < len(all_testing) else ""

            # Fixed width columns: 27, 29, 27
            setup = setup[:27] if setup else " " * 27
            artifacts = artifacts[:29] if artifacts else " " * 29
            testing = testing[:27] if testing else " " * 27

            lines.append(f"│  {setup}  {artifacts}  {testing}  │")

        lines.append(
            "│                                                                                          │"
        )
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")

    # Test Execution Scripts
    if scripts:
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " " * 24 + "TEST EXECUTION (.ci/pytorch/)" + " " * 30 + "│")
        lines.append("├" + "─" * 97 + "┤")
        lines.append(
            "│                                                                                          │"
        )

        # Key scripts to display in box format (matching reference)
        key_scripts = ["build.sh", "test.sh", "multigpu-test.sh", "docs-test.sh"]
        key_script_names = ["build", "test", "multigpu-test", "docs-test"]
        key_script_descs = [
            ["cmake config", "ninja build", "wheel create"],
            ["pytest run", "sharding", "TD selection"],
            ["multi-GPU", "distributed", "NCCL tests"],
            ["Sphinx build", "Doc validation", ""],
        ]

        # Print box header
        lines.append(
            "│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐  ┌────────────────────┐  │"
        )

        # Row 1: Script names
        row = "│  │"
        for name in key_script_names:
            row += f" {name:<14} │"
        lines.append(row + " " * (97 - len(row) - 3) + "│")

        # Row 2: Empty
        lines.append(
            "│  │                │  │                │  │                │                    │  │"
        )

        # Row 3-5: Descriptions
        for i in range(3):
            row = "│  │"
            for j, desc_list in enumerate(key_script_descs):
                desc = desc_list[i] if i < len(desc_list) else ""
                if desc:
                    row += f" • {desc:<11} │"
                else:
                    row += " " * 14 + "│"
            lines.append(row + " " * (97 - len(row) - 3) + "│")

        lines.append(
            "│  └────────────────┘  └────────────────┘  └────────────────┘  └────────────────────┘  │"
        )
        lines.append(
            "│                                                                                          │"
        )

        env_vars = [
            ("SHARD_NUMBER / NUM_TEST_SHARDS", "Test parallelization"),
            ("TEST_CONFIG", "Test configuration type"),
            ("BUILD_ENVIRONMENT", "Build identifier"),
            ("TORCH_CUDA_ARCH_LIST", "CUDA architectures"),
            ("SCCACHE_*", "Distributed compilation cache"),
        ]
        lines.append(
            "│  Environment Variables:                                                                  │"
        )
        for var, desc in env_vars:
            lines.append(f"│    • {var:<30} - {desc:<50}│")

        lines.append(
            "│                                                                                          │"
        )
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")

    # Binary Build Workflows
    if binary_wfs.get("linux") or binary_wfs.get("windows") or binary_wfs.get("macos"):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append(
            "│" + " " * 16 + "BINARY BUILD WORKFLOWS (Generated from Templates)" + " " * 15 + "│"
        )
        lines.append("├" + "─" * 97 + "┤")
        lines.append(
            "│                                                                                          │"
        )
        lines.append(
            "│  Templates: .github/templates/*.j2  →  Generated: .github/workflows/generated-*.yml     │"
        )

        if binary_wfs.get("linux"):
            lines.append(
                "│                                                                                          │"
            )
            lines.append(
                "│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │"
            )
            lines.append(
                "│  │                     LINUX BINARIES                                               │    │"
            )
            lines.append(
                "│  ├─────────────────────────────────────────────────────────────────────────────────┤    │"
            )

            for wf in binary_wfs["linux"][:5]:
                lines.append(f"│  │ {wf:<80}│    │")

            lines.append(
                "│  │   • manywheel-py3.9-cpu         • manywheel-py3.10-cuda11.8                   │    │"
            )
            lines.append(
                "│  │   • manywheel-py3.10-cpu        • manywheel-py3.10-cuda12.1                   │    │"
            )
            lines.append(
                "│  │   • manywheel-py3.11-cpu        • manywheel-py3.10-cuda12.4                   │    │"
            )
            lines.append(
                "│  └─────────────────────────────────────────────────────────────────────────────────┘    │"
            )

        if binary_wfs.get("macos"):
            lines.append(
                "│                                                                                          │"
            )
            lines.append(
                "│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │"
            )
            lines.append(
                "│  │                     MACOS BINARIES                                             │    │"
            )
            lines.append(
                "│  ├─────────────────────────────────────────────────────────────────────────────────┤    │"
            )

            for wf in binary_wfs["macos"][:3]:
                lines.append(f"│  │ {wf:<80}│    │")

            lines.append(
                "│  └─────────────────────────────────────────────────────────────────────────────────┘    │"
            )

        if binary_wfs.get("windows"):
            lines.append(
                "│                                                                                          │"
            )
            lines.append(
                "│  ┌─────────────────────────────────────────────────────────────────────────────────┐    │"
            )
            lines.append(
                "│  │                     WINDOWS BINARIES                                             │    │"
            )
            lines.append(
                "│  ├─────────────────────────────────────────────────────────────────────────────────┤    │"
            )

            for wf in binary_wfs["windows"][:3]:
                lines.append(f"│  │ {wf:<80}│    │")

            lines.append(
                "│  │   • py3.9-cpu, py3.10-cpu, py3.11-cpu, py3.12-cpu                              │    │"
            )
            lines.append(
                "│  │   • py3.10-cuda11.8, py3.10-cuda12.1, py3.10-cuda12.4                          │    │"
            )
            lines.append(
                "│  └─────────────────────────────────────────────────────────────────────────────────┘    │"
            )

        binary_reusable = [wf for wf in reusable_workflows.keys() if "binary" in wf.lower()]
        if binary_reusable:
            lines.append(
                "│  Binary workflow uses: "
                + ", ".join(binary_reusable[:3])
                + " " * (50 - len(", ".join(binary_reusable[:3])))
                + "│"
            )

        lines.append(
            "│                                                                                          │"
        )
        lines.append("└" + "─" * 97 + "┘")
        lines.append("                                        │")
        lines.append("                                        ▼")
        lines.append("")

    # Runner Types
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 31 + "RUNNER TYPES (Self-Hosted)" + " " * 33 + "│")
    lines.append("├" + "─" * 97 + "┤")
    lines.append(
        "│                                                                                          │"
    )

    runner_types = [
        ("linux.2xlarge", "8 vCPU, 32GB RAM"),
        ("linux.4xlarge", "16 vCPU, 64GB RAM"),
        ("linux.8xlarge.amx", "AMX SIMD support"),
        ("linux.10xlarge.avx2", "AVX2 SIMD support"),
        ("linux.12xlarge", "High memory"),
        ("linux.24xl.spr-metal", "Sapphire Rapids"),
        ("linux.g4dn.12xlarge.nvidia.gpu", "T4 GPU (4x)"),
        ("linux.g5.4xlarge.nvidia.gpu", "A10G GPU"),
        ("linux.g5.12xlarge.nvidia.gpu", "A10G GPU (4x)"),
        ("linux.g6.4xlarge.experimental.nvidia.gpu", "L4 GPU"),
        ("linux.gcp.a100", "A100 40GB (Google Cloud)"),
        ("linux.rocm.gpu", "AMD ROCm GPU"),
    ]

    macos_runners = [
        ("macos-m1-stable", "M1 Stable"),
        ("macos-m1-13", "M1 macOS 13"),
        ("macos-m1-14", "M1 macOS 14"),
    ]

    windows_runners = [
        ("windows.4xlarge.nonephemeral", "4xlarge non-ephemeral"),
    ]

    lines.append(
        "│  ┌──────────────────────── LINUX ────────────────────────┐    ┌────── MACOS ──────┐      │"
    )

    for i in range(max(len(runner_types), len(macos_runners), 1)):
        linux_part = ""
        if i < len(runner_types):
            name, desc = runner_types[i]
            linux_part = f"│  │ {name:<35} - {desc:<25} │"

        macos_part = ""
        if i < len(macos_runners):
            name, desc = macos_runners[i]
            macos_part = f"│ {name:<20} - {desc:<15} │"

        padding = " " * (97 - len(linux_part) - len(macos_part) - 2)
        lines.append(linux_part + padding + macos_part + "│")

    lines.append(
        "│  └────────────────────────────────────────────────────────┘    └───────────────────┘      │"
    )
    lines.append(
        "│                                                                                          │"
    )
    lines.append("└" + "─" * 97 + "┘")
    lines.append("")

    # Test Structure
    if tests.get("structure"):
        lines.append("┌" + "─" * 97 + "┐")
        lines.append("│" + " " * 30 + "TEST STRUCTURE" + " " * 48 + "│")
        lines.append("├" + "─" * 97 + "┤")

        large_tests = {k: v for k, v in tests["structure"].items() if v.get("total_tests", 0) > 100}
        medium_tests = {
            k: v for k, v in tests["structure"].items() if 30 < v.get("total_tests", 0) <= 100
        }

        if large_tests:
            lines.append(
                "│  LARGE TEST CATEGORIES (>100 tests):                                                   │"
            )
            for cat, info in sorted(large_tests.items(), key=lambda x: -x[1].get("total_tests", 0))[
                :8
            ]:
                count = info.get("total_tests", 0)
                samples = ", ".join(info.get("sample_tests", [])[:2])
                lines.append(f"│    • {cat:<30} ({count:>4} tests) - {samples[:45]:<45}│")

        if medium_tests:
            lines.append(
                "│                                                                                          │"
            )
            lines.append(
                "│  MEDIUM TEST CATEGORIES (30-100 tests):                                                │"
            )
            for cat, info in sorted(
                medium_tests.items(), key=lambda x: -x[1].get("total_tests", 0)
            )[:8]:
                count = info.get("total_tests", 0)
                lines.append(
                    f"│    • {cat:<40} ({count:>3} tests)                                       │"
                )

        lines.append("└" + "─" * 97 + "┘")
        lines.append("")

    # Summary
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " " * 35 + "SUMMARY" + " " * 53 + "│")
    lines.append("├" + "─" * 97 + "┤")
    lines.append(
        "│                                                                                          │"
    )
    lines.append(f"│  GitHub Actions Workflows: {len(workflows):<70}│")
    lines.append(f"│  Entry Workflows: {len(entry_workflows):<74}│")
    lines.append(f"│  Reusable Workflows: {len(reusable_workflows):<71}│")

    total_jobs = sum(len(v) for v in job_configs_by_wf.values())
    lines.append(f"│  Total Build/Test Jobs: {total_jobs:<69}│")

    if test_configs.get("all"):
        lines.append(f"│  Test Configurations: {len(test_configs['all']):<69}│")

    if tests.get("structure"):
        lines.append(f"│  Test Categories: {len(tests['structure']):<74}│")
        lines.append(f"│  Total Test Functions: {len(tests.get('all_tests', [])):<68}│")

    if lint_tools:
        lines.append(f"│  Lint Tools: {len(lint_tools):<79}│")

    total_actions = sum(len(v) for v in actions.values())
    if total_actions:
        lines.append(f"│  Composite Actions: {total_actions:<74}│")

    if scripts:
        lines.append(f"│  Test Scripts: {len(scripts):<78}│")

    lines.append(
        "│                                                                                          │"
    )
    lines.append("└" + "─" * 97 + "┘")
    lines.append("```")
    lines.append("")

    # Complete Job List by Workflow
    lines.append("## Complete Job List by Workflow")
    lines.append("")

    priority_wfs = [
        "pull.yml",
        "trunk.yml",
        "periodic.yml",
        "lint.yml",
        "slow.yml",
        "inductor.yml",
        "nightly.yml",
    ]

    for wf_name in priority_wfs:
        if wf_name in job_configs_by_wf and job_configs_by_wf[wf_name]:
            wf_jobs = job_configs_by_wf[wf_name]

            wf_type = (
                "PR validation"
                if "pull" in wf_name
                else (
                    "post-merge"
                    if "trunk" in wf_name
                    else (
                        "scheduled"
                        if "periodic" in wf_name
                        else (
                            "code lint"
                            if "lint" in wf_name
                            else (
                                "slow tests"
                                if "slow" in wf_name
                                else (
                                    "inductor"
                                    if "inductor" in wf_name
                                    else ("nightly" if "nightly" in wf_name else "")
                                )
                            )
                        )
                    )
                )
            )

            lines.append(f"### {wf_name} ({wf_type})")
            lines.append("")
            lines.append("| Job Name | Platform | Description |")
            lines.append("|----------|----------|-------------|")

            for job in wf_jobs[:25]:
                platform = job.get("os") or job.get("category", "-")
                desc = job.get("description", "-")
                lines.append(f"| `{job['name'][:50]}` | {platform} | {desc} |")

            lines.append("")

    content = "\n".join(lines)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    return content


def analyze_ci_architecture(repo_path: str = None, output_file: str = None):
    """Main function."""

    if repo_path is None:
        repo_path = os.getcwd()

    if output_file is None:
        output_file = "CI_ARCHITECTURE.md"

    repo_name = os.path.basename(os.path.abspath(repo_path))

    print(f"Analyzing CI architecture for {repo_name}...")

    workflows = analyze_workflows_deep(repo_path)
    print(f"  Found {len(workflows)} GitHub Actions workflows")

    orchestration = find_orchestration_workflows(workflows)

    job_configs_by_wf = extract_job_details_by_workflow(workflows)
    total_jobs = sum(len(v) for v in job_configs_by_wf.values())
    print(f"  Total jobs across all workflows: {total_jobs}")

    test_configs = extract_test_configs(workflows)

    tests = find_test_structure(repo_path)
    if tests.get("found"):
        print(f"  Found {len(tests.get('structure', {}))} test categories")

    lint_tools = find_lint_tools(repo_path)
    if lint_tools:
        print(f"  Found {len(lint_tools)} lint tools")

    actions = find_composite_actions(repo_path)
    total_actions = sum(len(v) for v in actions.values())
    if total_actions:
        print(f"  Found {total_actions} composite actions")

    scripts = find_test_scripts(repo_path)
    if scripts:
        print(f"  Found {len(scripts)} test scripts")

    binary_wfs = find_binary_workflows(workflows)

    doc = generate_architecture_doc(
        repo_name,
        workflows,
        job_configs_by_wf,
        test_configs,
        tests,
        lint_tools,
        actions,
        scripts,
        orchestration,
        binary_wfs,
        output_file,
    )

    print(f"\nSaved to: {output_file}")
    print(f"Total lines: {len(doc.splitlines())}")


if __name__ == "__main__":
    import sys

    repo_path = sys.argv[1] if len(sys.argv) > 1 else None
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    analyze_ci_architecture(repo_path, output_file)
