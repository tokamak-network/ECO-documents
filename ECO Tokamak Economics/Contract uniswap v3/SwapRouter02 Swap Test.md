## ERC20 ⇒ ERC20

```json
let deadline = Date.now() + 100000;
let amountIn = ethers.utils.parseEther('500');
//==============TOS => TOS (ERC20->ERC20)
let SwapParams = 
  {
    tokenIn: TOSAddress,
    tokenOut: TONAddress,
    fee: 3000,
    recipient: deployer.address,
    //deadline: deadline,
    amountIn: amountIn,
    amountOutMinimum: 0,
    sqrtPriceLimitX96: 0,
  }
;
try{
    const tx = await SwapRouterContract.exactInputSingle(SwapParams, {
      gasLimit: 3000000,
    });
    await tx.wait();
    const receipt = await providers.getTransactionReceipt(tx.hash);
    console.log("===TOS => TON (ERC20->ERC20)");
    console.log("transactionHash:", receipt.transactionHash);
    console.log("gasUsed: ",receipt.gasUsed);
    console.log();
    totalGasUsed = totalGasUsed.add(receipt.gasUsed);
  }
  catch(e) {
    console.log("e", e.message);
  }
```

## ETH ⇒ ERC20

```json
//==============ETH => TON (ETH->ERC20)
  amountIn = ethers.utils.parseEther('0.000804204211611148');
  SwapParams = 
    {
      tokenIn: WETHAddress,
      tokenOut: TONAddress,
      fee: 3000,
      recipient: deployer.address,
      deadline: deadline,
      amountIn: amountIn,
      amountOutMinimum: 0,
      sqrtPriceLimitX96: 0,
    }
  ;
  try{
      const tx = await SwapRouterContract.exactInputSingle(SwapParams, {
        gasLimit: 3000000, **value: amountIn**
      });
      await tx.wait();
      const receipt = await providers.getTransactionReceipt(tx.hash);
      console.log("===ETH => TON (ETH->ERC20)");
      console.log("transactionHash:", receipt.transactionHash);
      console.log("gasUsed: ",receipt.gasUsed);
      console.log();
      totalGasUsed = totalGasUsed.add(receipt.gasUsed);
    }
    catch(e) {
      console.log("e", e.message);
    }
```

설명 : 이렇게 ETH를 트랜잭션과 함께 보내면, 직접 Wrap안해도, SwapRouter02가 알아서 해준다. 

uniswapV3Pool 컨트랙트에서 SwapRouter02의 callback function을 호출하게 되는데, 이떄 callback function에서 아래 pay 함수를 호출한다. 이때, 내가 보내준 ETH의 balance를 체크하여, ETH를 WETH로 wrap하고, uniswapV3Pool 컨트랙트로 transfer를 직접 해준다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/27e55a36-a6dd-4ca6-8c22-4976d60e12b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF7WCBPB%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDm%2B6tKlnuv9pev7613PGR0q8aZoWp1e1lkoxP%2B%2FhgEVAiAhyYbLFOsGHJeXxQO59xWyKU0FBGSeUAobwUvK9%2FlGKir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMTgIa6Qs8Kf%2BpL00%2FKtwDxDh7ytz1mxmObo4vL%2BHhbumCYMsxkqarWQhhTC1ruaMnZYnDL%2BgAQ%2FK2lSrOSGJJlAbCMMm3klZ4YM%2B2GZN8NkuKuUi2lIixnrI9qBnNlkdonYM1iYDs2WJ%2BnOZYIr3QTP1FEQ7MJmlqNvajn56pIhLEXZpfYmLEt1x3ugnsgiIhQhDMU1zZfjt4bY6v2TfDtyNGyC5NDcWJEgDdoD47QMERSF0ap6yziN58nnKUxDFXI0E36q%2B4BBq9gi3phdIJSJpiNOXfNFBgDNqjl46xtoIfc2Bqwa27dBoMCMEaf5whAULXOXl4uNM9Py1LWZB8krScm1bCJwUrW2vqy4mW%2BkprmdKGNhMvR6oFB83WprEXtFjk0VZ1cYPWBs45k7sbiss%2FQgtCbNgVdMOGGfRu95JPPmIMJKzxV7iW5QNjFEmDimxjrqNM3BDo%2FeYMKseMwGwitMYxtxlOl475FPaX2OxWBZ4V3jKOmtOfH0sD5egv9769auHg29mbLV7dL9E4WlQmck2%2FJiDp4n5UBYgvP4TT8nuKl6Ok3JcKoqjBs6ujqu5MbrDw6Prpo2yL6HGVfhaYn%2BfoGTPSnJ9gw6TOHHjmvplJAkE4twRioFWd59qn199Me8bGexSPsSEwzfDZzAY6pgGsueS5CD51%2Fya4jhdFY4tBznJ7w42S83d5llmApHQp0%2BXRwidkMGrvLfJ0NCncIVhoIWW6ILmZBSiWBiAMlJKFo4TvznsPvySf1Q5ikqzDyFBVzHrLkni4Y4Pdrxzo9UVjPuMWrnvVgEmh%2FOCqA8pYCFXzLtzXXNL3nrh0YdOEJwmye1jF8Iuc0E7CnZ9byyPBHN2BIJPAvyUXw1W8%2FbIBLtXzLmQg&X-Amz-Signature=cb2f1a57666d9cce1858d42007077375ea445135af11017f90adf6e10acf0e83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## ERC20 ⇒ ETH

```json
//==============TON => ETH (ERC20->ETH)
  deadline = Math.floor(Date.now() / 1000) + 100000;
	amountIn = ethers.utils.parseEther('1');
  const params1 = 
    {
      tokenIn: TONAddress,
      tokenOut: WETHAddress,
      fee: 3000,
      recipient: **SwapRouterAddress**,
      deadline: deadline,
      amountIn: amountIn,
      amountOutMinimum: 0,
      sqrtPriceLimitX96: 0,
    }
  ;
  const **encData1 **= SwapRouterContract.interface.encodeFunctionData('exactInputSingle', [params1]);
  const amountMinimum = 0
  const **encData2 **= SwapRouterContract.interface.encodeFunctionData('**unwrapWETH9**(uint256,address)', [amountMinimum, deployer.address])

  const encMultiCall = SwapRouterContract.interface.encodeFunctionData('**multicall**(uint256,bytes[])', [deadline,[encData1, encData2]])
  //console.log(encMultiCall);
  
  try {
    const txArgs = {
        to: SwapRouterContract.address,
        from: deployer.address,
        data: encMultiCall,
        gasLimit: 300000,
    }
    const tx = await deployer.sendTransaction(txArgs)
    await tx.wait();
    const receipt = await providers.getTransactionReceipt(tx.hash);
    console.log("===TON => ETH (ETH->ERC20)");
    console.log("transactionHash:", receipt.transactionHash);
    console.log("gasUsed: ",receipt.gasUsed);
    console.log();
    totalGasUsed = totalGasUsed.add(receipt.gasUsed);
  } catch (e) {
    console.log(e.message);
  }
```

설명 : ETH를 받기 위해서는, exactInputSingle 함수의 parameter의 recipient에 내가 아닌 SwapRouterAddress를 설정한다. 그리고 unwrapWETH9 function을 같이 encode하여 multicall을 실행하면 WETH가 아닌 ETH를 받을 수 있다.