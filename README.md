# Google Cloud 生成式 AI

> **[Gemini 3.1 Pro](https://cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-1-pro) 已正式发布！**
>
> 以下是使用该新模型的最新笔记本和演示：
>
> - [Gemini 3.1 Pro 入门介绍](gemini/getting-started/intro_gemini_3_1_pro.ipynb)
>
<!-- markdownlint-disable MD033 -->

> **📌 提示：** 本仓库中的示例需要访问 Google Cloud 服务（Vertex AI 等），请确保您具备相应的网络访问环境。

本仓库包含笔记本（Notebook）、代码示例、示例应用及其他资源，演示如何使用 [Google Cloud 生成式 AI](https://cloud.google.com/ai/generative-ai) 和 [Vertex AI](https://cloud.google.com/vertex-ai) 来使用、开发和管理生成式 AI 工作流程。

## 如何使用本仓库

[![Applied AI Summit：生成式 AI 的云端工具包](https://img.youtube.com/vi/xT7WW2SKLfE/hqdefault.jpg)](https://www.youtube.com/watch?v=xT7WW2SKLfE)

<table>
  <tr>
    <th></th>
    <th style="text-align: center;">说明</th>
  </tr>
  <tr>
    <td>
      <img src="https://storage.googleapis.com/github-repo/img/gemini/Spark__Gradient_Alpha_100px.gif" width="45px" alt="Gemini">
      <br>
      <a href="gemini/"><code>gemini/</code></a>
    </td>
    <td>
      通过入门笔记本、应用场景、函数调用（Function Calling）、示例应用等探索 Gemini 的能力。
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://www.gstatic.com/images/branding/gcpiconscolors/service_discovery/v1/24px.svg" width="40px" alt="Search">
      <br>
      <a href="search/"><code>search/</code></a>
    </td>
    <td>如果您希望使用 <a href="https://cloud.google.com/enterprise-search">Vertex AI Search</a>（一种由 Google 托管的解决方案，可帮助您快速构建面向网站和企业数据的搜索引擎，前身为"生成式 AI 应用构建器上的企业搜索"），请使用此目录。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/nature_people/default/40px.svg" alt="RAG Grounding">
      <br>
      <a href="rag-grounding/"><code>rag-grounding/</code></a>
    </td>
    <td>此目录提供检索增强生成（RAG，Retrieval Augmented Generation）和基于 Vertex AI 的接地（Grounding）相关信息，是其他目录中该主题相关笔记本和示例的索引。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/image/default/40px.svg" alt="Vision">
      <br>
      <a href="vision/"><code>vision/</code></a>
    </td>
    <td>
      如果您希望使用 Vertex AI 上的 Imagen（Vertex AI Imagen API）从头构建自己的解决方案，请使用此目录。
      Vertex AI 上的 Imagen 提供以下功能：
      <ul>
        <li>图像生成</li>
        <li>图像编辑</li>
        <li>视觉描述（Visual Captioning）</li>
        <li>视觉问答（Visual Question Answering）</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/mic/default/40px.svg" alt="Speech">
      <br>
      <a href="audio/"><code>audio/</code></a>
    </td>
    <td>
      如果您希望使用 Vertex AI 上的 Chirp（Google 通用语音模型 USM 的一个版本，即 Vertex AI Chirp API）从头构建自己的解决方案，请使用此目录。
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/build/default/40px.svg" alt="Setup Env">
      <br>
      <a href="setup-env/"><code>setup-env/</code></a>
    </td>
    <td>关于如何配置 Google Cloud、Vertex AI Python SDK，以及在 Google Colab 和 Vertex AI Workbench 上设置笔记本环境的说明。</td>
  </tr>
  <tr>
    <td>
      <img src="https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/media_link/default/40px.svg" alt="Resources">
      <br>
      <a href="RESOURCES.md"><code>RESOURCES.md</code></a>
    </td>
    <td>关于 Google Cloud 生成式 AI 的学习资源（例如博客、YouTube 播放列表）。</td>
  </tr>
</table>
<!-- markdownlint-enable MD033 -->

## 相关仓库

- ✨ [Agent Development Kit (ADK) 示例](https://github.com/google/adk-samples)：该仓库提供基于 Agent Development Kit 构建的即用型智能体，旨在加速您的开发过程，涵盖从简单对话机器人到复杂多智能体工作流的各类常见场景。
- [🚀 Agent Starter Pack](https://github.com/GoogleCloudPlatform/agent-starter-pack)
  - 一套专为 Google Cloud 构建的生产就绪型生成式 AI 智能体模板集合。
  - 通过提供全面的生产就绪解决方案，解决构建和部署生成式 AI 智能体时的常见挑战（部署与运维、评估、定制化、可观测性），从而加速开发。
- [Gemini Cookbook](https://github.com/google-gemini/cookbook/)
- [Google Cloud 应用 AI 工程](https://github.com/GoogleCloudPlatform/applied-ai-engineering-samples)
- [Vertex AI GenMedia 创意工作室](https://github.com/GoogleCloudPlatform/vertex-ai-creative-studio) - 体验 Google 的生成式媒体基础模型与自定义工作流。
- [GenMedia 的 MCP 服务器](https://goo.gle/vertex-genmedia-mcp) - 为您的智能体赋能生成式媒体工具。
- [用于营销的生成式 AI（基于 Google Cloud）](https://github.com/GoogleCloudPlatform/genai-for-marketing)
- [用于提升开发者生产力的生成式 AI](https://github.com/GoogleCloudPlatform/genai-for-developers)
- Vertex AI 核心
  - [Vertex AI 示例](https://github.com/GoogleCloudPlatform/vertex-ai-samples)
  - [Vertex AI MLOps](https://github.com/GoogleCloudPlatform/mlops-with-vertex-ai)
  - [使用 T5X 和 Vertex AI 开发 NLP 解决方案](https://github.com/GoogleCloudPlatform/t5x-on-vertex-ai)
  - [使用 Vertex AI Pipelines 进行 AlphaFold 批量推理](https://github.com/GoogleCloudPlatform/vertex-ai-alphafold-inference-pipeline)
  - [使用 Vertex AI 服务 Spark ML 模型](https://github.com/GoogleCloudPlatform/vertex-ai-spark-ml-serving)
  - [Vertex AI 生成模型（PaLM2）的敏感数据保护（Cloud DLP）](https://github.com/GoogleCloudPlatform/Sensitive-Data-Protection-for-Vertex-AI-PaLM2)
- 对话式 AI
  - [联系中心 AI 示例](https://github.com/GoogleCloudPlatform/contact-center-ai-samples)
  - [重塑客户体验 360](https://github.com/GoogleCloudPlatform/dialogflow-ccai-omnichannel)
- Document AI（文档智能）
  - [Document AI 示例](https://github.com/GoogleCloudPlatform/document-ai-samples)
- Google Cloud 中的 Gemini
  - [Cymbal Superstore](https://github.com/GoogleCloudPlatform/cymbal-superstore)
- 云数据库
  - [Gen AI 数据库检索应用](https://github.com/GoogleCloudPlatform/genai-databases-retrieval-app)
- 其他
  - [ai-on-gke](https://github.com/GoogleCloudPlatform/ai-on-gke)
  - [ai-infra-cluster-provisioning](https://github.com/GoogleCloudPlatform/ai-infra-cluster-provisioning)
  - [solutions-genai-llm-workshop](https://github.com/GoogleCloudPlatform/solutions-genai-llm-workshop)
  - [terraform-genai-doc-summarization](https://github.com/GoogleCloudPlatform/terraform-genai-doc-summarization)
  - [terraform-genai-knowledge-base](https://github.com/GoogleCloudPlatform/terraform-genai-knowledge-base)
  - [genai-product-catalog](https://github.com/GoogleCloudPlatform/genai-product-catalog)
  - [solutionbuilder-terraform-genai-doc-summarization](https://github.com/GoogleCloudPlatform/solutionbuilder-terraform-genai-doc-summarization)
  - [solutions-viai-edge-provisioning-configuration](https://github.com/GoogleCloudPlatform/solutions-viai-edge-provisioning-configuration)
  - [mis-ai-accelerator](https://github.com/GoogleCloudPlatform/mis-ai-accelerator)
  - [dataflow-opinion-analysis](https://github.com/GoogleCloudPlatform/dataflow-opinion-analysis)
  - [genai-beyond-basics](https://github.com/meteatamel/genai-beyond-basics)
  - [Gemini by Example](https://geminibyexample.com)

## 贡献

欢迎贡献！请参阅[贡献指南](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/CONTRIBUTING.md)。

## 获取帮助

请使用 [Issues 页面](https://github.com/GoogleCloudPlatform/generative-ai/issues)提交建议、反馈或报告问题。

## 免责声明

本仓库本身并非 Google 官方支持的产品。仓库中的代码仅用于演示目的。
