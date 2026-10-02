# Chatlog to Agent

**把恋爱军师装进口袋。** Chatlog to Agent 是一套手机上的便携聊天分析助手方案：导入微信聊天记录，帮你梳理暧昧进展、分析互动信号、准备自然的回复，也能复盘一段关系中的关键转折。聊天卡壳、拿不准对方的态度、犹豫该不该邀约时，随手打开手机，就能带着真实上下文和 AI 商量下一步，让下一句更有底气。

**本仓库当前公开的文件只是初版。新版已经完成全链路更新，但因文件涉及个人隐私，后续更新不再上传 GitHub，本仓库也不再持续维护。**

初版主要记录了“微信聊天记录辅助导出 → Cherry Studio Mobile 提示词助手”的实践。现在实际使用的新版，已经更新为“PC 微信一键导出 TXT → Android Operit AI → 原版 Chat.skill”的全新完整链路。

**需要新版方案及相关文件，请联系：[854391415@qq.com](mailto:854391415@qq.com)。**

## 新版已经实现什么

- **PC 微信聊天记录轻松导出 TXT。**在 Windows 电脑上选择联系人或会话，将记录整理成带有时间、发言人和消息内容的文本，方便传到手机使用。
- **Android 端 Operit AI 运行原版 Chat.skill。**Skill、参考文件和聊天记录放在手机本地工作区，由 Operit 加载，用于聊天分析、回复建议和复盘，无需再把几份 Markdown 当作提示词来模拟 Skill。
- **手机可以独立使用，电脑可以关机。**电脑只负责需要时导出新的聊天记录，手机上的 Agent 不依赖电脑常开或电脑后端。

```text
PC 微信聊天记录 → 本机导出 TXT → 传到手机
                                  ↓
                    Android Operit AI + Chat.skill
                                  ↓
                      聊天分析、回复建议与复盘
```

关于离线使用：Skill 和文件工作区在手机本地运行；配置手机本地模型后，可完全离线使用。若选择在线模型 API，推理仍需联网，但同样无需电脑持续运行。

**以上描述的是已经完成的新版方案，不是本仓库初版文件直接提供的全部功能。**

## 三个主要项目的引用与说明

| 项目 | 作用与说明 |
| --- | --- |
| [WeChatMsg](https://github.com/little-KaoKao/WeChatMsg) | 微信本地聊天数据解析和导出的参考来源。这里链接的是公开归档分支；本仓库初版保留了经核对的上游源码子集。新版 PC 导出工具另行完成了本机适配。 |
| [Operit AI](https://github.com/AAswordman/Operit) | Android 上的 Agent 运行环境，提供本地文件工作区、Skill 加载，以及在线或本地模型接入，让手机独立运行这套工作流。安装包见 [官方 Releases](https://github.com/AAswordman/Operit/releases)，使用说明见 [官方文档](https://operit.app/)。 |
| [Chat.skill / Pronting/chat-skills](https://github.com/Pronting/chat-skills) | 提供聊天分析、回复建议与复盘的 Skill 规则和参考资料。新版通过 Operit 加载原版 Skill，本项目只记录组合使用经验，不代表上游官方。 |

感谢以上项目的作者与维护者。上游项目各自遵循原有许可证；仓库内保留的 WeChatMsg 源码带有原 MIT 许可证，固定版本与文件哈希见 [UPSTREAM_SOURCE.json](UPSTREAM_SOURCE.json)。初版公开材料的来源说明见 [ATTRIBUTION.md](ATTRIBUTION.md)。

## 仓库里实际保留的内容

- 初版 Cherry Studio Mobile 的提示词、会话启动与交接模板。
- 初版实践说明、隐私说明和完全虚构的演示材料。
- 经核对的 WeChatMsg 历史源码子集与来源清单。

这些文件作为初版记录保留。**新版导出工具、完整部署文件、手机工作区和私人配置没有上传到本仓库。**因此，克隆当前仓库得到的是初版，而不是已经更新完成的完整版。

## 停更与联系

由于更新后的文件和使用过程涉及个人隐私，本项目不再公开上传后续更新，也不公开真实聊天记录、数据库和私人配置。

有需要请通过邮件联系：**[854391415@qq.com](mailto:854391415@qq.com)**。
