# 从微信聊天导出到 Cherry Studio Mobile 聊天助手

这是一份个人实践记录和可复用的提示词模板：把**自己有权使用的聊天记录**整理成文本，在 Android 版 Cherry Studio 中创建专用助手，借鉴 [Chat.skill](https://github.com/Pronting/chat-skills) 的结构化分析思路，并用独立存档延续长会话。它不是 Chat.skill 的官方移植，也不包含微信客户端、原版 Skill 或任何真实聊天数据。

## 项目怎么来的

我想在手机上用一个聊天助手，又希望在日常网络环境下使用自己配置的模型。最初参考了两个开源项目：

1. [WeChatMsg 的公开归档分支](https://github.com/little-KaoKao/WeChatMsg)提供了理解和导出 Windows 本地微信记录的工具与示例。我的一次本地实践由此取得了可读的聊天文本；导出工具和数据库副本都没有放进这个公开项目。
2. [Pronting/chat-skills](https://github.com/Pronting/chat-skills)提供了聊天分析的规则和指标思路。我希望在 Cherry Studio Mobile 里借鉴这些思路，但手机端的这次实践**没有原生运行该仓库的 Skill**。

随后，我让 GPT 写了一份迁移与会话交接说明，把它交给 Cherry Studio 的默认智能体。默认智能体创建了专用助手，又生成了 Topic 启动包。最后，我把本地整理的聊天记录交给这个助手试用，主观上得到了有帮助的回复。这是一次个人使用体验，不是经过对照测试的效果结论。

这条实际路径是：

```text
本地记录导出 → 整理和脱敏 → GPT 迁移说明
                             ↓
Cherry 默认智能体创建专用助手 → Topic 启动包 → 私人会话试用
                                                  ↓
                                       存档与新会话交接
```

## 项目做了什么

- 整理了面向 Cherry Studio Mobile 的**助手创建请求、参考系统提示词、Topic 启动包和交接模板**。
- 把规则、长期事实存档和近期聊天分开；把事实、推测和未知分开。
- 对“样本不足”“明确拒绝和边界”“不凭指标读心”作出约束。IVI、SPE、EWS 等分数仅是启发式提示，不是人的真实心理概率。
- 提供完全虚构的演示材料和公开文件检查脚本，避免把真人对话作为仓库示例。

公开模板是在原有过程文件基础上整理的**可分享版本**。其中的参考系统提示词不冒充当时 Cherry 实际生成的原文；不同应用版本或模型的输出也可能不同。项目没有自动读取、解密或发送微信消息的程序。来源、使用边界和授权分别见 [来源声明](ATTRIBUTION.md) 与 [隐私说明](docs/PRIVACY.md)。

## 项目怎么运行

1. 安装 [Cherry Studio Mobile](https://github.com/CherryHQ/cherry-studio-app)，在应用内配置你自己选择的模型服务。API Key 只填在应用的凭据设置里，不写入仓库、提示词或截图。
2. 如需分析自己的历史记录，先在本机用你信任的方式得到可读文本，并在本机检查、脱敏。导出环节可参考 [WeChatMsg 的说明](https://github.com/little-KaoKao/WeChatMsg)，但本仓库不替它执行微信进程操作。没有历史记录时，可直接用[虚构示例](examples/synthetic-dialogue.md)熟悉流程。
3. 把 [创建请求](prompts/create-assistant.md) 和 [系统提示词模板](prompts/assistant-system.md) 一起交给 Cherry 的默认智能体，检查它实际创建的助手及系统提示词。如果当前版本不能代为创建，就手动新建助手并填入系统提示词模板。
4. 为一个讨论对象新建独立会话（界面可能称为 Topic），把 [Topic 启动包](prompts/topic-bootstrap.md) 作为首条消息，填入代号和必要背景。之后只提供完成隐私检查的近期聊天；演示时使用合成对话。
5. 需要保留长期上下文时，用 [存档与交接模板](prompts/handoff.md)生成完整状态，再以“状态 + 少量近期聊天”开始新会话。具体操作与检验方法见 [运行手册](docs/RUNBOOK.md)。

把聊天文本发送给在线模型时，**发送的内容会交给所选模型服务处理**。换成代号并不能保证对话无法被重新识别；第三方的私密内容应谨慎处理。请先读 [隐私说明](docs/PRIVACY.md)。

## 文件结构

```text
README.md                     项目来历、成果和运行入口
ATTRIBUTION.md                上游项目与许可说明
docs/PRIVACY.md               真实数据的处理边界
docs/RUNBOOK.md               分步使用及核验
prompts/create-assistant.md  给 Cherry 默认智能体的公开请求模板
prompts/assistant-system.md  手动创建助手时可用的参考配置
prompts/topic-bootstrap.md   每个新会话的首条消息模板
prompts/handoff.md           长会话存档和交接模板
examples/synthetic-dialogue.md  完全虚构的演示
scripts/check_public.py      可提交文件清单及基础隐私扫描
toolchain/                   本机工具和环境，Git 忽略，不发布
```

在公开前运行：

```powershell
python scripts/check_public.py
git status --short --untracked-files=all
```

检查脚本只能发现常见路径、账号和密钥形态，**不能代替人工逐字审阅**。本仓库尚未为原创文档和模板选择独立许可证；上游作品仍遵循各自的许可证。
