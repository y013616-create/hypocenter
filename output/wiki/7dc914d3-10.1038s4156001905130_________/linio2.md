---
tags: [wiki, battery-materials]
aliases: [LNO, LiNiO2, 리튬니켈산화물]
paper: "[[papers/7dc914d3-10.1038s4156001905130_________]]"
created: 2026-06-23
---

# LiNiO₂ (LNO)

## Definition
LiNiO₂(LNO)는 Ni를 전이금속 자리에 100% 사용하는 층상 산화물(R$\bar{3}$m)로, [[ncm_cathode]]·[[nca_cathode]] 계열의 화학적 기원이자 이론적 에너지 밀도 상한을 대표하는 조성이다. 4.3 V vs Li에서 최대 240–250 mAh g⁻¹ 비용량을 제공한다.

## Context in Paper
논문은 LNO에 대한 최근 관심 부활을 언급하며, Co·Mn·Al을 배제한 초고니켈 저코발트 층상 산화물 설계의 화학적 출발점으로 위치시킨다. 동시에 LNO 도핑 물질 선택에 대한 이론적 합의 부재, 무질서 암염 구조의 재조명(최근 도핑된 LNO에서 가능성 확인) 등 미해결 과제를 지적한다.

## Related Concepts
- [[high-nickel_layered_oxide]] — LNO는 Ni=1인 극단 조성; 상용 고니켈 산화물의 설계 기준점
- [[ncm_cathode]] — LNO에 Co·Mn 도핑 → NCM 계열
- [[nca_cathode]] — LNO에 Co·Al 도핑 → NCA 계열
- [[dopant_engineering]] — LNO 안정화를 위해 B, Ti, Zr, Nb, W, Mo, Mg 등 다양한 도펀트 연구 중
- [[surface_stabilization]] — LNO는 표면 반응성이 극도로 높아 후처리 필수

## Key Properties / Characteristics
- **비용량**: 4.3 V에서 240–250 mAh g⁻¹ (NCM-111 대비 ~60% 향상)
- **Li⁺/Ni²⁺ 혼합**: Ni²⁺(r=0.69 Å) ↔ Li⁺(r=0.76 Å) 이온 반경 유사 → 리튬 층에 Ni²⁺ 침입, 속도 성능 저하
- **다단계 2상 반응**: H1→M→H2→H3 전이가 가장 뚜렷하게 나타남 → 비가역 격자 붕괴
- **열적 불안정**: 고충전 상태에서 가장 낮은 발열 분해 온도
- **공기 저장 불안정**: 표면에 LiOH, Li₂CO₃ 신속 생성

### 도펀트 선택 지침 (이온 반경 기준)
$$r_{dopant} < r_{Ni^{3+}}(0.56\,\text{Å}) \Rightarrow \text{클러스터링 경향 (예: Al}^{3+}\text{, }0.535\,\text{Å)}$$
$$r_{dopant} > r_{Ni^{3+}} \Rightarrow \text{암염 구조 형성 촉진 (예: Ti}^{4+}\text{, Zr}^{4+}\text{, Nb}^{5+}\text{, W}^{6+})$$

## Examples
- Li[Ni₀.₉M₀.₁]O₂ (M = 복합 도펀트): 차세대 초고니켈 조성 연구의 주류
- NMA (Li[NiMnAl]O₂), NTMA (Li[NiTiMgAl]O₂): LNO 기반 단순 도핑 설계 후보

## References
- [[papers/7dc914d3-10.1038s4156001905130_________]] — 원본 논문
- Bianchini, M. et al. *Angew. Chem. Int. Ed.* **58**, 2–27 (2019) — LNO의 음극 활성 물질로서의 여정
