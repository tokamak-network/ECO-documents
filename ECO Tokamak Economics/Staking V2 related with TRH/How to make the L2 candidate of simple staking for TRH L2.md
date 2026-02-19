To register a candidate for your Layer2 on the Simple Staking page, you will need to follow these steps: 

***You must understand the contents of the white paper.**** * [https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md) 

# Step 1. Prepare the RollupConfig address 

Please prepare the address of the RollupConfig contract that stores your Layer2 information.

The supported layer 2 is the legacy optimism rollup and bedrock optimism rollup (with TON NATIVE TOKEN).

> [!tip]
> 💡 **If TRH's L2 is bedrock optimism rollup (with TON native token), please refer to section (2).**

## (1) Legacy Optimism Rollup 

- In legacy optimism rollup, create a contract that stores the rollup address and uses it as the RollupConfig address.
- For testing,
run as follows to create a DefaultSystemConfig contract,
  - setting

```javascript
git clone https://github.com/tokamak-network/ton-staking-v2.git
git checkout staking-v2.5
npm install --force 
cp .env.sample .env 

*Input your account's private key in **PRIVATE_KEY** and your node url in .env file .*

npx hardhat compile
```

  - execute create-rollup-config task  

```javascript
npx hardhat create-rollup-config \
--l1-bridge-register-address {l1BridgeRegisterAddress} \
--l1-cross-domain-messenger-address {l1CrossDomainMessengerAddress} \
--l1-standard-bridge-address {l1StandardBridgeAddress} \
--optimism-portal-address {optimismPortalAddress} \
--name {name} \
--network {network name} 
```

example: create-rollup-config task  on hardhat (local) 
    - Sepolia's l1-bridge-register-address is ‘0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC’.
    - For the remaining parameters, use the address appropriate for your Layer 2. 
    - Already registered Layer 2 contract information cannot be registered in L1BridgeRegistry. (step 2) Please use an address that has not been previously registered.

```javascript
>> npx hardhat create-rollup-config --l1-bridge-register-address '0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC' --l1-cross-domain-messenger-address '0x0000000000000000000000000000000000000000' --l1-standard-bridge-address '0x385076516318551d566CAaE5EC59c23fe09cbF65' --optimism-portal-address '0x7b6db1316e22167b56211cDDC33431098BaBC3c2' --name 'Thanos-Test1' --network sepolia   **
**
```

result

```javascript
 {
  l1BridgeRegisterAddress: '0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC',
  l1CrossDomainMessengerAddress: '0x0000000000000000000000000000000000000000',
  l1StandardBridgeAddress: '0x385076516318551d566CAaE5EC59c23fe09cbF65',
  optimismPortalAddress: '0x7b6db1316e22167b56211cDDC33431098BaBC3c2',
  name: 'Thanos-Test1'
}

LegacySystemConfig deployed to: **0xD63E39dD4EC7BFB901C7a77aa0470E1D9aD67FF8**
```

You can get the LegacySystemConfig address, you will use this LegacySystemConfig address to RollupConfig address.  

## (2) Bedrock Optimism Rollup (with TON native token ) 

- In bedrock optimism rollup, you use the [SystemConfig](https://github.com/tokamak-network/tokamak-thanos/blob/main/packages/tokamak/contracts-bedrock/src/L1/SystemConfig.sol) address to the RollupConfig address. 

# Step 2. Register the RollupConfig information to  L1BridgeRegistry 

You should register **rollupConfig, type, and L2TON**** address information **in L1BridgeRegistry.


There are two ways to register: one is through <u>(1) the administrator(TokamakDAO) reviewing the contract and then registering</u>, and the other is through <u>**(2)**</u><u> </u><u>**account with registration authority. **</u>

> [!tip]
> 💡 In TRH, you should use method (2) to be able to register without interrupting the L2 construction process. To do this, ECO team can grant registration authority to an account managed by TRH. TRH can register using an account with the registration authority. 
> Please send me TRH's address and I will grant you registration authority.

### Prerequisites for obtaining registration authority

Build a way to prevent seigniorage theft using upgrading.

We discussed this issue with Kevin a long time ago. At that time, Kevin proposed two solutions. Please refer to them. [doc](/bbe340158f2944aabedb3134e90b7a5b) 
**(1) Establish an upgrade DAO system
(2) Set non-upgradeable contracts or upgrade permission addresses to 0 on On-Demand L2 **

 

- An upgrade DAO system 

> [!tip]
> 💡 If the systemConfig, bridge, messaging, and portal contracts are upgradeable contracts, **the address with the upgrade authority must be the DAO for the upgrade**.
> The upgrade must be made through the UpgradeDAO, and the members of the UpgradeDAO must be the Foundation, the TokamakDAO, and the L2 operator(sequencer). <u>The upgrade can be made when all three members accept the upgrade</u>.
> 
> This prevents malicious operators from attempting to steal TON seigniorage by changing the contract code.
> 
> The above 3 member composition is subject to change. Please check later.

### Registering function

This **registerRollupConfig** function can only be used by authorized accounts. 

- Contract : L1BridgeRegistryProxy
  - mainnet: Not yet distributed
  - sepolia: [0x58813D18b019F670d43be0D80Af968C99cc82c05](https://sepolia.etherscan.io/address/0x58813D18b019F670d43be0D80Af968C99cc82c05#writeProxyContract)
- **Function : **[**registerRollupConfig**](https://sepolia.etherscan.io/address/0x58813D18b019F670d43be0D80Af968C99cc82c05#writeProxyContract#F6)** (address rollupConfig, uint8 _type, address _l2TON, string calldata _name) **
  - Paramers
    - rollupConfig:
      - If it is legacy optimism rollup, please make rollupConfig contract that suits your environment. Refer to above step1 - (1).
      - **If it is bedrock rollup, you can use SystemConfig contract address.**
    - type: Set to 1 if your Layer2 is a legacy optimism rollup, or 2 if it is a bedrock optimism rollup with TON native token.
    - L2 TON: If the type is 2, the address of the ton native token is 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000
    - _name: 

# Step 3. Register the CandidateAddOn

After completing the second step above (RollupConfig registration complete), you can create a CandidateAddOn.
After completing this procedure, the Candidate you registered will appear on the Simple Staking webpage. [https://sepolia.staking.tokamak.network/staking](https://sepolia.staking.tokamak.network/staking)

- Contract : Layer2Manager
  - mainnet: Not yet distributed
  - sepolia:  [0xffb690feeFb2225394ad84594C4a270c04be0b55](https://sepolia.etherscan.io/address/0xffb690feefb2225394ad84594c4a270c04be0b55#writeProxyContract)
- Function : [registerCandidateAddOn](/d76ffba7cf8d428a94a250399f7b09fe) (address rollupConfig, uint256 amount, bool flagTon, string calldata memo)
  - Paramers 
    - rollupConfig: rollupConfig registered in Step 2
    - amount: When creating a CandidateAddOn, you must pay a collateral. The minimum deposit is 1000.1 TON.  (Enter in Wei units. Minimum value: 1000100000000000000000)
    - flagTon: If true, the collateral is paid in TON, if false, it is paid in WTON.
    - memo: name registered in Step 2 (This is the name displayed on the Simple Staking web page.) 
- If you do not want to pre-approve for collateral payment, you can use TON.approveAndCall or WTON.approveAndCall.
- Once your CandidateAddOn is registered, your CandidateAddOn will appear on the Simple Staking screen.** **[**https://simple-staking-v2-one.vercel.app/staking**](https://simple-staking-v2-one.vercel.app/staking)

# Additional Check

### Interface for depositing to L2 in simple staking

- In simple staking, the function for depositing to L2 uses ~~**depositERC20To( L1ton, L2ton, to, amount, gasLimit, data )**~~.
→ We will be modified withdrawAndDepositL2 of DepositManagerV1_1.sol  as below.

***If l2Type = 2, use IL1Bridge(l1Bridge).***bridgeNativeTokenTo instead of IL1Bridge(l1Bridge).depositERC20To.

```
function bridgeNativeTokenTo(
        address _to,
        uint256 _amount,
        uint32 _minGasLimit,
        bytes calldata _extraData
    ) external;

```

### How to get the address(operator) that receives the seigniorage on-chain?

Currently, we gave seigniorage to the owner of SystemConfig ( SystemConfig.owner() ).

But in Thanos stack, SystemConfig.owner() = 0x000000000000000000000000000000000000dEaD, so this cannot be used.

In simple staking, this address(operator) is given seigniorage.

When an operator changes, it should be possible to query the operator on-chain.

**So, we decide to create the seigniorageReceiver storage in SystemConfig. **

~~We should use the ~~~~**SystemConfig.seigniorageReceiver() function to get **~~~~this address receiving seigniorage.~~

*We should use the ****SystemConfig.******unsafeBlockSigner******() function to get ****this address receiving seigniorage. *[https://tokamak-network.slack.com/archives/C06UKCF86TE/p1737711061309999](https://tokamak-network.slack.com/archives/C06UKCF86TE/p1737711061309999)

### Be designed to act as the DAO of L2.

The CandidateAddOn contract registered in the simple staking created in this way will act as the DAO of the L2.
The DAO function has not been implemented yet, but the necessary DAO functions should be implemented in this contract in the future.