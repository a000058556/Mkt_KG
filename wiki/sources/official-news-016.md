---
schema_version: "1.0.0"
id: "official-news-016"
type: "source"
title: "DefenseTrust 與 ISO 27001:2022 條款提醒（僅圖片）"
summary: "三語正文只有一句標語與圖片；ISO 條款內容在未讀圖片中，需以 news/17 為文字依據。"
language: "zh-TW"
status: "reference_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-016"]
related: ["concept-iso-27001", "entity-defensetrust", "official-news-017", "issue-source-gaps"]
---

# DefenseTrust 與 ISO 27001:2022 條款提醒（僅圖片）

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/16)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/44`，`id=16`，分類「台北訊息」。

- API `date`：2025-02-06
- `created_at`／`updated_at`：皆為 2026-05-25T14:45:44Z
- 內文日期：無

## 內容狀態

繁中正文僅有「DefenseTrust是對抗全球威脅情資的好選擇」一句、圖片 `security-dm.jpg.jpg`、一個「關於DefenseTrust」字樣（未帶連結）與 hashtag。英文（`news-en.json` `/data/44`）與日文（`news-jp.json` `/data/44`）同樣只有標語、同一圖片與 hashtag。標題所稱「新增重點條款提醒」的內容不在文字中，可能在圖片裡，但圖片未下載／OCR，不得推測。

## 時效與限制

- 不可用本篇證明 DefenseTrust 符合任何 ISO 條款；合規說法以 [official-news-017](official-news-017.md) 的文字為來源說法，且仍需人員確認。
- 本篇與 news/17 使用相同封面 `news-security-dm.jpg` 及正文圖 `security-dm.jpg.jpg`，應為同一 DM 的前後發布，不算獨立佐證。

## 原文瑕疵

- 標語「對抗全球威脅情資」字面上把情資當成對抗對象，語意不通（英文 "Against Global Cyber Threat Intelligence" 同樣）。
- 圖檔名重複副檔名 `.jpg.jpg`；「關於DefenseTrust」沒有連結目標。

## 整合去向

[ISO 27001](../concepts/iso-27001.md)、[DefenseTrust](../entities/defensetrust.md)、[來源缺口](../issues/source-gaps.md)。
