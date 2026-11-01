---
schema_version: "1.0.0"
id: "synthesis-messaging-timeline"
type: "synthesis"
title: "產品訊息演進：2024–2026"
summary: "依官網 API 日期整理產品組合、主打訊息與合作夥伴的變化，供選題與避免引用過時說法。"
language: "zh-TW"
status: "inferred"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-001", "official-news-006", "official-news-007", "official-news-008", "official-news-009", "official-news-011", "official-news-017", "official-news-024", "official-news-032", "official-news-033", "official-news-035", "official-news-037", "official-news-039", "official-news-044", "official-news-045", "official-news-046", "official-news-048", "official-news-054", "official-news-055", "official-news-057", "official-news-058", "official-news-059"]
related: ["entity-uguard", "entity-defensetrust", "entity-agilelink", "issue-threat-intel-figures"]
---

# 產品訊息演進：2024–2026

## 時間軸（依 API `date`）

| 期間 | 主打訊息 | 依據 |
|---|---|---|
| 2024 上半 | AgileLink 以 FortiWAN 替代、多線路備援切入；DefenseTrust 以「新世代威脅管理」登場 | [news/1](../sources/official-news-001.md)、[news/6](../sources/official-news-006.md) |
| 2024 下半 | GTC 入站分流、Traffic Shaper 部署模式；越南 Innotel 代理、AAEON 策略夥伴 | [news/7](../sources/official-news-007.md)、[news/8](../sources/official-news-008.md)、[news/9](../sources/official-news-009.md)、[news/11](../sources/official-news-011.md) |
| 2025 上半 | DefenseTrust 與 ISO 27001:2022、NGFW 對比；COMPUTEX 2025 推 X-View 與 AI 小助手 | [news/17](../sources/official-news-017.md)、[news/24](../sources/official-news-024.md) |
| 2025 下半 | 新加坡週年與 STARLINK；WarpTunnel；Traffic Shaper L7；艾訊硬體合作；NGFW 好幫手定位 | [news/32](../sources/official-news-032.md)、[news/33](../sources/official-news-033.md)、[news/35](../sources/official-news-035.md)、[news/37](../sources/official-news-037.md) |
| 2026 上半 | AgileLink 主控力、AI／SaaS 流量；邁達特代理；DefenseCloud 訂閱；COMPUTEX 2026 推 AgileCloud、AgileShaper；情資雲地整合 | [news/39](../sources/official-news-039.md)、[news/44](../sources/official-news-044.md)、[news/45](../sources/official-news-045.md)、[news/46](../sources/official-news-046.md)、[news/48](../sources/official-news-048.md)、[news/54](../sources/official-news-054.md) |
| 2026 下半 | DefenseTrust 對抗 AI 攻擊；多線路備援；頻寬迷思；FB 系列；PHP 漏洞公告 | [news/55](../sources/official-news-055.md)、[news/56](../sources/official-news-056.md)、[news/57](../sources/official-news-057.md)、[news/58](../sources/official-news-058.md)、[news/59](../sources/official-news-059.md) |

## 整合判斷（Agent 推論）

- 產品組合從「AgileLink／Traffic Shaper／DefenseTrust／SD-WAN」擴展到加入 X-View、AI 報告、DefenseCloud 訂閱、AgileCloud 與 AgileShaper；官網繁中文章最後一次提到 SD-WAN 是 [news/32](../sources/official-news-032.md)（2025-09），2026 年的文章都沒有出現，現況待確認。見 [UGUARD](../entities/uguard.md)。
- DefenseTrust 的數字說法隨時間變動且彼此不一致，越新的文章不代表越正確；見 [情資數字](../issues/threat-intel-figures.md)。
- 2026 下半年的文章（[news/57](../sources/official-news-057.md)、[news/58](../sources/official-news-058.md)）傾向反問標題、FAQ 與流程說明，數字與絕對化用語較少，可作新稿語氣參考。
- 合作敘事從硬體夥伴（AAEON、艾訊）延伸到通路代理（Innotel、朔宇、邁達特）；代理現況都未確認。

這是依來源日期的整理，不代表產品實際上市或停產時間。
