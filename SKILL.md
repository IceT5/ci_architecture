---
name: ci_architecture
description: |
  Analyzes GitHub Actions CI/CD architecture with LLM-powered classification and understanding.
  
  TRIGGERS: "Analyze ci/cd", "Analyze workflow", "CI architecture", "Test infrastructure", "CI/CD diagram"
---

# CI Architecture Analysis Skill

分析GitHub Actions CI/CD架构，使用LLM进行智能分类和理解。

## 设计理念

**最小化代码自动化，最大化LLM智能分析：**

- **代码只做数据提取**：Python脚本负责提取工作流、Job、Step、Action、脚本等原始数据
- **LLM负责所有理解**：分类、组织顺序、调用关系、摘要都由LLM分析和生成
- **不硬编码分类**：LLM根据项目实际情况动态定义阶段和分类
- **按逻辑顺序组织**：LLM按照CI/CD执行流程组织文档，而非简单的文件名排序

## 工作流程

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    数据提取 (Python)                                      │
│  ci_data_extractor.py                                                   │
│  • 扫描.github/workflows、.github/actions、脚本目录                       │
│  • 提取所有工作流、Job、Step、配置参数                                    │
│  • 提取脚本函数、调用关系                                                 │
│  • 输出完整的JSON数据                                                     │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ ci_data.json
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    生成LLM Prompt (Python)                               │
│  ci_diagram_generator.py                                                │
│  • 将原始数据格式化为详细的Prompt                                         │
│  • 包含所有工作流、Job、配置、关系信息                                     │
│  • 指导LLM按照执行逻辑组织内容                                            │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Prompt
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    LLM分析                                                │
│                                                                         │
│  LLM负责：                                                              │
│  • 分析CI/CD流程阶段                                                     │
│  • 确定执行顺序                                                          │
│  • 展示调用关系和依赖                                                     │
│  • 组织为易读的架构文档                                                   │
│  • 提供关键发现和建议                                                    │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ Markdown文档
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    保存结果 (Python)                                      │
│  ci_diagram_generator.py                                                │
│  • 清理格式                                                              │
│  • 保存为CI_ARCHITECTURE.md                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

## 使用方法

**重要：每次执行此skill后，必须生成最终结果文件 `CI_ARCHITECTURE.md`！**

### 第一步：提取数据

```bash
python ci_data_extractor.py /path/to/repo ci_data.json
```

这会输出 `ci_data.json`，包含：
- 所有工作流及其Job、Step详情
- Matrix配置和with_params参数
- Composite Actions及其输入输出
- CI脚本及其函数列表
- 工作流调用关系图
- Action使用统计

### 第二步：生成Prompt

```bash
python ci_diagram_generator.py prompt ci_data.json > prompt.txt
```

这会生成一个详细的中文Prompt，包含：
- 项目基本信息
- 脚本目录结构
- 工作流调用关系
- 完整的工作流详情（触发条件、Job、配置）
- Composite Actions详情
- CI脚本信息
- 输出格式指导

### 第三步：发送给LLM

将 `prompt.txt` 的内容发送给LLM（Claude、GPT等），让LLM分析并生成架构文档。

LLM会：
1. 分析CI/CD流程阶段（根据实际内容，不使用预设分类）
2. 按照执行逻辑顺序组织内容
3. 展示完整的调用链和依赖关系
4. 生成清晰的Markdown文档

保存LLM的响应为 `llm_response.md`

### 第四步：生成最终文档（必须执行！）

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.md CI_ARCHITECTURE.md
```

**此步骤必须执行，确保最终结果文件 `CI_ARCHITECTURE.md` 被创建。**

## 执行检查清单

执行完此skill后，请确认以下文件已生成：

- [ ] `ci_data.json` - 原始提取数据
- [ ] `prompt.txt` - 发送给LLM的Prompt
- [ ] `llm_response.md` - LLM的响应
- [ ] `CI_ARCHITECTURE.md` - **最终架构文档（必须存在！）**

## 输出文档结构

LLM生成的架构文档包含：

### 1. 项目概述
- 项目类型描述
- CI/CD整体架构说明

### 2. CI/CD流程概览
- 用文本或ASCII图展示整体流程
- 阶段划分和执行顺序

### 3. 按阶段组织的内容
每个阶段包含：
- 阶段说明（这个阶段做什么）
- 触发条件
- 相关工作流及详情
- 调用的脚本和Action
- 与上下游阶段的关系

### 4. 工作流详情
每个工作流包含：
- 目的和触发条件
- Job列表和依赖关系
- 关键配置参数
- 执行步骤概览

### 5. 脚本和Action索引
- 按目录组织
- 用途说明
- 被哪些工作流调用

### 6. 关键发现和建议

## LLM分析原则

Prompt指导LLM：

1. **不硬编码分类** - 根据项目实际内容定义阶段
2. **按执行顺序组织** - 从触发到执行的自然流程
3. **展示调用关系** - workflow_call、needs、action使用
4. **提供关键配置** - Matrix配置、重要参数
5. **保持简洁** - 足够详细但不冗余

## 文件说明

| 文件 | 用途 |
|------|------|
| `ci_data_extractor.py` | 提取原始数据 |
| `ci_diagram_generator.py` | 生成Prompt，保存结果 |
| `analyze_ci_architecture.py` | 旧版：带有硬编码规则的独立分析器 |

## 示例

```bash
# 分析PyTorch项目
python ci_data_extractor.py /path/to/pytorch ci_data.json

# 生成Prompt
python ci_diagram_generator.py prompt ci_data.json > prompt.txt

# 将prompt.txt发送给LLM，保存响应为analysis.md

# 生成最终文档
python ci_diagram_generator.py diagram ci_data.json analysis.md CI_ARCHITECTURE.md
```

## 优势

1. **灵活性** - LLM根据项目特点动态分析，不依赖硬编码规则
2. **逻辑性** - 按执行顺序组织，清晰展示流程
3. **完整性** - 展示调用关系、配置参数、依赖链
4. **可读性** - 结构清晰、层次分明的Markdown文档
5. **可维护** - 无需更新代码，LLM自动适应新项目

## 依赖

- Python 3.8+
- PyYAML

```bash
pip install pyyaml