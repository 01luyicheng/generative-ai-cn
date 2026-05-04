import json

FILEPATH = '/home/runner/work/generative-ai/generative-ai/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb'

with open(FILEPATH, 'r', encoding='utf-8') as f:
    data = json.load(f)

cells = data['cells']

# ── helpers ──────────────────────────────────────────────────────────────────
def replace_source(cell, old, new):
    cell['source'] = [line.replace(old, new) for line in cell['source']]

def set_source(cell, new_lines):
    cell['source'] = new_lines

def find_cell(id_val):
    for c in cells:
        if c.get('metadata', {}).get('id') == id_val:
            return c
    return None

# ─────────────────────────────────────────────────────────────────────────────
# CELL: JAPoU8Sm5E6e  (title + badge table)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('JAPoU8Sm5E6e')
set_source(c, [
    "# 使用 Vertex AI Memory Bank 进行治理\n",
    "\n",
    "<table align=\"left\">\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://www.gstatic.com/pantheon/images/bigquery/welcome_page/colab-logo.svg\" alt=\"Google Colaboratory logo\"><br> 在 Colab 中打开\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/colab/import/https:%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fagents%2Fagent_engine%2Fmemory_bank%2Fget_started_with_memory_bank_governance.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://lh3.googleusercontent.com/JmcxdQi-qOpctIvWKgPtrzZdJJK-J3sWE1RsfjZNwshCFgE_9fULcNpuXYTilIR2hjwN\" alt=\"Google Cloud Colab Enterprise logo\"><br> 在 Colab Enterprise 中打开\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://console.cloud.google.com/vertex-ai/workbench/deploy-notebook?download_url=https://raw.githubusercontent.com/GoogleCloudPlatform/generative-ai/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\">\n",
    "      <img src=\"https://www.gstatic.com/images/branding/gcpiconscolors/vertexai/v1/32px.svg\" alt=\"Vertex AI logo\"><br> 在 Vertex AI Workbench 中打开\n",
    "    </a>\n",
    "  </td>\n",
    "  <td style=\"text-align: center\">\n",
    "    <a href=\"https://github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\">\n",
    "      <img width=\"32px\" src=\"https://raw.githubusercontent.com/primer/octicons/refs/heads/main/icons/mark-github-24.svg\" alt=\"GitHub logo\"><br> 在 GitHub 上查看\n",
    "    </a>\n",
    "  </td>\n",
    "</table>\n",
    "\n",
    "<div style=\"clear: both;\"></div>\n",
    "\n",
    "**分享至：**\n",
    "\n",
    "<a href=\"https://www.linkedin.com/sharing/share-offsite/?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg\" alt=\"LinkedIn logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://bsky.app/intent/compose?text=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/7/7a/Bluesky_Logo.svg\" alt=\"Bluesky logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://twitter.com/intent/tweet?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/5a/X_icon_2.svg\" alt=\"X logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://reddit.com/submit?url=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://redditinc.com/hubfs/Reddit%20Inc/Brand/Reddit_Logo.png\" alt=\"Reddit logo\">\n",
    "</a>\n",
    "\n",
    "<a href=\"https://www.facebook.com/sharer/sharer.php?u=https%3A//github.com/GoogleCloudPlatform/generative-ai/blob/main/agents/agent_engine/memory_bank/get_started_with_memory_bank_governance.ipynb\" target=\"_blank\">\n",
    "  <img width=\"20px\" src=\"https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg\" alt=\"Facebook logo\">\n",
    "</a>"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: tvgnzT1CKxrO  (Overview)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('tvgnzT1CKxrO')
set_source(c, [
    "## 概述\n",
    "\n",
    "本 notebook 演示了如何使用 **Vertex AI Memory Bank 的治理功能** 构建**客户支持系统**。您将学习如何实施数据保留策略、维护审计追踪，并在构建智能客户支持代理的同时满足法规合规要求。\n",
    "\n",
    "完成本教程后，您将了解如何：\n",
    "\n",
    "* **管理基本记忆操作**：手动创建、更新、删除和检索记忆\n",
    "* **从对话中生成记忆**：从客户交互中提取结构化事实\n",
    "* **配置细粒度 TTL（Time-To-Live）**：为不同数据类型设置不同的保留期（30/90/365 天），以符合数据保留法规\n",
    "* **按主题过滤记忆**：检索特定类别的数据\n",
    "* **追踪记忆修订版本**：维护完整的审计追踪，展示客户数据随时间演变的过程\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 61RBz8LLbxCR  (Install Vertex AI SDK)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('61RBz8LLbxCR')
set_source(c, [
    "### 安装 Vertex AI SDK\n",
    "\n",
    "首先，安装 Vertex AI SDK。我们指定 1.111.0 或更高版本，以确保拥有所有最新的 Memory Bank 功能。\n",
    "\n",
    "**注意**：此操作将安装 SDK。安装完成后，Colab 可能会提示您重启运行时，这是正常现象——按提示点击"重启运行时"即可。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: No17Cw5hgx12  (Install Google Gen AI SDK)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('No17Cw5hgx12')
set_source(c, [
    "### 安装 Google Gen AI SDK 及其他所需包\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: dmWOrTJ3gx13  (Authenticate)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('dmWOrTJ3gx13')
set_source(c, [
    "### 验证您的 notebook 环境\n",
    "\n",
    "如果您在 **Google Colab** 中运行本 notebook，请运行以下单元格来验证您的账号。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: DF4l8DTdWgPY  (Set project info)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('DF4l8DTdWgPY')
set_source(c, [
    "### 设置 Google Cloud 项目信息\n",
    "\n",
    "要开始使用 Vertex AI，您必须拥有一个现有的 Google Cloud 项目，并[启用 Vertex AI API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com)。\n",
    "\n",
    "详细了解[设置项目和开发环境](https://cloud.google.com/vertex-ai/docs/start/cloud-environment)。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 5303c05f7aa6  (Import libraries)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('5303c05f7aa6')
set_source(c, [
    "### 导入库\n",
    "\n",
    "我们将导入标准 Python 库以及 Vertex AI SDK 中的多个专用类。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 6fc324893334  (code: imports)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('6fc324893334')
set_source(c, [
    "import datetime\n",
    "import os\n",
    "import uuid\n",
    "import warnings\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")\n",
    "\n",
    "# 为 Memory Bank 导入基于类的类型\n",
    "from vertexai import types\n",
    "\n",
    "# 基础配置类型\n",
    "MemoryBankConfig = types.ReasoningEngineContextSpecMemoryBankConfig\n",
    "SimilaritySearchConfig = (\n",
    "    types.ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig\n",
    ")\n",
    "GenerationConfig = types.ReasoningEngineContextSpecMemoryBankConfigGenerationConfig\n",
    "\n",
    "# 用于治理的高级配置类型\n",
    "TtlConfig = types.ReasoningEngineContextSpecMemoryBankConfigTtlConfig\n",
    "GranularTtlConfig = (\n",
    "    types.ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig\n",
    ")\n",
    "CustomizationConfig = types.MemoryBankCustomizationConfig\n",
    "MemoryTopic = types.MemoryBankCustomizationConfigMemoryTopic\n",
    "ManagedMemoryTopic = types.MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic\n",
    "CustomMemoryTopic = types.MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic\n",
    "GenerateMemoriesExample = types.MemoryBankCustomizationConfigGenerateMemoriesExample\n",
    "ConversationSource = (\n",
    "    types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource\n",
    ")\n",
    "ConversationSourceEvent = (\n",
    "    types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent\n",
    ")\n",
    "ExampleGeneratedMemory = (\n",
    "    types.MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory\n",
    ")\n",
    "ManagedTopicEnum = types.ManagedTopicEnum\n",
    "\n",
    "print(\"✅ 库导入成功！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: DQFPukme7p07  (helper function md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('DQFPukme7p07')
set_source(c, [
    "### 定义用于显示记忆的辅助函数\n",
    "\n",
    "该辅助函数在整个教程中为显示生成的记忆提供一致的格式。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: zMEtiWs27s48  (code: helper function)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('zMEtiWs27s48')
set_source(c, [
    "def display_generated_memories(operation, client, title=\"生成的记忆\"):\n",
    "    \"\"\"以一致的格式显示来自生成操作的记忆。\n",
    "\n",
    "    Args:\n",
    "        operation: client.agent_engines.memories.generate() 的返回结果\n",
    "        client: Vertex AI 客户端实例\n",
    "        title: 显示在记忆上方的标题\n",
    "    \"\"\"\n",
    "    if operation.response and operation.response.generated_memories:\n",
    "        print(f\"\\n✅ {title}：{len(operation.response.generated_memories)}\\n\")\n",
    "\n",
    "        for i, gen_memory in enumerate(operation.response.generated_memories, 1):\n",
    "            # 跳过已删除的记忆——我们只想显示活跃的记忆\n",
    "            if gen_memory.action != \"DELETED\" and gen_memory.memory:\n",
    "                try:\n",
    "                    # 获取完整的记忆详情，包括主题和元数据\n",
    "                    full_memory = client.agent_engines.memories.get(\n",
    "                        name=gen_memory.memory.name\n",
    "                    )\n",
    "                    # 视觉指示器：新记忆 vs 更新的记忆\n",
    "                    action_icon = \"🆕\" if gen_memory.action == \"CREATED\" else \"🔄\"\n",
    "                    print(f\"   {action_icon} {i}. {full_memory.fact}\")\n",
    "                except Exception as e:\n",
    "                    print(f\"   ⚠️ 无法检索记忆：{e}\")\n",
    "    else:\n",
    "        print(f\"\\n📭 未找到{title}\")\n",
    "\n",
    "\n",
    "print(\"✅ 辅助函数已定义！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: at-z4pQE7xuS  (Create basic Memory Bank md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('at-z4pQE7xuS')
set_source(c, [
    "## 在 Vertex AI Agent Engine 上创建基础 Memory Bank\n",
    "\n",
    "让我们从基础开始，使用基本配置创建一个简单的 Memory Bank，稍后再添加高级治理功能。AgentEngine 资源充当 Memory Bank 实例的容器。让我们以最小配置创建一个来入门。\n",
    "\n",
    "**基础配置组件**：\n",
    "\n",
    "1. **相似度搜索配置（Similarity Search Config）**：指定用于语义记忆检索的嵌入模型\n",
    "   - 我们使用 `text-embedding-005`，非常适合英文对话\n",
    "\n",
    "2. **生成配置（Generation Config）**：定义从对话中提取记忆所用的 LLM\n",
    "   - 我们使用 `gemini-2.5-flash`，速度快且功能强大"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: te9P-JUa756L  (code: create memory config)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('te9P-JUa756L')
set_source(c, [
    "print(\"🧠 正在创建基础 Memory Bank 配置...\\n\")\n",
    "\n",
    "# 创建最小化 Memory Bank 配置\n",
    "basic_memory_config = MemoryBankConfig(\n",
    "    # 用于相似度搜索的嵌入模型\n",
    "    similarity_search_config=SimilaritySearchConfig(\n",
    "        embedding_model=f\"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/text-embedding-005\"\n",
    "    ),\n",
    "    # 用于记忆提取的 LLM\n",
    "    generation_config=GenerationConfig(\n",
    "        model=f\"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-2.5-flash\"\n",
    "    ),\n",
    ")\n",
    "\n",
    "print(\"✅ 基础 Memory Bank 配置创建成功！\")\n",
    "print(\"   嵌入模型：text-embedding-005\")\n",
    "print(\"   生成模型：gemini-2.5-flash\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: FGOu_Na47-Ky  (Now let's create Agent Engine md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('FGOu_Na47-Ky')
set_source(c, [
    "现在，让我们使用此基础配置创建 Agent Engine。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 0nijEqyq8Ata  (code: create agent engine)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('0nijEqyq8Ata')
set_source(c, [
    "print(\"\\n🛠️ 正在使用基础 Memory Bank 创建 Agent Engine...\\n\")\n",
    "print(\"⏳ 正在配置后端基础架构...\")\n",
    "\n",
    "# 创建 Agent Engine\n",
    "agent_engine = client.agent_engines.create(\n",
    "    config={\"context_spec\": {\"memory_bank_config\": basic_memory_config}}\n",
    ")\n",
    "\n",
    "agent_engine_name = agent_engine.api_resource.name\n",
    "\n",
    "print(\"\\n✅ Agent Engine 创建成功！\")\n",
    "print(f\"   资源名称：{agent_engine_name}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 9DxjCyCq8Le4  (Basic Memory Operations md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('9DxjCyCq8Le4')
set_source(c, [
    "## 基本记忆操作\n",
    "\n",
    "现在我们已经有了一个 Memory Bank，让我们学习基本的 CRUD（创建、读取、更新、删除）操作。这些是所有记忆管理的基础构建块。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 1GVr94288Ns6  (Manually create a memory md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('1GVr94288Ns6')
set_source(c, [
    "### 手动创建记忆\n",
    "\n",
    "让我们手动创建第一条记忆。当您需要记录对话中未捕获到的信息时，这非常有用。\n",
    "\n",
    "**注意：** 创建方法功能有限，无法享受合并（consolidation）的好处。如果需要合并功能，请使用带 `direct_memories_source` 的 GenerateMemories。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: pp6_0Exu8Qka  (code: create first memory)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('pp6_0Exu8Qka')
set_source(c, [
    "print(\"🆕 手动创建您的第一条记忆\\n\")\n",
    "\n",
    "# 为本教程生成唯一的客户 ID\n",
    "customer_id = \"customer_alex_\" + str(uuid.uuid4())[:4]\n",
    "\n",
    "# 手动创建记忆\n",
    "first_memory = client.agent_engines.memories.create(\n",
    "    name=agent_engine_name,\n",
    "    fact=\"Customer prefers to be contacted via email for all communications\",\n",
    "    scope={\"user_id\": customer_id},\n",
    ")\n",
    "\n",
    "print(\"✅ 记忆创建成功！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: -gvhEdhV9NCQ  (Retrieve memories md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('-gvhEdhV9NCQ')
set_source(c, [
    "### 检索客户的记忆\n",
    "\n",
    "现在让我们检索刚刚创建的记忆。这演示了如何获取与特定客户关联的所有记忆。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: xvuQaFGL85t0  (code: retrieve memories)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('xvuQaFGL85t0')
set_source(c, [
    "print(\"\\n🔍 正在检索该客户的所有记忆\\n\")\n",
    "\n",
    "# 检索此客户的所有记忆\n",
    "results = client.agent_engines.memories.retrieve(\n",
    "    name=agent_engine_name, scope={\"user_id\": customer_id}\n",
    ")\n",
    "\n",
    "all_memories = list(results)\n",
    "\n",
    "print(f\"✅ 找到客户 {customer_id} 的 {len(all_memories)} 条记忆：\\n\")\n",
    "\n",
    "for i, retrieved_memory in enumerate(all_memories, 1):\n",
    "    print(f\"   {i}. {retrieved_memory.memory.fact}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 8n1jiBJj9Z4y  (Update memory md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('8n1jiBJj9Z4y')
set_source(c, [
    "### 更新现有记忆\n",
    "\n",
    "客户偏好会随时间变化。让我们更新记忆以反映新的联系方式偏好。\n",
    "\n",
    "要更新记忆，您可以从更新后的信息中生成新记忆。Memory Bank 会智能识别现有记忆并进行更新，同时自动创建修订历史。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 8QOHNSCX9aH8  (code: update memory)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('8QOHNSCX9aH8')
set_source(c, [
    "print(\"\\n✏️ 正在更新客户的联系方式偏好\\n\")\n",
    "\n",
    "first_memory = all_memories[0]\n",
    "\n",
    "print(f\"📋 当前偏好：'{first_memory.memory.fact}'\")\n",
    "print(\n",
    "    \"\\n💡 客户来电更新：'紧急问题优先使用短信，其他所有事项使用电子邮件'\\n\"\n",
    ")\n",
    "\n",
    "# 通过从新信息中生成来更新记忆\n",
    "# Memory Bank 将识别此次更新关联到现有记忆\n",
    "update_operation = client.agent_engines.memories.generate(\n",
    "    name=agent_engine_name,\n",
    "    scope={\"user_id\": customer_id},\n",
    "    direct_contents_source={\n",
    "        \"events\": [\n",
    "            {\n",
    "                \"content\": {\n",
    "                    \"parts\": [\n",
    "                        {\n",
    "                            \"text\": \"Customer prefers SMS for urgent issues and email for all other communications\"\n",
    "                        }\n",
    "                    ]\n",
    "                }\n",
    "            }\n",
    "        ]\n",
    "    },\n",
    "    config={\"wait_for_completion\": True},\n",
    ")\n",
    "\n",
    "# 获取更新后的记忆详情\n",
    "if update_operation.response and update_operation.response.generated_memories:\n",
    "    updated_memory_ref = update_operation.response.generated_memories[0]\n",
    "    updated_memory = client.agent_engines.memories.get(\n",
    "        name=updated_memory_ref.memory.name\n",
    "    )\n",
    "\n",
    "    print(\"✅ 记忆更新成功！\")\n",
    "    print(f\"   📝 新事实：{updated_memory.fact}\")\n",
    "    print(f\"   🔄 更新时间：{updated_memory.update_time}\")\n",
    "    print(f\"   🔄 操作：{updated_memory_ref.action}\")\n",
    "\n",
    "    if (\n",
    "        hasattr(updated_memory_ref, \"previous_revision\")\n",
    "        and updated_memory_ref.previous_revision\n",
    "    ):\n",
    "        print(\n",
    "            f\"   📜 已保留之前的修订版本：{updated_memory_ref.previous_revision.split('/')[-1]}\"\n",
    "        )"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 7I7b5xzyL6YL  (Create additional memories md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('7I7b5xzyL6YL')
set_source(c, [
    "### 创建更多记忆\n",
    "\n",
    "让我们再创建几条记忆，使示例更加真实。我们将添加不同类型的客户信息。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: pTj2fDp1Pgn_  (code: create additional memories)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('pTj2fDp1Pgn_')
set_source(c, [
    "print(\"\\n📝 正在添加更多客户信息\\n\")\n",
    "\n",
    "# 再创建几条记忆\n",
    "additional_memories = [\n",
    "    \"Customer's account type is Enterprise Pro with priority support\",\n",
    "    \"Customer reported issue with API authentication returning 401 errors\",\n",
    "    \"Customer prefers morning appointments between 9 AM and 11 AM EST\",\n",
    "]\n",
    "\n",
    "created_memories = []\n",
    "\n",
    "for fact in additional_memories:\n",
    "    memory = client.agent_engines.memories.create(\n",
    "        name=agent_engine_name, fact=fact, scope={\"user_id\": customer_id}\n",
    "    )\n",
    "    created_memories.append(memory)\n",
    "    print(f\"   ✅ 已创建：{fact}\")\n",
    "\n",
    "print(f\"\\n✅ 已创建 {len(created_memories)} 条额外记忆\")\n",
    "print(f\"   {customer_id} 的记忆总数：{len(created_memories) + 1}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: V1kQJe97P0tB  (Retrieve and display all memories md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('V1kQJe97P0tB')
set_source(c, [
    "### 检索并显示所有记忆\n",
    "\n",
    "让我们查看目前为该客户存储的所有内容。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: lWcapirHP7Mf  (code: retrieve all memories)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('lWcapirHP7Mf')
set_source(c, [
    "print(\"\\n📚 完整客户档案\\n\")\n",
    "\n",
    "# 检索所有记忆\n",
    "results = client.agent_engines.memories.retrieve(\n",
    "    name=agent_engine_name, scope={\"user_id\": customer_id}\n",
    ")\n",
    "\n",
    "all_customer_memories = list(results)\n",
    "\n",
    "print(f\"✅ 找到 {customer_id} 的 {len(all_customer_memories)} 条记忆：\\n\")\n",
    "\n",
    "for i, mem in enumerate(all_customer_memories, 1):\n",
    "    print(f\"   {i}. {mem.memory.fact}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 2LBQ-LBrQHNS  (Delete a specific memory md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('2LBQ-LBrQHNS')
set_source(c, [
    "### 删除特定记忆\n",
    "\n",
    "让我们演示如何删除特定记忆。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: XCXMO_IPQHf3  (code: delete memory)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('XCXMO_IPQHf3')
set_source(c, [
    "print(\"\\n🗑️ 正在删除特定记忆\\n\")\n",
    "\n",
    "# 删除 API 问题记忆\n",
    "memory_to_delete = all_customer_memories[2]\n",
    "\n",
    "print(\"🔍 待删除的记忆：\")\n",
    "print(f\"   📝 {memory_to_delete.memory.fact}\")\n",
    "print(f\"   🆔 ID：{memory_to_delete.memory.name.split('/')[-1]}\")\n",
    "\n",
    "print(\"\\n⚠️ 正在确认删除...\")\n",
    "\n",
    "# 删除该记忆\n",
    "client.agent_engines.memories.delete(name=memory_to_delete.memory.name)\n",
    "\n",
    "print(\"\\n✅ 记忆删除成功！\")\n",
    "\n",
    "# 验证删除\n",
    "results = client.agent_engines.memories.retrieve(\n",
    "    name=agent_engine_name, scope={\"user_id\": customer_id}\n",
    ")\n",
    "\n",
    "remaining_memories = list(results)\n",
    "\n",
    "print(\n",
    "    f\"\\n📊 剩余记忆数：{len(remaining_memories)}（原为 {len(all_customer_memories)}）\"\n",
    ")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: WZkPhsIISt7J  (Generate memories from conversations md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('WZkPhsIISt7J')
set_source(c, [
    "## 从对话中生成记忆\n",
    "\n",
    "到目前为止，我们一直在手动创建记忆。现在让我们了解 Memory Bank 如何自动从自然对话中提取结构化事实。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: RFpWWwucS0aj  (Create a session md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('RFpWWwucS0aj')
set_source(c, [
    "### 为客户支持创建会话\n",
    "\n",
    "**会话（Session）** 表示客户与支持人员之间的单次对话。让我们创建一个会话并添加真实的支持对话。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: kxu3oJhtSxXj  (code: create session)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('kxu3oJhtSxXj')
set_source(c, [
    "print(\"\\n💬 正在创建客户支持对话\\n\")\n",
    "\n",
    "# 为该客户创建会话\n",
    "session = client.agent_engines.sessions.create(\n",
    "    name=agent_engine_name,\n",
    "    user_id=customer_id,\n",
    "    config={\"display_name\": f\"Support session for {customer_id}\"},\n",
    ")\n",
    "\n",
    "session_name = session.response.name\n",
    "\n",
    "print(\"✅ 会话创建成功！\")\n",
    "print(f\"   会话：{session_name}\")\n",
    "print(f\"   客户 ID：{customer_id}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: XaZQe1l7S6mb  (Add support conversation md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('XaZQe1l7S6mb')
set_source(c, [
    "### 将支持对话添加到会话\n",
    "\n",
    "以下是一段包含重要信息的真实客户支持对话，这些信息应该被记住。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: eIIEZ1dUS4Ao  (code: add conversation)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('eIIEZ1dUS4Ao')
set_source(c, [
    "# 定义真实的客户支持对话\n",
    "support_conversation = [\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"message\": \"Hi, I'm having issues with my billing - I was charged twice for my enterprise subscription last month.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"model\",\n",
    "        \"message\": \"Hello! I apologize for the billing issue. Let me look into your enterprise subscription charges right away.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"message\": \"I'm on the Enterprise Pro plan at $299/month. The duplicate charge was on March 15th. My company is DataTech Solutions.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"model\",\n",
    "        \"message\": \"Thank you for those details. I see your Enterprise Pro subscription. I'll investigate the duplicate charge from March 15th.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"message\": \"Also, I prefer email communication over phone calls. I'm in EST timezone, so please don't call before 9 AM my time.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"model\",\n",
    "        \"message\": \"Noted! I've recorded your preference for email communication and your EST timezone availability after 9 AM.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"message\": \"I also opened ticket #SUP-2024-0847 last week about API authentication failures. Still not resolved.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"model\",\n",
    "        \"message\": \"I see ticket SUP-2024-0847 regarding API authentication. Let me prioritize getting that resolved for you.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"user\",\n",
    "        \"message\": \"The API returns 401 errors when using our production API key. We're using the REST API v2.1 endpoint.\",\n",
    "    },\n",
    "    {\n",
    "        \"role\": \"model\",\n",
    "        \"message\": \"Thank you for the technical details. I'll escalate the API authentication issue with our engineering team and get back to you within 24 hours via email.\",\n",
    "    },\n",
    "]\n",
    "\n",
    "print(\"\\n⬆️ 正在将对话添加到会话...\\n\")\n",
    "\n",
    "invocation_id = 0\n",
    "\n",
    "# 将每个对话轮次加上时间戳添加到会话中\n",
    "for turn in support_conversation:\n",
    "    client.agent_engines.sessions.events.append(\n",
    "        name=session_name,\n",
    "        author=customer_id,\n",
    "        invocation_id=str(invocation_id),\n",
    "        timestamp=datetime.datetime.now(tz=datetime.timezone.utc),\n",
    "        config={\n",
    "            \"content\": {\"role\": turn[\"role\"], \"parts\": [{\"text\": turn[\"message\"]}]}\n",
    "        },\n",
    "    )\n",
    "\n",
    "    invocation_id += 1\n",
    "    # 显示对话，使用视觉指示器\n",
    "    icon = \"👤\" if turn[\"role\"] == \"user\" else \"🤖\"\n",
    "    print(f\"{icon} {turn['message']}\")\n",
    "\n",
    "print(\"\\n✅ 对话已添加到会话！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 0r6rGzx5TZDl  (Generate memories from conversation md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('0r6rGzx5TZDl')
set_source(c, [
    "### 从对话中生成记忆\n",
    "\n",
    "Memory Bank 分析整个对话并自动提取结构化事实。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: f8LRkKsnTU6u  (code: generate memories)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('f8LRkKsnTU6u')
set_source(c, [
    "print(\"\\n🧠 正在从对话中生成记忆\\n\")\n",
    "\n",
    "# 从会话中生成记忆\n",
    "operation = client.agent_engines.memories.generate(\n",
    "    name=agent_engine_name,\n",
    "    vertex_session_source={\"session\": session_name},\n",
    "    config={\"wait_for_completion\": True},\n",
    ")\n",
    "\n",
    "print(\"✅ 记忆生成完成！\")\n",
    "\n",
    "# 显示生成的记忆\n",
    "display_generated_memories(operation, client, \"自动提取的记忆\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: E-sIlPIpTnv6  (View all memories md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('E-sIlPIpTnv6')
set_source(c, [
    "### 查看所有记忆（手动 + 生成）\n",
    "\n",
    "让我们查看完整的客户档案——将手动创建的记忆与自动生成的记忆合并在一起。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: Gz6X9fZVTgZQ  (code: view complete profile)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('Gz6X9fZVTgZQ')
set_source(c, [
    "print(\"\\n📊 完整客户档案（手动 + 自动生成）\\n\")\n",
    "\n",
    "# 检索该客户的所有记忆\n",
    "results = client.agent_engines.memories.retrieve(\n",
    "    name=agent_engine_name, scope={\"user_id\": customer_id}\n",
    ")\n",
    "\n",
    "complete_profile = list(results)\n",
    "\n",
    "print(f\"✅ {customer_id} 的记忆总数：{len(complete_profile)}\\n\")\n",
    "\n",
    "for i, mem in enumerate(complete_profile, 1):\n",
    "    print(f\"   {i}. {mem.memory.fact}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: iCVdOPxGYW0A  (Granular TTL md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('iCVdOPxGYW0A')
set_source(c, [
    "## 细粒度 TTL（Time-To-Live）\n",
    "\n",
    "现在让我们使用**细粒度 TTL** 添加自动数据保留策略。这确保数据在指定的保留期后被自动删除。\n",
    "\n",
    "细粒度 TTL 允许您指定三种不同的保留期：\n",
    "\n",
    "1. **create_ttl**：手动创建的记忆保留时长（30 天）\n",
    "2. **generate_created_ttl**：新生成的记忆保留时长（90 天）\n",
    "3. **generate_updated_ttl**：已更新的记忆保留时长（365 天）\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: UdLmueLic06J  (Define granular TTL md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('UdLmueLic06J')
set_source(c, [
    "### 定义细粒度 TTL 配置\n",
    "\n",
    "让我们为自动数据生命周期管理配置 TTL 策略：\n",
    "\n",
    "**TTL 配置参数**：\n",
    "\n",
    "| 参数 | 时长 | 秒数 | 使用场景 |\n",
    "|-----------|----------|---------|----------|\n",
    "| `create_ttl` | 30 天 | 2592000s | 手动创建的运营数据 |\n",
    "| `generate_created_ttl` | 90 天 | 7776000s | 新提取的支持记忆 |\n",
    "| `generate_updated_ttl` | 365 天 | 31536000s | 已整合、已验证的账户数据 |"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: OhCiMGHAZ74m  (code: TTL config)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('OhCiMGHAZ74m')
set_source(c, [
    "print(\"\\n⏱️ 正在配置细粒度 TTL 以实现自动数据保留\\n\")\n",
    "\n",
    "# 定义具有不同保留期的细粒度 TTL 配置\n",
    "ttl_config = TtlConfig(\n",
    "    granular_ttl_config=GranularTtlConfig(\n",
    "        create_ttl=\"2592000s\",  # 30 天  - 手动创建（临时记录）\n",
    "        generate_created_ttl=\"7776000s\",  # 90 天  - 新生成的记忆\n",
    "        generate_updated_ttl=\"31536000s\",  # 365 天 - 已更新/已整合的记忆\n",
    "    )\n",
    ")\n",
    "\n",
    "print(\"✅ 细粒度 TTL 配置创建成功！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: lF4-sMEjc-sx  (Update Agent Engine with TTL md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('lF4-sMEjc-sx')
set_source(c, [
    "### 使用 TTL 配置更新 Agent Engine\n",
    "\n",
    "现在让我们使用 TTL 治理配置更新现有的 Agent Engine。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 3hBQDkO4c5Rk  (code: update agent engine with TTL)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('3hBQDkO4c5Rk')
set_source(c, [
    "print(\"\\n🔧 正在使用 TTL 治理配置更新 Agent Engine\\n\")\n",
    "\n",
    "# 创建包含 TTL 的增强配置\n",
    "governance_memory_config = MemoryBankConfig(\n",
    "    # 保留现有模型\n",
    "    similarity_search_config=SimilaritySearchConfig(\n",
    "        embedding_model=f\"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/text-embedding-005\"\n",
    "    ),\n",
    "    generation_config=GenerationConfig(\n",
    "        model=f\"projects/{PROJECT_ID}/locations/{LOCATION}/publishers/google/models/gemini-2.5-flash\"\n",
    "    ),\n",
    "    # 添加 TTL 治理\n",
    "    ttl_config=ttl_config,\n",
    ")\n",
    "\n",
    "# 更新现有引擎\n",
    "updated_engine = client.agent_engines.update(\n",
    "    name=agent_engine_name,\n",
    "    config={\"context_spec\": {\"memory_bank_config\": governance_memory_config}},\n",
    ")\n",
    "\n",
    "print(\"✅ Agent Engine 已添加 TTL 配置并更新成功！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: _sTi6f-BdKgN  (Test TTL md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('_sTi6f-BdKgN')
set_source(c, [
    "### 使用新记忆测试 TTL\n",
    "\n",
    "让我们创建一条新记忆，并查看基于 TTL 配置的到期时间。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: QSm0g7undF2h  (code: test TTL)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('QSm0g7undF2h')
set_source(c, [
    "print(\"\\n🧪 正在通过创建新记忆测试 TTL\\n\")\n",
    "\n",
    "# 创建手动记忆（30 天 TTL）\n",
    "test_memory = client.agent_engines.memories.create(\n",
    "    name=agent_engine_name,\n",
    "    fact=\"Customer requested demo of new analytics dashboard feature\",\n",
    "    scope={\"user_id\": customer_id},\n",
    ")\n",
    "\n",
    "print(\"✅ 已创建含 TTL 的记忆！\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: DqWvGt-EfXdB  (Topic-Based Filtering md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('DqWvGt-EfXdB')
set_source(c, [
    "## 使用默认托管主题进行基于主题的过滤\n",
    "\n",
    "组织记忆最强大的功能之一是基于主题的过滤。即使没有自定义主题，Memory Bank 也会使用**默认托管主题**自动对记忆进行分类。\n",
    "\n",
    "**默认托管主题**：\n",
    "\n",
    "| 主题 | 描述 | 示例 |\n",
    "|-------|-------------|---------|\n",
    "| `USER_PERSONAL_INFO` | 用户的个人详情 | \"客户姓名为 Alex Chen，就职于 DataTech Solutions\" |\n",
    "| `USER_PREFERENCES` | 用户的偏好与喜恶 | \"客户偏好电子邮件而非电话沟通\" |\n",
    "| `KEY_CONVERSATION_DETAILS` | 重要结果或里程碑 | \"工单 #SUP-2024-0847 已针对 API 认证问题创建\" |\n",
    "| `EXPLICIT_INSTRUCTIONS` | 明确的记住/遗忘请求 | \"客户要求记住账号\" |"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: wCb0p1j-fcin  (Inspect memories with topic labels md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('wCb0p1j-fcin')
set_source(c, [
    "### 检查带有主题标签的记忆\n",
    "\n",
    "让我们详细检查记忆，查看其自动附加的主题标签。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: jN6vhfWQfX1n  (code: inspect memories)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('jN6vhfWQfX1n')
set_source(c, [
    "print(\"\\n🔍 正在检查带有自动主题标签的记忆\\n\")\n",
    "\n",
    "# 获取所有记忆以进行详细检查\n",
    "pager = client.agent_engines.memories.list(name=agent_engine_name)\n",
    "sample_memories = list(pager)[:5]  # 前 5 条记忆\n",
    "\n",
    "if sample_memories:\n",
    "    print(f\"显示 {len(sample_memories)} 条记忆的完整详情：\\n\")\n",
    "\n",
    "    for i, memory in enumerate(sample_memories, 1):\n",
    "        # 获取完整的记忆详情\n",
    "        full_memory = client.agent_engines.memories.get(name=memory.name)\n",
    "\n",
    "        print(f\"\\n📌 记忆 {i}：\")\n",
    "        print(f\"   事实：{full_memory.fact}\")\n",
    "        print(f\"   范围：{full_memory.scope}\")\n",
    "        print(f\"   创建时间：{full_memory.create_time}\")\n",
    "        print(f\"   到期时间：{full_memory.expire_time}\")\n",
    "\n",
    "        # 显示自动附加的主题\n",
    "        if hasattr(full_memory, \"topics\") and full_memory.topics:\n",
    "            topics = [\n",
    "                topic.managed_memory_topic\n",
    "                if hasattr(topic, \"managed_memory_topic\")\n",
    "                else str(topic)\n",
    "                for topic in full_memory.topics\n",
    "            ]\n",
    "            print(f\"   主题：{', '.join(str(t) for t in topics)}\")\n",
    "        else:\n",
    "            print(\"   主题：无\")\n",
    "else:\n",
    "    print(\"未找到记忆\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: AQb4o4FBglrh  (Filter memories by specific topic md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('AQb4o4FBglrh')
set_source(c, [
    "### 按特定主题过滤记忆\n",
    "\n",
    "现在让我们演示基于主题的过滤。这对于检索特定类别的信息非常有用。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: ah1E1YuqgpRN  (code: get_memories_by_topic function)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('ah1E1YuqgpRN')
set_source(c, [
    "def get_memories_by_topic(engine_name, topic_enum_value):\n",
    "    \"\"\"按指定托管主题检索记忆。\n",
    "\n",
    "    Args:\n",
    "        engine_name: Agent Engine 资源名称\n",
    "        topic_enum_value: 要过滤的主题（例如 'USER_PERSONAL_INFO'）\n",
    "\n",
    "    Returns:\n",
    "        匹配该主题的记忆列表\n",
    "    \"\"\"\n",
    "    # 获取所有记忆\n",
    "    all_memories_pager = client.agent_engines.memories.list(name=engine_name)\n",
    "    filtered_memories = []\n",
    "\n",
    "    # 按主题过滤\n",
    "    for memory in all_memories_pager:\n",
    "        full_memory = client.agent_engines.memories.get(name=memory.name)\n",
    "        topics = (\n",
    "            full_memory.topics\n",
    "            if hasattr(full_memory, \"topics\") and full_memory.topics\n",
    "            else []\n",
    "        )\n",
    "\n",
    "        for topic in topics:\n",
    "            if hasattr(topic, \"managed_memory_topic\"):\n",
    "                topic_value = str(topic.managed_memory_topic)\n",
    "                if topic_enum_value in topic_value:\n",
    "                    filtered_memories.append(full_memory)\n",
    "                    break\n",
    "\n",
    "    return filtered_memories"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: aVtUbFYBgrMP  (Now let's demonstrate filtering md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('aVtUbFYBgrMP')
set_source(c, [
    "现在让我们演示对每个默认托管主题的过滤。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: VnZCu5fafiv2  (code: demonstrate topic filtering)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('VnZCu5fafiv2')
set_source(c, [
    "print(\"\\n📊 演示基于主题的过滤\\n\")\n",
    "\n",
    "# 要过滤的默认托管主题列表\n",
    "topics_to_filter = [\n",
    "    (\"USER_PERSONAL_INFO\", \"个人信息：姓名、公司、账户详情\"),\n",
    "    (\"USER_PREFERENCES\", \"偏好：沟通渠道、支持偏好\"),\n",
    "    (\"KEY_CONVERSATION_DETAILS\", \"关键详情：工单号、重要结果\"),\n",
    "]\n",
    "\n",
    "for topic_label, description in topics_to_filter:\n",
    "    print(f\"\\n🔍 {description}\")\n",
    "    print(f\"   按主题过滤：{topic_label}\\n\")\n",
    "\n",
    "    # 获取该主题的记忆\n",
    "    topic_memories = get_memories_by_topic(agent_engine_name, topic_label)\n",
    "\n",
    "    if topic_memories:\n",
    "        print(f\"   ✅ 找到 {len(topic_memories)} 条记忆：\\n\")\n",
    "        for i, memory in enumerate(topic_memories, 1):\n",
    "            print(f\"      {i}. {memory.fact}\")\n",
    "            if memory.expire_time:\n",
    "                print(f\"         ⏱️ 到期时间：{memory.expire_time}\")\n",
    "    else:\n",
    "        print(f\"   📭 未找到主题为 '{topic_label}' 的记忆\")\n",
    "\n",
    "    print()"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: h6Fg-1O2hAlv  (Memory Revisions md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('h6Fg-1O2hAlv')
set_source(c, [
    "## 记忆修订版本：完整审计追踪\n",
    "\n",
    "Memory Bank 的**修订历史**提供了数据随时间演变的完整不可变记录。这对于合规、调试以及理解数据变更至关重要。\n",
    "\n",
    "每次创建、更新或删除记忆时，Memory Bank 都会创建一个**修订快照**。可以将其视为客户数据的版本控制。\n",
    "\n",
    "**修订操作**：\n",
    "- **CREATED**：记忆首次生成\n",
    "- **UPDATED**：记忆被修改（例如通过整合或手动更新）\n",
    "- **DELETED**：记忆被删除（手动删除或通过 TTL 到期）"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: n-jDy1QShN1W  (List revision history md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('n-jDy1QShN1W')
set_source(c, [
    "### 列出记忆的修订历史\n",
    "\n",
    "让我们选取其中一条记忆，检查其完整的修订历史。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: ct5gQEeWhTYO  (code: list revisions)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('ct5gQEeWhTYO')
set_source(c, [
    "print(\"\\n📋 查看完整修订历史\\n\")\n",
    "\n",
    "# 获取带有修订历史的记忆\n",
    "all_memories_pager = client.agent_engines.memories.list(name=agent_engine_name)\n",
    "memory_with_revisions = None\n",
    "\n",
    "# 查找第一条记忆用于演示\n",
    "for memory in all_memories_pager:\n",
    "    full_memory = client.agent_engines.memories.get(name=memory.name)\n",
    "    memory_with_revisions = full_memory\n",
    "    break\n",
    "\n",
    "if memory_with_revisions:\n",
    "    print(f\"📌 已选择的记忆：{memory_with_revisions.fact}\\n\")\n",
    "    print(\"📜 修订历史：\")\n",
    "\n",
    "    try:\n",
    "        # 列出此记忆的所有修订版本\n",
    "        revisions_pager = client.agent_engines.memories.revisions.list(\n",
    "            name=memory_with_revisions.name\n",
    "        )\n",
    "\n",
    "        revisions = list(revisions_pager)\n",
    "\n",
    "        if revisions:\n",
    "            for i, revision in enumerate(revisions, 1):\n",
    "                print(f\"\\n📜 修订版本 {i}：\")\n",
    "                print(f\"   🆔 修订 ID：{revision.name.split('/')[-1]}\")\n",
    "                print(f\"   ⏱️ 时间戳：{revision.create_time}\")\n",
    "                print(f\"   📝 事实：{revision.fact}\")\n",
    "                if hasattr(revision, \"expire_time\") and revision.expire_time:\n",
    "                    print(f\"   🔚 到期时间：{revision.expire_time}\")\n",
    "        else:\n",
    "            print(\"\\n   📭 暂无修订历史\")\n",
    "            print(\"   💡 记忆每次更新或整合时都会累积修订版本\")\n",
    "\n",
    "    except Exception as e:\n",
    "        print(f\"\\n   ⚠️ 注意：{e}\")\n",
    "else:\n",
    "    print(\"📭 没有可供检查修订版本的记忆\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: EzZrECEHhhuF  (Retrieve a specific revision md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('EzZrECEHhhuF')
set_source(c, [
    "### 检索特定修订版本（时间旅行查询）\n",
    "\n",
    "最强大的合规功能之一：检索记忆在某一特定时间点的精确状态。试想一下，某个数据访问请求询问"您在 3 月 20 日存有我的哪些数据?"——通过修订版本，您可以精确回答这个问题。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: BnHTL3iehbF4  (code: time-travel query)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('BnHTL3iehbF4')
set_source(c, [
    "print(\"\\n⏰ 时间旅行查询：检索特定修订版本\\n\")\n",
    "\n",
    "if memory_with_revisions and revisions:\n",
    "    try:\n",
    "        if revisions:\n",
    "            # 获取第一个修订版本（最早版本）\n",
    "            target_revision = revisions[0]\n",
    "            revision_id = target_revision.name.split(\"/\")[-1]\n",
    "\n",
    "            print(f\"🎯 正在检索修订版本：{revision_id}\")\n",
    "            print(f\"   ⏱️ 时间戳：{target_revision.create_time}\\n\")\n",
    "\n",
    "            # 获取特定修订版本\n",
    "            specific_revision = client.agent_engines.memories.revisions.get(\n",
    "                name=target_revision.name\n",
    "            )\n",
    "\n",
    "            print(\"📋 修订版本详情：\")\n",
    "            print(f\"   📝 记忆事实：{specific_revision.fact}\")\n",
    "            print(f\"   🛠️ 创建时间：{specific_revision.create_time}\")\n",
    "            if (\n",
    "                hasattr(specific_revision, \"expire_time\")\n",
    "                and specific_revision.expire_time\n",
    "            ):\n",
    "                print(f\"   🔚 到期时间：{specific_revision.expire_time}\")\n",
    "        else:\n",
    "            print(\"📭 无可用修订版本进行时间旅行查询\")\n",
    "\n",
    "    except Exception as e:\n",
    "        print(f\"⚠️ 无法检索修订版本：{e}\")\n",
    "else:\n",
    "    print(\"📭 没有可用于时间旅行演示的记忆\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 0KSjGjCrlQZ3  (Rollback md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('0KSjGjCrlQZ3')
set_source(c, [
    "### 将记忆回滚到之前的修订版本\n",
    "\n",
    "既然我们已经了解了如何查看和比较修订版本，让我们来探索最强大的治理功能之一：将记忆**回滚**到之前状态的能力。\n",
    "\n",
    "**何时使用回滚**：\n",
    "- 记忆在整合过程中被错误更新\n",
    "- 需要回退到已知良好状态以满足合规要求\n",
    "- 需要快速纠正错误的事实\n",
    "\n",
    "让我们用一条新记忆来演示这一功能。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: -IQN39KSm314  (Create initial memory with revision labels md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('-IQN39KSm314')
set_source(c, [
    "#### 使用修订标签创建初始记忆\n",
    "\n",
    "我们将创建一条记忆并为其添加修订标签，以追踪其来源和验证状态。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: OZx6OT-HlYrg  (code: create initial memory for rollback)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('OZx6OT-HlYrg')
set_source(c, [
    "print(\"\\n🎯 创建带修订追踪的初始记忆\\n\")\n",
    "\n",
    "# 创建带有修订标签的新客户记忆以进行追踪\n",
    "rollback_customer_id = \"customer_sarah_\" + str(uuid.uuid4())[:4]\n",
    "\n",
    "initial_operation = client.agent_engines.memories.generate(\n",
    "    name=agent_engine_name,\n",
    "    scope={\"user_id\": rollback_customer_id},\n",
    "    direct_contents_source={\n",
    "        \"events\": [\n",
    "            {\n",
    "                \"content\": {\n",
    "                    \"parts\": [\n",
    "                        {\n",
    "                            \"text\": \"Customer prefers email communication only, no phone calls\"\n",
    "                        }\n",
    "                    ]\n",
    "                }\n",
    "            }\n",
    "        ]\n",
    "    },\n",
    "    config={\n",
    "        \"wait_for_completion\": True,\n",
    "        \"revision_labels\": {\"data_source\": \"initial_preference\", \"verified\": \"true\"},\n",
    "    },\n",
    ")\n",
    "\n",
    "if initial_operation.response and initial_operation.response.generated_memories:\n",
    "    rollback_memory = initial_operation.response.generated_memories[0].memory\n",
    "    rollback_memory_name = rollback_memory.name\n",
    "\n",
    "    # 获取完整的记忆详情\n",
    "    full_memory = client.agent_engines.memories.get(name=rollback_memory_name)\n",
    "\n",
    "    print(\"✅ 初始记忆已创建！\")\n",
    "    print(f\"   📝 事实：{full_memory.fact}\")\n",
    "    print(f\"   🆔 记忆 ID：{rollback_memory_name.split('/')[-1]}\")\n",
    "else:\n",
    "    print(\"⚠️ 初始记忆创建失败\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: SpEPUPT5nK7N  (Simulate incorrect update md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('SpEPUPT5nK7N')
set_source(c, [
    "#### 模拟错误更新\n",
    "\n",
    "让我们用错误信息更新记忆（模拟整合过程中的误判）。注意 `verified: \"false\"` 标签。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: P88MwBf_lld3  (code: simulate incorrect update)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('P88MwBf_lld3')
set_source(c, [
    "print(\"\\n🎯 更新记忆（模拟错误更新）\\n\")\n",
    "\n",
    "# 模拟错误更新——客户偏好被误解\n",
    "update_operation = client.agent_engines.memories.generate(\n",
    "    name=agent_engine_name,\n",
    "    scope={\"user_id\": rollback_customer_id},\n",
    "    direct_contents_source={\n",
    "        \"events\": [\n",
    "            {\n",
    "                \"content\": {\n",
    "                    \"parts\": [\n",
    "                        {\"text\": \"Customer prefers phone calls for all communications\"}\n",
    "                    ]\n",
    "                }\n",
    "            }\n",
    "        ]\n",
    "    },\n",
    "    config={\n",
    "        \"wait_for_completion\": True,\n",
    "        \"revision_labels\": {\n",
    "            \"data_source\": \"updated_preference\",\n",
    "            \"verified\": \"false\",  # 此更新未经验证！\n",
    "        },\n",
    "    },\n",
    ")\n",
    "\n",
    "if update_operation.response and update_operation.response.generated_memories:\n",
    "    updated_ref = update_operation.response.generated_memories[0]\n",
    "\n",
    "    # 获取更新后的记忆\n",
    "    updated_memory = client.agent_engines.memories.get(name=updated_ref.memory.name)\n",
    "\n",
    "    print(\"✅ 记忆已更新（错误更新）！\")\n",
    "    print(f\"   📝 新事实：{updated_memory.fact}\")\n",
    "    print(f\"   🔄 操作：{updated_ref.action}\")\n",
    "\n",
    "    # 保存之前的修订版本用于回滚\n",
    "    if hasattr(updated_ref, \"previous_revision\") and updated_ref.previous_revision:\n",
    "        previous_revision_name = updated_ref.previous_revision\n",
    "        previous_revision_id = previous_revision_name.split(\"/\")[-1]\n",
    "        print(f\"   📜 之前的修订版本 ID：{previous_revision_id}\")\n",
    "else:\n",
    "    print(\"⚠️ 记忆更新失败\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 4DMqbrexnTPp  (View revision history before rollback md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('4DMqbrexnTPp')
set_source(c, [
    "#### 查看回滚前的修订历史\n",
    "\n",
    "让我们检查两个修订版本，在历史记录中查看错误的更新。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 99Rid5rbmP3Y  (code: view revision history before rollback)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('99Rid5rbmP3Y')
set_source(c, [
    "print(\"\\n📜 查看回滚前的修订历史\\n\")\n",
    "\n",
    "# 列出所有修订版本以查看历史\n",
    "revisions_before = list(\n",
    "    client.agent_engines.memories.revisions.list(name=rollback_memory_name)\n",
    ")\n",
    "\n",
    "print(f\"✅ 找到 {len(revisions_before)} 个修订版本：\\n\")\n",
    "\n",
    "for i, rev in enumerate(revisions_before, 1):\n",
    "    revision_id = rev.name.split(\"/\")[-1]\n",
    "    labels = rev.labels if hasattr(rev, \"labels\") and rev.labels else {}\n",
    "\n",
    "    print(f\"📌 修订版本 {i}：\")\n",
    "    print(f\"   🆔 ID：{revision_id}\")\n",
    "    print(f\"   📝 事实：{rev.fact}\")\n",
    "    print(f\"   ⏱️ 创建时间：{rev.create_time}\")\n",
    "    print(f\"   🏷️ 标签：{labels}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: Ixzu0s5toGS_  (Perform the rollback md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('Ixzu0s5toGS_')
set_source(c, [
    "#### 执行回滚\n",
    "\n",
    "现在我们将使用 `rollback()` 方法将记忆回滚到之前（正确的）修订版本。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: 6_FU1mG7oG0u  (code: perform rollback)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('6_FU1mG7oG0u')
set_source(c, [
    "print(\"\\n回滚到之前（正确的）修订版本\\n\")\n",
    "\n",
    "# 使用之前保存的修订版本 ID 进行回滚\n",
    "rollback_operation = client.agent_engines.memories.rollback(\n",
    "    name=rollback_memory_name, target_revision_id=previous_revision_id\n",
    ")\n",
    "\n",
    "print(\"✅ 回滚操作已完成！\")\n",
    "print(f\"   🎯 目标修订版本：{previous_revision_id}\")\n",
    "\n",
    "# 通过获取当前记忆状态来验证回滚\n",
    "restored_memory = client.agent_engines.memories.get(name=rollback_memory_name)\n",
    "\n",
    "print(\"\\n📋 回滚后的记忆：\")\n",
    "print(f\"   📝 当前事实：{restored_memory.fact}\")\n",
    "print(f\"   ⏱️ 最后更新：{restored_memory.update_time}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: IOKq7YP8h2tV  (Compare revision history after rollback md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('IOKq7YP8h2tV')
set_source(c, [
    "#### 比较回滚后的修订历史\n",
    "\n",
    "注意回滚如何删除较新（错误的）修订版本，从而维护数据完整性。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: IgZXjmYYhsYt  (code: compare revision history after rollback)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('IgZXjmYYhsYt')
set_source(c, [
    "print(\"\\n📊 比较回滚后的修订历史\\n\")\n",
    "\n",
    "# 列出回滚后的修订版本\n",
    "revisions_after = list(\n",
    "    client.agent_engines.memories.revisions.list(name=rollback_memory_name)\n",
    ")\n",
    "\n",
    "print(f\"✅ 回滚后的修订版本数：{len(revisions_after)}\\n\")\n",
    "\n",
    "for i, rev in enumerate(revisions_after, 1):\n",
    "    revision_id = rev.name.split(\"/\")[-1]\n",
    "    labels = rev.labels if hasattr(rev, \"labels\") and rev.labels else {}\n",
    "\n",
    "    print(f\"📌 修订版本 {i}（回滚后）：\")\n",
    "    print(f\"   🆔 ID：{revision_id}\")\n",
    "    print(f\"   📝 事实：{rev.fact}\")\n",
    "    print(f\"   🏷️ 标签：{labels}\")\n",
    "\n",
    "    # 若为已验证的原始版本则高亮显示\n",
    "    if labels.get(\"verified\") == \"true\":\n",
    "        print(\"   ✅ 这是已验证的原始修订版本\")\n",
    "    print()"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: -hGvdGDFok4h  (Filtering Revisions by Labels md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('-hGvdGDFok4h')
set_source(c, [
    "### 按标签过滤修订版本\n",
    "\n",
    "修订标签允许您追踪记忆创建或更新的时间和方式的元数据。您可以按这些标签过滤修订版本，以实现高级治理工作流。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: McuwANaKo1tw  (Filter revisions using label queries md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('McuwANaKo1tw')
set_source(c, [
    "#### 使用标签查询过滤修订版本\n",
    "\n",
    "让我们演示两种常见的过滤场景：查找已验证的修订版本和按数据来源过滤。\n"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: x2tVcf1fozjq  (code: filter verified revisions)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('x2tVcf1fozjq')
set_source(c, [
    "print(\"\\n🔍 按标签过滤修订版本\\n\")\n",
    "\n",
    "# 示例 1：仅获取已验证的修订版本\n",
    "print(\"示例 1：仅过滤已验证的修订版本\\n\")\n",
    "\n",
    "try:\n",
    "    verified_revisions = list(\n",
    "        client.agent_engines.memories.revisions.list(\n",
    "            name=rollback_memory_name, config={\"filter\": 'labels.verified=\"true\"'}\n",
    "        )\n",
    "    )\n",
    "\n",
    "    print(f\"✅ 找到 {len(verified_revisions)} 个已验证的修订版本：\\n\")\n",
    "\n",
    "    for rev in verified_revisions:\n",
    "        print(f\"   📝 {rev.fact}\")\n",
    "        print(f\"   ⏱️ 创建时间：{rev.create_time}\")\n",
    "        print(f\"   🏷️ 标签：{rev.labels}\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(f\"⚠️ 过滤操作：{e}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: GttiyPalo_Ip  (code: filter by data source)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('GttiyPalo_Ip')
set_source(c, [
    "# 示例 2：获取特定数据来源的修订版本\n",
    "print(\"\\n示例 2：按数据来源过滤\\n\")\n",
    "\n",
    "try:\n",
    "    source_revisions = list(\n",
    "        client.agent_engines.memories.revisions.list(\n",
    "            name=rollback_memory_name,\n",
    "            config={\"filter\": 'labels.data_source=\"initial_preference\"'},\n",
    "        )\n",
    "    )\n",
    "\n",
    "    print(\n",
    "        f\"✅ 找到来自 'initial_preference' 来源的 {len(source_revisions)} 个修订版本：\\n\"\n",
    "    )\n",
    "\n",
    "    for rev in source_revisions:\n",
    "        print(f\"   📝 {rev.fact}\")\n",
    "\n",
    "except Exception as e:\n",
    "    print(f\"⚠️ 过滤操作：{e}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: BjY4p9vCitMN  (Cleaning up md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('BjY4p9vCitMN')
set_source(c, [
    "## 清理资源\n",
    "\n",
    "为避免产生不必要的费用，最佳实践是删除不再需要的资源。"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: kdHamkNxh77Q  (code: cleanup)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('kdHamkNxh77Q')
set_source(c, [
    "print(\"\\n🧹 正在清理资源...\\n\")\n",
    "\n",
    "delete_agent_engine = True\n",
    "\n",
    "if delete_agent_engine:\n",
    "    print(\"⏳ 正在删除 Agent Engine（这将删除所有记忆和会话）...\\n\")\n",
    "\n",
    "    # 删除 agent engine\n",
    "    # force=True 参数确保所有包含的资源也被删除\n",
    "    client.agent_engines.delete(name=agent_engine_name, force=True)\n",
    "\n",
    "    print(\"✅ Agent Engine 删除成功！\")\n",
    "else:\n",
    "    print(\"⚠️ 跳过清理——Agent Engine 及所有数据已保留\")\n",
    "    print(f\"   📋 资源名称：{agent_engine_name}\")"
])

# ─────────────────────────────────────────────────────────────────────────────
# CELL: -47e4jPoi7n-  (Congratulations md)
# ─────────────────────────────────────────────────────────────────────────────
c = find_cell('-47e4jPoi7n-')
set_source(c, [
    "## 恭喜！\n",
    "\n",
    "您已完成"Memory Bank 入门 - 治理"教程！\n",
    "\n",
    "现在您已更好地理解如何管理记忆、配置细粒度 TTL（Time-To-Live）、按主题过滤记忆以及追踪记忆修订版本。\n",
    "\n",
    "**下一步？**\n",
    "- 在我们的进阶教程中探索 Memory Bank 的高级功能\n",
    "- 查阅 [Memory Bank 文档](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/memory-bank)\n",
    "- 加入 [Google Cloud AI 社区](https://discuss.google.dev/c/google-cloud/14) 分享您的项目"
])

# ─────────────────────────────────────────────────────────────────────────────
# Write back
# ─────────────────────────────────────────────────────────────────────────────
with open(FILEPATH, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=1)

print("Translation complete.")
