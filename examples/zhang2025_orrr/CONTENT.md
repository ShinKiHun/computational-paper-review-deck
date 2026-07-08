# CONTENT.md - Zhang et al. 2025 ORR Paper Review

## Paper Metadata

### Paper Title

Why Do Weak-Binding M-N-C Single-Atom Catalysts Possess Anomalously High Oxygen Reduction Activity?

### Authors / Journal / Year

Zhang et al., Journal of the American Chemical Society, 2025

### Field

DFT electrocatalysis, ORR microkinetics, M-N-C single-atom catalysts

### System

M-N-C and molecular M-N4 model catalysts for oxygen reduction reaction

### Main Methods

DFT adsorption energetics, electric-field response, solvation correction, pH-dependent microkinetic volcano modeling, XAS/XPS/ORR validation

### Validation

RRDE ORR activity, onset potential, TOF trend, N K-edge XAS, N 1s XPS, PDOS/COHP analysis

### One-sentence Korean Summary

이 논문은 weak-binding M-N-C catalyst의 ORR activity anomaly가 금속 atop site의 O*만으로는 설명되지 않으며, O*가 M-N bridge site로 이동할 때 scaling과 pH-dependent kinetics가 달라진다고 주장한다.

### Core Thesis

Weak-binding activity is not explained by weaker metal binding alone; it comes from site switching from metal-atop O* to M-N bridge O*.

---

## Slide 1 - Title / Thesis

### Message

Weak-binding catalyst가 active한 이유는 ORR이 metal-atop O* pathway에 갇혀 있지 않기 때문이다.

### Figure Filename

assets/zhang2025_fig2_bridge_scaling.png

### What To Emphasize

발표의 핵심 thesis를 먼저 말한다: active site를 metal center 하나가 아니라 M-N ensemble로 봐야 한다.

### Optional Presenter Note

처음부터 "Ni/Cu가 사실 강하게 bind한다"가 아니라 "O* adsorption geometry가 바뀐다"는 점을 구분한다.

---

## Slide 2 - Scientific Problem

### Message

Classical metal-atop volcano는 Ni/Cu/Zn 계열의 alkaline ORR activity를 설명하지 못한다.

### Figure Filename

assets/zhang2025_fig1_problem.png

### What To Emphasize

기존 descriptor와 실험 activity trend 사이의 mismatch가 이 논문의 출발점이다.

### Optional Presenter Note

질문은 descriptor 값 하나가 틀렸는지가 아니라, descriptor가 전제한 adsorption site가 맞는지이다.

---

## Slide 3 - Conventional Understanding

### Message

기존 모델은 O*가 metal atop site에 머문다고 가정한다.

### Figure Filename

assets/zhang2025_fig4_4e_focus.png

### What To Emphasize

Atop O* pathway만 쓰면 weak-binding metal은 HOO* -> O* step에서 불리하게 예측된다.

### Optional Presenter Note

Volcano는 좋은 언어지만 active geometry를 고정하면 mechanism을 놓칠 수 있다.

---

## Slide 4 - New Idea / Hypothesis

### Message

O*가 M-N bridge site로 이동하면 scaling relation 자체가 달라진다.

### Figure Filename

assets/zhang2025_fig2_bridge_scaling.png

### What To Emphasize

Ni/Cu 계열에서는 N ligand가 spectator가 아니라 adsorption ensemble의 일부가 된다.

### Optional Presenter Note

이 slide가 발표의 conceptual center다. Figure의 많은 panel을 다 설명하지 말고 bridge motif와 scaling 변화만 잡는다.

---

## Slide 5 - Computational Setup

### Message

논문의 계산 흐름은 adsorption geometry를 바꾸고, interface response와 microkinetics까지 연결하는 구조다.

### Figure Filename

assets/zhang2025_fig3_field_solvation.png

### What To Emphasize

DFT adsorption energy 하나가 아니라 electric field, solvation, pH-dependent kinetics가 함께 들어간다.

### Optional Presenter Note

Helmholtz capacitance, field mapping, solvation correction은 뒤의 limitation에서 다시 건드린다.

---

## Slide 6 - Main Result

### Message

Bridge-O* pathway는 high-activity region을 weak-binding metal 쪽으로 이동시킨다.

### Figure Filename

assets/zhang2025_fig4_volcano_clean.png

### What To Emphasize

Figure 4는 단순 adsorption plot이 아니라 pH-dependent activity prediction이다.

### Optional Presenter Note

Atop pathway와 bridge pathway의 volcano peak 위치가 어떻게 달라지는지 먼저 읽게 한다.

---

## Slide 7 - Mechanism / Interpretation

### Message

Site geometry는 field response와 solvation response까지 바꾸는 kinetic descriptor로 작동한다.

### Figure Filename

assets/zhang2025_fig3_field_solvation.png

### What To Emphasize

Atop O*와 bridge O*는 전기장/용매 안정화에 같은 방식으로 반응하지 않는다.

### Optional Presenter Note

이 slide에서는 "왜 pH-dependent volcano가 달라지는가"를 해석한다.

---

## Slide 8 - Validation / Benchmark

### Message

Activity trend와 spectroscopic N-O signature가 bridge-O* picture를 함께 지지한다.

### Figure Filename

assets/zhang2025_fig6_validation.png

### What To Emphasize

Onset potential, TOF, XAS/XPS, PDOS/COHP가 같은 mechanism을 향하는 validation stack이다.

### Optional Presenter Note

검증은 강하지만, 모든 interface dynamics가 직접 검증된 것은 아니라는 점을 남겨둔다.

---

## Slide 9 - Limitations / Assumptions

### Message

가장 약한 고리는 electrochemical interface와 finite-temperature site switching이다.

### Figure Filename

assets/zhang2025_fig5_experiment_model.png

### What To Emphasize

Static DFT, field/solvation model, model catalyst와 real SAC 사이의 gap을 토론한다.

### Optional Presenter Note

논문을 깎아내리는 slide가 아니라, 우리 계산과학 연구실에서 이어갈 수 있는 질문을 만드는 slide다.

---

## Slide 10 - Discussion / Take-home

### Message

Bridge-O*는 새로운 active-site model이면서, 기존 descriptor가 놓친 geometry correction이다.

### Figure Filename

assets/zhang2025_fig2_bridge_scaling.png

### What To Emphasize

후속 질문은 explicit electrolyte, AIMD, MLIP sampling으로 site switching을 직접 볼 수 있는가이다.

### Optional Presenter Note

마지막 질문: bridge-O*가 stationary DFT artifact인지, operando condition에서도 실제로 accessible한 state인지.
