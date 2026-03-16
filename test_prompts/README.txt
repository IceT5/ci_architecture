# Prompt文件说明

此项目CI/CD较大，已自动分割为多个prompt文件：

1. prompt_main.txt - 概览文档，包含：
   - 项目基本信息
   - 完整调用关系图
   - 所有工作流简要列表

2. prompt_1.txt ~ prompt_0.txt - 详细文档批次：
   - 每个包含完整调用关系图
   - 当前批次的详细工作流信息
   - 其他批次的简要信息

## 使用方式

### 方式一：并行处理（推荐）
使用多个subagent并行处理各批次：
- Subagent 1: 处理 prompt_main.txt → 生成概览文档
- Subagent 2: 处理 prompt_1.txt → 生成第1批详细分析
- Subagent 3: 处理 prompt_2.txt → 生成第2批详细分析
- ...
最后合并所有结果。

### 方式二：顺序处理
依次处理每个prompt文件，最后合并结果。

## 合并结果

所有subagent完成后，将响应合并为一个文件后执行：
python ci_diagram_generator.py diagram ci_data.json merged_response.md CI_ARCHITECTURE.md
