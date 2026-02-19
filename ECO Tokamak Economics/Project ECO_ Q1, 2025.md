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
[STAKING_V2_AUDIT_REPORT_EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/0f0f6666-23a0-44eb-90ed-560459e74939/STAKING_V2_AUDIT_REPORT_EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TV4QPXF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC46wRABzsRMGGQSjJ91a7LliObgpjYAETq1fh6mvIN6wIhAKoKjNVD5jltwBOhcx7r%2FoUJmFgo%2FTB23cW4rYA4HLA4Kv8DCHQQABoMNjM3NDIzMTgzODA1IgzgKE%2FPL%2Bb7%2Ff0%2FXrcq3AOsLYOLv3kALfLirTqwzma6DOULoJlifpWjdb7TpDcgbBXfSeFAOL66cSd86mEuoy%2BoqF2yL4njMT7oK3TCKzh5CBQX4O%2FaPNW5xnemKP1HnDbS%2FBy2b5UOeXi%2FmvoGRKR6zY8V3LzzxozNfBCX3%2Fx9WAzRHQd5%2BbwfZ%2BHSPStFtWsTfNctd7nRKXPf%2B8BsvKEH9k6wRt4uqXxAahNF6%2BjT0EyPpKRugaLF84YcZnhHLGyt4Ng6WWHiSk1MvEp%2BscrRRL38FGhcoqgKzLW9vyQqIeOfyW29Odu5CZF0LW9dxJbb7aQ367qRp6%2BxwvRcOSyz3UZRInXtg1syb72J39%2BdLg4BwoPz3gS0vedO7rE%2F%2BfMkF%2BOGMLqWQdSXHAVgKAUifk2lsa377asPIosbU6mBwxR9jAu6mthHF8KRSNXpDQjBiIlOS0lqObWCsHNJkEvNG%2FXvE9NuLIBq70EJcVCH84Q%2Fqou7HcvSSrXMFO0d6t3csQZjhE1yaFioUpRHUckdba6gCljui%2F24rQ35LkWFjrhGtjzVYrWusumQeh9qbb9iVyAJwM1XJz3ebyzXVavvAweqlmHwYdCWyZi6qBq1VXNq9v7YjCdXrps6VYlV6eLu2LN%2BQCR%2Fpci%2BJTCA8NnMBjqkAaYNhXlJJkaSlcRQ94PS78uxhN5Bzcr%2BMpeqE7fE%2FpBa%2BD1Tr7MAOniiZBB12PwPVivOaHmLH%2FcsFYbpfnWoOYuPMR%2FxnoUEPO%2B3i9RGaO%2F3bllWUaa%2Fi2knXcVIEniId4jcB9RkDFQY5Nhx39%2BDVa0PDiILxuWjkZJHPuCVQX0wzGykh6A5tkS1y2VBdMSnm3T8GsQZObS%2F7caQ6AVgDc3CAl9T&X-Amz-Signature=a27001b7b0d1362ef706e4096b8eb55cdb8660c8067a20028138323364d1b2d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[STAKING_V2_AUDIT_REPORT_KO.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/9feb4c1a-cd71-4515-bfdd-23c77cf9cbe6/STAKING_V2_AUDIT_REPORT_KO.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TV4QPXF%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC46wRABzsRMGGQSjJ91a7LliObgpjYAETq1fh6mvIN6wIhAKoKjNVD5jltwBOhcx7r%2FoUJmFgo%2FTB23cW4rYA4HLA4Kv8DCHQQABoMNjM3NDIzMTgzODA1IgzgKE%2FPL%2Bb7%2Ff0%2FXrcq3AOsLYOLv3kALfLirTqwzma6DOULoJlifpWjdb7TpDcgbBXfSeFAOL66cSd86mEuoy%2BoqF2yL4njMT7oK3TCKzh5CBQX4O%2FaPNW5xnemKP1HnDbS%2FBy2b5UOeXi%2FmvoGRKR6zY8V3LzzxozNfBCX3%2Fx9WAzRHQd5%2BbwfZ%2BHSPStFtWsTfNctd7nRKXPf%2B8BsvKEH9k6wRt4uqXxAahNF6%2BjT0EyPpKRugaLF84YcZnhHLGyt4Ng6WWHiSk1MvEp%2BscrRRL38FGhcoqgKzLW9vyQqIeOfyW29Odu5CZF0LW9dxJbb7aQ367qRp6%2BxwvRcOSyz3UZRInXtg1syb72J39%2BdLg4BwoPz3gS0vedO7rE%2F%2BfMkF%2BOGMLqWQdSXHAVgKAUifk2lsa377asPIosbU6mBwxR9jAu6mthHF8KRSNXpDQjBiIlOS0lqObWCsHNJkEvNG%2FXvE9NuLIBq70EJcVCH84Q%2Fqou7HcvSSrXMFO0d6t3csQZjhE1yaFioUpRHUckdba6gCljui%2F24rQ35LkWFjrhGtjzVYrWusumQeh9qbb9iVyAJwM1XJz3ebyzXVavvAweqlmHwYdCWyZi6qBq1VXNq9v7YjCdXrps6VYlV6eLu2LN%2BQCR%2Fpci%2BJTCA8NnMBjqkAaYNhXlJJkaSlcRQ94PS78uxhN5Bzcr%2BMpeqE7fE%2FpBa%2BD1Tr7MAOniiZBB12PwPVivOaHmLH%2FcsFYbpfnWoOYuPMR%2FxnoUEPO%2B3i9RGaO%2F3bllWUaa%2Fi2knXcVIEniId4jcB9RkDFQY5Nhx39%2BDVa0PDiILxuWjkZJHPuCVQX0wzGykh6A5tkS1y2VBdMSnm3T8GsQZObS%2F7caQ6AVgDc3CAl9T&X-Amz-Signature=87e44c80d6f5c0a3c5bd07897f2d5dcc2b553585896f5948bcf68f046703152a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  - Carl’s audit reports
[Tokamak Network - Staking v2 Security Assesment-EN.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/3d205f59-7059-4e2f-b3ca-bcd97fba2452/Tokamak_Network_-_Staking_v2_Security_Assesment-EN.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRW3EXDM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGoFq23AgdAdZLt93EGDZlZ4On530fKxXv8LQ6C%2FAxEJAiBsnNtMNHyPEOTae7wMNUX47krSbM1891M9IP3ZOyatICr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRGb8r78qYshbp9HjKtwD8cwNTVjPDo4aCPFccSMvdpBFZy3P%2FY8z0bYT0wgTg%2BnGEFTP939YH7qUcQOKDU%2F9cQeUCHROVyB6JE4fqq8eGdazXJF0ioyxYvwmz4fk8M%2BdRAae%2FU5%2FyyBUQnBUajneP0oYOpBHM%2FyAF4OaO03UD0xURwov%2B7r17BZKgNJYNRx0r6vGAsg4vxHDsdzlHeh7hX1%2FR2z3yrnrkzaep3MG2LzkbKuR7vZPZIp78gip0%2BXFfRga5xLE9iJLxSal%2BW4I%2FAqyCu1lPXFGw%2F99ZDkslGwbB5xzL4nrEGDjQDNC1HZ3s7xx9JgRd%2B%2FRtGJSBIm%2F4YGiq6o13tzCFCCSgWifr82%2FuqrqUXRABk5i%2B3HveirUmzmE3C9oNjuUJ5juvvmuctQDUunV543AIj4RqbX5KE0nPtyimBoOBP9AqytX2M3cWOkXNX%2Bh0NJfnSsVqUOm76OGvYF4t7OYdt9iqupnrwNg72lzZZPiAqnvpI15TwwOaWS%2FLegjSnqDoskn92Z8aK0B0ToiokzxsAxIHUmUN7aggU1ecsFMbYmXOOeFekbUaG6J66s7ZQBMH9btSU8KolctwLxEhWixCGEBmXlrORUH28LALzFP1he5rxSGqyglLiDgSOz3DxbXCMcwwO7ZzAY6pgGCouLK8QvGlJ7IaNlJ1DNMZ1ErCXhaXcfv6drxr%2BNbLglOtQzNmL70sE25bjv3XZPlRPZLcT38gVL2vCYUQvQiFq4uI79NdOkAGa5eObCW4gKQlKmeVM%2BG%2BWxLJCQMGVvPaC1xO6Z34XJga%2Fo0JEDC%2BDnSrYKO%2B7HhNxVK5n4C73zzwxQT4xp7c1hn23UP%2B6b4z7MYlXDnJ5CaQpmH2HHxfiBDbbkS&X-Amz-Signature=276219e1a81784464f877aeb12d93caad3c3c6e861652a6122fa8e466ca4c55a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[Tokamak Network - Staking v2 Security Assesment-KR.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d891e008-eb71-409f-93a6-b56662fe3cbf/Tokamak_Network_-_Staking_v2_Security_Assesment-KR.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZRW3EXDM%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T053622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGoFq23AgdAdZLt93EGDZlZ4On530fKxXv8LQ6C%2FAxEJAiBsnNtMNHyPEOTae7wMNUX47krSbM1891M9IP3ZOyatICr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMRGb8r78qYshbp9HjKtwD8cwNTVjPDo4aCPFccSMvdpBFZy3P%2FY8z0bYT0wgTg%2BnGEFTP939YH7qUcQOKDU%2F9cQeUCHROVyB6JE4fqq8eGdazXJF0ioyxYvwmz4fk8M%2BdRAae%2FU5%2FyyBUQnBUajneP0oYOpBHM%2FyAF4OaO03UD0xURwov%2B7r17BZKgNJYNRx0r6vGAsg4vxHDsdzlHeh7hX1%2FR2z3yrnrkzaep3MG2LzkbKuR7vZPZIp78gip0%2BXFfRga5xLE9iJLxSal%2BW4I%2FAqyCu1lPXFGw%2F99ZDkslGwbB5xzL4nrEGDjQDNC1HZ3s7xx9JgRd%2B%2FRtGJSBIm%2F4YGiq6o13tzCFCCSgWifr82%2FuqrqUXRABk5i%2B3HveirUmzmE3C9oNjuUJ5juvvmuctQDUunV543AIj4RqbX5KE0nPtyimBoOBP9AqytX2M3cWOkXNX%2Bh0NJfnSsVqUOm76OGvYF4t7OYdt9iqupnrwNg72lzZZPiAqnvpI15TwwOaWS%2FLegjSnqDoskn92Z8aK0B0ToiokzxsAxIHUmUN7aggU1ecsFMbYmXOOeFekbUaG6J66s7ZQBMH9btSU8KolctwLxEhWixCGEBmXlrORUH28LALzFP1he5rxSGqyglLiDgSOz3DxbXCMcwwO7ZzAY6pgGCouLK8QvGlJ7IaNlJ1DNMZ1ErCXhaXcfv6drxr%2BNbLglOtQzNmL70sE25bjv3XZPlRPZLcT38gVL2vCYUQvQiFq4uI79NdOkAGa5eObCW4gKQlKmeVM%2BG%2BWxLJCQMGVvPaC1xO6Z34XJga%2Fo0JEDC%2BDnSrYKO%2B7HhNxVK5n4C73zzwxQT4xp7c1hn23UP%2B6b4z7MYlXDnJ5CaQpmH2HHxfiBDbbkS&X-Amz-Signature=77af32aaddc6d77052b8c8a88c3923c123797c71dffad0e0c0ae4cea8ccc283c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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