---
schema_version: "1.0.0"
id: "official-news-007"
type: "source"
title: "全球流量協作（GTC）短文"
summary: "GTC 將外部連入內部服務的流量分散到不同線路，並列出支援的 DNS 記錄類型。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-007"]
related: ["concept-global-traffic-collaboration", "concept-wan-resilience", "entity-agilelink"]
---

# 全球流量協作（GTC）短文

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/7)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/53`，`id=7`，分類「台北訊息」。

- API `date`：2024-07-30
- `created_at`／`updated_at`：皆為 2026-05-25T14:45:44Z
- 內文日期：無

## 內容摘要

依正文唯一段落：Global Traffic Collaboration「其誘導技術將源自於 Internet 連入存取公司內部服務的流量，分散並引導到不同的線路，達到有效的線路頻寬使用並提升服務品質」；括號列出可支援 SOA、SRV、A、AAAA、CNAME、NS、MX、TXT、PTR 記錄。

## 時效與限制

- 本文未提及 GTC 所屬產品；[official-news-019](official-news-019.md) 稱 AgileLink 支援 Global Traffic Collaboration DNS。歸屬 AgileLink 須以該篇為據，不從本文推得。
- 支援記錄類型為 2024-07 的來源說法，未標示版本。
- 圖片 `GTC_news.jpg` 未下載／OCR。

## 原文瑕疵

- 「其誘導技術」缺少主詞前文，語句不完整；英文直譯為 "Its induction technology"。

## 整合去向

[全球流量協作](../concepts/global-traffic-collaboration.md)、[WAN 韌性](../concepts/wan-resilience.md)、[AgileLink](../entities/agilelink.md)。
