---
schema_version: "1.0.0"
id: "official-featured-partners"
type: "source"
title: "官網精選合作夥伴（2026-11-01 快照）"
summary: "官網 /partners/featured 在 2026-11-01 列出的 6 家通路夥伴與地區。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-featured-partners"]
related: ["entity-channel-partners", "entity-metaage", "entity-innotel", "entity-shuoyu"]
---

# 官網精選合作夥伴（2026-11-01 快照）

## 來源與時間

- 官網頁面：<https://www.uguardnetworks.com/partners/featured>；前端以 `/api/featured-partners?lang=` 取得資料。
- 快照：[繁中](../../raw/official/2026-11-01/official-featured-partners/r1-zh-TW.json)、[英文](../../raw/official/2026-11-01/official-featured-partners/r1-en.json)、[日文](../../raw/official/2026-11-01/official-featured-partners/r1-jp.json)，根物件 `/partners`；[擷取紀錄](../../raw/official/2026-11-01/official-featured-partners/r1-fetch-log.json)。
- 取得時間 2026-11-01（伺服器時間 13:39 GMT），依使用者指示「代理商狀況請去官網及時確認」查詢。API 沒有提供發布或更新日期。

## 內容摘要

地區篩選為 ALL、TAIWAN、THAILAND、VIETNAM、MALAYSIA。列出的夥伴（繁中名稱；英日版名稱為英文）：

| ID | 夥伴 | 地區 | 網站 |
|---|---|---|---|
| 1 | 邁達特（Metaage Corporation） | 台灣 | metaage.com.tw |
| 2 | 敦新科技（Dawning Technology） | 台灣 | dawningtech.com.tw |
| 3 | 創泓科技（UNIFORCE Technology） | 台灣 | uniforce.com.tw |
| 5 | INNOTEL CO., LTD | 越南 | innotel.com.vn |
| 6 | Sysnect Information Co., Ltd. | 泰國 | sysnect.co.th |
| 7 | SecureOne Distribution Sdn Bhd | 馬來西亞 | secureone.com.my |

每家附一段夥伴介紹，例如 Sysnect 自 2001 年成立、SecureOne 定位為資安代理商；這些是官網對夥伴的描述。

## 限制

- 頁面名稱是「精選合作夥伴」，沒有說明是代理、經銷或其他合作層級，也沒有合約範圍。
- 朔宇科技不在清單上；ID 4 缺號。缺號或未列都不能推論合作已終止，需業務確認。
- 硬體夥伴 AAEON、艾訊不在此頁，可能屬不同類別。整理見 [通路夥伴](../entities/channel-partners.md)。
