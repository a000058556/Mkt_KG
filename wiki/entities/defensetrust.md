---
schema_version: "1.0.0"
id: "entity-defensetrust"
type: "entity"
title: "DefenseTrust"
summary: "整合情資比對、策略阻擋、部署與報表的來源說法，數字與絕對化用語另列待確認。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["facebook-pfbid0AMmGpcRMbRVaJt5HDHR6Ap49giTEcmR8sXYGvPregZ75e8PrgB4LLGuPNoL3Ap1Vl", "official-news-045", "official-news-060", "official-news-005", "official-news-006", "official-news-012", "official-news-013", "official-news-017", "official-news-018", "official-news-020", "official-news-024", "official-news-034", "official-news-041", "official-news-054", "official-news-055", "official-news-058"]
related: ["human-2026-11-01-005", "human-2026-11-01-003", "human-2026-11-01-004", "human-2026-11-01-002", "concept-threat-intelligence", "issue-facebook-cta", "issue-time-sensitive-claims", "issue-promotion-language", "issue-threat-intel-figures", "concept-ngfw-complement", "concept-iso-27001", "entity-x-view", "entity-aaeon"]
---

# DefenseTrust


## 來源支持的產品說法

[Facebook 貼文](../sources/facebook-threat-intelligence-update.md) 說明 IP／Domain 情資分類比對、依企業安全策略處理命中連線，以及由日誌觀察紀錄。這是來源敘述，不是本次功能驗測。見 [威脅情資](../concepts/threat-intelligence.md)。

[合作公告](../sources/official-news-045.md) 繁中版稱 DefenseTrust 為「新世代威脅情資管理平台，整合全球即時黑名單與情資來源」；英日版未翻譯此段，依 [決策 Q8](../../docs/DECISIONS.md) 以繁中為準，見 [語言差異](../issues/promotion-language.md)。來源沒有列出情資來源名稱、數量或更新頻率。

## 2024–2026 功能與定位

| 面向 | 來源說法 | 來源 |
|---|---|---|
| 定位 | 2024「新世代威脅管理」；2024-11「企業的威脅情資中心」；2025-11「次世代防火牆的好幫手」 | [news/6](../sources/official-news-006.md)、[news/13](../sources/official-news-013.md)、[news/34](../sources/official-news-034.md) |
| 情資 | 在 Defense Cloud 之上整合 OSINT 與第三方情資（如 X-Force）；蜜罐與欺敵技術獵捕 | [news/18](../sources/official-news-018.md)、[news/24](../sources/official-news-024.md)、[news/34](../sources/official-news-034.md)、[news/55](../sources/official-news-055.md) |
| 阻擋範圍 | 惡意網站、惡意下載、釣魚、殭屍網路、C&C；稱可判斷加密 SSL 連線 | [news/12](../sources/official-news-012.md)、[news/41](../sources/official-news-041.md)、[news/54](../sources/official-news-054.md) |
| 功能條列 | 19 種惡意檢測引擎、IP 洗白名單（1 小時）、Geo-IP 國別阻擋、DNS 攔截、XFF 代理 IP 解析、DGA 偵測、Domain Reputation | [news/41](../sources/official-news-041.md)、[news/55](../sources/official-news-055.md) |
| 部署 | Inline 模式、DPDK 封包轉發、Non-SQL 資料庫、硬體與軟體旁路 | [news/18](../sources/official-news-018.md)（[iThome PR 同稿](../sources/external-c8131160ce99.md)）、[news/41](../sources/official-news-041.md) |
| 內建管理 | 群組／用戶、安全策略、流量管理、黑白名單、憑證管理、Radius；[X-View](x-view.md) 報表與 AI 情資分析報告 | [news/17](../sources/official-news-017.md)、[news/20](../sources/official-news-020.md)、[news/41](../sources/official-news-041.md) |
| 硬體 | 搭載 AAEON FWS-7541 的來源說法 | [news/24](../sources/official-news-024.md)，見 [AAEON](aaeon.md) |
| 流程與日誌 | 情資更新→分類比對→命中→依策略阻擋；日誌可見命中紀錄與處理結果 | [news/58](../sources/official-news-058.md) |

適用客群在不同篇寫法不同：政府、醫療、大型企業內網（[news/34](../sources/official-news-034.md)），政府、金融、跨國企業、大型製造業（[news/41](../sources/official-news-041.md)）。與防火牆的關係見 [補強 NGFW](../concepts/ngfw-complement.md)；合規說法見 [ISO 27001](../concepts/iso-27001.md)。

經 [使用者澄清](../sources/human-2026-11-01-002.md)（2026-11-01）：DefenseTrust **每 3 分鐘請求情資**，情資**最晚每小時更新**；不可寫成情資每 3 分鐘更新。另經使用者確認：最新情資保持在**百萬筆等級**（[確認](../sources/human-2026-11-01-003.md)），**有效攔截超過 80% 已知惡意網站**是正確描述（[確認](../sources/human-2026-11-01-004.md)）。情資涵蓋 224 個國家已確認；「零誤判」「誤報率近乎零」**不可使用**（可能被過度解釋，[確認](../sources/human-2026-11-01-005.md)）。見 [情資數字](../issues/threat-intel-figures.md)。

## 跨來源的語氣差異

[合作公告](../sources/official-news-045.md) 及 [news/21](../sources/official-news-021.md)、[news/24](../sources/official-news-024.md) 使用「零時差防禦」，[news/5](../sources/official-news-005.md) 甚至寫「情資不受零時差攻擊」；Facebook 說法帶有「命中情資」及「依策略」條件。兩者可並存為不同文案表達，不能將前者擴張成攔截所有未知攻擊的技術保證。撰稿應保留條件，待產品負責人確認正式宣稱。

## 待確認

[CTA 連結](../issues/facebook-cta.md) 目的地不符；[修補快照](../sources/official-news-060.md) 的驗證中狀態尚無較新資料。品牌別名 Defense Trust 僅用於檢索歸一，引用原文時保留原有拼法。
