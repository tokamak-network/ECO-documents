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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/27e55a36-a6dd-4ca6-8c22-4976d60e12b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664E53XMXH%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEpTOcRwWzTKm%2BQGWTquAdowAl6QbfsXc2snK0NH6qZ%2BAiBT91QmopQtYv%2FU3Cf53jzC%2FWQEmlzrKg7JRTuo92LYOyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMS8VbbsJj3%2BtQuHUFKtwDqb3YfDAfVpZWYGhBkXm%2B9AH3IqBdSp%2BYR%2B2KUnaTSnn8ekMpw3Wo0ytcEGcGLg2lOjJtMCkRUtZsYI5WD%2Biak6vxi7Ez3A6DyDvtlTNWrrn9DaeEObpSaGc01F7IhJHE0%2Fu94fO6HPbofSXkfiGlF4E4WFg%2BRZ4N0Njiil9P60qj9lEbPWwaQbX84vcs2yEexsun7kq4Y%2BznF5tyHFHrjkBsjrerysWCKdIxxg%2BbYhPEFqiNfTlB17N4%2FLh%2Bo2cOWkflnFurmxGVz1ha99hqfdZa8N7hc1hOFUtfHKTQnGtQ6EiWQ%2BLd0wJd274bvdb8XQfbPjhsl7QRa4Y7wZns9iTAOoURmmW4C8s6IpuP5wcR0IXai7j7YeS7IpXifp7skQlLIyYyxOqir937LQRcx0Zb1A9yADpbrJKPGkwYiA2pAmfH1YdK%2Bj%2Fb7CPMs8seicwzDi65Pc3pfOCpMQzK2rPT92yOFz4j5GYhzSNkj%2B2Tdwd5d%2BU1SgqXsjUMmuIdVxoVsULwxVVUbxxWSgUkpgZq9I15JeNOoed5yurW48k%2FcM3DG7WTXhw6rMjBiYoayu4ez4ChznzsAEcjIgq0j3UMoWXVAkjksFQutUv8e9fHQsJ5tveYHy79m3Iw9JrbzAY6pgHpDfQRcQ1%2B153FCrHcQML9VuYBJRbC0O%2FaU7zaGlCQbdIWUPM1fY7aq3geeRbcM8dWxTmeca6iUDYFEK6UxvisUvSzLLCohhagPqJIxdjB%2BLtKD%2BDP73ByFghEaWNRLKa%2BjFg7tFZAT%2Fl79v9WPLXHUCgJoCjLIkUOwEGhn1GzLBCjGdmC780%2BbQ8UIfX0emvZHSPwH9FSE90XhhzOkKpcBJYZamOo&X-Amz-Signature=17b4389188b9a2254bf0817939a3107b2178ff77ee4c4bb093b80b29620d3356&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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