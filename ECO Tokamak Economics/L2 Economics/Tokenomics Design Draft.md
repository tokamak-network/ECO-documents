Author: Suhyeon

Date: October 2025

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/28371f99-c0b5-4ff7-92d2-9d6dcf69baa0/basic_tokenomics_model.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQGX52UF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2nmo3ccn%2FJ8bt6fCZ964d%2BdJeUQIA7dykJMIjPe%2BbcAiAJ%2F5wxlitW65rSx9OH42h4kO%2FQ3HYESzF5FsZeKi81MCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRZZ9krMHVhFzemVpKtwDfvBbMgPDlHW5Wj4%2F5nLmiI8YjoNzw9tihEuUQsmz98r4rLEbpdj32uC%2B7VVrOwAvnelfFHSzqkHsUKS4H3Dokq8NGBQSd3gp5Wpv5PrIdN2ZGaVH9LwoVWh42vONKyLakfZaVXx3EZSs1huOlm8vSFmnJENrpzd1cwg3DXRnEgkbzXfckldAeabFrQ35%2FR7k%2FGepneR088BDM61M8F2cNJv%2BbUZyWUIRAM10jRY%2FprKCTbpkKsVJ194L%2F3hEf8QWb%2FE6PbMW7thERYjfBouq36LOljQu2U16gNpBBi4r94ELHtxkD3kMpxYFuJEW6XuSKVLhO0k283npIdg0oYt8Kme0PdzfR4gOyz%2F0KHqLX8BZRHQcD2hj4ymJj0VDm7tCXk%2F3fcx0VL5YqZ%2FLwq4D5954dTvOYTUF1UdVUsETwlUZxyd%2B%2BI4Q2hgQHIOCGI1cnYgPXSvAzdGkeM33199pQ69xsa9t8NhdF%2Bmmsonw9%2FuMiKn43EQkFfF5u9eoZ0jIFn20jji20S5%2FKNp7hx%2BZvobi90h7KN9MG82nKroK59szW%2BHs3CrTlQIc%2B%2BxYOP3ZHd0zpAIyFi2GMwWGbvjDxd2IN6IkwCFtxZw%2F7lii2B6jLOLYjueOOhnFfoAwtPHZzAY6pgHUjm7oQhSzynYHuVhJyRsYNvlKrQ0E3hk6xxJSOkg0Nd3m8%2FFjG7JmkbR62gKK0m%2B9wKZabm2tvcLEEF02FRnGpCXuzx8HI2KB4rWsLX9epFBmjMtsR93Hg2OjDykYJqF1TIeuk1Aa4pOK83NN0C5%2F2wbBiq1doC9k0UhhghqA7uyAM25ZtnLxoynncVK%2FO6pCiln0xxAKOiCrCL1SJ90dMXqnoDyh&X-Amz-Signature=65e84a0541b0227d22fa19398ab67e6825afb3b2a3340d8050456ff9d6e9da3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![ Hyperbolic Saturation Fuction](images/f5bfea5e6a38.png)

![Exponential Saturation Function](images/d4eba32c3466.png)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/ede9e4b0-d518-44e1-910c-2fa842e0de2a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQGX52UF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC2nmo3ccn%2FJ8bt6fCZ964d%2BdJeUQIA7dykJMIjPe%2BbcAiAJ%2F5wxlitW65rSx9OH42h4kO%2FQ3HYESzF5FsZeKi81MCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRZZ9krMHVhFzemVpKtwDfvBbMgPDlHW5Wj4%2F5nLmiI8YjoNzw9tihEuUQsmz98r4rLEbpdj32uC%2B7VVrOwAvnelfFHSzqkHsUKS4H3Dokq8NGBQSd3gp5Wpv5PrIdN2ZGaVH9LwoVWh42vONKyLakfZaVXx3EZSs1huOlm8vSFmnJENrpzd1cwg3DXRnEgkbzXfckldAeabFrQ35%2FR7k%2FGepneR088BDM61M8F2cNJv%2BbUZyWUIRAM10jRY%2FprKCTbpkKsVJ194L%2F3hEf8QWb%2FE6PbMW7thERYjfBouq36LOljQu2U16gNpBBi4r94ELHtxkD3kMpxYFuJEW6XuSKVLhO0k283npIdg0oYt8Kme0PdzfR4gOyz%2F0KHqLX8BZRHQcD2hj4ymJj0VDm7tCXk%2F3fcx0VL5YqZ%2FLwq4D5954dTvOYTUF1UdVUsETwlUZxyd%2B%2BI4Q2hgQHIOCGI1cnYgPXSvAzdGkeM33199pQ69xsa9t8NhdF%2Bmmsonw9%2FuMiKn43EQkFfF5u9eoZ0jIFn20jji20S5%2FKNp7hx%2BZvobi90h7KN9MG82nKroK59szW%2BHs3CrTlQIc%2B%2BxYOP3ZHd0zpAIyFi2GMwWGbvjDxd2IN6IkwCFtxZw%2F7lii2B6jLOLYjueOOhnFfoAwtPHZzAY6pgHUjm7oQhSzynYHuVhJyRsYNvlKrQ0E3hk6xxJSOkg0Nd3m8%2FFjG7JmkbR62gKK0m%2B9wKZabm2tvcLEEF02FRnGpCXuzx8HI2KB4rWsLX9epFBmjMtsR93Hg2OjDykYJqF1TIeuk1Aa4pOK83NN0C5%2F2wbBiq1doC9k0UhhghqA7uyAM25ZtnLxoynncVK%2FO6pCiln0xxAKOiCrCL1SJ90dMXqnoDyh&X-Amz-Signature=5d24a3a59528cf0712f87ebee2606e2db6348b1372ab4fd9d8d995526a760b3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- Numerical analysis code: 
[reward funciton analysis.py](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d4d992fb-7e23-496f-a4d9-fd6ff1291a2c/reward_funciton_analysis.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQC24I3P%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T061531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIClExtrlQ0VUbWY2Us899plKl6QhrYFYLYtFsc3iMRG6AiAlyOy7RQzHUZ8IRCOhfomYOHk2J9nCstDv6gp7u40z%2Fir%2FAwh3EAAaDDYzNzQyMzE4MzgwNSIMzapFHBCLY%2BuQWDsYKtwDD5udrXs61b59%2BFcsCPNunqtDpSgn89By4HQc5kiYhNmP2v%2B6b12VGTq62baZ59UxRpvX1YBt4DCyRP1J5tutvG8H8ciO54uFdttWKZFQxtRFXwYSnB6J9OB0svYCEBFSWGzAl3tSYbsexKHXnEzniHgo%2FRwZm3q7J%2BUogVgmnTBgXGGX7vrPOElrzs%2Fp86t4gyEQuRfdMtn62nqcMtmrmbyVgdabuGtLI5L7KJRB%2FHVvOxBAD6Lw8jjlJlLPNfGJEkdL5c3KO5vDzus1GaWI%2FjjYc%2BHYIlemlYEQMTYDlExs%2F9zzMAmrGgx5ddiCw93gPzsVobXc2qaSmSG7Rk9C0N4FP6%2B4E1t4JfIH99toeeWbf%2FuOSM5TFbI82GN6qCjaLdAnpv391R7FFmd2Dk9H8gdT5QGhpQGNmpcirxU%2Fq9gvR2rfjI4K7D0l2dRq2hU2R5Le5JT08tBUizRoVTK2gwPBh%2F7%2Fm3VWWKhbUKDiM2SRUYqmG13lQLVW1bbugSPGZHnuWGPQCxPUqRP6w3Z4GLFryZzogZumcLs6DJsubLGCvbJkC%2B8VfQapPQM4eRRNnT4PLTD6pQyjxIpM5gGG3JFsWxP6l%2FX6t%2Fm9SnL7%2BSWpBhzq0ayYvGASrpYwi8TazAY6pgGBbGWwYchEJ7JFG4xp8Fs6GbwXFnDhypEPDdjBX5O1MruX1H05YigFgK6CZFNDo%2FBEuXNbOyCMxrjVtd5XKnXwtWfTHO%2B%2F20iRh9b%2Fg%2BpBjA6Lv0Yoxh2N6CNwyQ7tn%2FaG8cPLK%2Be1aD53%2FoB3uC4zJ0k3ztijsjz9S7VT4t8NkSoEzlp2HfaiObAbdsZy6k1Np8iBs%2F0LGqR%2BnzsfxRM0d%2FvRpNfA&X-Amz-Signature=f7b8d57a2b2a761f9dd671d2a33627e2f283a61aaf8c36f93fad54d78be2e289&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)