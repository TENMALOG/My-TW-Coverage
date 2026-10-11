# 重驗筆記 — 晶心科 / 6533:objective_ranking_or_market_share:de4c47986928bfbe

原始 claim：[[Meta]](臉書第一代/第二代[[AI]]晶片MTIA主力IP供應商)、[[聯發科]]、[[聯詠]]、瑞薩([[Renesas]])及Axelera [[AI]]。

## 原子主張

1. `SUPPORTED` — Andes supplied processor IP used in Meta's first-generation MTIA.
   期間：MTIA-1 design from 2019; documented publicly in 2023 and later.
   說明：Andes identifies its NX27V/AX25-V100 processor IP in connection with MTIA-1. This supports an IP contribution, not the broader claim that Andes was the chip's main IP supplier.
   來源：[Andes Announces First Customer Tape-Out Delivery of the AX46MPV for Cloud AI Acceleration](https://www.andestech.com/en/2025/12/09/andes-announces-first-customer-tape-out-delivery-of-the-ax46mpv-for-cloud-ai-acceleration)；定位：Paragraph beginning “The NX27V was the first generation Andes RISC-V vector core…”
   來源：[Investor Conference](https://www.andestech.com/wp-content/uploads/2024_0531_Andes_Investor-Conference_E.pdf)；定位：Slide 22, “MTIA: Meta Training/Inference Accelerator”
2. `UNKNOWN` — Andes was the main IP supplier for Meta MTIA-1.
   期間：MTIA-1
   說明：Evidence supports Andes processor IP being used in MTIA-1, but does not establish that Andes was the main supplier of IP for the chip as a whole. The claim's qualifier “main” is not substantiated.
   來源：[Investor Conference](https://www.andestech.com/wp-content/uploads/2024_0531_Andes_Investor-Conference_E.pdf)；定位：Slide 22, “MTIA: Meta Training/Inference Accelerator”
3. `UNKNOWN` — Andes was the main IP supplier for Meta MTIA-2.
   期間：MTIA-2; second-generation chip described in 2025
   說明：The second-generation chip is documented, but the sources reviewed do not establish that Andes supplied its IP, much less that Andes was its main IP supplier.
   來源：[Meta's Second Generation AI Chip: Model-Chip Co-Design and Productionization Experiences](https://dl.acm.org/doi/10.1145/3695053.3731409)；定位：Paper title and section “Case Study: Porting a Model to MTIA 2i”
4. `SUPPORTED` — MediaTek is an Andes IP adopter/customer.
   期間：Documented by 2022; Andes reports adoption by MediaTek.
   說明：Andes identifies MediaTek among IC design companies that widely adopted its processors. This establishes a relationship, not its scale or current commercial status.
   來源：[Andes Technology Announces over 10 Billion Cumulative Shipments of Andes-Embedded SoCs and Records All-Time High Annual and Monthly Revenue in 2021](https://andestech.com/en/2022/03/08/andes-technology-announces-over-10-billion-cumulative-shipments-of-andes-embedded-socs-and-records-all-time-high-annual-and-monthly-revenue-in-2021)；定位：Paragraph beginning “Based on years of experience and know-hows…”
5. `SUPPORTED` — Novatek is an Andes IP adopter/customer.
   期間：Documented by 2022; Andes reports adoption by Novatek.
   說明：Andes identifies Novatek among IC design companies that widely adopted its processors. This establishes a relationship, not its scale or current commercial status.
   來源：[Andes Technology Announces over 10 Billion Cumulative Shipments of Andes-Embedded SoCs and Records All-Time High Annual and Monthly Revenue in 2021](https://andestech.com/en/2022/03/08/andes-technology-announces-over-10-billion-cumulative-shipments-of-andes-embedded-socs-and-records-all-time-high-annual-and-monthly-revenue-in-2021)；定位：Paragraph beginning “Based on years of experience and know-hows…”
6. `SUPPORTED` — Renesas is an Andes IP adopter/customer.
   期間：Selected Andes IP in 2020 for products sampling from the second half of 2021; adoption also reported by 2022.
   說明：Renesas announced selection of Andes CPU IP for new ASSPs, and Andes later included Renesas among adopters.
   來源：[Renesas Selects Andes RISC-V 32-Bit CPU Cores for its First RISC-V Implementation of ASSP/MCUs](https://www.andestech.com/en/2020/10/01/renesas-selects-andes-risc-v-32-bit-cpu-cores-for-its-first-risc-v-implementation-of-assps)；定位：Press release paragraphs beginning “Renesas Electronics Corporation…” and “Renesas selected…”
   來源：[Andes Technology Announces over 10 Billion Cumulative Shipments of Andes-Embedded SoCs and Records All-Time High Annual and Monthly Revenue in 2021](https://andestech.com/en/2022/03/08/andes-technology-announces-over-10-billion-cumulative-shipments-of-andes-embedded-socs-and-records-all-time-high-annual-and-monthly-revenue-in-2021)；定位：Paragraph beginning “Based on years of experience and know-hows…”
7. `SUPPORTED` — Axelera AI is an Andes IP adopter/partner.
   期間：Partnership and Europa AIPU integration announced June 1, 2026.
   說明：The companies announced a strategic partnership; Axelera AI integrated AndesCore AX65 into its Europa AI Processing Unit. This verifies a specific product relationship, not market share or a ranking.
   來源：[Axelera AI and Andes Technology Partner to Power Next-Generation “Europa” AI Platform with High-Performance RISC-V AX65 Cores](https://www.andestech.com/en/2026/06/01/axelera-ai-and-andes-technology-partner-to-power-next-generation-europa-ai-platform-with-high-performance-risc-v-ax65-cores)；定位：Opening announcement and section “The Synergy: D-IMC Meets Out-of-Order RISC-V”

## 判定

Overall `PARTIAL`。

建議改寫：Andes documented its processor IP in Meta MTIA-1 and reported MediaTek, Novatek, and Renesas among Andes processor adopters; Axelera AI later announced integration of Andes AX65 into its Europa AIPU. Available evidence does not establish Andes as the main IP supplier for MTIA-1 or MTIA-2, nor does it establish Andes IP use in MTIA-2.

來源限制：
- The supplied wording is a fragmentary list and does not explicitly state the relationship intended for each company; the customer/adopter interpretation is supported by issuer disclosures.
- The evidence establishes named customer/product relationships, not a market-share figure, market denominator, ranking, or comparative leadership claim.
- Andes is the issuer of several relationship disclosures; these are primary sources but issuer-attributed.
- The MTIA-1 evidence identifies processor IP and custom extensions, not Andes as the main supplier of all MTIA IP.

Focused review of official Andes disclosures and Meta's second-generation MTIA paper verified the named company relationships and Andes IP in MTIA-1. The reviewed sources did not resolve the “main IP supplier” qualifier or attribute MTIA-2 IP to Andes; those atoms remain UNKNOWN.

此紀錄來自獨立 Hermes 單筆重驗。只追加候選重驗結果，未修改原報告、作者決策或既有複核帳本。
