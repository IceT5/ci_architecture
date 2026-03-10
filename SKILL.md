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

**重要：此skill必须严格按照以下步骤执行，每个步骤都必须实际运行Python脚本！**

**禁止跳过步骤！禁止直接基于提取数据创建文档！必须通过LLM分析生成！**

**执行原则：**
1. **必须按步骤执行** - 不能跳过任何步骤
2. **遇到错误必须修复** - 如果某个步骤失败，必须分析错误原因并修复后重试
3. **subagent失败时** - 如果使用new_task创建subagent失败，必须：
   - 检查错误信息，理解失败原因
   - 调整new_task的context格式和内容
   - 重试直到成功
4. **最终必须输出** - 必须生成`CI_ARCHITECTURE.md`文件才算任务完成

### 第一步：提取数据（必须执行）

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
- **Pre-commit配置**（.pre-commit-config.yaml）及其Hook列表

### 第二步：生成Prompt

**对于小型项目（≤20个工作流）：**

```bash
# 方法一：直接输出到文件（推荐）
python ci_diagram_generator.py prompt ci_data.json prompt.txt

# 方法二：重定向输出
python ci_diagram_generator.py prompt ci_data.json > prompt.txt
```

**对于大型项目（>20个工作流）：**

```bash
# 使用split命令自动分割为多个prompt文件
python ci_diagram_generator.py split ci_data.json ./prompts/ [每批工作流数量]

# 示例：每批10个工作流
python ci_diagram_generator.py split ci_data.json ./prompts/ 10
```

这会生成多个文件：
- `prompt_main.txt` - 概览文档（项目信息、完整调用关系图、所有工作流列表）
- `prompt_1.txt`, `prompt_2.txt`, ... - 详细文档批次（每批包含完整调用关系图+当前批次详情）
- `README.txt` - 使用说明

**分割策略：**
- 每个批次prompt都包含完整的调用关系图
- 每个批次包含当前批次工作流的详细信息
- 每个批次包含其他批次的简要信息
- 确保subagent分析时有全局视角，不会丢失调用关系

### 第三步：发送给LLM（核心步骤！）

**⚠️ 关键要求：必须完整读取prompt.txt文件！**

1. **使用read_file工具完整读取prompt.txt**
   - 不能只读取部分内容
   - 如果文件很大，系统会自动处理分块读取
   - 必须获取完整的prompt内容

2. **将完整prompt发送给LLM进行分析**

3. **保存LLM的完整响应为llm_response.md**

**对于大型项目的优化处理：**

如果项目工作流数量很多（>20个），可采用以下策略：

**策略1：分批处理（推荐）**
```
将工作流分成多批（每批5-10个），使用subagent并行处理：
- 批次1：入口工作流（push、PR触发）
- 批次2：构建工作流
- 批次3：测试工作流
- 批次4：部署工作流
- 最后合并结果
```

**策略2：使用subagent并行分析**
```
1. 主agent读取完整的ci_data.json和prompt.txt
2. 根据工作流数量决定是否分批
3. 如果需要分批，使用new_task创建子任务：
   - 子任务1：分析入口阶段工作流
   - 子任务2：分析构建阶段工作流
   - 子任务3：分析测试阶段工作流
4. 并行执行子任务
5. 合并所有子任务的结果
```

**subagent创建要求：**

使用new_task创建subagent时，必须遵循以下格式：

```
<new_task>
<context>
Current Work: [当前任务描述]

Key Concepts:
- [关键概念1]
- [关键概念2]

Relevant Files/Code:
- [相关文件路径]: [简要说明]

Problem Solving:
- [需要解决的问题]
- [期望的输出]

Pending & Next:
- [待完成步骤]
- [下一步行动]
</context>
</new_task>
```

**注意事项：**
- context必须是简洁的纯文本
- 避免在context中使用复杂的XML或特殊字符
- 如果new_task失败，检查错误信息并调整context格式
- 必须重试直到成功创建subagent

**策略3：层级分析**
```
第一层：生成概览文档（工作流列表、整体流程）
第二层：为每个重要工作流生成详细文档
最后：合并为完整架构文档
```

### 第四步：生成最终文档（必须执行！）

```bash
python ci_diagram_generator.py diagram ci_data.json llm_response.md CI_ARCHITECTURE.md
```

**此步骤必须执行，确保最终结果文件 `CI_ARCHITECTURE.md` 被创建。**

### 执行流程图

```
┌─────────────────────────────────────────────────────────────────┐
│  第一步：python ci_data_extractor.py /repo ci_data.json        │
│  输出：ci_data.json                                              │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│  第二步：python ci_diagram_generator.py prompt ci_data.json prompt.txt │
│  输出：prompt.txt                                                │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│  第三步：完整读取prompt.txt → 发送给LLM → 保存响应              │
│                                                                  │
│  大型项目处理方式：                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │ Subagent 1   │  │ Subagent 2   │  │ Subagent 3   │ (并行)    │
│  │ 入口工作流   │  │ 构建工作流   │  │ 测试工作流   │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│           ↓              ↓              ↓                       │
│           └──────────────┴──────────────┘                       │
│                          ↓                                       │
│                   合并结果 → llm_response.md                     │
└─────────────────────────────────────────────────────────────────┘
                                ↓
┌─────────────────────────────────────────────────────────────────┐
│  第四步：python ci_diagram_generator.py diagram ci_data.json    │
│          llm_response.md CI_ARCHITECTURE.md                     │
│  输出：CI_ARCHITECTURE.md                                        │
└─────────────────────────────────────────────────────────────────┘
```

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

### 2. CI/CD流程概览（必须包含ASCII架构图）

**必须**在文档开头部分输出整体CI/CD架构图，使用ASCII diagram形式展示：

```
示例格式：

┌─────────────────────────────────────────────────────────────────────────────┐
│                           CI/CD 整体架构                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐         │
│   │  触发入口  │────▶│  代码检查  │────▶│   构建    │────▶│   测试    │         │
│   │          │     │          │     │          │     │          │         │
│   │ • push   │     │ • lint   │     │ • compile│     │ • unit   │         │
│   │ • PR     │     │ • format │     │ • package│     │ • e2e    │         │
│   │ • schedule│    │ • type   │     │ • docker │     │ • perf   │         │
│   └──────────┘     └──────────┘     └──────────┘     └──────────┘         │
│        │                │                │                │               │
│        │                │                │                │               │
│        │                ▼                ▼                ▼               │
│        │          ┌──────────────────────────────────────────┐            │
│        │          │              Artifact 仓库                │            │
│        │          └──────────────────────────────────────────┘            │
│        │                                   │                              │
│        │                                   ▼                              │
│        │          ┌──────────┐     ┌──────────┐                          │
│        └─────────▶│   部署    │────▶│  通知    │                          │
│                   │          │     │          │                          │
│                   │ • staging│     │ • slack  │                          │
│                   │ • prod   │     │ • email  │                          │
│                   └──────────┘     └──────────┘                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

ASCII架构图要求：
- 展示完整的CI/CD流程阶段
- 使用框线和箭头表示流程方向
- 标注每个阶段的关键操作
- 清晰展示阶段之间的依赖关系

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

### 6. Pre-commit配置（如存在）
- 外部Hook列表（来自各仓库）
- 本地Hook列表
- 默认阶段配置
- CI相关设置

### 7. 关键发现和建议

### 8. 附录（必须包含）

#### 工作流调用关系图（必须输出）

**必须**在附录中输出完整的工作流调用关系图，使用树状结构展示：

```
示例格式：

项目CI/CD调用关系树
├── 触发入口
│   ├── push事件
│   │   └── build.yml
│   ├── pull_request事件
│   │   └── ci.yml
│   └── workflow_call事件
│       └── reusable-build.yml
│
├── build.yml (push触发)
│   ├── Jobs:
│   │   ├── setup → build → test
│   │   └── lint (并行)
│   └── 调用:
│       └── reusable-setup.yml
│
├── ci.yml (PR触发)
│   ├── Jobs:
│   │   ├── check → build
│   │   └── test-unit → test-e2e
│   └── 调用:
│       ├── reusable-build.yml
│       └── ./.github/actions/setup
│
└── reusable-*.yml (可复用工作流)
    ├── reusable-build.yml
    │   └── 输入: platform, config
    └── reusable-setup.yml
        └── 输入: environment
```

树状结构要求：
- 根节点显示项目名称
- 第一层：触发入口类型（事件类型）
- 第二层：工作流文件
- 第三层：Job依赖链和调用的其他工作流/Action
- 使用 `→` 表示Job依赖关系（needs）
- 使用缩进表示层级关系

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