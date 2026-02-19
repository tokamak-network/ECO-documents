> ***operatorCheck는 candidate 주소가 올바른지 확인하는 데 사용된다. 유효한 candidate 주소로 실제 privateLayer2의 존재 여부를 확인할 수 있다. 현재 Tokamak Network의 ***[***모든 candidate***](https://github.com/tokamak-network/ton-staking-v2/blob/ton-staking-v2/docs/deployed-addresses-mainnet.md#layer-addresses)***는 privateLayer2가 아니다.***

1. ***tokamak1 — ******`0xea8e2ec08dcf4971bdcdfffe21439995378b44f3`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0xea8e2ec08dcf4971bdcdfffe21439995378b44f3`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 399108090210603611579491777921948***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0xea8e2ec08dcf4971bdcdfffe21439995378b44f3`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***DXM Corp — ******`0x566b98a715ef8f60a93a208717d9182310ac3867`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0x566b98a715ef8f60a93a208717d9182310ac3867`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 3738525159697347230515592172026***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0x566b98a715ef8f60a93a208717d9182310ac3867`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***DSRV — ******`0x8dfcbc1df9933c8725618015d10b7b6de2d2c6f8`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0x8dfcbc1df9933c8725618015d10b7b6de2d2c6f8`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 14590249931561149210257934351609***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0x8dfcbc1df9933c8725618015d10b7b6de2d2c6f8`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***Talken — ******`0xcc2f386adca481a00d614d5aa77a30984f264a07`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0xcc2f386adca481a00d614d5aa77a30984f264a07`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 1067764479327083241173068949634***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0xcc2f386adca481a00d614d5aa77a30984f264a07`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***staked — ******`0x247a0829c63c5b40dc6b21cf412f80227dc7fb76`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0x247a0829c63c5b40dc6b21cf412f80227dc7fb76`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 30113407412399409517522318085915***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0x247a0829c63c5b40dc6b21cf412f80227dc7fb76`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***level — ******`0xd1820b18be7f6429f1f44104e4e15d16fb199a43`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0xd1820b18be7f6429f1f44104e4e15d16fb199a43`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 5289723851212897571184406285920***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0xd1820b18be7f6429f1f44104e4e15d16fb199a43`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***decipher — ******`0xba33eddfd3e4e155a6da10281d9069bf44743228`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0xba33eddfd3e4e155a6da10281d9069bf44743228`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 2982781327690057607244190490473***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0xba33eddfd3e4e155a6da10281d9069bf44743228`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***DeSpread — ******`0xfc9c403993bea576c28ac901bd62640bff8b057a`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0xfc9c403993bea576c28ac901bd62640bff8b057a`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 3196201675391513285679975556980***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0xfc9c403993bea576c28ac901bd62640bff8b057a`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***Danal Fintech — ******`0x887af02970781a088962dbaa299a1eba8d573321`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0x887af02970781a088962dbaa299a1eba8d573321`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 2556734458887943769565832292809***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0x887af02970781a088962dbaa299a1eba8d573321`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***
1. ***Hammer DAO — ******`0x42adfaae7db56b294225ddcfebef48b337b34b23`***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"operatorCheck(address)(uint256)" **`0x42adfaae7db56b294225ddcfebef48b337b34b23`** \
--rpc-url https://ethereum-rpc.publicnode.com *
***—> 1135498633785642708986484508250***
  - *cast call 0xDD9f0cCc044B0781289Ee318e5971b0139602C26 \
"privateLayer2(address)(bool)" **`0x42adfaae7db56b294225ddcfebef48b337b34b23`** \
--rpc-url https://ethereum-rpc.publicnode.com*
***—> false (not privateLayer2)***