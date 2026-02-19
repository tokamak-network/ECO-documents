> WTON : [https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2](https://etherscan.io/address/0xc4A11aaf6ea915Ed7Ac194161d2fC9384F15bff2)

> DepositManager :  0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e [https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#writeProxyContract](https://etherscan.io/address/0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e#writeProxyContract)

> Talken  Info : {"oldLayer":"0xb9d336596ea2662488641c4ac87960bfdcb94c6e","newLayer":"**0x36101b31e74c5E8f9a9cec378407Bbb776287761**","operator":"**0xcc2f386adca481a00d614d5aa77a30984f264a07**","name":"Talken"}

**dev account: 0xba4EE4FAec3D13CeaB45BbE5F9700C5633c1e2f9**

1. stake -> 저희 EOA로 1150 TON staking (simple.staking.tokamak.network)
  - tx : [https://etherscan.io/tx/0x15838ef8765f38c2f46e28c272f62887989a0f62867fe31d90a7a2985799cd85](https://etherscan.io/tx/0x15838ef8765f38c2f46e28c272f62887989a0f62867fe31d90a7a2985799cd85)
1. approve WTON to DepositManager 
  - approve (0x0b58ca72b12f01fc05f8f252e226f3e2089bd00e ,  1001000000000000000000000000000) 
  - tx : [https://etherscan.io/tx/0xa5af5cd4311d519ebaec7a25ea90634c071c1bc8d45c00de45cd0de41bbf637c](https://etherscan.io/tx/0xa5af5cd4311d519ebaec7a25ea90634c071c1bc8d45c00de45cd0de41bbf637c)
1. stake -> etherscan으로 1000.0001 TON을 operator 명의로 stake
  - deposit ( **0x36101b31e74c5E8f9a9cec378407Bbb776287761, **0xcc2f386adca481a00d614d5aa77a30984f264a07, 1000000100000000000000000000000 ) 
  - tx: [https://etherscan.io/tx/0x46c5cd56b1e89040c1dc14a029860aa0368b2d3417b26d4fc61d80f04558becb](https://etherscan.io/tx/0x46c5cd56b1e89040c1dc14a029860aa0368b2d3417b26d4fc61d80f04558becb)
1. update seignorage => 약 1090 TON을 받을 수 있습니다 (simple.staking.tokamak.network)
  - tx: [https://etherscan.io/tx/0x709041fe070c007f8dcfdd28fd718fcdc6671e5fef0354541cd0fda5c2ca255f](https://etherscan.io/tx/0x709041fe070c007f8dcfdd28fd718fcdc6671e5fef0354541cd0fda5c2ca255f)
1. unstake -> 전체 물량 unstake (simple.staking.tokamak.network)
  - [https://etherscan.io/tx/0xc183dc0bdfd3b46afc970170822fc4056c81379b0ef481242b504195f91d3ae2](https://etherscan.io/tx/0xc183dc0bdfd3b46afc970170822fc4056c81379b0ef481242b504195f91d3ae2)
1. 14일 이후에 withdraw (simple.staking.tokamak.network)
  - 

 