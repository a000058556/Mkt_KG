---
schema_version: "1.0.0"
id: "official-news-012"
type: "source"
title: "DefenseTrust 全球 IP 分析與大規模阻擋"
summary: "DefenseTrust 可辨識破億 IP、阻擋多類已知惡意連線及 SSL 連線的來源說法；英日數量譯為十億。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-012"]
related: ["entity-defensetrust", "concept-threat-intelligence", "issue-time-sensitive-claims"]
---

# DefenseTrust 全球 IP 分析與大規模阻擋

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/12)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/48`，`id=12`，分類「台北訊息」。

- API `date`：2024-10-31
- `created_at`：2026-05-25T14:45:44Z；`updated_at`：2026-09-15T09:58:32Z
- 內文日期：無

## 內容摘要

依正文單段：DefenseTrust 設計來阻擋極大量惡意 IP，「能辦識到破億個IP」，可阻擋已知惡意連線，例舉惡意網站、惡意軟體下載、網路釣魚、殭屍網路、C&C 連線；「即便是加密的SSL連線一樣能精準的判斷與阻擋」。附 DefenseTrust 產品頁連結。

## 時效與限制

- 「破億個IP」「精準」為 2024-10 的來源說法，沒有統計方法或測試條件，不可寫成現行規格。
- 英文 "over a billion"、日文「10億件以上」，與繁中「破億」（一億以上）相差一個數量級；依決策 Q8 以繁中為準，記為翻譯差異，撰稿勿採英日數字。

## 原文瑕疵

- 「辦識」應為「辨識」。
- 英日版產品頁連結含 `fbclid` 追蹤參數；英日正文圖為 `dOS-security-intelligence.jpg`，繁中為 `ip-identification.jpg`。圖片皆未檢視。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[威脅情資](../concepts/threat-intelligence.md)、[時效敏感宣稱](../issues/time-sensitive-claims.md)。
