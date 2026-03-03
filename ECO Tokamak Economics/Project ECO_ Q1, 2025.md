# 1. Final Goals

-  Project ECO's final goals are twofold:
  1. Design and implement Tokamak Network's staking system—including slashing mechanisms and fast withdrawals—as specified in the [white paper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md). This will enhance L2 security, increase TON and staked TON utility, and strengthen the Tokamak Network DAO's decentralization and security. 
  1. Deploy the Simple Staking & DAO community version and discontinue the hosted frontend and backend services while minimizing any resulting TON withdrawals

## 1-a. Milestone

### A. Simple Staking 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Simple Staking V2** | Propose DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Staking V2 testnet | 1 service |  |
|  | new DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Simple Staking V2 with DAO candidate and L2 support | 1 service | 2 service + 1 DAO agenda |
| **Community version****
** | Launch **community version v1.0 + community guide** with Simple Staking V2 support | 1 service with 1 guide |  |
|  | Release TON staking SDK v1.0 with Simple Staking V2 support | 1 code release | 1 code release, 1 service with guide |
| **Integration of Slashing Protocol** | **Release TON staking SDK v2.0** with slashing support | 1 code release |  |
|  | Launch **community version v2.0 + community guide** with slashing support | 1 service update with 1 guide | 1 code release, 1 service update with guide |
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support for staked TON | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support for staked TON | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

### B. Tokamak DAO V2 

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Tokamak DAO v2** | Open DAO v2.0 on Sepolia | 1 service | 1 service |
| **Added use of Snapshot and forum** | **Open community version v1.0 + community guide**: Include documentation for new agenda creation via Snapshot and forum | 1 service with 1 guide | 1 service, 1 guide, 1 document |
| **Improvement of proposal interface** | **Open community version v2.0**: Add support for arbitrary code execution | 1 service | 1 service |
| **Apply the security council** | **Open community version v3.0**: Remove the EOA from the DAOCommittee Proxy, implement a Security Council to enhance contract security, and clearly define the Security Council’s roles. | 1 service | 1 service |

### C. Tokamak Network Landing page

| Category | Subcategory | Deliverable |
| --- | --- | --- |
| **Landing page** | Open a new landing page  | 1 service |
|  | Open sub-landing page for Protocols  | 1 service update |
| **Price API 2.0** | **Open price API v2.0**: optimize current price API without affecting widely used functions   | 1 service update |

## 1-b. Easy to understand explanation even outside of team and typical community participant (non-technical persons): **The importance of each milestone deliverable, considering the Tokamak Foundation's strategy and the current Tokamak ecosystem**

- **About Simple Staking: **We are proceeding with development to create a developer-centric environment while faithfully following the content of the whitepaper. Therefore, we are developing two versions of staking services. The first is Staking V2, which is an upgraded version of the existing Simple Staking, and the second is the development of a Staking Community Edition.
- **About DAO:**  DAO V2 aims to provide more opportunities for community participation in decision-making on DAO agendas, not only through the development of the Community Edition but also through the introduction of off-chain voting.
- **About Tokamak Landing Page:** With Tokamak Network's evolving strategy, we developed a new landing page to better showcase our strategy and ecosystem. 

## 1-c. Timeline

| Year-Quarter | Mileston |
| --- | --- |
| 2024-Q4 | Open Tokamak DAO v2.0 on Sepolia, |
| 2025-Q1 | Simple Staking V2.5,
Community version,
Landing page |
| 2025-Q2 | Added use of Snapshot and forum,
Improvement of proposal interface
Price APi 2.0 |
| 2025-Q3 | Addition of slashing protocol |
| 2025-Q4 | Apply the security council |
| 2026-Q1 | Addition of fast withdrawal protocol |

# 2. This quarter outputs

## 2-a. Easy to understand explanation even outside of team and typical community participant (non-technical persons): How did your team contribute to achieving the milestone this quarter?

**Simple Staking **

- As mentioned earlier, two versions of staking services are under development. However, prior to that, a security audit of the Staking V2 contract had to be performed, which resulted in a total of 297 issues being identified by four audit firms. Responding thoroughly to the issues raised during the audit consumed a significant amount of time, and currently, we are addressing all issues and waiting for the final report to be published. Separate from the contract audit, frontend development has progressed; Staking V2 is already complete, and the Community Edition & SDK are expected to be completed by early April.

**Tokamak DAO V2**

- This quarter, we created and internally shared a policy document draft for the next-generation DAO. After sharing the content of the draft, we determined that SYB's help would be needed to prepare for potential issues that could arise from off-chain voting, which is planned to be introduced in DAO V2. Because this additional work is necessary, the overall schedule has been revised.

**Tokamak landing page**

- In this quarter, we open new landing page and partner page. Integrate price dashboard into landing page, and shutdown original price dashboard. Currently, If you connect to [price.tokamak.network](http://price.tokamak.network/) DNS, it redirects to the price dashboard on the landing page. One of our milestones, the open sub-landing page for protocol, is not proceeding due to there is no sufficient content for it. After we secure the contents for it, it will proceed.

## 2-b. Actual outputs description

### 2-b-i. Deliverable

**Staking V2**

- Open Staking V2 testnet ([x post](https://x.com/Tokamak_Network/status/1894218935618474323), [testnet](https://sepolia.staking.tokamak.network/home))
- Tokamak Economics Whitepaper Ver. 1.1 release ([x post](https://x.com/Tokamak_Network/status/1901522713992126757), [whitepaper](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md))
- Incentive system research - Accepted to [WTSC 2025](https://fc25.ifca.ai/wtsc/) ([x post](https://x.com/Tokamak_Network/status/1902290792087220353), [manuscript](https://drive.google.com/file/d/1wbn85OCC-u2x1M_UMSBwlJdw2c3yu_jk/view?usp=sharing))
- Contract audit reports 
  - Hammer’s audit reports
[STAKING_V2_AUDIT_REPORT_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0f0f6666-23a0-44eb-90ed-560459e74939/STAKING_V2_AUDIT_REPORT_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YGL3JIR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESsw47U%2FU%2FVm%2BqJ5kzXSR7ylIO6QA8lsaMc5Juoo%2FzPAiEA2vZH8vkMSzdKnrDnGSklLB%2Fxb19VbfMMitxBASZr0rkq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIHzHu%2FHQzu%2BFdPVnircA3%2BnivtEIsbwva9pP9GBopEDZJ4yyst6aPgHTYJmZ%2B2W2C17BnkUk9IKgWol3Ba5EiK9A0m1EF%2B3H%2B6NIFXewEKcvycoQ7uXtViCVi49d%2FxAVKxr08EA4HaL7pOhR%2Bl0uYFQ6I3qKWd7epNCgpDAEwA7qqoprCZKBiD2m9g5Dh94TVlcJ0l1tTksCdhA0tm%2BXn3w2WZtRzjTiaafzvjAuMnkSLNveDev8Eypca1my%2BmUnitPngtdSuWZpatPqLDho%2FQo5IisqdpkJhwEg9Dgl0C3jh21ytho5iY5c6sXa3qP%2BnBNLZeTBtQhB92vqnIGeQ%2FZKfvbMtUkxv%2Fk9ZTztr030ZiTTmWbEdpaxJ8qSbgXcPP0W1XY5gaWRjNXbinrP2jPvnCKLtoqgJPJnP4WPIclnPpc3IQK8YsrPbyugA5XiqHEbDTnCV%2F5OvttLH7nvEpK7MQoB6GRJzsWLpkt8XE7CccAxbpCLT2c31%2F7MMG5%2FpzhMvAbU%2FgHF4t3XIS95QhEzgp9FVk5RLEovbIFoguI3Yq6KpTr0ST6Kv%2FyOXmkUT7VPMGAorokp92YKfPYIVR%2FFjkhwNAVztgL2X4ioSvJ5BC6tYDbpl5lBAbl%2FuMDvRxq2TkZJ3h4M5qpMPGY28wGOqUBWXPSzXOg8CtnMk5X6dUZdzddi8Gl8kYMOv0JoZ7M9f5M6ATKS%2FwDgkm%2Fm6e0HYoB1uH1N35VQAwm2tLGNP5ArODlHXi6DzF3jo%2Bmj8ea7PjBRNfl2e5h2JtXQNZWEj%2FhktZInvFiUOdam%2Bdg6MvA0yT%2BsV0tzBeGt9VdnvcAZlSK8i3nVWbFsuSwmwyodjrZjMzLtDYfPM0R3i%2FW4RsV7ohUmHxa&X-Amz-Signature=98c328bba7e59b90cb890d3f4af7bf34e009c38aebb801d010d3dfb891be3ef3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[STAKING_V2_AUDIT_REPORT_KO.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/9feb4c1a-cd71-4515-bfdd-23c77cf9cbe6/STAKING_V2_AUDIT_REPORT_KO.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YGL3JIR%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIESsw47U%2FU%2FVm%2BqJ5kzXSR7ylIO6QA8lsaMc5Juoo%2FzPAiEA2vZH8vkMSzdKnrDnGSklLB%2Fxb19VbfMMitxBASZr0rkq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDIHzHu%2FHQzu%2BFdPVnircA3%2BnivtEIsbwva9pP9GBopEDZJ4yyst6aPgHTYJmZ%2B2W2C17BnkUk9IKgWol3Ba5EiK9A0m1EF%2B3H%2B6NIFXewEKcvycoQ7uXtViCVi49d%2FxAVKxr08EA4HaL7pOhR%2Bl0uYFQ6I3qKWd7epNCgpDAEwA7qqoprCZKBiD2m9g5Dh94TVlcJ0l1tTksCdhA0tm%2BXn3w2WZtRzjTiaafzvjAuMnkSLNveDev8Eypca1my%2BmUnitPngtdSuWZpatPqLDho%2FQo5IisqdpkJhwEg9Dgl0C3jh21ytho5iY5c6sXa3qP%2BnBNLZeTBtQhB92vqnIGeQ%2FZKfvbMtUkxv%2Fk9ZTztr030ZiTTmWbEdpaxJ8qSbgXcPP0W1XY5gaWRjNXbinrP2jPvnCKLtoqgJPJnP4WPIclnPpc3IQK8YsrPbyugA5XiqHEbDTnCV%2F5OvttLH7nvEpK7MQoB6GRJzsWLpkt8XE7CccAxbpCLT2c31%2F7MMG5%2FpzhMvAbU%2FgHF4t3XIS95QhEzgp9FVk5RLEovbIFoguI3Yq6KpTr0ST6Kv%2FyOXmkUT7VPMGAorokp92YKfPYIVR%2FFjkhwNAVztgL2X4ioSvJ5BC6tYDbpl5lBAbl%2FuMDvRxq2TkZJ3h4M5qpMPGY28wGOqUBWXPSzXOg8CtnMk5X6dUZdzddi8Gl8kYMOv0JoZ7M9f5M6ATKS%2FwDgkm%2Fm6e0HYoB1uH1N35VQAwm2tLGNP5ArODlHXi6DzF3jo%2Bmj8ea7PjBRNfl2e5h2JtXQNZWEj%2FhktZInvFiUOdam%2Bdg6MvA0yT%2BsV0tzBeGt9VdnvcAZlSK8i3nVWbFsuSwmwyodjrZjMzLtDYfPM0R3i%2FW4RsV7ohUmHxa&X-Amz-Signature=5b50502eed5cb21c851db1472e3a708f0169ab7062f9aeb52298fcf923feb76b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - Carl’s audit reports
[Tokamak Network - Staking v2 Security Assesment-EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3d205f59-7059-4e2f-b3ca-bcd97fba2452/Tokamak_Network_-_Staking_v2_Security_Assesment-EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW3QXX4O%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7hNE1BwNsp%2B%2BBRuNkIGtTMczQaoo%2FYisbXFSNQikMQAiEA0jxIb65G031nfZ1b9qIjLvrKMdrLHlmU09E6W7MMg58q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDC8Vn2YyX3hKeKEOUircA50oFOSsVvjPjqOp8GtlDXFUdeCv0%2BRHUDn%2FVFFzyveJvLVL617AxMUdkhLxLkRT%2FKt%2F7IHli1qKbdvpmYLs9VAeRIYOA7099Vo6eTmKFuNqoj6Okf%2BZaoOBGfHaRIVB2e6a5%2FTY1a4CeTSfi1b%2BGbCgjH5EC0QA7D5Ak2sHKatb3TF%2FxJeShu9wx4aoOOMSseUXNQe8yMr%2FD1jA6toRHpW7oeb2OHWO%2BabZ45Jc2tZEweQ81sjauBUWU%2F6ibE%2BiNYugqO9G17VfmYVwZJ93uGLEiiWk%2B6w%2BBAVmZROVNHsXx61QeUOr3C5u3ARF6GSKATV3RIv6BL%2B5%2Bj9hfOZMfSS%2BsijE6x45gtJ9wbU3sfp%2BoU4l1GwlLew%2Bl27kAHWm4a6vWyree6pAK4yJwgWCy4E8p8N5DZaFHMscV6UCtNzxVrmG%2F9zsHaUjx43fc9LKRvHXlJgL%2Ftfaf%2B55NzzuC6WzsY1ht3xVwGokLSiPtlMi12YhY4ekCqUGQUiGL8v6bqqA67UWEisBbTVX3QrCuyEiy3sVhrruyVTGXu4tdB59MiksvBr4YV9oTUmW5KOsN3Rl9Sj5wWtHBspx48LICZc7u%2BscIO7zFKdCUpWO3iUvXOf1pEgsttUtiJHjMN2Z28wGOqUBE5oJG%2BvaEnuQKemwaBkviR2K6CLevfyVHq%2FXWpTnx4y12qXxgMyvLiOGFZKzpau5gUy1cY51eqeHICeNS2oE8lIO7esZ4YNFF0m%2Bjq3yegPmpCt%2Fn8Pibc87Tzrxtsp8rmdlyv0Yusn3rmKteqhZdgN25uH6jAjZ%2BppUukBWO95V69ILsOP0QB%2BfXC1BSDuUXaJnzaiSFKGRZjbCVE9CfGdJqpqa&X-Amz-Signature=fae7b9f8fc9ffb35f1919bf7c44a58e0dc675e8e3182e893cf0b96305e0a8711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[Tokamak Network - Staking v2 Security Assesment-KR.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d891e008-eb71-409f-93a6-b56662fe3cbf/Tokamak_Network_-_Staking_v2_Security_Assesment-KR.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VW3QXX4O%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7hNE1BwNsp%2B%2BBRuNkIGtTMczQaoo%2FYisbXFSNQikMQAiEA0jxIb65G031nfZ1b9qIjLvrKMdrLHlmU09E6W7MMg58q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDC8Vn2YyX3hKeKEOUircA50oFOSsVvjPjqOp8GtlDXFUdeCv0%2BRHUDn%2FVFFzyveJvLVL617AxMUdkhLxLkRT%2FKt%2F7IHli1qKbdvpmYLs9VAeRIYOA7099Vo6eTmKFuNqoj6Okf%2BZaoOBGfHaRIVB2e6a5%2FTY1a4CeTSfi1b%2BGbCgjH5EC0QA7D5Ak2sHKatb3TF%2FxJeShu9wx4aoOOMSseUXNQe8yMr%2FD1jA6toRHpW7oeb2OHWO%2BabZ45Jc2tZEweQ81sjauBUWU%2F6ibE%2BiNYugqO9G17VfmYVwZJ93uGLEiiWk%2B6w%2BBAVmZROVNHsXx61QeUOr3C5u3ARF6GSKATV3RIv6BL%2B5%2Bj9hfOZMfSS%2BsijE6x45gtJ9wbU3sfp%2BoU4l1GwlLew%2Bl27kAHWm4a6vWyree6pAK4yJwgWCy4E8p8N5DZaFHMscV6UCtNzxVrmG%2F9zsHaUjx43fc9LKRvHXlJgL%2Ftfaf%2B55NzzuC6WzsY1ht3xVwGokLSiPtlMi12YhY4ekCqUGQUiGL8v6bqqA67UWEisBbTVX3QrCuyEiy3sVhrruyVTGXu4tdB59MiksvBr4YV9oTUmW5KOsN3Rl9Sj5wWtHBspx48LICZc7u%2BscIO7zFKdCUpWO3iUvXOf1pEgsttUtiJHjMN2Z28wGOqUBE5oJG%2BvaEnuQKemwaBkviR2K6CLevfyVHq%2FXWpTnx4y12qXxgMyvLiOGFZKzpau5gUy1cY51eqeHICeNS2oE8lIO7esZ4YNFF0m%2Bjq3yegPmpCt%2Fn8Pibc87Tzrxtsp8rmdlyv0Yusn3rmKteqhZdgN25uH6jAjZ%2BppUukBWO95V69ILsOP0QB%2BfXC1BSDuUXaJnzaiSFKGRZjbCVE9CfGdJqpqa&X-Amz-Signature=a458425aad28c016878d122701c2f8d4e9089dbd073325426560052c1dc58416&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**Landing page**

- Open a new landing page ([a new landing page](https://www.tokamak.network/), [Partners page](https://www.tokamak.network/about/partners), [price dashboard](https://www.tokamak.network/about/price), [x post](https://x.com/Tokamak_Network/status/1887320825449349536))

### 2-b-ii. Work

1. **Resource**
  - A new member joined: Suhyeon
    - He is contributing to the research slashing protocols
1. **Product**
  - **Simple Staking V2(WIP)**
    - **Expected opening date: **early May** **
    - Front-end([git](https://github.com/tokamak-network/simple-staking-v2/tree/sepolia))
    - Issue list of Audit ([Hammer](/19dd96a400a3800ebeb7cdb5e3bdbee7), [Carl](/1a7d96a400a3804e9eaaff5c5504498d), [CertiK](/1a1d96a400a380deaca3df7dd08dcb76), [Omniscia](/1a8d96a400a38078a819c9413f4677e5))
      - Feedback Report ([Hammer](https://hackmd.io/@JWIJNWSZQYe4YscQzAySwQ/rksDtCpskl), [Carl](/1a7d96a400a3800ca930e1b38da72d68), [Omniscia](/1a8d96a400a38016a1e3df627cc83b02))
    - Collaboration with TRH Team ([review1](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1741251736618339), [review2](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742216559576259), [review3](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1742477324498319?thread_ts=1742368700.088929&cid=C06UKCF86TE)) 
    - Building TON Staking Development  Environment ([A guide doc](/1bbd96a400a380aa9b47f975110011f9) , [Development   address of Sepolia](/1bbd96a400a380aa9b47f975110011f9#1bbd96a400a380ed8515cd9255b652aa))
  - **Staking community edition(WIP)**
    - **Expected date: **end of Apr
    - Staking community edition frontend, storyboard & design([git](https://github.com/tokamak-network/staking-community-version/commit/5941fe5c16c5626b5c4233cb2d86a4fab143d4fc), [Link](https://www.figma.com/design/78o8cJqIF4q8d8pcEyQPak/Simple-Staking-Community-Edition?node-id=281-79&t=Vq3JRuEsUnfBVFHK-0), [Figma](https://www.figma.com/design/AiJnU7khvyiVwCXO4LNDpy/Tokamak-management?node-id=2144-31155&t=IGrBX12ErrXlYMZK-11))
    - Staking community edition user guide ([Link](/1add96a400a38076bc2af9a03c3615ad))
  - **TON Staking SDK(WIP)**
    - **Expected date**: end of Apr
    - Alpha version([git](https://github.com/tokamak-network/ton-staking-sdk-monorepo))
1. **Knowledge**
  - **Staking V2:** internal seminar([seminar](https://drive.google.com/file/d/1r1D83UUTpwb0OPIw2_fyZIMIJQZIdjBs/view?usp=drive_web)), final demo([slide](https://docs.google.com/presentation/d/1WHlG6I1FeLtnti57wjOFV4DmrWkNX7N2/edit?pli=1&slide=id.p12#slide=id.p12), [seminar](https://drive.google.com/file/d/1WRkiZIC-vuhpEXaqaZGmRyRE2oH--AoA/view))
  - **DAO V2: **policy document draft seminar([seminar](https://drive.google.com/file/d/1J0QKE3zPVYmoeAFOzCzVP-qv_yXdWri4/view), [slide](https://docs.google.com/presentation/d/1waA2bmfTIWKckle11KLBRNoIeLNqUrAs/edit#slide=id.p1))
1. **Policy**
  - DAO V2 policy document draft([KR](/190d96a400a380a39613ce208e0c6dbb), [EN](/193d96a400a3809baa9fd5970489eb5e))

## 2-c. The reason why each under

### 2-c-i. List of challenges faced for each under-achieved deliverable

The timeline for Staking & DAO is delayed because there are bottlenecks in both tasks.

- **Staking V2: **Significant technical challenges arose during contract security audits, with 297 vulnerabilities identified by four audit firms. Addressing these complex and critical security issues consumed substantial time and resources, causing delays.
- **DAO V2:** The integration of SYB’s PoU technology, crucial for secure off-chain voting and Sybil attack prevention, faced delays due to external dependencies. The SYB PoU system was not ready as expected, complicating internal scheduling and causing significant project delays.

### 2-c-ii. List of solved challenges

- No solved challenge

### 2-c-iii. Strategy for unsolved challenges

- **Staking V2:**  To mitigate delays caused by ongoing contract audits, the team adopted a parallel development approach, continuing frontend development simultaneously with contract improvements. This approach strategically reduces potential delays, allowing rapid deployment upon audit completion.
- **DAO V2:** Given the current external dependency on SYB’s PoU system, our strategy involves deepening internal expertise regarding PoU integration. We will closely collaborate with SYB to define integration requirements cleary and identify specific areas where we can independently accelerate preparation, thus minimizing further scheduling risks.

# 3. Change in next quarter's deliverables

**Original deliverables**

- **Open community version v1.0 + community guide**: Add information about new agenda creation (snapshot and discord)
- **Open community version v2.0**: Add support for arbitrary code execution 

**Change deliverables**

- **Open community version for DAO V1:** change work order in **original deliverables**. Because first work in original deliverables needs readiness.
- **Audit memoir(blog post, **[**audit checklist**](/1bbd96a400a38043a479c3a64e5b5c49)**):** We aim to document the trials and errors encountered during the audit process and create an internal checklist to help other teams avoid repeating similar issues.
- **Submit a new agenda for a contract upgrade:** Contracts are changed through audit, we need to propose a new agenda. 
- **Launch Staking V2 on mainnet:** Delayed deliverables due to audit
- **Publish the staking community version & guide & SDK:** Delayed deliverables due to audit

# 4. Budget request

## 4-a. (this quarter)Previous budget requested

- 16,500 TON

## 4-b. (next quarter)Next budget request

- 16,500 TON

## 4-c. Gap(Next - Previous) and why?

- There are no Gap

# 5. Change in the road map

## 5-a. Change in the milestone


**Staking V2**

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Simple Staking V2** | Propose DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Launch Staking V2 testnet | 1 service |  |
|  | new DAO agenda for staking contract upgrade | 1 dao agenda |  |
|  | Contracts audit | 4 final reports, 1 blog post, 1 internal report |  |
|  | Launch Simple Staking V2 with DAO candidate and L2 support | 1 service | 2 service + 1 DAO agenda |
| **Community version** | Launch **community version v1.0 + community guide** with Simple Staking V2 support | 1 service with 1 guide |  |
|  | Release TON staking SDK v1.0 with Simple Staking V2 support | 1 code release | 1 code release, 1 service with guide |
| **Integration of Slashing Protocol** | **Release TON staking SDK v2.0** with slashing support | 1 code release |  |
|  | Launch **community version v2.0 + community guide** with slashing support | 1 service update with 1 guide | 1 code release, 1 service update with guide |
| **Integration of fast withdrawal protocol** | **Release TON staking SDK v3.0** with fast withdrawal support for staked TON | 1 code release |  |
|  | **Launch** **community version v3.0 + community guide** with fast withdrawal support for staked TON | 1 service update with 1 guide | 2 code release, 1 service update with 1 guide |

**DAO V2**

| **Category** | Subcategory | Deliverable | Subtotal |
| --- | --- | --- | --- |
| **Improvement of proposal interface** | **Open community version for DAO V1**: Add support for arbitrary code execution | 1 service | 1 service |
| **Testing DAO V2 on testnet** | Testing Snapshot with PoU  | 1 testnet |  |
| **Policy document for DAO V2** | Including Discord based RFC, Snapshot, PoU for sybil-attack | 1 documents |  |
| **Added use of Snapshot and forum** | **Open community version for DAO V2 **: Include new agenda creation via Discord and Snapshot with PoU | 1 service | 1 service, |

## 5-b. Change in the timeline

| Year-Quarter | Milestone |
| --- | --- |
| 2025-Q1 | - Landing page |
| 2025-Q2 | - Open Simple Staking V2
- Staking community version
- DAO 1.0 community version |
| 2025-Q3 | - Staking V2: Slashing protocol
- DAO V2: Policy document
- DAO V2: Snapshot test with PoU |
| 2025-Q4 |  |
| 2026-Q1 | - Addition of fast withdrawal protocol
- DAO 2.0 Community version |