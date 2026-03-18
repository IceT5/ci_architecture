# CI Architecture Analyzer

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

一个强大的 GitHub Actions CI/CD 架构分析工具，使用 LLM 进行智能分类和理解。

## 功能特性

- **全面的数据提取**：提取所有 CI/CD 组件，包括工作流、Job、Step、复合 Action 和脚本
- **LLM 驱动分析**：使用 LLM 进行智能分类和理解，无硬编码规则
- **可复用工作流支持**：完整支持 GitHub Actions 可复用工作流（`workflow_call`）
- **Matrix Job 展开**：完整展开 matrix 配置的所有 Job 变体
- **脚本分析**：分析 Python、Shell、PowerShell 和 Batch 脚本，提取函数信息
- **关系映射**：构建工作流调用图、Job 依赖图和 Action 使用图
- **Pre-commit 集成**：提取并记录 pre-commit hook 配置
- **多 CI 系统支持**：支持 CircleCI、GitLab CI、Azure Pipelines 等其他 CI 系统

## 设计理念

**最小化代码自动化，最大化 LLM 智能：**

- **代码只负责数据提取**：Python 脚本从工作流、Job、Step、Action 和脚本中提取原始数据
- **LLM 负责所有理解工作**：分类、组织、关系分析和摘要都由 LLM 处理
- **无硬编码分类**：LLM 根据项目实际内容动态定义阶段和分类
- **按逻辑顺序组织**：LLM 按照 CI/CD 执行流程组织文档

## 安装

### 前置条件

- Python 3.8+
- PyYAML

### 安装依赖

```bash
pip install pyyaml
```

## 快速开始

### 第一步：提取数据

```bash
python ci_data_extractor.py /path/to/repo ci_data.json
```

这将输出 `ci_data.json`，包含：
- 所有工作流及其 Job 和 Step 详情
- Matrix 配置和 with_params 参数
- 复合 Action 及其输入/输出
- CI 脚本及其函数列表
- 工作流调用关系图
- Action 使用统计
- Pre-commit 配置

### 第二步：生成 Prompt

**中小型项目（≤30 个工作流）：**

```bash
python ci_diagram_generator.py prompt ci_data.json prompt.txt
```

**大型项目（>30 个工作流）：**

```bash
python ci_diagram_generator.py split ci_data.json ./prompts/ 10
```

这将生成多个 prompt 文件用于并行处理。

### 第三步：发送给 LLM

读取 prompt 文件并发送给 LLM 进行分析。将响应保存为 `llm_response.md`。

### 第四步：生成最终文档

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.md CI_ARCHITECTURE.md
```

## 项目结构

```
ci_architecture/
├── ci_data_extractor.py      # 核心数据提取模块
├── ci_diagram_generator.py   # Prompt 生成和结果处理
├── SKILL.md                  # LLM Agent 使用说明文档
├── README.md                 # 本文件
└── LICENSE                   # Apache 2.0 许可证
```

## 工作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    数据提取 (Python)                                     │
│  ci_data_extractor.py                                                   │
│  • 扫描 .github/workflows、.github/actions、脚本目录                     │
│  • 提取所有工作流、Job、Step、配置参数                                   │
│  • 提取脚本函数和调用关系                                                │
│  • 输出完整的 JSON 数据                                                  │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ ci_data.json
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    生成 LLM Prompt (Python)                             │
│  ci_diagram_generator.py                                                │
│  • 将原始数据格式化为详细的 prompt                                       │
│  • 包含所有工作流、Job、配置、关系信息                                   │
│  • 指导 LLM 按照执行逻辑组织内容                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Prompt
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    LLM 分析                                              │
│                                                                         │
│  LLM 负责：                                                             │
│  • 分析 CI/CD 流程阶段                                                  │
│  • 确定执行顺序                                                         │
│  • 展示调用关系和依赖                                                   │
│  • 组织为易读的架构文档                                                 │
│  • 提供关键发现和建议                                                   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Markdown 文档
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    保存结果 (Python)                                     │
│  ci_diagram_generator.py                                                │
│  • 清理格式                                                             │
│  • 保存为 CI_ARCHITECTURE.md                                            │
└─────────────────────────────────────────────────────────────────────────┘
```

## 输出文档结构

生成的架构文档包含：

1. **项目概述** - 项目类型和 CI/CD 整体架构
2. **CI/CD 流程图** - 展示整体架构的 ASCII 图
3. **按阶段组织的内容** - 按执行阶段组织的工作流
4. **工作流详情** - 完整的 Job 列表、依赖关系、关键配置
5. **Matrix Job 展开** - 所有 matrix 变体完整列出
6. **脚本和 Action 索引** - 按目录/用途组织
7. **Pre-commit 配置** - 外部和本地 hooks
8. **关键发现和建议**
9. **附录** - 工作流调用关系树

## 支持的 CI 系统

- **GitHub Actions**（主要支持）
  - Workflows (.github/workflows/*.yml)
  - Composite Actions (.github/actions/*/action.yml)
  - Reusable Workflows (workflow_call 触发器)
- **CircleCI** (.circleci/config.yml)
- **GitLab CI** (.gitlab-ci.yml)
- **Azure Pipelines** (azure-pipelines.yml)
- **Jenkins** (Jenkinsfile)
- **Travis CI** (.travis.yml)
- **Drone CI** (.drone.yml)
- **Buildkite** (buildkite.yml)
- **Pre-commit** (.pre-commit-config.yaml)

## 脚本分析

支持分析以下脚本类型：
- **Python** (.py) - 函数定义、导入、subprocess 调用
- **Shell** (.sh) - 函数、source 命令、脚本执行
- **PowerShell** (.ps1) - Dot-sourcing、脚本调用
- **Batch** (.bat) - Call 命令、脚本引用

## 核心类

### CIDataExtractor

主要提取类，负责：
- 查找 CI 相关目录
- 提取完整的工作流数据
- 解析复合 Action
- 分析脚本并跟踪嵌套调用
- 构建关系图

### 数据类

- `WorkflowData` - 完整的工作流信息
- `JobData` - Job 详情及 matrix 展开
- `StepData` - Step 执行详情
- `ActionData` - 复合 Action 信息
- `ScriptData` - 脚本分析结果
- `PreCommitConfigData` - Pre-commit 配置
- `WorkflowCallInput` / `WorkflowCallOutput` - 可复用工作流输入/输出

## 系统要求

- Python 3.8+
- PyYAML

```bash
pip install pyyaml
```

## 许可证

基于 Apache License, Version 2.0 许可。详见 [LICENSE](LICENSE)。

## 版权

Copyright (c) 2026 IceT5. All rights reserved.

## 贡献

欢迎贡献！请随时提交 Pull Request。

## 作者

**IceT5**

---

*本工具专为 LLM Agent 设计，以实现最大的灵活性和智能化 CI/CD 架构分析。*