---
schema_version: "1.0.0"
id: "official-news-054"
type: "source"
title: "DefenseCloud 雲端情報與 DefenseTrust 地端防禦"
summary: "雲地整合敘事：DefenseCloud 情資來源、DefenseTrust 地端阻擋、應用情境與企業版方案。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-054"]
related: ["entity-defensetrust", "entity-cloud-platforms", "concept-threat-intelligence", "concept-ngfw-complement"]
---

# DefenseCloud 雲端情報與 DefenseTrust 地端防禦

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/54)；[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/6`，`id=54`。API `date` 2026-06-30；`created_at` 2026-06-30T10:20:24Z；`updated_at` 2026-09-15T09:58:32Z。 英日同 ID 為翻譯版本，不算獨立證據；圖片未下載、未 OCR，不推測圖內內容。

## 內容摘要

- 開頭：勒索軟體、惡意網站、釣魚與 C&C 增加，挑戰「不只是防火牆是否存在」，以三個勾選問題引導。
- 「全球威脅情報即時更新」：DefenseCloud 為 SaaS，透過蜜罐獵捕系統更新情資；列出即時查詢、結合 DefenseTrust、訂閱制、情資買斷／年度服務四種形式；「百萬筆攻擊來源」地圖、「涵蓋 224 個國家」。
- 「地端即時自動防禦」：DefenseTrust 段落與 [news/41](official-news-041.md) 開頭逐字相同（80%、Inline、每天更新、業界最快、誤報率近乎零、旁路）。
- 「雲地整合，降低維運負擔」：自動更新、同步至地端、可視化報表、簡化維運。
- 「應用情境」：勒索軟體／惡意下載、釣魚、異常外連（C&C）、「強化零信任防護架構」。
- 企業版 Enterprise Custom 方案同 [news/46](official-news-046.md)。

## 時效與限制

- 80%、224 國、「業界最快」「誤報率近乎零」等為來源宣稱；「零信任」只是應用情境用語，非架構認證。
- 「即時同步」與「每天更新」在同篇並存，更新頻率需產品確認。

## 原文瑕疵

- 公司簡介末尾官網連結目標為 `\`（斷連結），顯示文字為 www.uguardnetworks.com。
- 「Defense Cloud」「DefenseCloud」寫法混用。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[雲端平台](../entities/cloud-platforms.md)、[威脅情資](../concepts/threat-intelligence.md)、[補強 NGFW](../concepts/ngfw-complement.md)。
