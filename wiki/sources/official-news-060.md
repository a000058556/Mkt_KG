---
schema_version: "1.0.0"
id: "official-news-060"
type: "source"
title: "2026-10-30 修補進度快照"
summary: "保留公告當時三項產品的不同處理狀態，不作目前修補建議。"
language: "zh-TW"
status: "historical_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-060"]
related: ["entity-agilelink", "entity-defensetrust", "entity-trafficshaper", "issue-time-sensitive-claims"]
---

# 2026-10-30 修補進度快照


## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/60)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/0`，`id=60`。發布 2026-10-27，更新 2026-10-30T10:55:09Z；內文狀態截至 2026-10-30。

## 歷史內容摘要

以下僅轉述原公告「受影響產品與最新修補進度」表，不是獨立漏洞驗證或目前升級指引。

| 產品 | 該快照記錄的進度 |
|---|---|
| [AgileLink](../entities/agilelink.md) | 列出修補版 5.11.38105329_1030、5.10.1194076_1030 |
| [DefenseTrust](../entities/defensetrust.md) | 完成修補、發版驗證中 |
| [TrafficShaper](../entities/trafficshaper.md) | 修復中 |

公告另描述特定條件下的風險、舊版本維護終止資訊及當時的攻擊觀察。這些時間敏感資料使用前需向產品／資安負責人確認。不得將「尚未發現成功攻擊案例」轉寫為「不受影響」或「沒有風險」。

## 三語核對與使用限制

三語的修補版本及上述三種進度重點一致；未完成逐句翻譯驗收。CVE 編號、評分及技術細節本次只作歷史公告識別，不聲稱已與漏洞主管機構查核。

## 行銷可用的結構觀察

公告使用「風險背景 → 產品／版本／狀態表 → 觀察時間 → 建議行動」結構。可沿用資訊呈現形式，但版本數字與狀態不能直接複製為今日資訊。見 [時效事項](../issues/time-sensitive-claims.md) 與 [品牌與用語觀察](../writing/brand-observations.md)。
