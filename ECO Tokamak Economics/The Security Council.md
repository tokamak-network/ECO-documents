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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c9311ca2-47df-4a4d-b831-56b07e1b388a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-11-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_11.13.34.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IEQMR42%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T040154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsKfRdD6UKUxKYX1mAXP8licX52V3dmxt2NYZaY%2FZ3NQIhAOzT4H5z8FnM7TGuhcToMWh6bJtQfRjOBr%2BA6qayihs0Kv8DCHQQABoMNjM3NDIzMTgzODA1IgwWRrmaaq0DYeSmUY4q3ANeq8QCJqQZbgPIFMSQutrHqTvJpH0zBdBaO2PDw2ZZUe80ucCONpdnZyWQfAaHzZF8FaS%2F8zL3pBVQ1RU79Ig41F2lm4wAKySM4dDNEC%2BXS1ffHPy43ODsDjgTEJjpdTD087lRKvHb%2FJCT2QJjnI1QTJxwTINLCcjt6pBmc%2FJXcpHM%2BLGjhwlULB%2B2vrQSbTYBLYUHZqSOMLOMTKlUGyEHK3EmWOYe1T3Q3D%2F5Yo%2BbmpFHB5zwTezixKD0Men2G%2FnCbM2qjdT1F0pDZt6JWfSml%2F7xKTCbalIunFqirxsb3glx2zaRK%2BULguEzs88sNqYJ9me0tu4AKNyOVzE8P4he1tMVwrwTzpjw9gnW4lnvd412laVzbnNtJDtIu1jq1bZJ9MTXTySJvdWLz%2BBeOFmPbsz8QJ3OxIrn4%2FeIu1zYn8ivuYeIPzXZxEbzjyjyamiDw6xVk8yOMcwSlg4cW6ANE%2FnNz5bl5LtAAf3lFnEEDaUooeUYUzdZb5Q9gOGz6gd6Ll121Iou5NjgxLVkxikcwebB7nODfRYYDNy%2BwZrMfbS%2B1dU%2FPFwVsbh1pHXuMzuNjR78rgzfT00WuCf3evSC1yC0m4%2FWAf2umnDX78WGl%2Fcp9uGrqa%2B1jKAJ4DDL7tnMBjqkAbavWU90N890h19mJ5gid9KhW%2BFDm5ypkTcVRg0fye2ox3jv1UVI0g9OpOsILPLs8p7pKI0bYG30NotIG0fCA8kiVVU%2FHd%2FtT0kT7h%2F32joSUezkzxTynirmy8Rk%2FBp1frWhbARLpQdOqI5wGPDUH%2FKDBL2IuJA%2FO7JB1Z7Kz1LK3wV%2FnAdILFDWEAzXGymPQsBkpfYGepzA4FD5NI3J8Twt8ZRf&X-Amz-Signature=c5d8db1027c2ecfdcd7d2a5e9fe7077eaa72413bec444226760df8d6b8a91090&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)