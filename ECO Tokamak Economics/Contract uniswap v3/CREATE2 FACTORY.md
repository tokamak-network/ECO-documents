(CREATE2 Factory, CREATE2 Deployer, Deterministic Deployment Proxy 라고도 불림).

현재 Darius L2 Testnet에 CREATE2 Factory가 배포가 안되어 있어서, Permit2를 배포할 때 아래 에러가 발생합니다.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b7e2c39d-c878-46bd-b379-c7f235ee4798/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DH5Z72L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFGbDermTgYxUpXrm2uQexTM9osFJ6v2FlXqejgNAA0QIhALopIsaonD5f8xomYIlUEyHY%2F1Rn1gsLnySURrPW5JFbKv8DCHQQABoMNjM3NDIzMTgzODA1IgyE3iImJVQ0tooJCvkq3AOBjKwTau8WshTO7jEuUa%2B%2Fm7CPWF9A3IUEgfyesvBQvXBLcA8nzIvoxFiibBkw2fQXMWobEbOCK2t%2BSwGMLuV8hGnvPL8zLAIkpHtftwK6ekkPX2N2v4w0IPQT7dSaE1VIHDCHg%2FM9j5N%2BYJYe0OcTOxL8wKPWBUxcvHFmVBO5LPZEuTksv4hkH36L2JOczzpyLPHTVFR0KYhh%2BQUSZeHVC1kCb%2B3Gvam9iRxvREE6kPwSTZZvO9Ox0kI72LW6ggi6lPiVjENWLuUuaUSQUUAnyFxm7BsEN7V2YYg%2BJJzNino7Qner2R%2FFSeY1C70%2FVZVzAIJqp6iNoJ4w44RITbT5H3aHV6mIaIk9kNltAJs06%2BAhnJcL3gBtG%2BbMSN%2BQC3ERWOpVWkq%2FdQFmkpDtQXSBH34Fpi3Vi9RMgxD821mz6ckEhnXY4V%2BQSlBGnsb2cY0wTFKyJ6Jiu4iEbbXeUUZM4hTDKyQY717nNaaW4AtmXcUwkBFXAhfz4Mwvi0%2BKr%2FJTN2IoIhl6VifYsv9kkZgZNcwgsi9uQJGt2qh5ZioqnfnGASBHHAtsbeP%2BsD17TIWS5yA8VgsIk0d%2Bsr60MUjUxTLS%2FPwHH5%2FZ9nwcDRPNDbr2U6UksOs8fx0vPjD38dnMBjqkAXGvUVNShTGeMJqmlp9F4CAMgqxSq2ztLH%2BDO4RvZstjpuj9H%2Bkz5Ui5YJZnyzZdi4udc65LMi2PrPnIPM%2B6sNXzImBDYpcGoEQIPv5VKaakdEL6mpDuUuqmQilxkP2eatAdMpdaxSFfmEWgofUzyuoH8BLBCt6paHNwGTfqyzGj5BxAp1BtE1ft6NRM97voFfavs0TZRUH%2FipJmKHhylTqN2XKH&X-Amz-Signature=1b2c6c17ade20f3c3782f1b3fbf16bb09ddc0df795494a2c710275670b6943ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 목적

1. CREATE2 Factory를 배포 
1. CREATE2 Factory를 사용해서 유니스왑의 Permit2 컨트랙트 배포

### 설명

Create2 Factory or Deterministic Deployment Proxy  은 동일한 주소의 모든 체인에 배포할 수 있는 프록시 컨트랙트이며, CREATE2를 사용하여 결정론적 위치에 모든 컨트랙트를 배포할 수 있습니다.

주소 : 0x4e59b44847b379578588920ca78fbf26c0b4956c [optimism](https://optimistic.etherscan.io/address/0x4e59b44847b379578588920ca78fbf26c0b4956c) , 모든 체인에 배포되어 있음. except for tokamakgoerli

### [CREATE2 Factory 배포 코드](https://github.com/tokamak-network/tokamak-uniswap-v3-contract/blob/deployWeth9_testCollect/scripts/v3/9.deploy_deterministic-deployment-proxy.js)

스크립트 : npx hardhat run scripts/v3/9.deploy_deterministic-deployment-proxy.js --network tokamakgoerli

```json
const ethers = require("ethers")
require('dotenv').config()
const hre = require('hardhat');
async function main() {
    const provider = hre.ethers.provider;
    
    
    let balance = await provider.getBalance("0x3fAB184622Dc19b6109349B94811493BF2a45362");
    console.log(balance);
    let tx;
    try {
        tx = await provider.sendTransaction('0xf8a58085174876e800830186a08080b853604580600e600039806000f350fe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe03601600081602082378035828234f58015156039578182fd5b8082525050506014600cf31ba02222222222222222222222222222222222222222222222222222222222222222a02222222222222222222222222222222222222222222222222222222222222222');
    } catch (e) {
        console.log(e.message);
        throw e;
    }
    console.log(tx);
    await tx.wait();
    const receipt = await provider.getTransactionReceipt(tx.hash);
    console.log('receipt', receipt);
    
    balance = await provider.getBalance("0x3fAB184622Dc19b6109349B94811493BF2a45362");
    console.log(balance);
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
```

**고정되는 값.**

```json
{
	"gasPrice": 100000000000, (0.0000001 Ether (100 Gwei))
	"gasLimit": 100000,
	"signerAddress": "0x3fab184622dc19b6109349b94811493bf2a45362",
	"transaction": "0xf8a58085174876e800830186a08080b853604580600e600039806000f350fe7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe03601600081602082378035828234f58015156039578182fd5b8082525050506014600cf31ba02222222222222222222222222222222222222222222222222222222222222222a02222222222222222222222222222222222222222222222222222222222222222",
	"배포되는 address": "0x4e59b44847b379578588920ca78fbf26c0b4956c"
}
```

이 값들은 Optimism Contract Creation TX에도 나와 있습니다. [옵티미즘 Contract Creation TX](https://optimistic.etherscan.io/tx/0xeddf9e61fb9d8f5111840daef55e5fde0041f5702856532cdbb5a02998033d26)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/46d17211-ef0d-476d-8bce-d7b5f96eaa6f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DH5Z72L%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFGbDermTgYxUpXrm2uQexTM9osFJ6v2FlXqejgNAA0QIhALopIsaonD5f8xomYIlUEyHY%2F1Rn1gsLnySURrPW5JFbKv8DCHQQABoMNjM3NDIzMTgzODA1IgyE3iImJVQ0tooJCvkq3AOBjKwTau8WshTO7jEuUa%2B%2Fm7CPWF9A3IUEgfyesvBQvXBLcA8nzIvoxFiibBkw2fQXMWobEbOCK2t%2BSwGMLuV8hGnvPL8zLAIkpHtftwK6ekkPX2N2v4w0IPQT7dSaE1VIHDCHg%2FM9j5N%2BYJYe0OcTOxL8wKPWBUxcvHFmVBO5LPZEuTksv4hkH36L2JOczzpyLPHTVFR0KYhh%2BQUSZeHVC1kCb%2B3Gvam9iRxvREE6kPwSTZZvO9Ox0kI72LW6ggi6lPiVjENWLuUuaUSQUUAnyFxm7BsEN7V2YYg%2BJJzNino7Qner2R%2FFSeY1C70%2FVZVzAIJqp6iNoJ4w44RITbT5H3aHV6mIaIk9kNltAJs06%2BAhnJcL3gBtG%2BbMSN%2BQC3ERWOpVWkq%2FdQFmkpDtQXSBH34Fpi3Vi9RMgxD821mz6ckEhnXY4V%2BQSlBGnsb2cY0wTFKyJ6Jiu4iEbbXeUUZM4hTDKyQY717nNaaW4AtmXcUwkBFXAhfz4Mwvi0%2BKr%2FJTN2IoIhl6VifYsv9kkZgZNcwgsi9uQJGt2qh5ZioqnfnGASBHHAtsbeP%2BsD17TIWS5yA8VgsIk0d%2Bsr60MUjUxTLS%2FPwHH5%2FZ9nwcDRPNDbr2U6UksOs8fx0vPjD38dnMBjqkAXGvUVNShTGeMJqmlp9F4CAMgqxSq2ztLH%2BDO4RvZstjpuj9H%2Bkz5Ui5YJZnyzZdi4udc65LMi2PrPnIPM%2B6sNXzImBDYpcGoEQIPv5VKaakdEL6mpDuUuqmQilxkP2eatAdMpdaxSFfmEWgofUzyuoH8BLBCt6paHNwGTfqyzGj5BxAp1BtE1ft6NRM97voFfavs0TZRUH%2FipJmKHhylTqN2XKH&X-Amz-Signature=6851025994e351b22c3576ed57b34b95d8506631711aee3d065b153fcac17703&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**에러 코드 **

gas price too high: 100000000000 wei, use at most tx.gasPrice = 250000 wei

**에러 코드 해석**

현재, L2 OVM_GASPriceOracle의 gasPrice값이 250000 wei로 설정되어 있습니다. [link](https://goerli.explorer.tokamak.network/address/0x420000000000000000000000000000000000000F/read-contract#address-tabs)

그래서 시퀀서가 위의 TX를 거부하는 것으로 보입니다.

**관련 github의 issue**

1. 똑같이 Create2 Factory를 L2에 배포하려다가 실패한 경우

[Link](https://github.com/Zoltu/deterministic-deployment-proxy/issues/7)

1. 똑같이 rawTransaction을 사용해서 **ERC-1820**를 배포하려다가 실패한 경우

[Link](https://github.com/ethereum-optimism/optimism/issues/1883)

두 issue 모두 [https://github.com/smartcontracts](https://github.com/smartcontracts) ← 이 옵티미즘 개발자가 직접 배포하여 해결. (시퀀서 쪽을 업그레이드해서 해결한 거로 추정) [EIP-1820](https://optimistic.etherscan.io/address/0x1820a4b7618bde71dce8cdc73aab6c95905fad24#code),  [EIP-2470](https://optimistic.etherscan.io/address/0xce0042b868300000d44a59004da54a005ffdcf9f#code)  (이 두개 표준 컨트랙트들 배포 또한 gasPrice 이슈가 있었으나, 옵티미즘 개발자가 직접 배포)

**내가 생각하는 해결방법**

L2 OVM_GASPriceOracle의 gasPrice를 100000000001로 바꾸고, CREATE2Factory 배포하고, 다시 250000으로 돌려 놓는다. 그렇기 위해서는 GASPriceOracle의 owner인 **0x8f3e9a5c4ee4092e8cf3159dc65090cfd7e63d2e 의 프라이빗키가 필요.**