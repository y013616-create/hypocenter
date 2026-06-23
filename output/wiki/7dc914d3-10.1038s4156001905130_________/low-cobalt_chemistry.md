---
tags: [wiki, battery-materials, supply-chain]
aliases: [저코발트 전략, zero-cobalt, 코발트 저감]
paper: "[[papers/7dc914d3-10.1038s4156001905130_________]]"
created: 2026-06-23
---

# 저코발트 전략 (Low-Cobalt Chemistry)

## Definition
리튬이온 배터리 양극재에서 코발트(Co) 함량을 kWh당 50 g 이하(또는 완전 제거)로 낮추는 재료 설계 방향. 코발트의 지정학적 공급 위험과 높은 가격을 완화하면서 에너지 밀도를 유지하는 것이 목표다.

## Context in Paper
논문은 코발트가 중앙아프리카(주로 DRC)에 집중 생산되며, 현재 연간 공급량 120,000톤이 전기차 수요 급증 시 부족해질 수 있음을 경고한다. 2030년 글로벌 EV 전기화 목표 달성을 위해 NCM/NCA의 Co 함량이 kWh당 50 g 미만이어야 하며, Co 수요는 Co, Li, Ni 각각 120,000, 1,000,000, 1,100,000톤/년을 초과할 것으로 추정된다.

## Related Concepts
- [[ncm_cathode]] — NCM에서 Co 제거는 속도 성능·사이클 안정성 문제로 NCA보다 복잡
- [[nca_cathode]] — Al이 Co 기능을 일부 대체 → Co 제거 경로가 더 단순
- [[linio2]] — Co·Mn 모두 배제한 제로코발트 극단 조성의 기준
- [[dopant_engineering]] — Co 대체 도펀트(Mg, Zr, Ti, Mo, Cr 등)로 안정성 확보
- [[high-nickel_layered_oxide]] — 고니켈화는 단위 용량당 Co 사용량 절감 수단

## Key Properties / Characteristics

### Co의 역할
| 기능 | 설명 |
|------|------|
| 속도 성능 | Li⁺/Ni²⁺ 혼합 억제 → 이온 전도도 향상 |
| 구조 안정화 | 다단계 2상 반응 억제, 층상 구조 유지 |
| 표면 안정화 | 잔류 Li 화합물(LiOH, Li₂CO₃) 형성 억제 |

### 코발트 공급 현황 (2018 기준)
- 연간 공급량: **120,000 톤**
- 배터리용 수요 (2025 예측, Umicore): **90,000 톤**
- 2025년 Co 가격: ~US$75–175/kWh 기여분

### 저코발트화 경로
- **NCM 경로**: Mn 유지 + 대체 도펀트(Al, Mg, Zr) 활용 → 속도 성능 손실 보완 필요
- **NCA 경로**: Al이 5% 소량으로도 효과적 → Co 제거 시 성능 영향 최소화

## Examples
- Panasonic-Tesla: kWh당 Co 50 g 미만 NCA 상용화 (Tesla Model 3)
- Panasonic-Tesla: 제로 Co 자동차 배터리 개발 발표
- NCM-811: kWh당 80–100 g Co (현재 상용화 초기)

## References
- [[papers/7dc914d3-10.1038s4156001905130_________]] — 원본 논문
- Pillot, C. *Li-ion battery raw material supply and demand 2016–2025* (AABC Europe, 2017)
- Vandepitte, K. AABC Europe (2019) — 빠른 전기차 성장 시나리오에서 양극재 공급 탄력성
