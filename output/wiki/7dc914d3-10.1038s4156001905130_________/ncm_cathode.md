---
tags: [wiki, battery-materials]
aliases: [NCM, NMC, Li[NiCoMn]O2]
paper: "[[papers/7dc914d3-10.1038s4156001905130_________]]"
created: 2026-06-23
---

# NCM 양극재

## Definition
NCM(Li[Ni_a Co_b Mn_c]O₂, a+b+c=1)은 니켈(Ni), 코발트(Co), 망간(Mn)을 전이금속 자리에 혼합한 층상 산화물 구조의 리튬이온 배터리 양극재다. 조성 비율에 따라 NCM-111, NCM-523, NCM-622, NCM-811 등으로 분류된다.

## Context in Paper
논문은 승용 전기차용 배터리에서 NCM이 LMO·LFP를 대체하며 2018년 기준 설치 용량의 90%(33.1 GWh)를 차지함을 보인다. 특히 NCM-811(LiNi₀.₈Co₀.₁Mn₀.₁O₂)을 중심으로 에너지 함량 증대와 저코발트화 경로를 분석하며, NCM-811 탑재 첫 양산 전기차(CATL 공급, NIO ES6)가 2019년 출시되었음을 언급한다.

## Related Concepts
- [[nca_cathode]] — Co 대신 Al을 사용하는 유사한 고니켈 층상 산화물; NCA에서 Co 제거가 NCM보다 용이함
- [[high-nickel_layered_oxide]] — NCM-811 이상 Ni 분율이 높은 NCM의 상위 개념
- [[linio2]] — Ni 100% 극단 조성; NCM 계열의 화학적 기반
- [[low-cobalt_chemistry]] — NCM에서 Co 함량을 kWh당 50 g 이하로 낮추는 설계 목표
- [[dopant_engineering]] — Mn, Al 외 Mg·Zr·Ti 등 대체 도펀트로 NCM 안정성 보완
- [[co-precipitation_synthesis]] — NCM 산업 생산의 표준 합성 경로
- [[surface_stabilization]] — 고니켈 NCM의 잔류 Li 화합물·가스 발생 억제를 위한 후처리

## Key Properties / Characteristics
| 조성 | 비용량 (mAh g⁻¹, 4.3 V) | 특징 |
|------|--------------------------|------|
| NCM-111 | ~160 | 기준 조성, 안정적 |
| NCM-523 | ~170 | 현재 주력 상용 제품 |
| NCM-622 | ~180 | 중간 단계 |
| NCM-811 | ~200 | 고에너지, 양산 초기 단계 |

- **다단계 2상 반응**: Ni 분율 증가 시 (탈)리튬화 중 비가역적 상전이 발생 → 수명 저하
- **표면 잔류 Li 화합물** (LiOH, Li₂CO₃): 저장 불안정성·가스 발생 원인
- **Li⁺/Ni²⁺ 혼합(cation mixing)**: Co 감소 시 속도 성능 저하 유발

## Examples
- NCM-811: CATL(파우치형)이 300 Wh kg⁻¹ 셀 수준 에너지를 달성
- NCM-622: 현대 코나 전기차(64 kWh, 415 km 주행)에 탑재
- NCM-523: 현재 가장 넓은 시장 점유율

## References
- [[papers/7dc914d3-10.1038s4156001905130_________]] — 원본 논문
- Kim, J. et al. *Adv. Energy Mater.* **8**, 1702028 (2018) — NCM 상용화 전망
