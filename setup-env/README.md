# 在 Google Cloud 上使用生成式 AI 的环境配置说明

> **📌 提示：** 以下配置步骤需要访问 Google Cloud 控制台及相关服务，请确保您具备相应的网络访问环境。

本目录包含以下内容的配置说明：

- 配置您的 Google Cloud 项目
- 笔记本环境
  - 配置 Colab
  - 配置 Vertex AI Workbench
- Vertex AI Python SDK

## 配置您的 Google Cloud 项目

1. [选择或创建一个 Google Cloud 项目](https://console.cloud.google.com/cloud-resource-manager)。
   首次创建账号时，您将获得 300 美元的免费积分用于计算/存储费用。

2. [确保为您的项目启用了结算功能](https://cloud.google.com/billing/docs/how-to/modify-project)。

3. [启用 Vertex AI API 和 Google Cloud Storage API](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com,storage.googleapis.com)。

## 笔记本环境

### Colab

[Google Colab](https://colab.research.google.com/) 允许您在浏览器中以最少的配置编写和执行 Python 代码。

要将 Colab 与本仓库配合使用，请点击本仓库中任意笔记本文件顶部的"在 Colab 中打开"链接，在 Colab 中启动该笔记本，然后按照其中的说明操作。

在 Colab 中，您需要进行身份验证才能从 Colab 使用 Google Cloud：

```py
from google.colab import auth
auth.authenticate_user()
```

使用 vertexai Python SDK 时，还需要使用您的 Google Cloud `project_id` 和 `location` 对其进行初始化：

```py
PROJECT_ID = "your-project-id"
LOCATION = "" #e.g. us-central1

import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)
```

### Vertex AI Workbench

[Vertex AI Workbench](https://cloud.google.com/vertex-ai-workbench) 是 Google Cloud 上的 JupyterLab 笔记本环境，可帮助您创建和自定义笔记本实例。使用时无需额外的身份验证步骤。

#### 在 Vertex AI Workbench 上创建笔记本实例

要在 Vertex AI Workbench 上创建新的 JupyterLab 实例，请参照[此处的说明创建用户管理的笔记本实例](https://cloud.google.com/vertex-ai/docs/workbench/user-managed/create-new)。

#### 在 Vertex AI Workbench 上使用本仓库

启动笔记本实例后，您可以在 JupyterLab 环境中克隆本仓库。请在 JupyterLab 中打开一个终端（Terminal），然后运行以下命令将仓库克隆到您的实例中：

```sh
git clone https://github.com/GoogleCloudPlatform/generative-ai.git
```

#### 本地开发

- 安装 [Google Cloud SDK](https://cloud.google.com/sdk)。

- 获取身份验证凭据。通过运行以下命令并按照 oauth2 流程操作来创建本地凭据（了解更多关于该命令的信息，请参阅[此处](https://cloud.google.com/sdk/gcloud/reference/beta/auth/application-default/login)）：

  ```bash
  gcloud auth application-default login
  ```

## Python 库

安装最新版 Python SDK：

```sh
%pip install google-cloud-aiplatform --upgrade
```

您需要使用您的 `project_id` 和 `location` 初始化 `vertexai`：

```py
PROJECT_ID = "your-project-id"
LOCATION = "" #e.g. us-central1

import vertexai
vertexai.init(project=PROJECT_ID, location=LOCATION)
```
