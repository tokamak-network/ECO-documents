*1/ L2 TVL*

```solidity
*uint256 cappedTotalLayer2TVL = Math.min(
    totalLayer2TVL * GWEI_UNIT, // Sum of TVL of all L2s
    tos - prevTotalSupply // Unstaked remaining TON amount
);*
```

*2/ l2TotalSeigs*

```solidity
*l2TotalSeigs = FullMath.rdiv(FullMath.rmul(maxSeig, cappedTotalLayer2TVL), tos);*
```

*3/ l2RewardPerUnit*

```solidity
*l2RewardPerUint** += (l2TotalSeigs * WEI_UNIT) / totalLayer2TVL;*
```

---

```solidity
(address rollupConfig, bool allowed) = _allowIssuanceLayer2Seigs(msg.sender);

if (allowed && !_isPauseL2Seigniorage(msg.sender)) {
    uint256 curLayer2Tvl = IL1BridgeRegistry(l1BridgeRegistry).layer2TVL(rollupConfig);
    Layer2Reward storage newLayer2Info = layer2RewardInfo[msg.sender];
    Layer2Reward memory oldLayer2Info = layer2RewardInfo[msg.sender];

    // update layer2 tvl if it has changed
    // Because the previous information(oldLayer2Info) was loaded into memory, the storage immediately reflects the latest information.
    if (oldLayer2Info.layer2Tvl != curLayer2Tvl) {
        newLayer2Info.layer2Tvl = curLayer2Tvl;
        // TODO: can this calculation be manipulated?
        totalLayer2TVL = totalLayer2TVL + curLayer2Tvl - oldLayer2Info.layer2Tvl;
    }

    // If this the first commit, set up an initial debt
    if (oldLayer2Info.startBlock == 0) {
        newLayer2Info.startBlock = block.number;
    } else {
        // distribute seigniorage to layer2 based on previous layer2 tvl
        // layer2Tvl would be 0 when layer2 has been paused
        if (oldLayer2Info.layer2Tvl > 0) {
            layer2Seigs =
                ((l2RewardPerUint * oldLayer2Info.layer2Tvl) / WEI_UNIT) -
                oldLayer2Info.initialDebt;
            // rewards just increase higher than layer2Debt because it is calculated based on previous layer2 tvl
            if (layer2Seigs != 0)
                ILayer2Manager(layer2Manager).transferL2Seigniorage(
                    msg.sender,
                    layer2Seigs
                );
        }
    }
    newLayer2Info.initialDebt = (l2RewardPerUint * curLayer2Tvl) / WEI_UNIT;
}
```

*4/ layer2TVL*

```solidity
*if (oldLayer2Info.layer2Tvl != curLayer2Tvl) {
    newLayer2Info.layer2Tvl = curLayer2Tvl;
    totalLayer2TVL = totalLayer2TVL + curLayer2Tvl - oldLayer2Info.layer2Tvl;
}*
```

- *과거 TVL과 현재 TVL이 다르면 업데이트한다.*
- *과거 TVL을 빼고 현재 TVL을 더해서 최신 상태로 맞춘다.*

*5/ 지난 기간 동안 예치했던 금액에 대해 보상을 준다*

```solidity
*if (oldLayer2Info.layer2Tvl > 0) {
    layer2Seigs =
        ((l2RewardPerUint * oldLayer2Info.layer2Tvl) / WEI_UNIT) -
        oldLayer2Info.initialDebt;
    // rewards just increase higher than layer2Debt because it is calculated based on previous layer2 tvl
    if (layer2Seigs != 0)
        ILayer2Manager(layer2Manager).transferL2Seigniorage(
            msg.sender,
            layer2Seigs
        );
}

newLayer2Info.initialDebt = (l2RewardPerUint * curLayer2Tvl) / WEI_UNIT;*
```

- *과거 청산 (Settlement)*
  - *대상: 지난번 정산 - 지금 이 순간까지의 보상*
  - *이 기간동안 실제로 예치되어 있었던 돈은 oldLayer2Info.layer2Tvl이기 때문에 oldLayer2Info 기준으로 계산해서 돈을 준다.*
- *미래 준비 (Reset for future)*
  - *대상: 지금 이 순간 ~ 다음번 정산까지의 보상*
  - *이제부터 예치되어 있을 돈은 curLayer2Tvl이다. 다음번에 계산할 때 지금까지 쌓인 보상을 또 달라고 하면 안되니 현재 TVL에 해당하는 현재까지의 누적 보상을 미리 initialDebt로 잡아둔다.*

---

*지수(L2RewardPerUint)는 시간이 지날수록 계속 증가한다.*

- *T1: 지수 10*
- *T2: 지수 20*
- *T3: 지수 30*
- …

### 1단계 — T1, 최초 예치

- 지수: 10
- TVL: 100
- Debt: 10 * 100 = 1,000
*—> 지수가 10일 때 들어왔으니 10 이전에 쌓인 보상은 내 것이 아니다.*

### 2단계 — T2, 추가 예치 및 정산

- 지수: 10 —> 20
- TVL: 100 —> 200

과거 보상 정산

- T1 ~ T2 기간 동안 예치해둔 돈은 100원이다.
- 보상 계산: (현재 지수 20 * 과거 TVL 100) - Debt 1,000
—> 2,000 - 1,000 = 1,000

Debt 재설정 — 새로운 TVL 기준

- 현재 TVL은 200이다.
- 현재 지수는 20이다.
- Debt: 20 * 200 = 4,000
*—> 지수 20까지 쌓인 보상은 이미 정산했기 때문에 총 4,000은 내 것이 아니다.*

### 3단계 — 미래 정산

- *지수: 20 —> 30*
- *TVL: 200 유지*
- 보상 계산: (현재 지수 30 * 과거 TVL 200) - Debt 4,000
—> 6,000 - 4,000 = 2,000

*Debt 재설정*

- *현재 TVL은 200이다.*
- *현재 지수는 30이다.*
- *Debt: 30 * 200 = 6,000*