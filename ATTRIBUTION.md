# 来源与署名

本项目记录的是对现有工具和规则的**个人使用与提示词适配经验**。以下项目分别承担不同角色；没有任何上游项目参与、认可或维护本仓库。

| 来源 | 在本实践中的作用 | 公开仓库的处理方式 |
| --- | --- | --- |
| [LC044/WeChatMsg](https://github.com/LC044/WeChatMsg) 及 [little-KaoKao/WeChatMsg 归档分支](https://github.com/little-KaoKao/WeChatMsg) | Windows 本地聊天记录导出的参考工具 | `third_party/WeChatMsg/` 收录本地实践使用的 98 个上游文件；保留原 `LICENSE`，版本与哈希见 `UPSTREAM_SOURCE.json` |
| [Pronting/chat-skills](https://github.com/Pronting/chat-skills) | 结构化聊天分析与指标思路的来源 | 明确标注“借鉴”；未包含其 `SKILL.md` 或 `references/` 原文件，也不声称原生执行 |
| [Cherry Studio Mobile](https://github.com/CherryHQ/cherry-studio-app) | 创建、配置和运行手机端助手的应用 | 只描述使用过程，不包含其应用源码 |
| GPT 与 Cherry Studio 中的模型 | 生成早期迁移说明和助手提示词草稿 | 公开模板经过人工整理；不把模型生成的内容冒充上游项目原文 |

收录的 WeChatMsg 文件逐个与 [little-KaoKao/WeChatMsg 的 `v4-new-arch` 提交 `3613e4668f2a202c154869c67ecb77ffd9ea40b2`](https://github.com/little-KaoKao/WeChatMsg/tree/3613e4668f2a202c154869c67ecb77ffd9ea40b2) 比对，内容一致。这只是该分支的**部分文件**，并非完整上游仓库；原样保留了 MIT License 和 `Copyright (c) 2024 SiYuan` 声明。[Chat.skill 的 MIT License](https://github.com/Pronting/chat-skills/blob/main/LICENSE) 版权标注为 `Copyright (c) 2026 pront`，本仓库没有复制其规则文件。Cherry Studio Mobile 的应用源码另按其[仓库许可证](https://github.com/CherryHQ/cherry-studio-app/blob/main/LICENSE)管理；本项目没有复制该源码。

本仓库目前仅发布原创整理的说明、参考提示词和合成示例，尚未选择这些内容自己的许可证。公开可见不自动代表允许任何方式再分发。
