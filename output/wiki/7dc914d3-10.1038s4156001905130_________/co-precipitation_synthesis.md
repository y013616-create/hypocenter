---
tags: [wiki, synthesis, manufacturing]
aliases: [공침법, co-precipitation, 공동침전]
paper: "[[papers/7dc914d3-10.1038s4156001905130_________]]"
created: 2026-06-23
---

# 공침법 합성 (Co-Precipitation Synthesis)

## Definition
전이금속 이온(Ni²⁺, Co²⁺, Mn²⁺ 등)을 수용액에서 NaOH와 NH₃ 존재 하에 공동 침전시켜 전구체(수산화물) 입자를 생성한 후, 리튬 소스(LiOH 또는 Li₂CO₃)와 혼합·소성하여 층상 산화물 양극재를 합성하는 표준 산업 공정이다.

## Context in Paper
논문은 공침법이 현재 NCM/NCA 산업 생산의 표준 경로임을 설명하고, 고니켈 조성(예: NCM-811)에서 요구되는 더 엄격한 공정 조건—pH·암모니아 농도 조정, LiOH 사용(Li₂CO₃ 대신), 유동 O₂ 분위기, 다단계 소성, 내부식성 장비, 습도 제어—을 상세히 다룬다. 원자재가 전체 비용의 75–90%를 차지하며, 그중 Co가 상당 비중임을 비용 분석으로 보여준다.

## Related Concepts
- [[ncm_cathode]] — 공침법의 주요 생산 대상; 고니켈 NCM일수록 공정 복잡도 증가
- [[nca_cathode]] — NCA 합성에도 공침법 적용; Al은 불순물 상 억제를 위해 좁은 용해도 범위 관리 필요
- [[high-nickel_layered_oxide]] — 고니켈 조성에서 pH, 온도, 소성 조건의 정밀 제어가 핵심
- [[single-crystal_particles]] — 단결정 합성은 공침법보다 복잡하고 비용이 높음
- [[surface_stabilization]] — 소성 후 표면 처리(세척, 코팅)가 공침법 공정에 포함

## Key Properties / Characteristics

### 공침법 주요 공정 단계
```
전이금속 용액 + NaOH + NH₃
        ↓  (pH, 온도, 시간 제어)
전구체 침전 (수산화물)
        ↓  (세척, 건조, 분쇄)
LiOH or Li₂CO₃ 혼합
        ↓  (소성, O₂ 분위기)
층상 산화물 분말
        ↓  (표면 처리, 체질, 포장)
최종 양극재
```

### 고니켈 조성에서의 공정 변수 (그림 3b 요약)
| 변수 | 저니켈 (NCM-111) | 고니켈 (NCM-811) |
|------|-----------------|-----------------|
| 침전 pH | 낮음 | 높음 |
| NH₃ 농도 | 적음 | 많음 |
| Li 소스 | Li₂CO₃ | LiOH |
| 소성 온도 | 높음 (>900 °C) | 낮음 (~750 °C) |
| O₂ 분위기 | 공기 | 유동 O₂ 필수 |

### 비용 구조 (kWh당, 2018년 기준)
- **원자재**: 전체 비용의 75–90% (Ni, Co, Mn, Li 원료)
- **생산 비용**: 에너지, O₂ 가스, NaOH, NH₄·H₂O, 인건비, 감가상각
- NCM-811의 kWh당 총 비용 ≈ NCM-523 수준 (높은 에너지 함량·낮은 Co 사용량 상쇄)

## Examples
- NCM-523: 현재 가장 경제적인 공침법 생산 조성
- NCM-811: 유동 O₂, LiOH, 내식성 장비, 습도 제어 등 추가 인프라 필요
- 농도 구배 NCM: 공침법 변형 적용이나 대규모 생산에서 조성 불균일성 문제 미해결

## References
- [[papers/7dc914d3-10.1038s4156001905130_________]] — 원본 논문
- Yakovleva, M. *From Raw Materials to Next-Generation Advanced Batteries* (FMC Corporation, 2017)
