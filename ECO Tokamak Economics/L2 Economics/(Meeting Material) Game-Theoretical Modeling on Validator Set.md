## **1. 기본 변수**

- $G$: 공격 성공 시 얻는 이득
- $B_{\text{total}}$: 공격자가 밸리데이터들에게 지급하는 총 뇌물(슬래싱 보상 제외)
- $S_{\text{exposed}}$: 공격 탐지 시 손실이 적용되는 스테이크 총합
- $d$: 공격이 탐지되어 제재(슬래싱 등)가 발생할 확률 ($0 ≤ d ≤ 1$)

## **2. 공격자의 기대효용**

공격이 탐지되지 않으면 $ G - B_{\text{total}}$의 이익을 얻고, 탐지되면 $S_{\text{exposed}}$만큼 손실이 발생하므로:

$\mathbb{E}[U_A] = (1-d)(G - B_{\text{total}}) + d(G - B_{\text{total}} - S_{\text{exposed}})$

정리하면:

$\mathbb{E}[U_A] = G - B_{\text{total}} - dS_{\text{exposed}}$

즉, 공격자가 감수해야 하는 최소비용(기대비용)은 탐지확률 및 슬래싱 보상에 비례:

$\boxed{C_{\text{attack}} = dS_{\text{exposed}}}$

### **1) Model M (완전 분리형, weakest-link)**

- 공격자는 **가장 약한 롤업 1개**만 노려도 이득을 실현 가능.

$\qquad
C_{\text{attack}}^{(M)} \;=\; d\;\min_{i} S_i$

### **2) Model S (Shard Validator Set + 공유 스테이킹, 크로스 슬래싱)**

- 슬래싱이 공유 풀 전체에 파급. 탐지되면 공유 풀 전체가 노출되므로:
$\qquad
C_{\text{attack}}^{(S)} \;=\; d\sum_i w_i S_i
$
- 공유 스테이킹이 반드시 동반되어야 하는 이유: 다른 롤업의 트랜잭션을 공유할 수 있더라도 공유 스테이킹/크로스 슬래싱이 없을 경우 다른 풀의 트랜잭션을 검증해야 할 경제적 유인이 없음.
- 공유 스테이킹, 크로스 슬래싱의 문제점
  - ~~Risk Propagation & Economic Misalignment: 자신의 잘못이 아니더라도 다른 밸리데이터의 잘못에 의해 슬래싱될 위험이 있음 → 위험의 전가 및 참여 동기 저하 유발.~~
  - ~~Difficulty in Contract Management: 밸리데이터가 밸리데이터 셋에 추가될 때 마다 해당 밸리데이터를 포함시키는 새로운 컨트랙트 체결 필요 → 컨트렉트 관리의 어려움.~~

### **3) RAT + Shared Validator Set (공유 스테이킹 없음)**

- 다른 롤업에 대한 검증의 충실도 역시 RAT에 의해 강제되므로:
$C_{\text{attack}}^\text{(RAT+SV)} \;=\; d\sum_{i} S_i$
- 장점
  - RAT rate가 충분히 높을 경우($p > \tau$), d가 1에 수렴한다고 가정.
    - 일반적으로 $d_{RAT} \geq d_S \geq d_M$ → 즉, $C_{\text{attack}}^\text{(RAT+SV)} \geq C_{\text{attack}}^{(S)} \geq C_{\text{attack}}^{(M)}$ 성립.
  - ~~Economic Misalignment 없이 Risk Isolation 가능: 오로지 밸리데이터 자신의 잘못으로만 슬래싱 발생~~
  - ~~개별 컨트렉트를 통한 관리 가능 → 컨트렉트 관리의 이점~~