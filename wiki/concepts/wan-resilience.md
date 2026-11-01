---
schema_version: "1.0.0"
id: "concept-wan-resilience"
type: "concept"
title: "WAN 韌性與多線路備援"
summary: "把線路多樣性、替代路徑與流量政策連到營運需求。"
language: "zh-TW"
status: "inferred"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-056", "official-news-001", "official-news-033", "official-news-039", "external-93018eaab6d5"]
related: ["entity-agilelink", "writing-product-article", "concept-global-traffic-collaboration", "entity-warptunnel", "concept-legacy-replacement"]
---

# WAN 韌性與多線路備援


## 本庫採用的解釋

依 [AgileLink 來源](../sources/official-news-056.md) 的開頭與 PBR 段落，可把多線路議題拆成三個行銷問句：有哪些可用線路？異常時由哪條接手？平時哪些應用走哪條路？這是對原文的結構化整理。

## 概念邊界

多一條線路本身不能證明服務一定不中斷；來源本身也提出這項限制。備援、PBR 與應用連線保持是不同需要查證的事項，不從備援功能推導具體 SLA。

## 其他來源的補充

- [news/1](../sources/official-news-001.md)（2024）已用線路狀態偵測與故障自動導向說明備援，並結合域名解析維持服務；入站方向見 [GTC](global-traffic-collaboration.md)。
- [news/39](../sources/official-news-039.md)（2026-01）的痛點：ISP 或線路異常、單一線路中斷造成停擺、無法即時掌握網路狀態與歷史數據。
- [news/33](../sources/official-news-033.md) 以台灣周邊海纜故障、跨境連線延遲中斷切入據點互連，產品是 [WarpTunnel™](../entities/warptunnel.md)。
- 備援文章另有 [CTIMES 轉載](../sources/external-93018eaab6d5.md)，非獨立佐證。

## 撰稿用途

適合以 ERP、VPN、視訊或跨點工作作為需求背景；[產品文章範本](../writing/product-article.md) 可用於組織問題與證據，產品關聯為 [AgileLink](../entities/agilelink.md)。
