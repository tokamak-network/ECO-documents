To register a candidate for your Layer2 on the Simple Staking page, you will need to follow these steps: 

# Step 1. Prepare the RollupConfig address 

Please prepare the address of the RollupConfig contract that stores your Layer2 information.

The supported layer 2 is the legacy optimism rollup and bedrock optimism rollup (with TON NATIVE TOKEN).

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

# Step 2. Request the RollupConfig registration 

You should register **rollupConfig, type, and L2TON**** address information **in L1BridgeRegistry.
This **registerRollupConfigByManager** function can only be used by authorized accounts, so
**Please request RollupConfig registration to L1BridgeRegistry through the “tokamak-dev” channel.**
The information to be submitted when requesting is the rollupConfig address, type, and L2 TON address.

- type: Set to 1 if your Layer2 is a legacy optimism rollup, or 2 if it is a bedrock optimism rollup with TON native token.
- L2 TON: If the type is 2, the address of the ton native token is 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000.

example: l1bridge-register-rollup-config-manager  on hardhat (local) 
  - Sepolia's l1-bridge-register-address is ‘0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC’.
  - For the remaining parameters, use the address appropriate for your Layer 2. 
  - Already registered Layer 2 contract information cannot be registered in L1BridgeRegistry. (step 2) Please use an address that has not been previously registered.

```javascript
>> npx hardhat l1bridge-register-rollup-config-manager --l1-bridge-register-address '0xC8479A9F10a1E6275e0bFC4F9e058631fe63b8dC' --rollup-config '**0xD63E39dD4EC7BFB901C7a77aa0470E1D9aD67FF8**' --type 2 --l2-ton '0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000' --network sepolia   **
 **
```

# Step 3. Register the CandidateAddOn

After completing the second step above (RollupConfig registration complete), you can create a CandidateAddOn.
After completing this procedure, the Candidate you registered will appear on the Simple Staking webpage. [https://sepolia.staking.tokamak.network/staking](https://sepolia.staking.tokamak.network/staking)

- setting 
```javascript
git clone https://github.com/tokamak-network/ton-staking-v2.git
git checkout staking-v2.5
npm install --force
cp .env.sample .env 

*Input your account's private key in PRIVATE_KEY and your infrastructure key in your key in .env file .*

npx hardhat compile
```
- execute register-candidate-add-on task  
  - parameters 
    - ton-address: the TON address  
      - Sepolia's TON address is 0xa30fe40285b8f5c0457dbc3b7c8a280373c40044
    - layer2-manager-address: the layer2Manager address 
      - Sepolia's Layer2Manager address is 0xffb690feeFb2225394ad84594C4a270c04be0b55
    - rollup-config: This is the RollupConfig address prepared in Step 1.
    - amount: When creating a CandidateAddOn, you must pay a collateral. The minimum deposit is 1000.1 TON. 
(Enter in Wei units. Minimum value: 1000100000000000000000)
    - memo: The name of the CandidateAddOn being created. This is the name displayed on the SimpleStaking webpage.

```javascript
>> npx hardhat register-candidate-add-on --ton-address {ton address} --layer2-manager-address {Layer2Manager address} --rollup-config {RollupConfig address} --amount {amount} --memo {displayed name} --network {network name}  **
** 
```

example register-candidate-add-on   
    - Sepolia's TON address is 0xa30fe40285b8f5c0457dbc3b7c8a280373c40044
    - Sepolia's Layer2Manager address is 0xffb690feeFb2225394ad84594C4a270c04be0b55
    - For the remaining parameters, use the address appropriate for your Layer 2.

```javascript
>> npx hardhat register-candidate-add-on --ton-address '0xa30fe40285b8f5c0457dbc3b7c8a280373c40044' --layer2-manager-address '0xffb690feeFb2225394ad84594C4a270c04be0b55' --rollup-config '**0xD63E39dD4EC7BFB901C7a77aa0470E1D9aD67FF8**' --amount 1000100000000000000000 --memo 'Thanos-Test1' --network sepolia  **
**
```

    - result 

```javascript
registerCandidateAddOn tx:  0x274427fcc3141101b6e3a92abe57fba913f0d47b36b2fdfb7fe14296c3976acf
rollupConfig     :  0xc71B998Ef224Ef2cc71872495781dc4b21DEb121
candidateAddOn   :  0x5513f491b72E2C0C7Cbe8ab7B6f77C907ff722B6
operatorManager  :  0xef4F71F01A7f9995BD810F993BF6250851b5DFb2
operatorManager's manager  :  0xc1eba383D94c6021160042491A5dfaF1d82694E6
```