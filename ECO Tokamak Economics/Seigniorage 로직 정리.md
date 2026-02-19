**_increaseTot()함수**

```
// short circuit if already seigniorage is given.
if (block.number <= _lastSeigBlock) return false;
```

현재 블록이 마지막 시뇨리지 분배 블록보다 이후가 아니면 처리하지 않고 즉시 종료합니다.

```
if (RefactorCoinageSnapshotI(_tot).totalSupply() == 0) {
    _lastSeigBlock = block.number;
    return false;
}
```

총 공급량이 0이면 현재 블록을 _lastSeigBlock으로 설정하고 종료합니다.

```
uint256 prevTotalSupply;
uint256 nextTotalSupply;

// 1. increase total supply of {tot} by maximum seigniorages * staked rate
// staked rate = total staked amount / total supply of (W)TON
prevTotalSupply = _tot.totalSupply();
```

이전 총 공급량을 저장합니다.

```
uint256 span = block.number - _lastSeigBlock;
if (_unpausedBlock > _lastSeigBlock) span -= (_unpausedBlock - _pausedBlock);
```

마지막 시뇨리지 분배 이후 경과된 블록 수를 계산합니다.

일시 중지 기간이 있었다면 해당 기간을 제외합니다.


가능한 로직 오류: _unpausedBlock이 _lastSeigBlock보다 크고 _pausedBlock이 _lastSeigBlock보다 작은 경우, span 계산이 부정확할 수 있습니다.

```
// maximum seigniorages
uint256 maxSeig = span * _seigPerBlock;
```

최대 시뇨리지 양을 계산합니다(블록 범위 * 블록당 시뇨리지).

```
// total supply of (W)TON , <https://github.com/tokamak-network/TON-total-supply>
uint256 tos = _totalSupplyOfTon(block.number);
```

현재 블록 기준 TON의 총 공급량을 가져옵니다.

```
// maximum seigniorages * staked rate
uint256 stakedSeig = rdiv(
    rmul(
        maxSeig,
        // total staked amount
        prevTotalSupply
    ),
    tos
);
```

스테이킹된 시뇨리지 양을 계산합니다(최대 시뇨리지 * 스테이킹 비율).

```
// L2 sequencers
uint256 l2TotalSeigs;
uint256 curLayer2Tvl;
address rollupConfig;
bool layer2Allowed;
```

L2 시퀀서 관련 변수들을 선언합니다.

```
// L2 seigs settlement
address _layer2Manager = layer2Manager;
Layer2Reward memory oldLayer2Info = layer2RewardInfo[msg.sender];
if (layer2StartBlock == 0) layer2StartBlock = block.number - 1;
```

layer2Manager와 현재 레이어2의 보상 정보를 가져옵니다.

layer2StartBlock이 0이면 이전 블록으로 설정합니다.

```
// layer2StartBlock == 1 이면, l2TotalSeigs 발급을 안한다.
if (
    _layer2Manager != address(0) && layer2StartBlock != 1 && layer2StartBlock < block.number
) {
```

L2 시뇨리지 발행 조건을 검사합니다.

```
    (rollupConfig, layer2Allowed) = allowIssuanceLayer2Seigs(msg.sender);
    if (layer2Allowed && !isPauseL2Seigniorage(msg.sender))
        curLayer2Tvl = IL1BridgeRegistry(l1BridgeRegistry).layer2TVL(rollupConfig);
    if (totalLayer2TVL != 0) l2TotalSeigs = rdiv(rmul(maxSeig, totalLayer2TVL * 1e9), tos);
}
```

레이어2의 시뇨리지 발행 허용 여부를 확인합니다.

허용되고 일시 중지되지 않았다면 레이어2 TVL을 가져옵니다.

totalLayer2TVL이 0이 아니면 L2 총 시뇨리지를 계산합니다.

가능한 로직 오류: curLayer2Tvl이 설정되지 않은 상태로 나중에 사용될 가능성이 있습니다.

```
uint256 unstakedSeig = maxSeig - stakedSeig - l2TotalSeigs;
uint256 totalPseig = rmul(unstakedSeig, relativeSeigRate);
nextTotalSupply = prevTotalSupply + stakedSeig + totalPseig;
```

다음 총공급량은 이전 총공급량 + 스테이크에 대한 시뇨리지 + 언스테이크에 대한 시뇨리지입니다.

```
_lastSeigBlock = block.number;
_tot.setFactor(_calcNewFactor(prevTotalSupply, nextTotalSupply, _tot.factor()));
```

마지막 시뇨리지 블록을 업데이트합니다.

새로운 팩터를 계산하여 설정합니다.

```
uint256 powertonSeig;
uint256 daoSeig;
uint256 relativeSeig;
address wton_ = _wton;
```

시뇨리지 분배 관련 변수들을 선언합니다.

```
if (l2TotalSeigs != 0) IWTON(wton_).mint(_layer2Manager, l2TotalSeigs);
```

L2 시뇨리지가 있으면 layer2Manager에게 발행합니다.

```
if (_powerton != address(0)) {
    powertonSeig = rmul(unstakedSeig, powerTONSeigRate);
    IWTON(wton_).mint(_powerton, powertonSeig);
}
```

PowerTON 주소가 있으면 해당 시뇨리지를 계산하여 발행합니다.

```
if (dao != address(0)) {
    daoSeig = rmul(unstakedSeig, daoSeigRate);
    IWTON(wton_).mint(dao, daoSeig);
}
```

DAO 주소가 있으면 해당 시뇨리지를 계산하여 발행합니다.

```
if (relativeSeigRate != 0) {
    relativeSeig = totalPseig;
    accRelativeSeig += relativeSeig;
}
```

상대적 시뇨리지 비율이 있으면 누적 상대적 시뇨리지를 업데이트합니다.

```
if (l2TotalSeigs != 0 && totalLayer2TVL != 0) {
    _insertL2UpdateBlock_Reward(l2TotalSeigs, totalLayer2TVL);
}
```

L2 시뇨리지와 총 레이어2TVL이 있으면 L2 블록 보상을 업데이트 합니다.

```
uint256 layer2Seigs;
if (layer2Allowed) {
    Layer2Reward storage newLayer2Info = layer2RewardInfo[msg.sender];
    if (oldLayer2Info.startBlock != 0 && oldLayer2Info.layer2Tvl != 0) {
        _insertCommitLayer2Tvl(msg.sender, oldLayer2Info.layer2Tvl);
        layer2Seigs =
            (((l2TotalSeigs * WEI_UINT) / totalLayer2TVL) * oldLayer2Info.layer2Tvl) /
            WEI_UINT;
        newLayer2Info.layer2Tvl = curLayer2Tvl;
    } else if (oldLayer2Info.startBlock == 0 && curLayer2Tvl != 0) {
        newLayer2Info.startBlock = block.number;
        newLayer2Info.layer2Tvl = curLayer2Tvl;
        if (l2UpdateBlock.length != 0) newLayer2Info.claimedLastIndex = l2UpdateBlock.length - 1;
        commitLayer2Tvl[msg.sender][block.number] = oldLayer2Info.layer2Tvl;
    }
}
```

레이어2가 허용되면 레이어2 보상 정보를 업데이트합니다.

가능한 로직 오류:

curLayer2Tvl이 설정되지 않았는데 newLayer2Info.layer2Tvl에 할당될 수 있습니다.

```
totalLayer2TVL = totalLayer2TVL + curLayer2Tvl - oldLayer2Info.layer2Tvl;
```

총 레이어2 TVL을 업데이트합니다.

가능한 로직 오류: curLayer2Tvl이 설정되지 않은 경우 부정확한 계산이 될 수 있습니다.

**_insertL2UpdateBlock_Reward()함수**

```
if (l2TotalSeigs_ != 0 && totalLayer2TVL_ != 0) {
            uint256 len = l2UpdateBlock.length;
            if (len == 0) {
                // l2UpdateBlock's 0 index is unused, it's a dummy
                l2UpdateBlock.push(0);
            } else {
                require(l2UpdateBlock[len - 1] < block.number, 'error insertL2RewardPerUnit');
            }

            l2UpdateBlock.push(block.number);
            l2RewardAtBlock[block.number] = (l2TotalSeigs_ * WEI_UINT) / totalLayer2TVL_;
}
```

1. **조건 검사**: 함수는 l2TotalSeigs_와 totalLayer2TVL_이 모두 0이 아닌 경우에만 진행됩니다. 이는 0으로 곱하고 나누는 오류를 방지하고 의미 있는 데이터만 기록하기 위함입니다.
1. **배열 초기화 처리**: l2UpdateBlock 배열이 비어있는 경우, 첫 번째 인덱스(0)에 더미 값 0을 추가합니다.  0번 인덱스는 실제로 사용되지 않습니다.
1. **시간적 일관성 확인**: 배열이 이미 존재하는 경우, 마지막으로 기록된 블록 번호가 현재 블록 번호보다 작은지 확인하여 블록이 시간 순서대로 기록되도록 보장합니다.
1. **현재 블록 기록**: 현재 블록 번호를 l2UpdateBlock 배열에 추가합니다.
1. **세이뇨리지 비율 계산 및 저장**: 현재 블록에서의 단위 TVL당 시뇨리지 비율을 계산하여 l2RewardAtBlock 매핑에 저장합니다. 이 값은 총 L2 시뇨리지를 총 L2 TVL로 나눈 값으로, WEI_UINT(10^18)를 곱하여 계산합니다.

이는 새로운 시뇨리지가 계산될 때마다 L2 운영자들을 위한 블록별 보상 정보를 업데이트하는 역할을 합니다.

**_insertCommitLayer2Tvl() 함수**

```
function _insertCommitLayer2Tvl(address layer2, uint256 layer2Tvl_) internal {
    uint256 len = l2UpdateBlock.length;
    if (len > 1 && !isPauseL2Seigniorage(layer2)) {
        layer2L2UpdateBlockIndexes[layer2].push(len - 1);
        commitLayer2Tvl[layer2][block.number] = layer2Tvl_;
    }
}
```

1. **배열 길이 확인**:
  - **`l2UpdateBlock`** 배열의 길이를 가져옵니다. 이 배열은 시뇨리지 계산이 이루어진 블록 번호를 저장하는 배열입니다.
1. **조건 검사**:
  - **`len > 1`**: l2UpdateBlock 배열에 실제 데이터가 있는지 확인합니다(0번 인덱스는 더미 값).
  - **`!isPauseL2Seigniorage(layer2)`**: 해당 layer2의 세이뇨리지 지급이 일시 중지되지 않았는지 확인합니다.
1. **인덱스 저장**:
  - 조건이 충족되면, **`layer2L2UpdateBlockIndexes[layer2]`** 배열에 현재 l2UpdateBlock 배열의 마지막 인덱스(len - 1)를 추가합니다.
  - 이는 해당 layer2가 어떤 블록 업데이트 인덱스에서 활성화되었는지 추적하는 데 사용됩니다.
1. **TVL 정보 저장**:
  - **`commitLayer2Tvl[layer2][block.number]`**에 해당 layer2의 TVL 정보를 저장합니다.
  - 이 정보는 나중에 세이뇨리지 계산 및 분배에 사용됩니다.

시뇨리지 분배 시 각 Layer2의 기여도를 정확하게 반영하기 위함입니다.

**claimableL2Seigniorage() 함수**

```
uint256[] memory layer2BlockIndexes = layer2L2UpdateBlockIndexes[layer2];
uint256 len = layer2BlockIndexes.length;
if (len == 0) return (0, 0);
```

해당 Layer2의 업데이트 블록 인덱스 배열을 가져옵니다.

배열의 길이가 0이면 청구할 세이뇨리지가 없으므로 (0, 0)을 반환합니다.

```
Layer2Reward memory rewardInfo = layer2RewardInfo[layer2];
uint256 globalLen = l2UpdateBlock.length;
```

Layer2의 보상 정보를 메모리에 로드합니다.

전역 업데이트 블록 배열의 길이를 가져옵니다.

```
if (rewardInfo.claimedLastIndex < globalLen) {
```

마지막으로 청구한 인덱스가 전역 업데이트 블록 배열의 길이보다 작은 경우에만 계속 진행합니다.

```
    uint256[] memory globalIndexes = l2UpdateBlock;
    // Index after the last claim
    uint i = rewardInfo.claimedLastIndex + 1;
    uint256 sCurIndex;
    uint256 sNextIndex;
    uint256 fIndex = layer2BlockIndexes.findIndexMemory(i);
    sCurIndex = fIndex;
    if (fIndex == len - 1) sNextIndex = fIndex;
    else sNextIndex = fIndex + 1;

```

전역 인덱스 배열을 메모리에 로드합니다.

마지막으로 청구한 인덱스 다음부터 시작합니다.

**`findIndexMemory`**를 사용하여 주어진 인덱스에 해당하는 위치를 찾습니다.

현재 인덱스와 다음 인덱스를 설정합니다.

```
    // Find pauseBlock Index.
    (uint256 pauseStartIndex, uint256 pauseEndIndex) = _nearbyPauseBlockIndex(layer2, i);
    uint256 maxCount = maxCommitCountForClaim;
    if (maxCount == 0) maxCount = MAX_COMMIT_CLAIM;
```

근처의 일시 중지 블록 인덱스를 찾습니다.

한 번에 처리할 최대 청구 수를 설정합니다(기본값: MAX_COMMIT_CLAIM, 200).

```
    uint256 count = 0;
    uint256 blockForLiquidity;
    uint256 gCurIndex;
    uint256 gNextIndex;
```

계산에 필요한 변수들을 초기화합니다.

```
    for (i; i < globalLen; i++) {
```

마지막으로 청구한 인덱스부터 전역 업데이트 블록 배열의 끝까지 반복합니다.

```
if (pauseStartIndex != 0 && pauseStartIndex <= i) {
    if (i <= pauseEndIndex || pauseEndIndex == 0) {
        continue;
    }
}
```

현재 인덱스가 일시 중지 기간에 속하는 경우 해당 인덱스를 건너뜁니다.

```
gCurIndex = layer2BlockIndexes[sCurIndex];
gNextIndex = layer2BlockIndexes[sNextIndex];
```

현재와 다음 글로벌 인덱스 값을 가져옵니다.

```
if (i < gNextIndex) {
    blockForLiquidity = globalIndexes[gCurIndex];
} else {
    blockForLiquidity = globalIndexes[gNextIndex];
    gCurIndex = gNextIndex;
    if (sNextIndex < layer2BlockIndexes.length - 1) {
        sNextIndex++;
        gNextIndex = layer2BlockIndexes[sNextIndex];
    }
}
```

현재 인덱스의 위치에 따라 유동성 블록을 결정합니다.

필요한 경우 인덱스를 업데이트합니다.

```
amount += (l2RewardAtBlock[globalIndexes[i]] * commitLayer2Tvl[layer2][blockForLiquidity]) / WEI_UINT;
uptoIndex = i;
count++;
```

현재 인덱스에 대한 세이뇨리지를 계산하여 총액에 더합니다.

처리한 마지막 인덱스를 업데이트합니다.

처리 횟수를 증가시킵니다.

```
        if (count >= maxCount) break;
        if (pauseEndIndex != 0 && i > pauseEndIndex) {
            (pauseStartIndex, pauseEndIndex) = _nearbyPauseBlockIndex(layer2, i);
        }
    }
}

```

최대 처리 수량에 도달하면 루프를 종료합니다.

현재 일시 중지 기간을 지나갔다면 다음 일시 중지 기간을 찾습니다.

layer2L2UpdateBlockIndexes[layer2] = 해당 layer2에서 일어난 commit에 대한 BlockIndex들

l2UpdateBlock = 모든 layer2에 대한 commit block

maxCommitCountForClaim은 어디서 초기화 값이 정해지는가?