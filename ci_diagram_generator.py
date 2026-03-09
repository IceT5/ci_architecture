#!/usr/bin/env python3
"""
CI Architecture Diagram Generator - Generate architecture diagrams from LLM analysis

This module generates LLM prompts and processes LLM responses.
ALL classification and organization logic is handled by LLM for maximum flexibility.
"""

import json
from pathlib import Path
from typing import Dict, List, Any


def generate_llm_prompt(raw_data: Dict) -> str:
    """Generate a comprehensive prompt for LLM to analyze CI architecture.
    
    The LLM is responsible for:
    - Determining category structure and order
    - Analyzing workflow execution flow
    - Identifying call relationships
    - Organizing content by logical software engineering stages
    - Creating readable architecture documentation
    """
    
    prompt = """# CI/CD 架构分析请求

**重要：本文档必须使用中文输出！所有内容、标题、描述、分析都必须使用中文！**

你是一位资深DevOps工程师，请深入分析项目的CI/CD架构，并生成一份结构清晰的架构文档。

## 你的任务

### 1. 分析并确定CI/CD流程阶段

请根据项目的实际情况，分析并确定CI/CD的各个阶段。不要使用预设的分类，而是根据项目的工作流内容来定义合理的阶段划分。

考虑：
- 工作流的触发条件（on字段）
- 工作流之间的调用关系（uses字段）
- Job之间的依赖关系（needs字段）
- 每个工作流/Job的实际目的

### 2. 按照执行逻辑顺序组织

请按照CI/CD的实际执行顺序来组织文档内容：
- 首先是触发入口
- 然后是前置检查和准备
- 接着是构建、测试等核心流程
- 最后是收尾和发布

### 3. 展示完整的调用链

对于每个工作流，请展示：
- 它被哪些工作流调用（或被什么事件触发）
- 它调用了哪些其他工作流
- 它使用了哪些Action
- 它执行了哪些脚本

### 4. 提供关键配置信息

对于重要的Job，请列出：
- 运行环境（runs-on）
- 关键配置参数
- Matrix配置内容
- 输入输出参数

### 5. 【必须】完整列出所有Job

**严格要求**：必须完整列出每个工作流中的所有Job，不能省略任何Job！
- 必须包含所有Job的名称
- 必须描述每个Job的目的
- 不能使用"..."或其他省略符号
- 即使Job数量很多，也必须全部列出

---

## 项目数据

"""
    
    # Add repository info
    prompt += f"### 仓库名称\n{raw_data.get('repo_name', 'Unknown')}\n\n"
    
    # Add CI directories
    ci_dirs = raw_data.get("ci_directories", [])
    if ci_dirs:
        prompt += "### CI相关目录\n```\n"
        for d in ci_dirs:
            prompt += f"{d}\n"
        prompt += "```\n\n"
    
    # Add scripts by directory
    scripts_by_dir = raw_data.get("scripts_by_directory", {})
    if scripts_by_dir:
        prompt += "### 脚本目录结构\n```\n"
        for dir_path, scripts in scripts_by_dir.items():
            prompt += f"{dir_path}/\n"
            for s in scripts[:10]:
                prompt += f"  - {s}\n"
            if len(scripts) > 10:
                prompt += f"  ... (+{len(scripts)-10} more)\n"
        prompt += "```\n\n"
    
    # Add workflow relationships first
    relationships = raw_data.get("relationships", {})
    workflow_calls = relationships.get("workflow_calls", {})
    if workflow_calls:
        prompt += "### 工作流调用关系\n```\n"
        prompt += "# 格式: 被调用工作流 <- 调用者\n"
        for callee, callers in workflow_calls.items():
            caller_list = ", ".join(callers[:5])
            if len(callers) > 5:
                caller_list += f" (+{len(callers)-5})"
            prompt += f"{callee}\n  <- {caller_list}\n"
        prompt += "```\n\n"
    
    # Add actions usage
    action_usages = relationships.get("action_usages", {})
    if action_usages:
        prompt += "### Action使用统计\n```\n"
        for action, users in list(action_usages.items())[:20]:
            prompt += f"- {action}: 被 {len(users)} 处使用\n"
        prompt += "```\n\n"
    
    # Add detailed workflow information
    workflows = raw_data.get("workflows", {})
    if workflows:
        prompt += "### 工作流完整信息\n\n"
        for wf_name, wf in workflows.items():
            prompt += f"---\n\n#### {wf_name}\n\n"
            
            # Basic info
            prompt += f"**名称**: {wf.get('name', 'N/A')}\n\n"
            prompt += f"**路径**: `{wf.get('path', 'N/A')}`\n\n"
            
            # Triggers
            triggers = wf.get("triggers", [])
            trigger_details = wf.get("trigger_details", {})
            prompt += f"**触发条件**: {', '.join(triggers)}\n"
            if trigger_details:
                prompt += "```yaml\n"
                for trigger, details in list(trigger_details.items())[:3]:
                    if isinstance(details, dict):
                        prompt += f"# {trigger}:\n"
                        for k, v in list(details.items())[:3]:
                            prompt += f"#   {k}: {v}\n"
                prompt += "```\n"
            prompt += "\n"
            
            # Jobs
            jobs = wf.get("jobs", {})
            if jobs:
                prompt += f"**Jobs** ({len(jobs)}个):\n\n"
                for job_name, job in jobs.items():
                    prompt += f"##### `{job_name}`\n\n"
                    
                    # Display name
                    display_name = job.get("display_name", "")
                    if display_name and display_name != job_name:
                        prompt += f"显示名称: {display_name}\n\n"
                    
                    # Dependencies
                    needs = job.get("needs", [])
                    if needs:
                        prompt += f"**依赖**: {', '.join(needs)}\n\n"
                    
                    # Reusable workflow
                    uses = job.get("uses", "")
                    if uses:
                        prompt += f"**调用工作流**: `{uses}`\n\n"
                        # with params
                        with_params = job.get("with_params", {})
                        if with_params:
                            prompt += "**传入参数**:\n```yaml\n"
                            for k, v in list(with_params.items())[:8]:
                                v_str = str(v)
                                if len(v_str) > 100:
                                    v_str = v_str[:100] + "..."
                                prompt += f"{k}: {v_str}\n"
                            prompt += "```\n\n"
                    
                    # Runner
                    runs_on = job.get("runs_on", "")
                    if runs_on:
                        prompt += f"**运行环境**: `{runs_on}`\n\n"
                    
                    # Condition
                    if_condition = job.get("if_condition", "")
                    if if_condition:
                        prompt += f"**条件**: `{if_condition[:100]}`\n\n"
                    
                    # Matrix
                    matrix = job.get("matrix", {})
                    if matrix:
                        include = matrix.get("include", [])
                        if include:
                            prompt += f"**Matrix配置** ({len(include)}个变体):\n```\n"
                            for cfg in include[:5]:
                                if isinstance(cfg, dict):
                                    items = list(cfg.items())[:4]
                                    prompt += "  " + ", ".join(f"{k}={v}" for k, v in items) + "\n"
                            if len(include) > 5:
                                prompt += f"  ... (+{len(include)-5} more)\n"
                            prompt += "```\n\n"
                    
                    # Steps
                    steps = job.get("steps", [])
                    if steps:
                        prompt += f"**执行步骤** ({len(steps)}步):\n```\n"
                        for i, step in enumerate(steps[:15], 1):
                            step_name = step.get("name", "") or step.get("uses", "") or step.get("id", f"step-{i}")
                            if step.get("uses"):
                                prompt += f"{i}. [{step_name}] -> uses: {step.get('uses', '')}\n"
                            elif step.get("run"):
                                run_preview = step.get("run", "")[:80].replace("\n", " ")
                                prompt += f"{i}. [{step_name}] -> run: {run_preview}...\n"
                            else:
                                prompt += f"{i}. [{step_name}]\n"
                        if len(steps) > 15:
                            prompt += f"   ... (+{len(steps)-15} more)\n"
                        prompt += "```\n\n"
                    
                    # Calls
                    calls_workflows = job.get("calls_workflows", [])
                    calls_actions = job.get("calls_actions", [])
                    if calls_workflows:
                        prompt += f"**调用工作流**: {', '.join(calls_workflows)}\n\n"
                    if calls_actions:
                        prompt += f"**使用Action**: {', '.join(calls_actions[:10])}\n\n"
                    
                    prompt += "---\n\n"
    
    # Add actions
    actions = raw_data.get("actions", [])
    if actions:
        prompt += "### Composite Actions\n\n"
        for action in actions:
            prompt += f"#### `{action.get('name')}`\n\n"
            prompt += f"**路径**: `{action.get('path')}`\n\n"
            desc = action.get("description", "")
            if desc:
                prompt += f"**描述**: {desc}\n\n"
            
            inputs = action.get("inputs", {})
            if inputs:
                prompt += f"**输入参数**:\n```\n"
                for name, inp in inputs.items():
                    req = "required" if inp.get("required") else "optional"
                    default = inp.get("default", "")
                    prompt += f"  {name} ({req}): {inp.get('description', '')[:50]}"
                    if default:
                        prompt += f" [default: {str(default)[:30]}]"
                    prompt += "\n"
                prompt += "```\n\n"
            
            used_by = action.get("used_by", [])
            if used_by:
                prompt += f"**被使用于**: {len(used_by)} 处\n\n"
    
    # Add scripts
    scripts = raw_data.get("scripts", [])
    if scripts:
        prompt += "### CI脚本\n\n"
        for script in scripts[:30]:
            prompt += f"#### `{script.get('name')}`\n\n"
            prompt += f"**路径**: `{script.get('path')}`\n\n"
            prompt += f"**类型**: {script.get('type')}\n\n"
            
            funcs = script.get("functions", [])
            if funcs:
                prompt += f"**函数**: {', '.join(funcs[:10])}\n\n"
            
            called_by = script.get("called_by", [])
            if called_by:
                prompt += f"**被调用**: {len(called_by)} 次\n\n"
    
    # Add pre-commit configurations
    pre_commit_configs = raw_data.get("pre_commit_configs", [])
    if pre_commit_configs:
        prompt += "### Pre-commit 配置\n\n"
        prompt += "**说明**: Pre-commit 是一个本地代码质量检查框架，在git commit前自动运行检查。虽然不通过GitHub Actions触发，但属于CI/CD整体能力的一部分。\n\n"
        
        for config in pre_commit_configs:
            prompt += f"#### 配置文件: `{config.get('path')}`\n\n"
            
            # CI settings
            ci_settings = config.get("ci", {})
            if ci_settings:
                prompt += f"**CI设置**:\n```\n"
                for k, v in ci_settings.items():
                    prompt += f"  {k}: {v}\n"
                prompt += "```\n\n"
            
            # Default stages
            default_stages = config.get("default_stages", [])
            if default_stages:
                prompt += f"**默认阶段**: {', '.join(default_stages)}\n\n"
            
            # External repo hooks
            repos = config.get("repos", [])
            if repos:
                prompt += f"**外部Hook** ({len(repos)}个):\n```\n"
                # Group by repo for better readability
                repos_by_source = {}
                for hook in repos:
                    repo = hook.get("repo", "unknown")
                    if repo not in repos_by_source:
                        repos_by_source[repo] = []
                    repos_by_source[repo].append(hook)
                
                for repo_url, hooks in repos_by_source.items():
                    prompt += f"\n# 来源: {repo_url}\n"
                    for hook in hooks:
                        hook_id = hook.get("id", "")
                        desc = hook.get("description", "")[:50] if hook.get("description") else ""
                        prompt += f"  - {hook_id}"
                        if desc:
                            prompt += f": {desc}"
                        prompt += "\n"
                prompt += "```\n\n"
            
            # Local hooks
            local_hooks = config.get("local_hooks", [])
            if local_hooks:
                prompt += f"**本地Hook** ({len(local_hooks)}个):\n```\n"
                for hook in local_hooks:
                    hook_id = hook.get("id", "")
                    desc = hook.get("description", "")[:50] if hook.get("description") else ""
                    prompt += f"  - {hook_id}"
                    if desc:
                        prompt += f": {desc}"
                    prompt += "\n"
                prompt += "```\n\n"
    
    # Expected output format
    prompt += """
---

## 输出格式要求

**语言要求：本文档必须使用中文输出！所有标题、描述、分析内容都必须是中文！**

请输出一个完整的Markdown格式文档，按照你分析出的逻辑顺序组织内容。

### 文档结构要求

1. **项目概述** - 简要描述项目类型和CI/CD整体架构

2. **CI/CD流程图** - 用文本或ASCII图形展示整体流程

3. **按阶段组织的内容** - 每个阶段包含：
   - 阶段说明（这个阶段做什么）
   - 相关工作流列表
   - 工作流详情（触发条件、**完整Job列表**、关键配置）
   - 调用的脚本和Action
   - 与其他阶段的关系

4. **脚本和Action索引** - 按目录或用途组织

5. **关键发现和建议**

### Job列表要求

**必须完整列出所有Job！** 对于每个工作流：
- 列出所有Job的名称（不能省略任何一个）
- 每个Job都要有简要描述
- 标注Job之间的依赖关系（needs）
- 如果有Matrix配置，说明有多少个变体

### 格式示例

```markdown
# [项目名] CI/CD架构分析

## 项目概述
[项目类型和CI/CD整体描述，使用中文]

## CI/CD流程概览
[流程图或执行顺序，使用中文]

## 阶段一：触发与入口

### 触发条件
- push事件触发：xxx工作流
- PR事件触发：xxx工作流
- 定时触发：xxx工作流

### 入口工作流

#### pull.yml
- **目的**: PR验证入口
- **触发**: pull_request
- **包含的Job**（共X个）:
  1. get-label-type: 确定运行器类型
  2. target-determination: 确定测试目标
  3. linux-build: 构建Linux版本
  4. linux-test: 运行测试
  5. [必须列出所有Job，不能省略]
- **依赖关系**: get-label-type -> target-determination -> linux-build -> linux-test
- **关键配置**: [列出重要的with_params]

#### trunk.yml
- **目的**: 主分支构建
- **触发**: push到main分支
- **包含的Job**（共X个）:
  1. job1: 描述
  2. job2: 描述
  3. [完整列出]
- **依赖关系**: ...
- **关键配置**: ...

## 阶段二：构建
[类似结构，完整列出所有工作流的所有Job]

...

## 脚本目录
### .github/scripts/
- build.sh: 构建脚本
- test.sh: 测试脚本
[完整列出所有脚本]

## 复合Action目录
### .github/actions/setup-linux/
- 用途: Linux环境设置
- 输入: [参数列表]
- 使用于: [工作流列表]
[完整列出所有Action]

## 发现和建议
1. [发现或建议，使用中文]
2. [...]
```

**重要提醒**:
1. **必须使用中文输出所有内容**
2. **必须完整列出每个工作流的所有Job，不能省略**
3. 不要硬编码分类，根据实际内容分析
4. 展示调用关系和依赖关系
5. 提供足够的细节但不冗余
6. 使用清晰的层级结构
"""

    return prompt


def parse_llm_response(llm_response: str) -> str:
    """Parse LLM response - just return the content as-is.
    
    The LLM is expected to produce a complete Markdown document.
    We don't need to do any processing - just save it.
    """
    # Extract content - if wrapped in code blocks, extract it
    content = llm_response.strip()
    
    # Remove markdown code block wrapper if present
    if content.startswith("```markdown"):
        content = content[len("```markdown"):]
    elif content.startswith("```"):
        content = content[3:]
    
    if content.endswith("```"):
        content = content[:-3]
    
    return content.strip()


def generate_architecture_diagram(
    raw_data: Dict,
    llm_response: str,
    output_file: str
) -> str:
    """Generate architecture diagram from LLM's analysis.
    
    This function simply processes and saves the LLM's output.
    All the intelligence is in the LLM prompt and response.
    """
    
    # Parse the LLM response (just clean up any code block wrappers)
    content = parse_llm_response(llm_response)
    
    # Write to file
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Architecture diagram saved to: {output_file}")
    
    return content


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python ci_diagram_generator.py prompt <raw_data.json> - Generate LLM prompt")
        print("  python ci_diagram_generator.py diagram <raw_data.json> <llm_response.md> [output_file] - Generate diagram")
        print()
        print("Workflow:")
        print("  1. Extract data: python ci_data_extractor.py /path/to/repo ci_data.json")
        print("  2. Generate prompt: python ci_diagram_generator.py prompt ci_data.json > prompt.txt")
        print("  3. Send prompt to LLM and save response as llm_response.md")
        print("  4. Generate diagram: python ci_diagram_generator.py diagram ci_data.json llm_response.md CI_ARCHITECTURE.md")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "prompt":
        # Generate LLM prompt from raw data
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        prompt = generate_llm_prompt(raw_data)
        print(prompt)
    
    elif command == "diagram":
        # Generate diagram from raw data + LLM response
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            raw_data = json.load(f)
        
        with open(sys.argv[3], "r", encoding="utf-8") as f:
            llm_response = f.read()
        
        output_file = sys.argv[4] if len(sys.argv) > 4 else "CI_ARCHITECTURE.md"
        
        diagram = generate_architecture_diagram(raw_data, llm_response, output_file)
        print(f"Done. Output saved to: {output_file}")
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)