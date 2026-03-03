## 작업 관련 링크

1. Rolling Hub Devnet : [https://docs.tokamak.network/home/~/changes/agYOWEeK7NUEeofss2bX/service-guide/rollup-hub/devnet/parameter-definitions](https://docs.tokamak.network/home/~/changes/agYOWEeK7NUEeofss2bX/service-guide/rollup-hub/devnet/parameter-definitions)
1. Fault Proofs: Decentralized Proposer : [https://docs.tokamak.network/home/~/changes/agYOWEeK7NUEeofss2bX/service-guide/rollup-hub/mainnet-beta/operation-guide/fault-proof-system/overview](https://docs.tokamak.network/home/~/changes/agYOWEeK7NUEeofss2bX/service-guide/rollup-hub/mainnet-beta/operation-guide/fault-proof-system/overview)
1. Thanos Github : [https://github.com/tokamak-network/tokamak-thanos](https://github.com/tokamak-network/tokamak-thanos)
1. FPS User Guide : https://www.notion.so/tokamak/FPS-User-Guide-1910e556ef5647d9ae0e685c85d214ea
1. https://www.notion.so/tokamak/tokamak-titan-canyon-execution-process-1ea7e4c6b31a43f5aa74c0dba8dae620
1. 

[[Fault Dispute Game]]

## PreRequirements

| **Dependency** | **Minimum Version** | **Recommend Version** | **Version Check Command** |
| --- | --- | --- | --- |
| git | `^2` | `Minimum version or higher` | git --version |
| go | `^1.21` | `^1.22.7 and earlier` | go version |
| node | `^20` | `Minimum version or higher` | node --version |
| pnpm | `^8` | `Minimum version or higher` | pnpm --version |
| foundry | `0.2.0 (a5efe4f)` | `0.2.0 (63fff35)` | forge --version |
| make | `^3`  | `Minimum version or higher` | make --version |
| jq | `^1.6` | `Minimum version or higher` | jq --version |
| direnv | `^2` | `Minimum version or higher`  | direnv --version |
| cargo |  1.78.0 (54d8815d0 2024-03-26) |  | cargo --version |

Change Foundry Version

```shell
> forge --version
forge 0.3.0 (5a8bd89)

find . -name "crate*" -type d
find . -name "testdat*" -type d

sudo rm -f ~/crates/chisel/benches/session_source.rs

sudo rm ./.foundry/foundry-rs/foundry/crates/chisel/benches/session_source.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/common/src/fmt/console.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/common/src/fmt/dynamic.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/common/src/fmt/mod.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/common/src/fmt/ui.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/evm/core/src/abi/HardhatConsole.json
sudo rm ./.foundry/foundry-rs/foundry/crates/evm/core/src/abi/console.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/evm/core/src/abi/hardhat_console.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/evm/core/src/abi/mod.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/forge/benches/test.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/forge/bin/cmd/geiger/error.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/forge/bin/cmd/geiger/find.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/forge/bin/cmd/geiger/mod.rs
sudo rm ./.foundry/foundry-rs/foundry/crates/forge/bin/cmd/geiger/visitor.rs
sudo rm ./.foundry/foundry-rs/foundry/testdata/cancun/cheats/BlobBaseFee.t.sol

> foundryup -C 63fff35 
> foundryup -C a5efe4f 

fail
```

How to install direnv

```shell
> brew install direnv
```

Change pnpm global

```shell
> export PATH=/Users/harvey/Library/pnpm/global/5:$PATH
```

## Install rollup Devnet

```shell
tokamak-thanos > ./install-devnet-packages.sh
```

```shell
tokamak-thanos > make build
```

## Solve ERROR 

1. pnpm lock error occur
```shell
toksmak-thanos > pnpm install --no-frozen-lockfile 
```

 2. [https://cloud.nx.app/runs/EXxpYJguJK](https://cloud.nx.app/runs/EXxpYJguJK) 에러 발생

1. docker 에러 발생
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b2296e18-a486-436d-abca-0a3c8100bc07/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCF3RIKG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T101553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2BBxsmN5vjXnLnebg%2BA5WRVxOjdiIr4ToclfY18%2BviLAiEAlm9hXKXzfv5NEt%2F4TP21RjHXZylNTZPR9dYl5I0GEw0q%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDKtx6L9GsnOpZ3If0ircA7maUiyMktHpcYRiuAgvDHvlIN%2FuWpABCc2yG9M1pPSxgMG8DizWSQKFwMGjtRyr6uCC7WcDRnklBk8Qv7yHj%2FL62jNAJCJFyPVpVED6%2FuXxsJusuRViRLAbM1%2FwbGPX%2BSPW5zUfhOhtizfoLVOo3mjIR4L7notdUGtaUobPnRzphNqJGhLOSZjaSqDWyeJwLxyy5KUDMetPgflZQKtXBjxZWwevknInKnd277x5siJPmtkutTNzZTBK8cnBLCmBOb173XPv01vSaBTjIGLVWDzF5DRkYdpIb4mtSNHY6B14WycgMPI7ZW%2FB9KqeHBRczOZ%2BFwhSxj6A6Ld2OV24KLNYPFjpnu4tAtWDmswl2mB6tmPIBGbJ564lv%2Bi614UlembPO6MSFpzZqVT141vqMLU0xljQIPj13eJ9bc7Tnow0S4SNW2bpdQpVSBwc5UlBJQOiDbOTTIYFWACi%2F1DbyPUWFXdE%2FhR2qQReu6%2F45nzqLEZLyHKJXaS8RrK6fv%2BmapxqxUB2lXt%2FqtZv0iU25l7WsDeAajmS4CF8QdFj%2FtK%2FSCX3J%2BENe7FyGtAYWLpKIp3VXYaa%2Feyeqs0qsqdPD%2BHpmZpCbHtjz5QBsuD3cZTy2GRSCxgfrv%2Bx0io0MJqZ28wGOqUBn%2FnRHlXUNDOB1UZwi6HG6hZSrMGscqpzNH3Nvl5NV7Fq%2BCbyCoCcG%2FJwqL2g4aBkm4cGLESWSycxFisQaf19GOrhWqtORdBVMMCmnIR4q8DG2H8rs08Z28DzZRkJx1aNd2vYhT0DXxgI%2BfUXbeXoR8Q5cRLfBZY%2FRMsoKuoqHo3Jjw8CXcQ1KJMw1rTp2zt6LAK0x6Y1jhAWIZKqpbf3p62GeIGc&X-Amz-Signature=6b8d8af79369967bd05b2bf9fdfc79732837b8bd3ec7b413b732fd3fbf45ac01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

  1. brew install cask
  1. docker 삭제
```
sudo rm -Rf /Applications/Docker.app
sudo rm -f /usr/local/bin/docker
sudo rm -f /usr/local/bin/docker-machine
sudo rm -f /usr/local/bin/docker-compose
sudo rm -f /usr/local/bin/docker-credential-desktop
sudo rm -f /usr/local/bin/docker-credential-ecr-login
sudo rm -f /usr/local/bin/docker-credential-osxkeychain
sudo rm -Rf ~/.docker
sudo rm -Rf ~/Library/Containers/com.docker.docker
sudo rm -Rf ~/Library/Application\ Support/Docker\ Desktop
sudo rm -Rf ~/Library/Group\ Containers/group.com.docker
sudo rm -f ~/Library/HTTPStorages/com.docker.docker.binarycookies
sudo rm -f /Library/PrivilegedHelperTools/com.docker.vmnetd
sudo rm -f /Library/LaunchDaemons/com.docker.vmnetd.plist
sudo rm -Rf ~/Library/Logs/Docker\ Desktop
sudo rm -Rf /usr/local/lib/docker
sudo rm -f ~/Library/Preferences/com.docker.docker.plist
sudo rm -Rf ~/Library/Saved\ Application\ State/com.electron.docker-frontend.savedState
sudo rm -f ~/Library/Preferences/com.electron.docker-frontend.plist

brew uninstall docker
brew uninstall docker-compose
```
  1. brew install —cask docker
  1. brew install docker-compose
  1. [https://docs.docker.com/desktop/setup/install/mac-install/](https://docs.docker.com/desktop/setup/install/mac-install/) 에서 docker desktop 설치

## docker execution result

```shell
toksmak-thanos > make devnet-up
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/809e4210-7023-44a8-990f-25599a03ea4d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LWUHSG4%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuqwCO%2Fl3L6PyWfaC7kwPS7evO5%2BpGMGisshdm6Zc%2FcwIhAJCmlzMaiESdy9Sqn7EDjfbkR0qH4FGuzmemIq2q1xgyKv8DCHkQABoMNjM3NDIzMTgzODA1Igw1GzJIxP1hRSAtk%2Boq3ANxvI7UrLFPs2vNtcuQFDveZEpG%2BqriYwrTH3IvIzsL98hDZtqcYjpPCHgR2IaP60RRwjuQzO3Fd6KOKgSfA%2Ffwo5e7iFRg%2BW8DRs82YiI97dswhDdx5X0KU6g%2FYDKJzf%2FyAW4Fcw2cXI%2BxafsNEB0oq4G01HEiA%2FT74px2FYe37SAHlBmvCyVJcHqrkLaOaBCYVi6HzbjHFuEfg3vgR4klCnv4iQGgx2vqKPQKrOwcFvdbHngJM1lEb2eAu9KV1j0BueGHP7WD%2FM0ll%2BmKwN2Pk%2F3Bf2J9GIVRY5POj0OYOK588%2Fpov0c81SfEIKqVj2CzH26sewZwoxR7TP60tBGLNmfu8K0gNxc6%2BGM133hNbPg6KksHgOjEqcIPR%2FDsJc1LCciGPCo2u8VJaS%2BVJWG%2B6Rpvn8kTV%2Bnc1O1dIPynDanHjIQJOCPchiODehArey1LW6WDMt%2B8yPISgC8IB6QC5rrfRm%2FTZ8P2JClXme5jBB7kaDCcnvOUJd7jPQG0TKhfh%2F4kR3ZhXk7GB9zuhuakI6ukBZudIhwMn9suXxpEyyc2YGh5TN%2B9bINKckMmo80sL2GUMXPDx%2FddC3DwwWWCyh0PNevnz3y3HvQGyDILDJJ5EhkyCUuE4U4cLTDX%2BtrMBjqkAcZXHKo6NwcE6UVZFtFaIYvzcgX3vKJDdPhhgSHHH5zFFzsQNPMcqtJWSqg%2BdprB2kbNRxLq4jXl3U0xF4nzr4NJH3vsoaiZ108B0m7qvEn1yb0vPQGgUYKBQG%2BKbYFZM5izxdmYQJvTdjrSV2Kcqd8g5jVS6QGa9w8t61n19Nhfh0xG47T%2FNAL3nt74VoOsJQX16%2FMyxPOwkewl%2BQJu%2BsB9W1%2B2&X-Amz-Signature=033f1bc8a02d5c50a6790d11d343ab2b2e80405ec0a8369b7b936e8575ce8cbc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## op-challenger setting

      OP_CHALLENGER_TRACE_TYPE: cannon,<Game_Type : fast>

### **Finding the Required Parameters**

1. **Retrieve Output Roots Using L2 Ethereum RPC: **
  - `--l2.outputroot`: The output root of the block before the block you are claiming, serving as the prior state.evd
  -  `--l2.claim`: The output root of the specific L2 block you're claiming is correct.
```bash
curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"optimism_outputAtBlock","params":["<L2_BLOCK_NUMBER>"],"id":1}' \
<L2_URL>

curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"optimism_outputAtBlock","params":["120"],"id":1}' \
http://localhost:9545

curl -X POST -H "Content-Type: application/json" \
--data '{"jsonrpc":"2.0","method":"optimism_outputAtBlock","params":["0x10"],"id":1}' \
http://localhost:9545

curl -X POST -H "Content-Type: application/json" \ --data '{"jsonrpc":"2.0","method":"optimism_outputAtBlock","params":["<0x11>"],"id":1}' \ http://localhost:7545

curl http://localhost:7545 \
 -X POST \
 -H "Content-Type: application/json" \
 --data '{"method":"optimism_outputAtBlock","params":["0x6DAA86C"],"id":1,"jsonrpc":"2.0"}'
 
 
curl http://localhost:7545 \
 -X POST \
 -H "Content-Type: application/json" \
 --data '{"method":"optimism_outputAtBlock","params":["0x11"],"id":1,"jsonrpc":"2.0"}'
 
curl http://localhost:7545 \
 -X POST \
 -H "Content-Type: application/json" \
 --data '{"method":"optimism_outputAtBlock","params":["0x12"],"id":1,"jsonrpc":"2.0"}'

op-node에 요청해야함
```
1. **Find the Correct Claim Using ****`eth_getBlockByNumber`**
  - You need to use the RPC URLs for both L1 and L2 to get the `--l1.head`, `--l2.head`: 
```bash
//Layer 1
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}' \
-H "Content-Type: application/json" <L1_URL>

curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}' \
-H "Content-Type: application/json" http://localhost:8545

//Layer 2
curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}' \
-H "Content-Type: application/json" <L2_URL>

curl -X POST --data '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["latest", true],"id":1}' \
-H "Content-Type: application/json" http://localhost:9545

```
1. **Cannon Command Breakdown**
```javascript
cd ../op-program
make op-program

cd ../cannon
make cannon

./bin/cannon load-elf --path=../op-program/bin/op-program-client.elf

./bin/cannon run \
  --pprof.cpu \
  --info-at '%10000000' \
  --proof-at never \
  --input ./state.json \
  -- \
  ../op-program/bin/op-program \
  --l2.genesis /path/to/genesis-l2.json \
  --rollup.config /path/to/rollup.json \
  --l1.rpckind debug_g.eth \
  --l1 <L1_URL> \
  --l2 <L2_URL> \
  --l1.head <L1_HEAD> \ 가장 최신블록 Head (Hash)
  --l2.head <L2_HEAD> \ 가장 최신블록 Head (Hash)
  --l2.outputroot <L2_OUTPUT_ROOT> \ blockNumber가 18번이라면 17번의 Outputroot
  --l2.claim <L2_CLAIM> \ blockNumber가 18번이라면 18번의 outputroot
  --l2.blocknumber <L2_BLOCK_NUMBER> \ 18
  --datadir /tmp/fpp-database \
  --log.format terminal \
  --server
```

```javascript
./bin/cannon run \
  --pprof.cpu \
  --info-at '%10000000' \
  --proof-at never \
  --input ./state.json \
  -- \
  ../op-program/bin/op-program \
  --l2.genesis /path/to/genesis-l2.json \
  --rollup.config /path/to/rollup.json \
  --l1.rpckind debug_g.eth \
  --l1 http://localhost:8545 \
  --l2 http://localhost:9545 \
  --l1.head 0x72d0adba5109095da99ba0afdd05ab8a0f2c6f62a93b83082bba50e22ca5f9e6 \ 
  --l2.head 0xcc347abd6ac558d68fb7054232de4bb6eedf021c4c84e3bfb723769fb15e6204 \ 
  --l2.outputroot 0xdc4eee3a1e8a523602c4c9bf2722460deb0596d77d13086452695ddceadf6851 \ 
  --l2.claim 0xa84a89ba9faa9973126218446f0a825b53c5b93a81555a18f38cd77d90f402d2 \
  --l2.blocknumber 18 \
  --datadir /tmp/fpp-database \
  --log.format terminal \
  --server
  
  
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a8d88399-1f09-4932-b7f2-b45f35c499d0/E081180B-F53C-4098-B162-484FCC39E2F5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LWUHSG4%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T083524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuqwCO%2Fl3L6PyWfaC7kwPS7evO5%2BpGMGisshdm6Zc%2FcwIhAJCmlzMaiESdy9Sqn7EDjfbkR0qH4FGuzmemIq2q1xgyKv8DCHkQABoMNjM3NDIzMTgzODA1Igw1GzJIxP1hRSAtk%2Boq3ANxvI7UrLFPs2vNtcuQFDveZEpG%2BqriYwrTH3IvIzsL98hDZtqcYjpPCHgR2IaP60RRwjuQzO3Fd6KOKgSfA%2Ffwo5e7iFRg%2BW8DRs82YiI97dswhDdx5X0KU6g%2FYDKJzf%2FyAW4Fcw2cXI%2BxafsNEB0oq4G01HEiA%2FT74px2FYe37SAHlBmvCyVJcHqrkLaOaBCYVi6HzbjHFuEfg3vgR4klCnv4iQGgx2vqKPQKrOwcFvdbHngJM1lEb2eAu9KV1j0BueGHP7WD%2FM0ll%2BmKwN2Pk%2F3Bf2J9GIVRY5POj0OYOK588%2Fpov0c81SfEIKqVj2CzH26sewZwoxR7TP60tBGLNmfu8K0gNxc6%2BGM133hNbPg6KksHgOjEqcIPR%2FDsJc1LCciGPCo2u8VJaS%2BVJWG%2B6Rpvn8kTV%2Bnc1O1dIPynDanHjIQJOCPchiODehArey1LW6WDMt%2B8yPISgC8IB6QC5rrfRm%2FTZ8P2JClXme5jBB7kaDCcnvOUJd7jPQG0TKhfh%2F4kR3ZhXk7GB9zuhuakI6ukBZudIhwMn9suXxpEyyc2YGh5TN%2B9bINKckMmo80sL2GUMXPDx%2FddC3DwwWWCyh0PNevnz3y3HvQGyDILDJJ5EhkyCUuE4U4cLTDX%2BtrMBjqkAcZXHKo6NwcE6UVZFtFaIYvzcgX3vKJDdPhhgSHHH5zFFzsQNPMcqtJWSqg%2BdprB2kbNRxLq4jXl3U0xF4nzr4NJH3vsoaiZ108B0m7qvEn1yb0vPQGgUYKBQG%2BKbYFZM5izxdmYQJvTdjrSV2Kcqd8g5jVS6QGa9w8t61n19Nhfh0xG47T%2FNAL3nt74VoOsJQX16%2FMyxPOwkewl%2BQJu%2BsB9W1%2B2&X-Amz-Signature=8eee5491a8bbdf0b10c55859c687a04ea67f1345b84d2832d5d24e36abbcae31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**OP-Programs (How to Verify Claim[**[**link**](https://drive.google.com/file/d/1Nm6rzQkkLm_UbjLW3iYHRvrorLY5wrDp/view)**])**

```json
//op-challenger 하나 더 생성 (필요없음)
make op-challenger

challenger:
    user: "1000"
    image: us-docker.pkg.dev/oplabs-tools-artifacts/images/op-challenger:v0.2.11
    command:
      - "op-challenger"
      - "--l1-eth-rpc=http://sepolia-el-1:8545"
      - "--l1-beacon=http://sepolia-cl-1:5051"
      - "--l2-eth-rpc=http://op-sepolia-el-1:8545"
      - "--rollup-rpc=http://op-sepolia-cl-1:5051"
      - "--selective-claim-resolution"
      - "--private-key=...."
      - "--network=..."
      - "--datadir=/data"
      - "--cannon-prestates-url=..."
    volumes:
      - "./challenger-data:/data"

DISPUTE_GAME_FACTORY=$(jq -r .DisputeGameFactoryProxy .devnet/addresses.json)

./op-challenger/bin/op-challenger \
  --trace-type cannon \
  --l1-beacon unset \
  --l1-eth-rpc http://localhost:8545 \
  --rollup-rpc http://localhost:7545 \ (opNode의 rpc)
  --game-factory-address $DISPUTE_GAME_FACTORY \
  --datadir temp/challenger-data \
  --cannon-rollup-config .devnet/rollup.json  \
  --cannon-l2-genesis .devnet/genesis-l2.json \
  --cannon-bin ./cannon/bin/cannon \
  --cannon-server ./op-program/bin/op-program \
  --cannon-prestate ./op-program/bin/prestate.json \
  --l2-eth-rpc http://localhost:9545 \
  --mnemonic "test test test test test test test test test test test junk" \
  --hd-path "m/44'/60'/0'/0/8" \
  --num-confirmations 1
  
-----------------
 
//op-program을 이용해서 Claim verified하는 법
cd op-program
make
cd ../
 
 
make cannon-prestate
cd cannon && make

cd op-program
cd bin
./op-program \
 --l1 http://localhost:8545 \
 --l2 http://localhost:9545 \
 --l1.head 최근 L1 block Hash \
 --l2.head 최근 L2 block Hash \
 --l2.outputroot 17번의 outputroot \
 --l2.claim 18번의 outputroot \ 
 --l2.blocknumber 18 \
 --datadir /tmp/fpp-database \
 --log.format terminal \
 --rollup.config /Users/harvey/Desktop/project/FaultProofTest/tokamak-thanos/.devnet/rollup.json \
 --l2.genesis /Users/harvey/Desktop/project/FaultProofTest/tokamak-thanos/.devnet/genesis-l2.json \


./bin/op-program \
 --l1 http://localhost:8545 \
 --l2 http://localhost:9545 \
 --l1.head 0x7278715e4575846391c9fe8578df0e192599ac242594ddb204830f388ef340a9 \
 --l2.head 0x4cb41f2b43a58ecb644876d7e74879d38e82323b566be10c574ed8c616636595 \
 --l2.outputroot 0x305235347405670e57158880474be664c2f8ae371426c65bcbc7a418bb37bfae \
 --l2.claim 0x69ff13eef99f599ede25fe780e4525bec78f46f863a06fa8c2cfb12db5cd05f1 \ 
 --l2.blocknumber 18 \
 --datadir /tmp/fpp-database \
 --log.format terminal \
 --rollup.config /Users/harvey/Desktop/project/FaultProofTest/tokamak-thanos/.devnet/rollup.json \
 --l2.genesis /Users/harvey/Desktop/project/FaultProofTest/tokamak-thanos/.devnet/genesis-l2.json \

 

```

## How to make the Game

```
//생성된 게임 리스트 보기
docker exec -it 7df98d0e9476(Container ID) op-challenger list-games \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d (fixed Value)

**docker exec -it 1ef669ae11e7 op-challenger list-games \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d


./bin/op-challenger list-games \
  --l1-eth-rpc http://l1:8545/ \
  --game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d**


//게임 생성하기
docker exec -it 7df98d0e9476 op-challenger create-game \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d \
--output-root 0x4f65f4c41291764702b14a1ba4ffeb4fab19025791609109a86a7d73e67131ac \
--l2-block-num 0x12

**docker exec -it 1ef669ae11e7 op-challenger create-game \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d \
--output-root 0x99e34aed13a5d37d2668dfa609315a77ec8f899c7f510e296ba1c44765397871 \
--l2-block-num 0x6b1

docker exec -it 1ef669ae11e7 op-challenger create-game \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d \
--output-root 0x37ddb4e90759b885b3b4004eecb5653b937ece40bd1e5d702420ed62a8b84790 \
--l2-block-num 0x1073

0x37ddb4e90759b885b3b4004eecb5653b937ece40bd1e5d702420ed62a8b8479c


docker exec -it 1ef669ae11e7 op-challenger create-game \
--l1-eth-rpc http://l1:8545/ \
--game-factory-address 0x11c81c1A7979cdd309096D1ea53F887EA9f8D14d \
--output-root 0xba5938c99b2fbf2897222b1ad52debbff0ad285aeb35ca6bed52a1e8a13d2b44 \
--l2-block-num 0x84f

0xba5938c99b2fbf2897222b1ad52debbff0ad285aeb35ca6bed52a1e8a13d2b4f**

//생성된 게임의 결과 보기
docker exec -it 7df98d0e9476 op-challenger list-claims \
--l1-eth-rpc http://l1:8545/ \
--game-address 0x0E0d57F13aD481b7f8A737bad5429949573E8077 (list-games에서 나온 game address)

**docker exec -it 1ef669ae11e7 op-challenger list-claims \
--l1-eth-rpc http://l1:8545/ \
--game-address 0x7bB80cE881FF65f9334ab556b400B988f3262128 

docker exec -it 0a8d4c14bd85 op-challenger list-claims \
--l1-eth-rpc http://l1:8545/ \
--game-address 0x4A7C0948dc4C675A8FF4F97133309b16C3b53b3a 

docker exec -it 1ef669ae11e7 op-challenger list-claims \
--l1-eth-rpc http://l1:8545/ \
--game-address 0x6ef36C36671055CF7B3CCDE08610be5eF233ED08


docker exec -it 1ef669ae11e7 op-challenger list-claims \
--l1-eth-rpc http://l1:8545/ \
--game-address 0x1E4cb5B6aBBD2f897C3C67e93D407A156AA3B543

0x1E4cb5B6aBBD2f897C3C67e93D407A156AA3B543**


//attack or defend
docker exec -it 7df98d0e9476 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x38C07a2e7E1455B2c92c2992C5263669937Aa9D7 \
  --attack \
  --parent-index latest \
  --claim 0x4f65f4c41291764702b14a1ba4ffeb4fab19025791609109a86a7d73e67131ad
  
**docker exec -it 1ef669ae11e7 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x7bB80cE881FF65f9334ab556b400B988f3262128 \
  --attack \
  --parent-index latest \
  --claim 0x9f6461708f7ba1a4517bfb421abb91a0fc047f719381aa27caad3e13c886b891
  
docker exec -it 1ef669ae11e7 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x06B9F754E74E733109B11695f14DFf2f8d0467f2 \
  --attack \
  --parent-index latest \
  --claim 0xba5938c99b2fbf2897222b1ad52debbff0ad285aeb35ca6bed52a1e8a13d2b44
  
docker exec -it 1ef669ae11e7 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x6ef36C36671055CF7B3CCDE08610be5eF233ED08 \
  --attack \
  --parent-index latest \
  --claim 0xba5938c99b2fbf2897222b1ad52debbff0ad285aeb35ca6bed52a1e8a13d2b44**

docker-compose exec challenger op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x71a4CA19625aF5e2D89303f68f2227Ed63D8c387 \
  --defend \
  --parent-index latest \
  --claim 0x4f65f4c41291764702b14a1ba4ffeb4fab19025791609109a86a7d73e67131ad
  
  
**docker exec -it 0a8d4c14bd85 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x1D3283d1a7c6880fD3fFB7d8C0cB39D46C9147D1 \
  --defend \
  --parent-index 0 \
  --claim 0x4f65f4c41291764702b14a1ba4ffeb4fab19025791609109a86a7d73e67131ad
  
docker exec -it 1ef669ae11e7 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x7bB80cE881FF65f9334ab556b400B988f3262128 \
  --defend \
  --parent-index 2 \
  --claim 0x9f6461708f7ba1a4517bfb421abb91a0fc047f719381aa27caad3e13c886b891
  
  
docker exec -it 1ef669ae11e7 op-challenger move \
  --l1-eth-rpc http://l1:8545/ \
  --game-address 0x06B9F754E74E733109B11695f14DFf2f8d0467f2 \
  --defend \
  --parent-index 2 \
  --claim 0xba5938c99b2fbf2897222b1ad52debbff0ad285aeb35ca6bed52a1e8a13d2b4f**
```