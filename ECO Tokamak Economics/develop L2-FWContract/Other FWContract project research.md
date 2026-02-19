## Hop protocol

1. Contracts
  1. **Bridges**
    1. Accounting.sol - _credit 과 _debit을 이용하여서 잔액을 관리하는 컨트랙트
    1. BonderRegistry.sol - Bonder를 관리하는 컨트랙트
    1. Bridge.sol - L1, L2Bridge 컨트랙트에서 사용하는 컨트랙트, TransferRoot를 설정
    1. HopBridgeToken.sol - HopBridgeToken 컨트랙트 (Owner가 mint, burn가능)
    1. L1_Bridge.sol - L1의 Bridge기능을 하는 컨트랙트 (L2로 토큰을 입금하고 L2에서 토큰을 withdraw하고)
    1. L2_AmmWrapper.sol - L2에서 Swap기능이 있고 Swap을 하는 동시에 L2의 bridge의 send함수를 호출할 수 있게하였음
    1. L2_Bridge.sol - withdraw기능과 함께 추가적으로 다른 chain으로 보낼수 있는 기능이 있음
    1. SwapDataConsumer.sol - swapData struct 컨트랙트
  1. **connectors**
    1. Connector.sol
    1. L1_ArbitrumConnector.sol
    1. L1_OptimismConnector.sol
    1. L1_PolygonConnector.sol
    1. L1_XDaiConnector.sol
    1. L2_ArbitrumConnector.sol
    1. L2_OptimismConnector.sol
    1. L2_PolygonConnector.so**l**
    1. L2_XDaiConnector.sol
  1. governance
  1. interfaces
  1. libraries
  1. polygon
  1. saddle
  1. test
1. How to check 
  1. Check using Connection Contract
  1. **Since it is not in the same FW format as ours, we need to think more about the security method.**

## stargate protocol