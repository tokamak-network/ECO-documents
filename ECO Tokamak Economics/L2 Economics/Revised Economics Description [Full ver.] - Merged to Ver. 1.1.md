Writer: Suhyeon (suhyeon@tokamak.network)

Date: 2025-03-07

The original whitepaper and the highlighted revised whitepaper are as follows:

[original.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/40d38a60-cd88-41a4-b31b-17d4a544d62c/original.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QVRGQSX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIASl%2FLlIzr9Yv9k8BoiFzbon%2BIllDGoyXEgH5XnWwHVDAiBsq6u6ElR2i2w81Opk4Ch63MMdQQaaOgQO8sx5k29Vjyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMQZRuu8RUh4myUOjHKtwDK%2FjOZX4vigIHYVylkMVovo7Ocw6e1WEjRnsVYtO3zoeWXLctGLe3zso4T0WNi2%2Beb%2FHPYpFKL6lhR%2Bd8esvb7H3%2F%2FkctQ79WQr9D5IoNdkIpX%2F9u9OGmu3JA%2F%2F41LMRz3ndeK1DKVHNYZzOcSusylqZ9cJcigim1QPPew%2BPi92QKteDl%2FIbEwLShzqjdX3frIbOBg6coC1VbCeNE2NOWyYYRJaIMLbiC0AB%2B8AwKrblHYzpodSAel4QeE4KuhWOhdE4HeBAzjeERrt%2FgeV0hVRTPzVOJomJYdmR8ytEvduR%2FotkhdTjQQrOWqzWa1GakOmKAPgSf1CISp7Af2wcqO9D%2BPeGP145kUVsBHM0X0p%2FwkNxQJUktVUTxotdhYdp6ltXceufHzmLTB8ygPyTOwTSAnhyEvnnkVU0D%2FEtQqnJUhArukMy9PnyPjhFFANXyt%2Bq95IY4MGQJ4Q3vtnWu9cnH4NSkNJnvQfeLp%2B4mMtG0ghyt5eD%2BNDee52ZwD4E2o8vU5eKxg6d6TdrCqYaHgtPZry4T0X1BOVKfXknB3%2FznXovUh9jNs%2FmREMVl%2Bgu35wvpEwcqAzyOpok%2FM%2BYKf2m4afnA%2BfK3crXihQAu5QIvLJnUVCSOLJ1U6CcwrZrbzAY6pgEVJM4Ckab5wNdr0hYqXfXxHbFZTlQbaFHBZPs1EluC%2BLQP5ED%2FbLu0q0Y%2FequAVBLJoNwYTWI1%2FVht0xmHwwdtM4hh7seyaKf6Xx3xvNTeyW0T2G8tLp6HLDjHVDE9snlliNhl%2BBX24Lx%2F6NUf9QEypp1bzO4Kr0joP8GsxlChHAwF3w1VS8Lc5Vzz3vTdiQOevhC0%2F8rs6qZXWKIm3ipTqw5SQbK1&X-Amz-Signature=c539533825acf23c4a04404f554eb3f9a3b7fe31f8cef877dc55df39ae2a123c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[revised.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/77905a7e-9485-40a6-b701-840b8d4bec03/revised.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QVRGQSX%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIASl%2FLlIzr9Yv9k8BoiFzbon%2BIllDGoyXEgH5XnWwHVDAiBsq6u6ElR2i2w81Opk4Ch63MMdQQaaOgQO8sx5k29Vjyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMQZRuu8RUh4myUOjHKtwDK%2FjOZX4vigIHYVylkMVovo7Ocw6e1WEjRnsVYtO3zoeWXLctGLe3zso4T0WNi2%2Beb%2FHPYpFKL6lhR%2Bd8esvb7H3%2F%2FkctQ79WQr9D5IoNdkIpX%2F9u9OGmu3JA%2F%2F41LMRz3ndeK1DKVHNYZzOcSusylqZ9cJcigim1QPPew%2BPi92QKteDl%2FIbEwLShzqjdX3frIbOBg6coC1VbCeNE2NOWyYYRJaIMLbiC0AB%2B8AwKrblHYzpodSAel4QeE4KuhWOhdE4HeBAzjeERrt%2FgeV0hVRTPzVOJomJYdmR8ytEvduR%2FotkhdTjQQrOWqzWa1GakOmKAPgSf1CISp7Af2wcqO9D%2BPeGP145kUVsBHM0X0p%2FwkNxQJUktVUTxotdhYdp6ltXceufHzmLTB8ygPyTOwTSAnhyEvnnkVU0D%2FEtQqnJUhArukMy9PnyPjhFFANXyt%2Bq95IY4MGQJ4Q3vtnWu9cnH4NSkNJnvQfeLp%2B4mMtG0ghyt5eD%2BNDee52ZwD4E2o8vU5eKxg6d6TdrCqYaHgtPZry4T0X1BOVKfXknB3%2FznXovUh9jNs%2FmREMVl%2Bgu35wvpEwcqAzyOpok%2FM%2BYKf2m4afnA%2BfK3crXihQAu5QIvLJnUVCSOLJ1U6CcwrZrbzAY6pgEVJM4Ckab5wNdr0hYqXfXxHbFZTlQbaFHBZPs1EluC%2BLQP5ED%2FbLu0q0Y%2FequAVBLJoNwYTWI1%2FVht0xmHwwdtM4hh7seyaKf6Xx3xvNTeyW0T2G8tLp6HLDjHVDE9snlliNhl%2BBX24Lx%2F6NUf9QEypp1bzO4Kr0joP8GsxlChHAwF3w1VS8Lc5Vzz3vTdiQOevhC0%2F8rs6qZXWKIm3ipTqw5SQbK1&X-Amz-Signature=1a4bcc007520e2d21643a10f75c9fdd6b6fb02d3681bdd2b7c16ec1039f5df5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Major Changes

- In general, removed ambiguous notations and ensured consistency
- Replaced the abbreviation "$Seig$" for seigniorage with $\Phi$ to make it more concise and visually distinct
- Removed the weight constant for STOS which is not used anymore
- The seigniorage weight constant for the DAO has been removed, as the DAO's seigniorage can be simply expressed as the total seigniorage minus the amounts allocated to staking and L2

## Notations for Supply

- $T$: Total TON supply
  - $T=T_{L1}+T_{L2}$
- $T_{L1}$: TON L1 Native Supply
  - TON existing or staked in L1, excluding the amount bridged to L2
- $T_{L2}$: TON L2 Bridged Liquidity
  - Previously, named $D$
  - TON L2 supply is only TON bridged to L2 from L1

## Notations for Staking & Seiniorage

- $S$: Total staking amount in L1
  - $S \subset T_{L1}$

## Notations for seigniorage and Its Distribution

- $\Phi$: Total seigniorage
  - $\Phi = \Phi_{L1} + \Phi_{L2} + \Phi_{DAO}$
- $T_{\Phi}$: Effective TON supply for seigniorage
  - The staked amount and the L2 amount mainly affects to the seigniorage distribution
  - $T_{\Phi} = S+T_{L2}$
- $\Phi_{L1}$: seigniorage for L1 staking Users
  - $\Phi_{L1} = W_S \cdot \frac{S}{T_\Phi}\Phi$ where $W_S \leq 1$
- $\Phi_{L2}$: seigniorage for L2 seqeuncers based on the TON amounts in L2
  - $\Phi_{L2} = W_{L2} \cdot \frac{T_{L2}}{T_\Phi} \Phi$ where $W_{L2} \leq 1$
- $\Phi_{DAO}$: seigniorage for Tokamak Network DAO
  - $\Phi_{DAO} = \Phi - \Phi_{L1} - \Phi_{L2} = \frac{T_\Phi-W_S \cdot S - W_{L2} \cdot T_{L2}}{T_\Phi} \cdot \Phi \geq 0$ 

## Notations for Multiple L2 Environment

- Let’s assume there’re mutliple rollups $1,2,...,k$
- Each rollups gets proportional seigniorage to the TON amount in their rollup
  - $\Phi_{L2,m} = \big( T_{L2,m} / \sum_{i} T_{L2,i} \big) \cdot \Phi_{L2}$ 

## References

- Tokamak Docs
[Link](https://github.com/tokamak-network/papers/blob/ae9bf27c631d3363bf03f492b3468c1f20b7e1b3/cryptoeconomics/tokamak-cryptoeconomics-en.md)

[https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-kr.md#3-%EA%B2%80%EC%A6%9D-%EA%B2%BD%EC%A0%9Cverification-economics)
- Research Posts
[https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup](https://www.paradigm.xyz/2021/01/almost-everything-you-need-to-know-about-optimistic-rollup)

[https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a](https://medium.com/l2beat/fraud-proof-wars-b0cb4d0f452a)

[https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html](https://specs.optimism.io/fault-proof/stage-one/fault-dispute-game.html)
- Research Papers
[https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf](https://github.com/OffchainLabs/bold/blob/main/docs/research-specs/Economics.pdf)

[https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3](https://link.springer.com/chapter/10.1007/978-3-031-48731-6_3)

[https://arxiv.org/pdf/2308.02880](https://arxiv.org/pdf/2308.02880)