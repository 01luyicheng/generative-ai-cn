# 如何贡献

我们非常欢迎您向本项目提交补丁和贡献。只需遵循以下几条简单的指引。

## 贡献者许可协议（CLA）

向本项目提交贡献时，必须附带一份贡献者许可协议（Contributor License Agreement，CLA）。您（或您的雇主）保留对贡献内容的版权；此协议仅授权我们使用并重新分发您的贡献作为项目的一部分。请访问 <https://cla.developers.google.com/> 查看您已签署的协议或签署新协议。

通常情况下，您只需提交一次 CLA。如果您已经为其他项目提交过，则无需再次提交。

## 笔记本模板

如果您正在创建 Jupyter 笔记本，请使用 [`notebook_template.ipynb`](notebook_template.ipynb) 作为模板。

## 代码质量检查

本项目中的所有笔记本都会进行格式和风格检查，以确保一致的使用体验。在提交 Pull Request 之前，您可以按照以下步骤测试您的笔记本。

在命令行终端（例如 Vertex AI Workbench 或本地终端）中运行以下代码块来格式化您的代码。
如果无法自动修复，则需要在提交 PR 前手动解决这些问题。

```shell
python3 -m pip install --upgrade nox
nox -s format
```

## 代码审查

所有提交（包括项目成员的提交）都需要经过审查。我们使用 GitHub Pull Request 来完成此过程。请参阅 [GitHub 帮助文档](https://help.github.com/articles/about-pull-requests/) 了解更多关于 Pull Request 的信息。

## 社区准则

本项目遵循 [Google 开源社区准则](https://opensource.google/conduct/)。

## 贡献者指南

如果您是开源贡献的新手，可以在本指南中找到有用的信息。

您可以按照以下步骤进行贡献：

1. **Fork 官方仓库。** 这将在您的账户下创建官方仓库的副本。
2. **同步分支。** 这将确保您的仓库副本与官方仓库的最新更改保持同步。
3. **在您 Fork 的仓库的功能分支上进行开发。** 这是您修改代码的地方。
4. **在您 Fork 的仓库功能分支上提交更新。** 这将把您的更改保存到您的仓库副本中。
5. **向官方仓库的 main 分支提交 Pull Request。** 这将请求将您的更改合并到官方仓库中。
6. **解决所有代码检查（linting）错误。** 这将确保您的更改格式正确。
   - 对于 [check-spelling](https://github.com/check-spelling/check-spelling) 生成的错误，请前往 [Job Summary](https://github.com/GoogleCloudPlatform/generative-ai/actions/workflows/spelling.yaml) 查看错误详情。
     - 修正发现的任何拼写错误。
     - 禁用的模式以正则表达式定义，您可以将其复制粘贴到大多数 IDE 中以查找对应位置。[Visual Studio Code 示例](https://medium.com/@nikhilbaxi3/visual-studio-code-secrets-of-regular-expression-search-71723c2ecbd2)。
     - 将误报添加到 [`.github/actions/spelling/allow.txt`](.github/actions/spelling/allow.txt)。请务必确认拼写确实正确！

在整个过程中还需注意以下几点：

- **阅读 [Google 开源社区准则](https://opensource.google/conduct/)。** 贡献指南将为您提供更多关于项目及如何贡献的信息。
- **测试您的更改。** 在提交 Pull Request 之前，请确保您的更改按预期工作。
- **保持耐心。** 您的 Pull Request 可能需要一些时间来完成审查和合并。

---

## 致 Google 员工

请完成以下步骤以注册您的 GitHub 账户并被添加为本仓库的贡献者。

1. 在 [go/GitHub](http://go/github) 注册您的 GitHub 账户。

1. 注册完成后，前往 [go/github-googlecloudplatform](http://go/github-googlecloudplatform) 申请加入 GoogleCloudPlatform 组织。勾选"I need write access on a public repository"选项。

1. 您将收到一封发送至您 GitHub 注册邮箱的邮件，要求您批准加入请求。请批准该请求。

1. 申请加入该团队：[GoogleCloudPlatform/teams/generative-ai-samples-contributors](https://github.com/orgs/GoogleCloudPlatform/teams/generative-ai-samples-contributors/members)
