[[The Security Council Management  ]]

[[Nominee vetting guidelines]]

[[Gnosis ]]

[[Tally’s Gnosis Safe]]

 [https://github.com/ArbitrumFoundation/governance/blob/main/docs/overview.md](https://github.com/ArbitrumFoundation/governance/blob/main/docs/overview.md)

- Quorum according to the type of action of The Security Council
  - (In case of an **emergency**) can take **quick action** in an <u>emergency</u>:  It is made up of  9 of 12 multisig. (75 % agree  in **Arbitrum**) 
  - (In case of a **non-emergency**) can take **slow action** for <u>routine upgrades that bypass the DAO vote</u>:  It is made up of  7 of 12 multisig.(58.3 % agree in **Arbitrum**) 
- What The Security Council Does
  - **Upgrade** the system: 
    - Only passed proposals made through the constitutional governor (the DAO) or a Security Council can upgrade the system.
  - **Cancel or block the proposal:** Only Security Council  
  - **The 9/12 Security Council should be able to make an upgrade without any delay** ( withdrawal delay, L1 timelock) 

# Governance contracts overview

- Timelock
  -  [https://github.com/tokamak-network/ton-staking-tally-contract/blob/dev/contracts/TokamakTimelockController.sol](https://github.com/tokamak-network/ton-staking-tally-contract/blob/dev/contracts/TokamakTimelockController.sol)
  - 이 타임록은  TokamakGovernor의 제안을 누구든지 실행할 수 있도록 하기 허용하기 전에,   3 일의 지연(timelock delay : Determined during initial setup.)을 적용합니다.
| **Contract** | **By whom are received proposals?** | **Timelock** |
| --- | --- | --- |
| TokamakTimelockController ( L1 ) | TokamakGovernor,
**7-12 in Security Council ( in case of the slow action)** | 3 days  |
  - Initialize of TokamakTimelockController  
    - In the above case,
      - minDelay : 3 days
      - proposers : [TokamakGovernor, **7-12 in Security Council**]
        - 제안 가능 
        - 취소 가능
          - TokamakGovernor : 제안한 계정이 취소가능 
          - **7-12 in Security Council 이 취소가능 **
          - 투표 시작하기 전까지만 취소가능 
      - executors: 
        - [address(0)] → 누구나 실행가능 

```javascript
/**
 * @dev Initializes the contract with the following parameters:
 *
 * - `minDelay`: initial minimum delay in seconds for operations
 * - `proposers`: accounts to be granted proposer and canceller roles
 * - `executors`: accounts to be granted executor role
 * - `admin`: optional account to be granted admin role; disable with zero address
 *
 * IMPORTANT: The optional admin can aid with initial configuration of roles after deployment
 * without being subject to delay, but this role should be subsequently renounced in favor of
 * administration through timelocked proposals. Previous versions of this contract would assign
 * this admin to the deployer automatically and should be renounced as well.
 */
function __TimelockController_init(uint256 minDelay, address[] memory proposers, address[] memory executors, address admin) internal onlyInitializing {
    __TimelockController_init_unchained(minDelay, proposers, executors, admin);
}
```
- Drawing the contracts  

[app.diagrams.net](https://app.diagrams.net/#G1P5YLJaMqzyup4mlB6NgdcivvluW39qwT#%7B%22pageId%22%3A%22rFmZGRvop43g4m-QShxf%22%7D)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c9311ca2-47df-4a4d-b831-56b07e1b388a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-11-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.13.34.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN7D5SEV%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSHLrhKY5gsSYMfPBLS2CW%2FF2GEXzRnzO8Apl2Xak72AIgReDPg14W7SXdes9Pmv6U8VbZYcSdOOVkoR%2B5j1q24O0q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDJ74%2BlNK%2BhEPwDVeNircA5CMU17oq%2BAb3lJdf7H2%2BMwvO3MugWe6x3OBdh%2Fn6qyjj9glXEsTAFLu2JrwH4gBKxZf%2BLiyDxEHECawGkpeLrIOYdG8ynCth%2F%2BeBCqZKmVlOi%2BGRaKmsKjxqJVWd169Wmk8LQw4CsfeiVshFQaZ5nTM%2FWBamgNB6FmJFyfPipYUwNq%2Bigr6HuOPN%2F4Aka7m%2Fc3kqHnA1ZwjMNzUtlU%2FG2dHcloyYLmYn4po2acoCu%2FgYgJkbUvRKy638XwERBHjPMEcw4lj%2BH%2FjNECvFshOTiuVMPvbXnxWcExmYPGcUvNQifZQKQFGbWK%2FAGxMt%2FE6wf9ICoQDuGreIeXgyjb2yiYNSGlAZp1JQ6mmOfJiNZANuqQnxqB28wl%2Bksnsm%2BnIRYdcJSAiWJj9bx7XpplMqgKkEcsAWwwxGhqoa4572%2BFw%2BYQH3pwHNlqr8BTPrDGXBW8ObrC4kEEVYmq%2B5nyXsxqV9dAo0HEEQgaIPWzFTJ%2Fy1mYWknfNh5iYiRfH7JUXBem8mnhRu8xg5M3qwbzRDy9qFG3RcDIV4Szvzwh5Y0HNfNYY8IkzeiCp1RqdgRLBe%2BnDKU027rFk8OdiI0%2FBSgJhRPgTiLDvD3Ou7wjHPl%2F11nuTlvfGAOSJfUfWMKLv2swGOqUBow%2BufXWRbQpF5fys3mAljNscn3I%2F%2F%2FHPgwG4mbjK8Rk6NZnZOTcA%2BMiOzN3BmfjqLoA4yWPuvB9XA9U%2B6xl5SWtDCHWYs5n0hk1jMlWo6kHDdzSQCmBNjvAy7b6o8dqzm5x6sHDZQr%2BE07gkQrcsmYXau4UG6Pk3xyW1tty3uNguivCvdJEfwO9Fx5UAj5b8l%2Bev%2FZoJHJylhOFGdZh97BJj%2FdmZ&X-Amz-Signature=5bd7b44aab729f748b62e821b1c43537c85dc89aa9acb5b4aae56fbbf44c44a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)