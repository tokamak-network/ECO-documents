[https://github.com/tokamak-network/ton-staking-v2/tree/setup-dev-ton-staking-v2.5](https://github.com/tokamak-network/ton-staking-v2/tree/setup-dev-ton-staking-v2.5)

# Setup TON Staking Contracts for dev 

```json
git clone https://github.com/tokamak-network/ton-staking-v2/tree/setup-dev-ton-staking-v2.5

npm i 

/// compile 
npx hardhat compile

/// run node local 
npx hardhat node 


/// deploy on local network  
npx hardhat deploy  


/// deploy on sepolia network  
npx hardhat deploy --network sepolia 


/// test the ton staking v2.5
npx hardhat test test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts


/// test the DAO
/// Before testing, you need to check if multiSigWalletOwners is set to local in deploy-staking-all-sepolia/deploy.ts.
npx hardhat test test/layer2/units/12.dao-staking-v2.5.developmetns.test.ts
```

# Deployed Addresses on Sepolia 

deployer: 0xf0B595d10a92A5a9BC3fFeA7e79f5d266b6035Ea

```json
 **"TON" at 0x33a66929dE3559315c928556FcFF449b3E708c62
 "WTON" at 0x3FC550D4C381c170D83077c27ff8637a12cE48Fa**
 **"Faucetv2" at 0x943aF138e5e0E98573D7fdEBfC8F6798426Bc43a**
 "SeigManagerV1_2" at 0x67A86a81F61E078798780262c43E344b2D239e4C
 "SeigManagerV1_3" at 0xaE446072c51264d1f8249C243308c474dC811533
 **"SeigManagerProxy" at 0xd439DB92Afa684A21496120495F5083B816FC336**
 "DepositManager" at 0x84F4a9BFa625Aa49D24fde4AE06590954fc6F721
 "DepositManagerV1_1" at 0x4Eb7Dd7Bded7fea588b37b68805d7A88EC78AcA9**
 ****"DepositManagerProxy" at 0xe45bD303C463beb0B29ae1D0e021f84B26eeB866**
 "Layer2Registry" at 0xA0204342d453C839e2E52040012a62bA0B41b702
 **"Layer2RegistryProxy" at 0x39d0c47576042044f665EeB5276aa490F48441c0**
 "DAOAgendaManager" at 0x45BB5D06286ACF08d6bc75F0b315C27FE6eB3f34
 "CandidateFactory" at 0x1ED41e3351b4b6609d9Bf9A9C03b76057942de6c
 "CandidateFactoryProxy" at 0x2dc0f16eA6a6C8ca5C9De46f9BC19197286B94E1
 "DAOVault" at 0x649D4B1B9A8A465369805752bb4542C3B799F49D
 "MultiSigWallet" at 0xf2203EF17c7E434a74Cd1272EA240be52933853e
 "DAOCommittee_V1" at 0xF33144aA644112d4Dfc53523F1E42FE0aF9B3345
 "DAOCommitteeOwner" at 0xc6b3dA7c37Ca15C2Dc3D9e5e292f5784947b7a16
 "DAOCommitteeProxy2" at 0xa56d14018c3b82C22B06B0ABFf0C3d65eA8a0988
 **"DAOCommitteeProxy" at 0x83F78b1b172Fb31787c99156Ec0869C1D017A66F**
 "Candidate" at 0x39EcEf6bB64b83d03abbe0D58aD8fFaF72Ad8d68
 "RefactorCoinageSnapshot" at 0xCb54071516f1b51A0D1EBa2717Ed31A9cB08714A
 "CoinageFactory" at 0x023E7B881E0c7891E15CDA8F05bA1D34Fe81bDee
 "L1BridgeRegistryV1_1" at 0xa3025f0266BcbcbF3C3Aa67e5C31B27228602aF9
 **"L1BridgeRegistryProxy" at 0x472591A35A0c43Ad1942C6c47d1939BCcA7F6c13**
 "OperatorManagerV1_1" at 0x1781Ad61Fc468e573E2177Ff50BEC0Ea4E71881b
 "OperatorManagerFactory" at 0x35f0B157b01b9Dc7584F0F86Fa6907625083e70A
 "CandidateAddOnV1_1" at 0xf16AD756c46998Cc8A2246eac581a4521E80f776
 "CandidateAddOnFactory" at 0xb109f4c20BDb494A63E32aA035257fBA0a4610A4
 "CandidateAddOnFactoryProxy" at 0xd6510984FcC24783E6871faAB742587c0256709f
 "Layer2ManagerV1_1" at 0x8071431278b48c5c47f48Ef0D17AdC0AEa9acDAA
 **"Layer2ManagerProxy" at 0xb5e7b66D695485C96cb7Cf33ceE75383B8800D14**
```

** To verify DAOVault, DAOAgendaManger contracts, please refer [the verify-oldDAO repository readme](https://github.com/tokamak-network/verify-oldDAO).

# 1. To create Candiate 

Anyone can create a candidate.

[test](https://github.com/tokamak-network/ton-staking-v2/blob/622a36416ad86f758ab8bd22dba4daa0b7375a6c/test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts#L1173-L1197)

```json
describe('# **createCandidate** ', () => {
  it('Candidate ', async () => {

    const memo = "Candidate1"
    **const receipt = await (await daoCommitteeContract.connect(addr1).createCandidate(
        memo
    )).wait()**

    const topic = daoCommitteeContract.interface.getEventTopic('CandidateContractCreated');
    const log = receipt.logs.find(x => x.topics.indexOf(topic) >= 0);
    const deployedEvent = daoCommitteeContract.interface.parseLog(log);

    const candidateContract = new ethers.Contract(
        deployedEvent.args.candidateContract, DAOCandidate_Json.abi, deployer)

    expect(deployedEvent.args.candidate).to.be.eq(addr1.address)
    expect(deployedEvent.args.candidateContract).to.be.eq(candidateContract.address)
    expect(deployedEvent.args.memo).to.be.eq(memo)

    candidate1 = {
        address : deployedEvent.args.candidateContract,
        contract: candidateContract
    }

  });

})
```

# 2. To create CandiateAddOn 

You can create a CandidateAddOn using TRH's SDK. Please refer to TRH SDK.

- Registrant : 
- Verification Contract for dev :

 

# 3. To create Layer2Candidate  

Only Owner(DAO) can create a Layer2Candidate.

[test](https://github.com/tokamak-network/ton-staking-v2/blob/34e7c13788712123a58404131eaee15721cb61a3/test/layer2/units/11.staking-v2.5.developments.dev-sepolia.test.ts#L1201-L1252) 

```json
describe('# MockLayer2 registerLayer2CandidateByOwner ', () => {
  it('MockLayer2 ', async () => {
      mockLayer2 = (await (await ethers.getContractFactory("MockLayer2")).connect(layer2Operator).deploy(
          seigManager.address
      )) as MockLayer2;
  });

  it('**registerAndDeployCoinage** ', async () => {

      await (await **layer2Registry.connect(layer2Operator).registerAndDeployCoinage(
          mockLayer2.address,
          seigManager.address
      ))**.wait()

  });

  it('Operators must stake at least 1000.1 TON', async () => {
      let layer2 = mockLayer2.address
      let account = layer2Operator
      let tonAmount = ethers.utils.parseEther("1000.1")

      await depositApproveAndCall(layer2, account, tonAmount)

  })

  it('**registerLayer2CandidateByOwner** ', async () => {
      const memo = "MockLayer2"

      **const receipt = await (await daoCommitteeContract.connect(deployer).registerLayer2CandidateByOwner(
          layer2Operator.address,
          mockLayer2.address,
          memo
      )).wait()**

      const topic = daoCommitteeContract.interface.getEventTopic('Layer2Registered');
      const log = receipt.logs.find(x => x.topics.indexOf(topic) >= 0);
      const deployedEvent = daoCommitteeContract.interface.parseLog(log);

      const candidateContract = new ethers.Contract(
          deployedEvent.args.candidateContract, DAOCandidate_Json.abi, deployer) as Candidate

      expect(deployedEvent.args.candidate).to.be.eq(mockLayer2.address)
      expect(deployedEvent.args.candidateContract).to.be.eq(candidateContract.address)
      expect(deployedEvent.args.memo).to.be.eq(memo)

      layer2Candidate1 = {
          address : deployedEvent.args.candidateContract,
          contract: candidateContract,
          layer2: mockLayer2
      }
  });
})
```