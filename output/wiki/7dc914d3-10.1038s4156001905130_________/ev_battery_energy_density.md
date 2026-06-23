---
tags: [wiki, ev-battery, energy-density]
aliases: [전기차 배터리 에너지 밀도, EV battery, 셀 비에너지, Wh/kg]
paper: "[[papers/7dc914d3-10.1038s4156001905130_________]]"
created: 2026-06-23
---

# 전기차 배터리 에너지 밀도 (EV Battery Energy Density)

## Definition
전기차용 리튬이온 배터리의 단위 질량(Wh kg⁻¹, 비에너지) 또는 단위 부피(Wh l⁻¹, 에너지 밀도)당 저장 가능한 전기 에너지의 양. 주행거리를 결정하는 핵심 지표이며, 재료→전극→셀→팩 수준에서 계층적으로 감소한다.

## Context in Paper
논문의 근본 동기. 내연기관 대비 주행거리 불안 해소를 위해 US DOE는 팩 수준 235 Wh kg⁻¹/500 Wh l⁻¹, US$100 kWh⁻¹ 목표를 제시한다. 이를 달성하려면 양극재 수준에서 최소 800 Wh kg⁻¹이 필요하며, 셀 수준 목표는 350 Wh kg⁻¹이다. 논문 전체는 이 에너지 목표를 달성하기 위한 고니켈 층상 산화물 설계 전략을 논의한다.

## Related Concepts
- [[high-nickel_layered_oxide]] — 에너지 밀도 향상의 핵심 재료 전략
- [[ncm_cathode]] — 에너지 함량 증대를 위해 NCM-111→523→622→811로 진화
- [[nca_cathode]] — Panasonic NCA-80으로 300 Wh kg⁻¹ 달성
- [[single-crystal_particles]] — 높은 전극 밀도(Wh l⁻¹) 향상 잠재력
- [[low-cobalt_chemistry]] — 에너지 함량 유지하면서 비용 절감

## Key Properties / Characteristics

### 에너지 밀도의 계층적 감소
```
재료 수준: ~800 Wh kg⁻¹ (목표)
    ↓ × 0.5–0.6
전극 수준: ~400–500 Wh kg⁻¹
    ↓ × 0.7–0.8
셀 수준: ~300–350 Wh kg⁻¹
    ↓ × 0.6–0.7
팩 수준: ~200–250 Wh kg⁻¹
```

### 현재 전기차 배터리 성능 (2019년 기준, 표 1)
| 가격대 | 대표 모델 | 화학 | 배터리 (kWh) | 주행거리 (km) |
|--------|----------|------|-------------|--------------|
| ~$30K | 쉐보레 볼트 LT | NCM | 60 | 383 |
| ~$40K | 현대 코나 전기 | NCM | 64 | 415 |
| ~$60K | 테슬라 Model 3 롱 레인지 | NCA | ~75 | 500 |
| ~$100K | 테슬라 S 롱 레인지 | NCA | ~100 | 595 |

### 에너지 목표 및 달성 경로
| 목표 | 현황 | 경로 |
|------|------|------|
| 350 Wh kg⁻¹ (셀, 흑연 음극) | 300 Wh kg⁻¹ (최신) | NCM/NCA 고니켈화 |
| 500 Wh kg⁻¹ (셀, Li 금속 음극) | 연구 단계 | Li 금속 음극 + 고니켈 양극 |
| 235 Wh kg⁻¹ (팩) | 180–190 Wh kg⁻¹ (현재) | 셀-팩 효율 향상 |
| US$100 kWh⁻¹ | US$176 kWh⁻¹ (2018) | 대량 생산, 저코발트화 |

## Examples
- CATL NCM-811 파우치: 300 Wh kg⁻¹ 셀 수준 달성
- Panasonic NCA 21700: 300 Wh kg⁻¹ 셀 수준 달성
- 2025년 예상: NCM/NCA + 흑연-실리콘 음극 → 350 Wh kg⁻¹ 근접

## References
- [[papers/7dc914d3-10.1038s4156001905130_________]] — 원본 논문
- *US DRIVE Electrochemical Energy Storage Tech Team Roadmap* (USCAR, 2017) — 팩 수준 에너지 밀도 목표
- Schmuch, R. et al. *Nat. Energy* **3**, 267–278 (2018) — 자동차 배터리 재료 성능 및 비용
