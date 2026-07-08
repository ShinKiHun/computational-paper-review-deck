# Zhang et al. 2025 JACS 발표자 노트

## 00. Opening

- 한 문장으로 시작: 이 논문은 weak-binding M-N-C의 ORR anomaly를 adsorption site 문제로 다시 해석한다.
- 핵심 표현: "weak binding 자체가 답이 아니라, O*가 metal-atop에서 M-N bridge로 이동할 수 있다는 점이 답이다."

## 01. Problem

- 기존 volcano 직관에서는 Fe/Co처럼 moderate binding metal이 유리해야 한다.
- Figure 1에서 Ni/Cu/Zn 계열이 alkaline condition에서 예상보다 높은 activity를 보이는 점을 강조한다.
- 여기서 질문은 "descriptor 값이 틀렸나?"가 아니라 "descriptor가 가정한 geometry가 틀렸나?"이다.

## 02. Model Shift

- conventional view: O*가 metal atop site에 남는다고 가정한다.
- this paper: O*가 M-N bridge site로 이동할 수 있다고 본다.
- 이 변화는 adsorption energy 하나가 아니라 scaling, field response, solvation, kinetic barrier를 함께 바꾼다.

## 03. DFT Evidence

- Figure 2: atop/bridge adsorption을 비교하며 Ni/Cu에서 bridge O* 안정화 가능성을 제시한다.
- Figure 3: bridge O*와 atop O*의 electric-field/solvation response가 다름을 보여준다.
- 말할 포인트: site geometry가 electrochemical response까지 바꾼다.

## 04. Microkinetics

- Figure 4가 계산 파트의 핵심이다.
- HOO* -> O* bottleneck이 bridge pathway에서 다르게 작동하고, high-activity region이 weak-binding Ni/Cu 쪽으로 이동한다.
- 단순 adsorption energy plot이 아니라 pH-dependent activity prediction으로 설명한다.

## 05. Validation

- Figure 5는 molecular model catalyst와 pH-dependent ORR 실험 플랫폼이다.
- Figure 6은 onset potential, TOF, XAS/XPS, PDOS/COHP가 bridge-O* picture를 지지한다는 검증 스택이다.
- 말할 포인트: 계산, activity, spectroscopy가 같은 mechanism을 향한다는 convergence가 논문의 설득력이다.

## 06. Critical Read

- 강점: hidden metal-atop assumption을 건드리고, 계산-실험-분광을 하나의 mechanism으로 묶었다.
- 약점: Helmholtz capacitance, field mapping, static DFT approximation은 model-dependent하다.
- 토론 질문: explicit electrolyte/AIMD/MLIP sampling으로 bridge O* site switching을 직접 볼 수 있을까?

## 07. Take-home

- 마지막 메시지: weak-binding catalyst가 active한 이유는 ORR이 metal-atop O* pathway에 갇혀 있지 않기 때문이다.
- 후속 토론: bridge-O*는 새로운 active-site model인가, 아니면 기존 descriptor가 놓친 geometry correction인가?
