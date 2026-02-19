[Link](https://tokamak-network.slack.com/archives/C07JU6K4KDY/p1764923109777099?thread_ts=1764660309.457889&cid=C07JU6K4KDY)

**type: ****`business logic`**

SeigManager의 onDeposit 함수는 새로운 토큰을 발행하기 전에 updateSeigniorage를 호출하지 않는다. 이로 인해 신규 입금자가 참여하지 않은 과거 기간의 시뇨리지까지 분배받게 되어, 시간 기반 공정성이 훼손된다.

**index**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dcd3f2fb-2950-4679-b570-8d36c5b643c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQOOO2UZ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T050528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGslsp1wjWWrCNF7PYSGr9CNMUujJ7FyZFA5ADhrLFqHAiAg9mV147W12KB2gEI%2BUuOB%2B5vfM5Gx6n9NqBuP%2BUvl4ir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMFsQAhVECccMy%2B000KtwDCwlTD57YKY6hQ0zQMsCqzX%2Fuu67UjMh0Y85ddS8OfAFXVKCvUVuT%2Ffc8U7r%2BOqCWMgIdXRdY5Jtn6IvTBjISMCPyycR6mgPXWUrXM0V%2B3Ibf3LnDPfYvBOiSaFbPlBdfY6QW0FkTRnL1mAkg90JciLEeECtx29L20zOKsrLqnwYDt52Pe3OiAhIuaudcLMM4UHEtBMhOxaS%2BoFxqJY8Q1D9dmefLQ9Jva7wpyRFe%2BAp%2FidinQtc1eclVsj0mI9%2B6UX%2FFpxUf1qzm%2FxqNHGU1iVwdlCKdO5GG35RqjD4N670%2FecQPrUK6H4Po9F%2FThM0yLOMlhM5iNXb4d2wPZ3mp423VHkw%2FK8ShsHoIT%2By1dOO9Yo0Nf0p00yRkSldzFUHi4D7ivGb4FDjgNzVEpDh9L6nxPzYh7Dyn3oyX0IKYbr5TQ4s2dIxuGPrpwNm8LK1gQzphU%2B3sPN342EqgKg9DUuCyBu8bjcD2y4KoEx%2FT4VDUsKkmx%2FX5TltCr%2BZVUqqJIW3oNq66qmJ3sQ0NIi5AmOZDzhNHLwBkZeN%2BQESV0NlhavPsQ6csgBm91vzJE6fsJ6Gsgwnai6DWe0O%2B0UpUD6TqGDP8bMaewY9lCdYgFTLP%2Bj47snGqiNyL%2FVcwu%2B7ZzAY6pgEw2K8lZeaojc%2FYjNVH0kWMghL9Ub9nG8%2BRjhfGEgNQCXGPbicer%2Bg7IgBt1Poh7Hx6u0b5KO0VKfV8vIj1tu4isl7bZxzyZ9lXpgFMYqwhPmZtGfP35dsRQ4VDQ9LhvVXWNBnMEFqs6bO5R1LFZk%2BogOFQ%2F8AVqBbYUu4v%2FXSf4glZTcKqDWyAIZzBiBoDbUBRq1ZP5yoGHoBFvMGGxDU1K9I8PH92&X-Amz-Signature=a585595cbd93cff5b0315d01aa0d56ce1a41bb3573629a8d51a6f6b4d3b25b88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Test scenario

### Setting

**run local blockchain**

```bash
anvil \
  --fork-url https://eth-sepolia.g.alchemy.com/v2/GeyuOmyqufBJhmabG5svz \
  --chain-id 11155111 \
  --fork-block-number 9752799
```

**set values**

```bash
export RPC_URL="http://127.0.0.1:8545"

export ALICE_ACCOUNT="0x488f3660fcd32099f2a250633822a6fbf6eb771b"
export ALICE_PRIVATE_KEY="dc719aa7ad72b35f639a38fe17422e18bd5b05bdcb76e2e98bacfd3827a90c5a"

export BOB_ACCOUNT="0x31b4873b1730d924124a8118bba84ee5672be446"
export BOB_PRIVATE_KEY="c368845af5c800d2bb8883c8394574df4476d8219ddcfd15d09a83537a531d7c"

export TON="0xa30fe40285b8f5c0457dbc3b7c8a280373c40044"
export WTON="0x79e0d92670106c85e9067b56b8f674340dca0bbd"
export DEPOSIT_MANAGER="0x90ffcc7F168DceDBEF1Cb6c6eB00cA73F922956F"
export SEIG_MANAGER="0x2320542ae933FbAdf8f5B97cA348c7CeDA90fAd7"
export CANDIDATE="0xaeb0463a2fd96c68369c1347ce72997406ed6409"
```

**faucet TON (set forcibly balance storage)**

```bash
export FAUCET_AMOUNT=$(cast to-wei 1000000000000) # 1,000,000,000,000 TON
export NEW_BALANCE=$(cast to-uint256 $FAUCET_AMOUNT)
echo $NEW_BALANCE

export ALICE_BALANCE_STORAGE_SLOT=$(cast index address $ALICE_ACCOUNT 0)
export BOB_BALANCE_STORAGE_SLOT=$(cast index address $BOB_ACCOUNT 0)
```

```bash
cast rpc anvil_setStorageAt $TON $ALICE_BALANCE_STORAGE_SLOT $NEW_BALANCE --rpc-url $RPC_URL 
```

```bash
cast rpc anvil_setStorageAt $TON $BOB_BALANCE_STORAGE_SLOT $NEW_BALANCE --rpc-url $RPC_URL 
```

```bash
cast call $TON "balanceOf(address)" $ALICE_ACCOUNT --rpc-url $RPC_URL
```

```bash
cast call $TON "balanceOf(address)" $BOB_ACCOUNT --rpc-url $RPC_URL
```

### Scenario #1

Alice는 0.00101588725 WTON (100001015887254197740629912646 - 99999999999999999999999999997)만큼의 시뇨리지를 받게 된다.

1. updateSeigniorage
```bash
cast send --rpc-url $RPC_URL --private-key $ALICE_PRIVATE_KEY \
  $CANDIDATE "updateSeigniorage()"
```
1. Check Alice's balance
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```
1. Alice deposits 100 TON
```bash
export AMOUNT=$(cast to-wei 100)

export PART1=$(cast to-uint256 $DEPOSIT_MANAGER)
export PART2_RAW=$(cast to-uint256 $LAYER2)
export PART2=${PART2_RAW:2}
export DATA="${PART1}${PART2}"

cast send --rpc-url $RPC_URL --private-key $ALICE_PRIVATE_KEY \
  $TON "approveAndCall(address,uint256,bytes)" \
  $WTON $AMOUNT $DATA
```
1. Check Alice's balance —> 99999999999999999999999999997 [9.999e28]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```
1. Mine 100 blocks
```bash
cast rpc anvil_mine 100 --rpc-url $RPC_URL
```
1. Check current block number — 9752901
```bash
cast block-number --rpc-url $RPC_URL
```
1. Alice calls the updateSeigniorage function in the SeigManager contract
```bash
cast send --rpc-url $RPC_URL --private-key $ALICE_PRIVATE_KEY \
  $CANDIDATE "updateSeigniorage()"
```
1. Check Alice's balance — 100001015887254197740629912646 [1e29]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```

### Scenario #2

Alice는 0.00961548623 WTON (1000009615486225035061210874368 - 999999999999999999999999999993)만큼의 시뇨리지를 받게 된다. Bob은 단 1블록 만에 9.61548623 WTON (1000009615486225035061210874374847 - 999999999999999999999999999999992)의 시뇨리지를 받게 된다.

> ***Reset the blockchain and ***[***faucet TON***](/2bed96a400a3813ebfd6dee5e54fee58#2bed96a400a381cf9c1bf4759d20b20d)*** before testing scenario #2***

1. updateSeigniorage
```bash
cast send --rpc-url $RPC_URL --private-key $ALICE_PRIVATE_KEY \
  $CANDIDATE "updateSeigniorage()"
```
1. Check Alice's balance
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```
1. Check Bob's balance
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $BOB_ACCOUNT
```
1. Alice deposits 100 TON
```bash
export AMOUNT=$(cast to-wei 1000)

export PART1=$(cast to-uint256 $DEPOSIT_MANAGER)
export PART2_RAW=$(cast to-uint256 $LAYER2)
export PART2=${PART2_RAW:2}
export DATA="${PART1}${PART2}"

cast send --rpc-url $RPC_URL --private-key $ALICE_PRIVATE_KEY \
  $TON "approveAndCall(address,uint256,bytes)" \
  $WTON $AMOUNT $DATA
```
1. Mine 99 blocks — *Since Bob's deposit generates 1 block, we mine only 99 blocks to reach a total of 100. It is necessary to verify that the block count is the same.*
```bash
cast rpc anvil_mine 99 --rpc-url $RPC_URL
```
1. Bob deposits 1,000,000 TON
```bash
export AMOUNT=$(cast to-wei 1000000)

export PART1=$(cast to-uint256 $DEPOSIT_MANAGER)
export PART2_RAW=$(cast to-uint256 $LAYER2)
export PART2=${PART2_RAW:2}
export DATA="${PART1}${PART2}"

cast send --rpc-url $RPC_URL --private-key $BOB_PRIVATE_KEY \
  $TON "approveAndCall(address,uint256,bytes)" \
  $WTON $AMOUNT $DATA
```
1. Check Alice's balance —> 999999999999999999999999999993 [9.999e29]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```
1. Check Bob's balance —> 999999999999999999999999999999992 [9.999e32]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $BOB_ACCOUNT
```
1. Check current block number — 9752901 (same as Scenario #1)
```bash
cast block-number --rpc-url http://127.0.0.1:8545
```
1. Bob calls the updateSeigniorage function in the SeigManager contract
```bash
cast send --rpc-url $RPC_URL --private-key $BOB_PRIVATE_KEY \
  $CANDIDATE "updateSeigniorage()"
```
1. Check Alice's balance —> 1000009615486225035061210874368 [1e30]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $ALICE_ACCOUNT
```
1. Check Bob's balance —> 1000009615486225035061210874374847 [1e33]
```bash
cast call --rpc-url $RPC_URL \
  $SEIG_MANAGER "stakeOf(address,address)(uint256)" \
  $CANDIDATE $BOB_ACCOUNT
```

## Result

Bob은 1 블록만 참여했지만 9.61548623 WTON의 시뇨리지를 받았다. 블록당 시뇨리지가 3.92 WTON임을 고려하면, Bob은 약 2.45블록치의 보상을 받은 셈이다. 이는 _increaseTot() 함수가 과거 모든 블록(100블록)에 대해 현재 시점의 totalSupply(Alice 1,000 + Bob 1,000,000)를 기준으로 시뇨리지를 계산하기 때문이다.

Alice는 Scenario #1에서 0.00101588725 WTON을 받았지만, Scenario #2에서는 0.00961548623 WTON을 받아 약 9.5배 증가했다. 이는 전체 스테이킹량 증가로 시스템 전체가 받는 보상이 커진 효과다. 그러나 Bob이 참여하지 않은 99 블록의 보상까지 Bob에게 분배되었다는 점에서 시간 기반 공정성이 훼손되었다고 볼 수 있다.

### solution

> 이 이슈가 승인되면 onWithdraw 시에도 updateSeigniorage 함수 호출이 필요한지 확인해야 한다. 또한 updateSeigniorage 함수 추가 시 발생할 수 있는 부작용도 검토가 필요하다.

```solidity
*function onDeposit(
    address layer2,
    address account,
    uint256 amount
) external onlyDepositManager checkCoinage(layer2) returns (bool) {**
****    if (block.number > _lastSeigBlock) {
        _updateSeigniorage();
    }****

**    if (_isOperator(layer2, account)) {
        uint256 newAmount = _coinages[layer2].balanceOf(account) + amount;
        require(newAmount >= minimumAmount, "minimum amount is required");
    } else {
        require(
            _getOperatorAmount(layer2) >= minimumAmount,
            "OperatorCollateral is insufficient."
        );
    }

    _tot.mint(layer2, amount);
    _coinages[layer2].mint(account, amount);

    return true;
}*
```