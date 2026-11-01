---
schema_version: "1.0.0"
id: "entity-agilelink"
type: "entity"
title: "AgileLink"
summary: "整合多 WAN、策略路由與 DNS 安全定位的歷史產品敘述，與修補狀態分層保存。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-056", "official-news-045", "official-news-060", "official-news-001", "official-news-007", "official-news-019", "official-news-024", "official-news-031", "official-news-032", "official-news-033", "official-news-039", "official-news-044", "official-news-048", "official-news-059"]
related: ["concept-wan-resilience", "event-metaage-partnership", "issue-time-sensitive-claims", "issue-promotion-language", "entity-warptunnel", "concept-global-traffic-collaboration", "entity-x-view", "concept-legacy-replacement", "event-cve-2026-php", "concept-traffic-management"]
---

# AgileLink


## 來源支持的產品說法

[2026-08 備援文章](../sources/official-news-056.md) 的功能條列描述多 WAN 整合、備援及 PBR，列出專線、寬頻（繁中原文寫「頻寬」，見來源頁）、4G/5G、STARLINK；對應需求是降低單線故障影響並安排應用流量路徑。見 [WAN 韌性](../concepts/wan-resilience.md)。

DNS 安全定位：同一篇三語均稱 AgileLink 是「WAN Load Balance 與 DNS Security」產品。[合作公告](../sources/official-news-045.md) 繁中版另寫支援 GTC DNS 與 DNSSEC 保護機制、可整合多線路與低軌衛星，並以 X-View 集中報表與 AI 情資分析報告掌握風險；英日版未翻譯此段，依 [決策 Q8](../../docs/DECISIONS.md) 以繁中為準，見 [語言差異](../issues/promotion-language.md)。兩篇都沒有說明 DNS 防護的機制細節或適用版本。

以上均為 source_reported，型號、版本與部署條件待確認。

## 2024–2026 來源中的功能演進

| 功能／訴求 | 來源 |
|---|---|
| 「New Generation WAN Management (NGWM)」；線路狀態偵測、故障自動導向；FortiWAN 替代訴求 | [news/1](../sources/official-news-001.md)，見 [舊設備替代](../concepts/legacy-replacement.md) |
| GTC DNS 入站分流與 DNSSEC | [news/19](../sources/official-news-019.md)、[news/24](../sources/official-news-024.md)、[news/39](../sources/official-news-039.md)，見 [GTC](../concepts/global-traffic-collaboration.md) |
| [WarpTunnel™](warptunnel.md) VPN／多 WAN 聚合 | [news/24](../sources/official-news-024.md)、[news/33](../sources/official-news-033.md)、[news/39](../sources/official-news-039.md) |
| STARLINK 低軌衛星整合（2025-08 東京整合的來源說法） | [news/32](../sources/official-news-032.md)、[news/39](../sources/official-news-039.md)、[news/48](../sources/official-news-048.md) |
| PBR、Flow Control 頻寬管理、內建 [X-View](x-view.md) 報表、CEF／Syslog 整合 SOC／SIEM | [news/39](../sources/official-news-039.md) |
| 與 Traffic Shaper 一起處理 AI／SaaS 流量 | [news/44](../sources/official-news-044.md)，見 [流量管理](../concepts/traffic-management.md) |

news/39 另有 [iThome PR 同稿](../sources/external-a101bb7881fe.md)，非獨立佐證。[news/31](../sources/official-news-031.md)（2025-07）是 AgileLink 升版公告，三語正文只有圖片，版本與內容未知。[news/39](../sources/official-news-039.md) 原文同樣寫「頻寬」指寬頻線路。以上皆為 source_reported。

## 行銷可用的議題

可用「備援是否能接手」與「關鍵應用走哪條線」作為訪談和文章題目；原文提到 ERP、雲端、VPN 等場景，不代表已驗證所有場景效能。

## 應分開處理的內容

- [合作公告](../sources/official-news-045.md) 的 2026 優惠已到原訂截止日，不能繼續使用限時促銷 CTA。
- [修補快照](../sources/official-news-060.md) 只記錄 2026-10-30 的產品處理狀態，不是此頁的現行版本清單。
- 2026-10 PHP 漏洞的說明與修補歷程見 [CVE 事件](../events/cve-2026-php.md)。
- 切換時間、會話保持與零中斷保證沒有測試資料（[news/1](../sources/official-news-001.md) 甚至稱網路電話「不會有任何中斷或延遲的感覺」）；見 [時效及宣稱事項](../issues/time-sensitive-claims.md)。
