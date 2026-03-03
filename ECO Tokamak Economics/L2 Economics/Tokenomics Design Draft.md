Author: Suhyeon

Date: October 2025

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/28371f99-c0b5-4ff7-92d2-9d6dcf69baa0/basic_tokenomics_model.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTCAPXQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfvUvDPG268ProrAPA%2BffF8sbZQzR2yeQCeDAKTQY4pAIhALpMuHfcUMU5OpuaswQWWYGtcnUVaW136zS5BXmMaHNXKv8DCHoQABoMNjM3NDIzMTgzODA1IgzfrS9pjYwtkqe%2BCcsq3AP6bilxWtfGEoy0LzyBEIdKMMEEnS%2BGI9HwcYHtDaKAcDsTTIB5f2bQOVngXk4fp9Zx1RTjVFzmkYN7M4AgYhmSzYQGwHP5Qwpr3NaOA%2By0WtnHB271v9o%2B%2BtGPXB30JFEIU4fBxjiAgfe3iFR1a2WazgitdMhVyLZ9D6xfzzb6DI%2FE6jeUQYfNMNKX%2BfguuPxaGEPneoeve84DPTV9vKmpTNpoKAuNuLGyu6RU%2BJ18%2Ft06BjWinSL%2FXMv%2FXQaZRpUeS5aT%2BcPe%2BLscJt6G6gSWEjjiKJFRS8qsF2FgUnhC0VdtwyZa%2FNjcUj4ZUBcXjV%2FZF6Qpw0t1l7aq7Fgz%2BUSjVnsOQh5hFnOxLVUiPqleYh4KKDgE63rQjQJGymPZ5bkIj5%2BhgdhzqBadGhWRnjvBGfsjoY0P22GXNaYvm%2Fl0XoYR1Inlt5oKEf%2Fd4yY9YDQRSBhzvuMIg%2B%2B5qm2BCCfLrEgp6jRwUdK%2BcqTB0JuMUnu4Prk366dRwE3KwyVUj8A3%2BZXaN5L7G0U3tgQmIGmKThlD2zKTAEGZ54L9xm53bxjfnptXPqa43bjEDK5cNXNnxLd94bX2p18%2BWnHpN8NAucn7IZbUqRtI9qd6wnUCqNVhDeaeZPW6Sr4USTCEmdvMBjqkAXgOTSEjCkUOae62ztfETDyTkJtZO2B1%2Bd1UucGd7sgZm0AoEe3NSf8NyhAnMARpdNIWGlkiHCeTYLwnqLA5wa2Vqm8esat%2F1jbBcRahkKlvsSzfa3dQJ9WcNIFPQHORLo9vLa2M7ATVmbQ%2B7%2BYAxI63BZtwQd4nYL7Rp46f3IZzk2ImQ%2FGxAln76WDfloE9eTX0raCrFND5O2D6GPKzNuQzg7tN&X-Amz-Signature=ec91591edbcff244ccc16f8a50e727a75d96ae149e41c4212e366600acde9055&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Design Goals

- Staking rewards are distributed in proportion to each L2’s **measured performance**.
- As performance increases, the **reward per unit of performance** decreases.
- RAT (Randomized Attention Test) validators are rewarded **proportional to L2 performance**.
- When aggregate L2 performance is low, the **effective** total seigniorage distributed decreases.

## Tokenomics Rule

1. **(Fixed  Annual Seigniorage)** The **total annual seigniorage** is fixed.
1. **(Fixed Seigniroage to DAO)** Any **undistributed** seigniorage to L2 is allocated to the DAO (treasury and potential burning).
  - Under Rule 1, this indirectly controls the **effective** supply actually released.
1. **(Bridged TON as Performance)** L2 performance is measured by **the L2’s bridged TON amount **(deposit), which is **independent** of the operator’s L1 TON staking.
  1. Bridged TON: Amount of TON bridged to the L2. 
  1. Staked TON: Amount of TON staked by the L2 operator on the L1 TON staking **contract**.
1. **(Minimum Staking Guardrail)** Seigniorage allocation is not weighted by staking size. However, an L2 must maintain a minimum **Staked TON** relative to its **Bridged TON** to be eligible for seigniorage in a given period.
  1. **Rationale:** Enforces a baseline of economic security and discourages under-secured TVL growth without turning staking into a reward weight.
  1. **Example:** For L2 *i*, let **Bᵢ** be Bridged TON and **Sᵢ** be Staked TON, both measured over the same window. Eligibility requires **Sᵢ ≥ θ · Bᵢ**, with default **θ as a minimum staking ratio parameter**.

## Concerns

- Potential issue: **TON TVL should be evaluated periodically using an averaged metric** for the period (e.g., Time-Weighted Average), not a single snapshot.
- We need to divide a year to multiple periods to evaluate L2 performance and distribute seigniorage.

## Formalization

**We use Hyperbolic Saturation Function (Refer alternative in **[**Appendix 1**](/286d96a400a38012a496d43965b05e8f#295d96a400a380d0973cf81a97359f43)**) for L2 distribution:**

$$
 y (x) = L \cdot \frac{x}{k + x}
$$

- $L$** (Limit): **The maximum upper bound that the function will approach
- $k$** (Steepness Factor)**: A coefficient determining how quickly the curve rises. A smaller $k$ makes early growth fater and reduces marginal reward per unit more quickly.

Memo: The $k$ values provides flexibility by making it easy to adjust the curve’s initial growth rate. This model is widely used for designing **Bonding Curves** and distributing staking rewards.

### Performance input with staking eligibility

- First, we define metrics of each rollup $i$
  - $B_i$: Bridged TON
  - $S_i$: Staked TON
  - $\theta \in (0,1]$: Minimum staking ratio parameter
- Seigniorage eliegibility indicator
$$
\mathbf{1}_i =
\begin{cases}
1, & S_i \ge \theta B_i \\
0, & \text{otherwise}
\end{cases}
$$
- Eligible deposit

$$
\tilde{B}_i = \mathbf{1}_i\, B_i

$$

### Aggregation and allocation

- Total performance

$$
x=\sum_i \tilde{B_i} = \sum_i 1_i B_i
$$

- Total seigniorage to L2s

$$
y(x) = L \cdot \frac{\sum_i \tilde{B_i}}{k+\sum_i \tilde{B_i}}
$$

- Validators and operatros split with ratio $\alpha$ and the number of validators, $n$

$$
v_i = \frac{\alpha}{n} \cdot y, \qquad o_i = (1-\alpha) y_i
$$

- DAO fixed share under the fixed annual issuance $A$ with the DAO distribution parameter $d$

$$
\mathrm{DAO}_{\mathrm{fixed}} \;=\; d \cdot A
$$

## Scenario Examples

In this section, we provide example scenarios. Especially, only sceanrio 1 is described with calculation details. The other scenarios are calculated in the same way.

Also, you can simulate easily in [this Google canvas app](https://gemini.google.com/share/68ea8b964a49).

### Scenario Overview

| Scenario | DAO Distribution | L2 Reward Function | Total Performance (Deposit) | Total L2 Seigniorage |
| --- | --- | --- | --- | --- |
| 1 | 1 M (10%) | $y(x)=\dfrac{90\text{M}\cdot x}{1\text{M}+x}$ | 30k TON | ≈ 270k |
| 2 | 2 M (20%) | $y(x)=\dfrac{8\text{M}\cdot x}{0.5\text{M}+x}$ | 90k TON | ≈ 1.34 M |
| 3 | 1.5 M (15%) | $y(x)=\dfrac{8.5\text{M}\cdot x}{0.8\text{M}+x}$ | 450k TON | ≈ 3.99 M |

### Scenario 1 (with calculation details)

Parameter Setting

- Annual Issuance: 10 M (rationale: [whitepaper](https://tokamak-network.github.io/papers/tokamak-cryptoeconomics-en.pdf))
- Annual distribution to DAO: 1 M (10 %)
- Max annual distribution to L2: 9 M (90 %)
- Validator / Operator reward distribution ratio: 20 %
- L2 reward function: $y(x;deposit)= \frac{90 M \cdot x}{1 M+x}$

Rollups

- Rollup 1 (R1):
  - Staking: 5k TON
  - Deposit: 10k TON
- Rollup 2 (R2):
  - Staking: 1k TON
  - Deposit: 20k TON

Result — Seigniorage Allocation:

- Total performance: 10k+20k = 30k
- Total seigniorage: 90M$\cdot$30k/(1M+30k) = 269,192 ≈ 270k
- Reward to Validators: 54 k
- Reward to R1: 72 k
- Reward to R2: 142 k

### Scenario 2 (only with results)

Parameter Setting

- Annual Issuance: 10 M (fixed)
- Annual distribution to DAO: 2 M (20 %)
- Max annual distribution to L2: 8 M (80 %)
- Validator / Operator reward distribution ratio: 25 %
- L2 reward function: $y(x;deposit)= \frac{8\text{ M} \cdot x}{0.5\text{ M}+x}$

Rollups

- Rollup 1 (R1):
  - Staking: 8k TON
  - Deposit: 25k TON
- Rollup 2 (R2):
  - Staking: 3k TON
  - Deposit: 50k TON
- Rollup 3 (R3):
  - Staking: 2k TON
  - Deposit: 15k TON

Result — Seigniorage Allocation:

- Total performance: 25k+50k+15k = 90k
- Total seigniorage: ≈ 1.34 M
- Reward to Validators: ≈ 335 k
- Reward to R1 (operator share): ≈ 286 k
- Reward to R2 (operator share): ≈ 545 k
- Reward to R3 (operator share): ≈ 175 k

### Scenario 3 (results only, table)

**Parameter Setting**

| 항목 | 값 |
| --- | --- |
| Annual Issuance | 10 M |
| Annual distribution to DAO | 1.5 M (15%) |
| Max annual distribution to L2 | 8.5 M (85%) |
| Validator / Operator reward ratio | 30% / 70% |
| L2 reward function | $y(x;deposit)=\dfrac{8.5\text{ M}\cdot x}{0.8\text{ M}+x}$ |
| R1 Staking / Deposit | 120k TON / **200k TON** |
| R2 Staking / Deposit | 60k TON / **150k TON** |
| R3 Staking / Deposit | 30k TON / **100k TON** |

**Result — Seigniorage Allocation**

| 항목 | 값 |
| --- | --- |
| Total performance | 200k + 150k + 100k = **450k** |
| Total seigniorage | **≈ 3.99 M** |
| Reward to Validators (총) | **≈ 1.20 M** |
| Operator reward to R1 | **≈ 1.19 M** |
| Operator reward to R2 | **≈ 0.94 M** |
| Operator reward to R3 | **≈ 0.66 M** |

## Appendix 1. Reward Function Comparison

| Aspect | Hyperbolic saturation | Exponential saturation |
| --- | --- | --- |
| Definition | $f(x)=L\cdot \dfrac{x}{k+x}$ | $g(x)=L\cdot\big(1-e^{-a x}\big)$ |
| Main knob | $k$ is the *half-saturation point*: $f(k)=L/2$ | $a$ is the rate. Half-saturation at $x_{1/2}=\ln 2/a$ |
| Initial slope | $f'(0)=L/k$ | $g'(0)=L a$ |
| Shape intuition | Rational curve, climbs fast then slows smoothly as $x\to\infty$ | Closer to a classic “discounting” curve, reaches near-$L$ more aggressively for large $a$ |
| Numerical profile | Only mul/div. Friendly to fixed-point maths and gas | Needs `exp` (or approximation). More gas and care with underflow for large $a x$ |
| Parameter calibration | Choose $k=x_{1/2}$ directly | Choose $a=\ln 2 / x_{1/2}$ |
| When to prefer | You want the simplest safe saturating curve with intuitive half-point | You want a memoryless, smooth discount-like rise or need faster approach to $L$ |

![ Hyperbolic Saturation Fuction](images/19e2a642295c.png)

![Exponential Saturation Function](images/73377e3b645f.png)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ede9e4b0-d518-44e1-910c-2fa842e0de2a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROTCAPXQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfvUvDPG268ProrAPA%2BffF8sbZQzR2yeQCeDAKTQY4pAIhALpMuHfcUMU5OpuaswQWWYGtcnUVaW136zS5BXmMaHNXKv8DCHoQABoMNjM3NDIzMTgzODA1IgzfrS9pjYwtkqe%2BCcsq3AP6bilxWtfGEoy0LzyBEIdKMMEEnS%2BGI9HwcYHtDaKAcDsTTIB5f2bQOVngXk4fp9Zx1RTjVFzmkYN7M4AgYhmSzYQGwHP5Qwpr3NaOA%2By0WtnHB271v9o%2B%2BtGPXB30JFEIU4fBxjiAgfe3iFR1a2WazgitdMhVyLZ9D6xfzzb6DI%2FE6jeUQYfNMNKX%2BfguuPxaGEPneoeve84DPTV9vKmpTNpoKAuNuLGyu6RU%2BJ18%2Ft06BjWinSL%2FXMv%2FXQaZRpUeS5aT%2BcPe%2BLscJt6G6gSWEjjiKJFRS8qsF2FgUnhC0VdtwyZa%2FNjcUj4ZUBcXjV%2FZF6Qpw0t1l7aq7Fgz%2BUSjVnsOQh5hFnOxLVUiPqleYh4KKDgE63rQjQJGymPZ5bkIj5%2BhgdhzqBadGhWRnjvBGfsjoY0P22GXNaYvm%2Fl0XoYR1Inlt5oKEf%2Fd4yY9YDQRSBhzvuMIg%2B%2B5qm2BCCfLrEgp6jRwUdK%2BcqTB0JuMUnu4Prk366dRwE3KwyVUj8A3%2BZXaN5L7G0U3tgQmIGmKThlD2zKTAEGZ54L9xm53bxjfnptXPqa43bjEDK5cNXNnxLd94bX2p18%2BWnHpN8NAucn7IZbUqRtI9qd6wnUCqNVhDeaeZPW6Sr4USTCEmdvMBjqkAXgOTSEjCkUOae62ztfETDyTkJtZO2B1%2Bd1UucGd7sgZm0AoEe3NSf8NyhAnMARpdNIWGlkiHCeTYLwnqLA5wa2Vqm8esat%2F1jbBcRahkKlvsSzfa3dQJ9WcNIFPQHORLo9vLa2M7ATVmbQ%2B7%2BYAxI63BZtwQd4nYL7Rp46f3IZzk2ImQ%2FGxAln76WDfloE9eTX0raCrFND5O2D6GPKzNuQzg7tN&X-Amz-Signature=15a58148798cf821824813950c526f880cb4d2f87fcb91d67f5b46c48253a0e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Numerical analysis code: 
[reward funciton analysis.py](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d4d992fb-7e23-496f-a4d9-fd6ff1291a2c/reward_funciton_analysis.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGWCVMND%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T104950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICifYs1OHXbhwf3%2BlJu1IH1x68D%2BzmQaGVgEUasMscG3AiARDs8NlHl9GihPxy40XNe%2Bq0mTTkM2aRuji6PcIsrcxyr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMvdWvtNHNP6SVGUmIKtwDqXSSjRbUjGSnpDoOlIEEy674tiEn6ObHlWgMn6H8rqOsNQ2YdzjVk91ylhF174Xac1vwiqnWBlfKjv9M4LlA%2BQM%2F56TMwyhu%2BxtsJJh28xEXqBa8Xh6F1Kmczd07C9bKB9FuBltIsJw0EXqhZSaWo36k9jjNo%2BIPt03mvQO8ircKzlHAkgLdcC9Fuhi400jCOfy7ndVOCNTTwbYtpbqjVbwINpFXlUXQYf9O10BRqKKyKjucx5e5Yfo3QMynG89V1vwOdGBrKkeSIRKBtiG7reODplvN6RAAy2HXbSjZeFVFETtYMiQuOqBcalR9UOtoUEYiiYQcYeygn1lVxPecD5spqcQF7LQRlKOvsJZUVmmQ0506ZnKvITJOh9luOodXMeEIcio7w0%2FfsJuxDanTmQL1OPUqZg0%2BynJcLjSLzo%2BXJbMaVSN4LvvV1Th9%2Bkm0tQN9QWDMIEklxT%2BBe2bc%2BHF4KFoMRHQ9Uku38UMFHfI5sRyRgppvrlUpq5H%2BeYdRf9Txsy3kzpxziUmOryvW7q%2FcvLksAZP8m5okeMmTD6BOZdR2sEPhjgAmPOl7Q3caO0A4f0wBRHwJ9v5Ny3ifdxwFF9Tm5NeIJmDSOb0CaSt0Jano7vmVtJ9oE9gwnszbzAY6pgFVvKiMnWa5XaJnHkdREHdEwoVJ2AoChH2q1u5SMNT264DohbLPqiUkPSz%2BrayPUkWO6Zqa7JYu7kVLR1rP9oqnA1OFTNMP8z2genzmp65YVO0xc7aItdil8Ernn8I5flwOqhpb8xSY26EIhNjMoih7NFIFoQk9xQALV7OMO6vd%2BN7ONS1Oibk5T%2FQtS9Y%2ByP2u7lEwgoPPusUp%2FnRzbYK2C6o1qQsM&X-Amz-Signature=5c2c99da4b1347203f2458735e8c0807743ac9e0ef839b4374431db73e69a6d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)