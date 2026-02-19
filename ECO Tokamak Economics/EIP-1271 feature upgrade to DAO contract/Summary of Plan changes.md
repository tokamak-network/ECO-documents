# Plan comparison

1. Original Plan
  - Phase 1: Basic architecture design and functional implementation (1 weeks) (25.08.07~25.08.13)
  - Phase 2: Test script development and documentation (1 week) (25.08.14~25.08.20)
  - Phase 3: Internal audit and feedback implementation & testing on Sepolia(1-2 weeks) (25.08.21~25.09.03)
  - Phase 4: Deployment after consultation with TRH team
1. Added plans
  - Further development : Changed signing logic, SafeWallet ProtocoKit Test, Development of a dedicated script for using SafeWallet's Contract, 2nd Internal Review, Front-end provided using Cloudflare service, Develop the LLM Prompt
  - Changed signing logic (25.08.29~25.09.01)
    - If only one signer of MultiSigWallet signs, it passes -> According to MultiSigWallet's policy, at least two signers must sign to pass.
  - SafeWallet ProtocoKit Test (25.09.01 ~ 25.09.12)
    - To test if it is actually linked to SafeWallet
    - A little more testing is needed according to DAOContract
    - Once the Safe-SDK usage version is confirmed, the contract needs to be modified and tested according to the version.
  - Development of a dedicated script for using SafeWallet's Contract (25.09.08~25.09.19)
  - ~~2nd Internal Review (25.09.22~25.09.26)~~
  - 2nd Internal Review (25.09.24~25.09.30)
  - ~~Contract Sepolia Apply (For TRH Team SDK Sepolia Open) (25.10.06)~~
    - **Contract Sepolia Apply (For TRH Team SDK Sepolia Open) (25.10.13)**
    - **Upgraded sign function DAOContract Mainnet Deployment (25.10.14 or 25.10.15)**
    - **Create Agenda on Mainnet** **(25.10.14 or 25.10.15)**
  - ~~Front-end provided using Cloudflare service (25.10.06~25.10.17)~~
    - **Front-end provided using Cloudflare service (25.10.13~25.10.24)**
  - **Sign Test on Mainnet With TRH, ECO, Kevin (Early November 25th)**
    - *TRH-SDK Mainnet Test (25.10.23~25.10.30)*
1. Policy for further discussion
  - Should we manage txHash and signature in DAOContract? (To do this, we need to call the transaction) (Managing can be inconvenient) 
    - No Need

# Why the Plan Changed

1. A review regarding logic changes was conducted during the Internal Review, and the logic was changed accordingly. (There was no significant difference in the time period due to the use of LLM Prompt.)
1. I didn't initially plan to test SafeWallet integration.
1. There were many bugs in the SafeWallet integration test, and it took a long time to find the cause of the bugs.
  1. in Detail : [[Using SafeWallet Problem]] 
1. Due to this bug, if a member of SafeWallet is a Contract, the Front of SafeWallet cannot be used, so a script must be provided.