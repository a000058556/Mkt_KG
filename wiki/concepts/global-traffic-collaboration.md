---
schema_version: "1.0.0"
id: "concept-global-traffic-collaboration"
type: "concept"
title: "GTC：全球流量協作與 DNS 保護"
summary: "AgileLink 的 GTC DNS 以入站流量分流與 DNSSEC 敘述 DNS 層面的可用性與安全。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-007", "official-news-019", "official-news-022", "official-news-024", "official-news-039"]
related: ["entity-agilelink", "concept-wan-resilience"]
---

# GTC：全球流量協作與 DNS 保護

## 來源中的機制

- [news/7](../sources/official-news-007.md)（2024-07）說明 Global Traffic Collaboration（GTC）把源自 Internet、連入存取公司內部服務的流量分散引導到不同線路，以有效使用線路頻寬並提升服務品質；列出支援 SOA、SRV、A、AAAA、CNAME、NS、MX、TXT、PTR 記錄。該篇未說明屬於哪個產品。
- [news/19](../sources/official-news-019.md)、[news/24](../sources/official-news-024.md) 把 GTC DNS 與 DNSSEC 防護列為 [AgileLink](../entities/agilelink.md) 的功能；[news/39](../sources/official-news-039.md)（2026-01）重述入站分流，記錄類型列表與 [news/7](../sources/official-news-007.md) 略有不同（未列 PTR，多列 CNAME *.domain.com）。
- COMPUTEX 2025 講座 5/20 的 AgileLink 主題含 GTC DNS 保護，見 [news/22](../sources/official-news-022.md)。

## 撰稿用途與限制

可把 GTC 寫成「對外服務的入站流量也能走多條線」，補足 [WAN 韌性](wan-resilience.md) 只談出站備援的角度。各篇支援記錄類型不一致，引用規格前需產品確認；「不中斷的 DNS 查詢」屬宣傳用語，不能當可用性保證。
