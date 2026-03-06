#!/usr/bin/env python3
"""
CI Architecture Analysis Skill
Generates detailed CI/CD architecture diagrams for any GitHub Actions project.
"""

import os
import sys
import yaml
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict


def find_ci_files(repo_path: str) -> Dict[str, Any]:
    """Find all CI-related directories."""
    repo = Path(repo_path)
    if not repo.exists():
        print(f"Error: Repository path does not exist: {repo_path}")
        return {}
    return {
        "workflows_dir": repo / ".github" / "workflows",
        "actions_dir": repo / ".github" / "actions",
        "ci_scripts_dir": repo / ".ci",
        "scripts_dir": repo / "scripts",
        "test_dir": repo / "test",
        "repo_name": repo.name,
    }


def read_workflow(wf_file: Path) -> Dict:
    """Read and parse a workflow file."""
    try:
        with open(wf_file, "r", encoding="utf-8") as f:
            wf = yaml.safe_load(f) or {}
            if True in wf and "on" not in wf:
                wf["on"] = wf.pop(True)
            return wf
    except:
        return {}


def extract_triggers(on_config: Any) -> List[str]:
    """Extract trigger events."""
    triggers = []
    if isinstance(on_config, str):
        triggers = [on_config]
    elif isinstance(on_config, list):
        triggers = on_config
    elif isinstance(on_config, dict):
        for key in on_config.keys():
            if key in [
                "pull_request",
                "push",
                "schedule",
                "workflow_dispatch",
                "release",
                "workflow_call",
                "workflow_run",
                "tags",
                "label",
            ]:
                triggers.append(key)
    return triggers


def extract_job_details(wf: Dict) -> List[Dict]:
    """Extract job details."""
    jobs = []
    if "jobs" not in wf:
        return jobs

    for job_name, job_data in wf["jobs"].items():
        job_info = {
            "name": job_name,
            "runs_on": job_data.get("runs-on", ""),
            "needs": job_data.get("needs", []),
        }

        if "steps" in job_data:
            for step in job_data["steps"]:
                step_info = {
                    "name": step.get("name", ""),
                    "uses": step.get("uses", ""),
                }
                job_info.setdefault("steps", []).append(step_info)

        jobs.append(job_info)
    return jobs


def analyze_workflows(workflows_dir: Path) -> List[Dict]:
    """Analyze all workflow files."""
    workflows = []
    if not workflows_dir.exists():
        return workflows

    for wf_file in sorted(workflows_dir.glob("*.yml")) + sorted(workflows_dir.glob("*.yaml")):
        wf = read_workflow(wf_file)
        if not wf:
            continue

        workflows.append(
            {
                "file": wf_file.name,
                "name": wf_file.stem,
                "triggers": extract_triggers(wf.get("on", {})),
                "jobs": extract_job_details(wf),
            }
        )

    return workflows


def analyze_actions(actions_dir: Path) -> List[Dict]:
    """Analyze composite actions."""
    actions = []
    if not actions_dir.exists():
        return actions

    for action_file in actions_dir.rglob("action.yml"):
        try:
            with open(action_file, "r", encoding="utf-8") as f:
                action = yaml.safe_load(f) or {}
            actions.append(
                {
                    "name": action_file.parent.name,
                    "description": action.get("description", ""),
                }
            )
        except:
            pass

    return actions


def find_ci_scripts(ci_dirs: Dict) -> List[str]:
    """Find CI scripts."""
    scripts = []
    for dir_key in ["ci_scripts_dir", "scripts_dir"]:
        d = ci_dirs.get(dir_key)
        if d and d.exists():
            for f in d.rglob("*.sh"):
                scripts.append(f.name)
            for f in d.rglob("*.py"):
                if f.name not in scripts:
                    scripts.append(f.name)
    return scripts


def find_test_categories(test_dir: Path) -> Dict[str, int]:
    """Find test categories."""
    categories = {}
    if test_dir and test_dir.exists():
        for d in test_dir.iterdir():
            if d.is_dir() and not d.name.startswith("_"):
                count = len(list(d.glob("test_*.py")))
                if count > 0:
                    categories[d.name] = count
    return categories


def collect_data(repo_path: str) -> Dict[str, Any]:
    """Collect all CI/CD data."""
    ci_dirs = find_ci_files(repo_path)

    workflows = analyze_workflows(ci_dirs.get("workflows_dir", Path("")))
    actions = analyze_actions(ci_dirs.get("actions_dir", Path("")))
    scripts = find_ci_scripts(ci_dirs)
    test_cats = find_test_categories(ci_dirs.get("test_dir", Path("")))

    # Categorize workflows
    entry = [
        w
        for w in workflows
        if not w["name"].startswith("_") and not w["name"].startswith("generated")
    ]
    reusable = [w for w in workflows if w["name"].startswith("_")]
    generated = [w for w in workflows if w["name"].startswith("generated")]

    # Group by type
    categorized = defaultdict(list)
    for wf in entry:
        name = wf["name"].lower()
        if name in ["pull", "trunk", "main"]:
            cat = "core_ci"
        elif any(x in name for x in ["periodic", "nightly", "slow"]):
            cat = "periodic"
        elif "lint" in name or "format" in name:
            cat = "lint"
        elif any(x in name for x in ["build", "docker", "image", "wheel"]):
            cat = "build"
        elif any(x in name for x in ["test", "inductor", "benchmark"]):
            cat = "test"
        elif any(x in name for x in ["rocm", "xpu", "mps", "aarch64"]):
            cat = "hardware"
        elif any(x in name for x in ["upload", "publish", "release"]):
            cat = "upload"
        elif any(x in name for x in ["merge", "revert", "cherry", "stale", "label"]):
            cat = "automation"
        elif any(x in name for x in ["runner", "target", "determin"]):
            cat = "infrastructure"
        else:
            cat = "other"
        categorized[cat].append(wf)

    # Count runners
    runners = defaultdict(int)
    for wf in workflows:
        for job in wf.get("jobs", []):
            runs_on = job.get("runs_on", "")
            if runs_on:
                if isinstance(runs_on, list):
                    runs_on = ",".join(runs_on)
                runners[runs_on] += 1

    # All triggers
    triggers = set()
    for wf in workflows:
        for t in wf.get("triggers", []):
            triggers.add(t)

    return {
        "repo_name": ci_dirs.get("repo_name", "REPO"),
        "workflows": workflows,
        "entry": entry,
        "reusable": reusable,
        "generated": generated,
        "categorized": categorized,
        "triggers": triggers,
        "runners": runners,
        "actions": actions,
        "scripts": scripts,
        "test_cats": test_cats,
    }


def generate_diagram(data: Dict[str, Any], output_dir: str):
    """Generate ASCII diagram."""
    repo = data.get("repo_name", "REPO")
    lines = []

    lines.append("```")
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + f" {repo.upper()} CI/CD ARCHITECTURE".center(97) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("")

    # 1. TRIGGER SOURCES
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 1. TRIGGER SOURCES".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    for t in sorted(data["triggers"]):
        lines.append(f"│  • {t:<20}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 2. MAIN ENTRY WORKFLOWS
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 2. MAIN ENTRY WORKFLOWS".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    lines.append("│" + " " * 97 + "│")

    cat = data.get("categorized", {})
    for cat_name, wfs in cat.items():
        if wfs:
            lines.append(f"│  [{cat_name.upper()}] ({len(wfs)} workflows)".ljust(98) + "│")
            for wf in wfs[:5]:
                tr = ", ".join(wf.get("triggers", []))[:35]
                lines.append(f"│    • {wf['name']:<25} (Triggers: {tr})".ljust(98) + "│")
            lines.append("│" + " " * 97 + "│")

    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 3. PRE-BUILD PHASE
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 3. PRE-BUILD PHASE".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    infra = cat.get("infrastructure", []) + cat.get("automation", [])[:3]
    for wf in infra:
        lines.append(f"│  ⚙️  {wf['name']:<45}".ljust(98) + "│")
        for job in wf.get("jobs", [])[:2]:
            lines.append(f"│      └─ {job['name']:<35}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 4. BUILD JOBS
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 4. BUILD JOBS".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    build_wfs = [w for w in data["reusable"] if "build" in w["name"].lower()]
    for wf in build_wfs[:5]:
        lines.append(f"│  📦 {wf['name']:<40} ({len(wf.get('jobs', []))} jobs)".ljust(98) + "│")
        for job in wf.get("jobs", [])[:2]:
            lines.append(f"│      └─ {job['name']:<35}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 5. TEST CONFIGURATIONS
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 5. TEST CONFIGURATIONS".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    sorted_tests = sorted(data["test_cats"].items(), key=lambda x: -x[1])
    for cat_name, count in sorted_tests[:15]:
        lines.append(f"│    • {cat_name:<25} ({count:>3} tests)".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 6. TEST WORKFLOWS
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 6. TEST WORKFLOWS".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    test_wfs = [w for w in data["reusable"] if "test" in w["name"].lower()]
    for wf in test_wfs:
        lines.append(f"│  🧪 {wf['name']:<35} ({len(wf.get('jobs', []))} jobs)".ljust(98) + "│")
        for job in wf.get("jobs", [])[:1]:
            lines.append(f"│      └─ {job['name']:<35}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 7. COMPOSITE ACTIONS
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 7. COMPOSITE ACTIONS".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    actions = data.get("actions", [])
    setup = [a["name"] for a in actions if "setup" in a["name"].lower()][:4]
    artifacts = [
        a["name"]
        for a in actions
        if "download" in a["name"].lower() or "upload" in a["name"].lower()
    ][:4]
    lines.append("│  SETUP:                      ARTIFACTS:                 │")
    for i in range(max(len(setup), len(artifacts), 2)):
        s = setup[i] if i < len(setup) else ""
        a = artifacts[i] if i < len(artifacts) else ""
        lines.append(f"│    • {s:<22}      • {a:<22} │".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 8. TEST EXECUTION
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 8. TEST EXECUTION".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    for s in data.get("scripts", [])[:8]:
        lines.append(f"│    • {s:<40}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 9. BINARY BUILD
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 9. BINARY BUILD".ljust(98) + "│")
    lines.append("├" + "─" * 97 + "┤")
    for wf in data.get("generated", [])[:5]:
        lines.append(f"│    • {wf['name']:<60}".ljust(98) + "│")
    lines.append("└" + "─" * 97 + "┘")
    lines.append("                                        │")
    lines.append("                                        ▼")

    # 10. RUNNER TYPES
    lines.append("┌" + "─" * 97 + "┐")
    lines.append("│" + " 10. RUNNER TYPES".ljust(98) + "│")
    lines.append("├" + "─" * 50 + "┬" + "─" * 20 + "┬" + "─" * 24 + "┤")
    lines.append(
        "│" + " Runner".ljust(51) + "│" + " Type".ljust(21) + "│" + " Jobs".ljust(25) + "│"
    )
    lines.append("├" + "─" * 50 + "┼" + "─" * 20 + "┼" + "─" * 24 + "┤")
    runner_list = sorted(data["runners"].items(), key=lambda x: -x[1])[:10]
    for runner, count in runner_list:
        r = runner.replace("${{", "").replace("}}", "")[:48]
        r_type = "Linux"
        if "macos" in r.lower():
            r_type = "macOS"
        elif "windows" in r.lower():
            r_type = "Windows"
        elif "rocm" in r.lower():
            r_type = "ROCm"
        elif "xpu" in r.lower():
            r_type = "XPU"
        lines.append(f"│  {r:<48} │ {r_type:<18} │ {count:>20} │")
    lines.append("└" + "─" * 50 + "┴" + "─" * 20 + "┴" + "─" * 24 + "┘")
    lines.append("```")

    # Summary
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- **Workflows:** {len(data['workflows'])}")
    lines.append(
        f"- **Entry:** {len(data['entry'])}, **Reusable:** {len(data['reusable'])}, **Generated:** {len(data['generated'])}"
    )
    lines.append(f"- **Actions:** {len(data['actions'])}")
    lines.append(f"- **Scripts:** {len(data['scripts'])}")
    lines.append(f"- **Test Categories:** {len(data['test_cats'])}")
    lines.append(f"- **Runners:** {len(data['runners'])}")

    output_file = os.path.join(output_dir, "CI_ARCHITECTURE.md")
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Saved: {output_file}")


def main():
    repo_path = sys.argv[1] if len(sys.argv) > 1 else "."
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."

    print(f"Exploring: {repo_path}")
    print("=" * 60)

    data = collect_data(repo_path)

    if not data.get("workflows"):
        print("No workflows found")
        return

    generate_diagram(data, output_dir)
    print("\nDone!")


if __name__ == "__main__":
    main()
