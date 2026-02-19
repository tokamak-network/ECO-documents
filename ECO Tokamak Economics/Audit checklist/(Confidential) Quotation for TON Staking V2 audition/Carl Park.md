Zena님, Carl님 연락처 공유 드립니다.

- 이름: 박주형(Carl)
- 핸드폰: 01020716047
- 이메일: [dkdkajej@gmail.com](mailto:dkdkajej@gmail.com)

참고로 가장 최근 계약은 프리랜서가 아닌 사업자로 진행하였다고 합니다.

추가로 일정상 업무 진행이 쉽지 않거나, 단가가 오를 수 있다고 합니다.이전에 진행한 업무 토대로 일정 개요 공유 드립니다. 만약 함께 업무하신다면 참고해주시면 좋을것 같습니다.

> [업무 일정 개요]
> - 오딧 파악 및 견적: 1~3일
> - 오딧: 2~3주 내용이 많으면 4주까지도 걸립니다.
> 
> (평균 오딧 기간 보다, 단기로 요청하게 되면 단가가 높아집니다.)
> 
> - 결과 보고서 전달: 1일

감사합니다.

## 진행사항 

- 2025.1.9 : 오딧 가능여부 문의 메일 보냄 
- 오딧 견적 답신 옴. 2025.1.13

![](images/117f54f18126.png)

문의 주신 오딧 견적 알려드립니다.

첨부하신 [문서](https://tokamak.notion.site/Audit-Contents-Of-Ton-Staking-V2-5-175d96a400a380779395cba6edc3bf0d)에 따라 아래 코드베이스를 기준으로 계산했습니다.

github: [https://github.com/tokamak-network/ton-staking-v2](https://github.com/tokamak-network/ton-staking-v2)

branch: v2.5-audit-request

commit hash: 9d96b55b92f079b329ec70d593b69f74b44bf6cb

29개의 파일, 2935 라인 기준으로 **오딧 예상 소요 시간은 18 영업일이며, 비용은 15,000 USD 혹은 2,200 만원 입니다.**

오딧 대상 재선정 및 코드 라인 수는 아래 내용을 참고해주시면 감사하겠습니다.

첨부하신 문서의 Contract scope항목에 있는 solidity 파일들은 아래와 같이 import 를 하고 있습니다. (interface 및 open zeppelin 제외)

- contracts/proxy/DAOCommitteeProxy2.sol

- contracts/dao/StorageStateCommittee.sol

- contracts/proxy/ProxyStorage2.sol

- contracts/dao/DAOCommittee_V1.sol

- contracts/dao/lib/Agenda.sol

- contracts/dao/StorageStateCommittee.sol

- contracts/proxy/ProxyStorage2.sol

- contracts/dao/StorageStateCommitteeV2.sol

- contracts/dao/DAOCommitteeOwner.sol

- contracts/dao/StorageStateCommittee.sol

- contracts/proxy/ProxyStorage2.sol

- contracts/dao/StorageStateCommitteeV2.sol

- contracts/stake/managers/SeigManagerV1_3.sol

- contracts/proxy/ProxyStorage.sol

- contracts/common/AuthControlSeigManager.sol

- contracts/common/AuthRoleSeigManager.sol

- contracts/stake/managers/SeigManagerStorage.sol

- contracts/stake/managers/SeigManagerV1_1Storage.sol

- contracts/stake/managers/SeigManagerV1_3Storage.sol

- contracts/stake/managers/DepositManagerV1_1.sol

- contracts/proxy/ProxyStorage.sol

- contracts/common/AccessibleCommon.sol

- contracts/stake/managers/DepositManagerStorage.sol

- contracts/stake/managers/DepositManagerV1_1Storage.sol

- contracts/layer2/L1BridgeRegistryV1_1.sol

- contracts/proxy/ProxyStorage.sol

- contracts/common/AuthControlL1BridgeRegistry.sol

- contracts/common/AuthRoleL1BridgeRegistry.sol

- contracts/layer2/L1BridgeRegistryStorage.sol

- contracts/layer2/Layer2ManagerV1_1.sol

- contracts/layer2/Layer2ManagerStorage.sol

- contracts/proxy/ProxyStorage.sol

- contracts/common/AccessibleCommon.sol

- contracts/layer2/OperatorManagerV1_1.sol

- contracts/layer2/OperatorManagerStorage.sol

- contracts/dao/CandidateAddOnV1_1.sol

- contracts/proxy/ProxyStorage.sol

- contracts/common/AccessibleCommon.sol

- contracts/dao/CandidateStorage.sol

- contracts/dao/CandidateAddOnStorage.sol

따라서 이번 오딧은 아래 29개의 파일을 대상으로 합니다.

contracts/proxy/DAOCommitteeProxy2.sol

contracts/dao/StorageStateCommittee.sol

contracts/proxy/ProxyStorage2.sol

contracts/dao/DAOCommittee_V1.sol

contracts/dao/lib/Agenda.sol

contracts/dao/DAOCommitteeOwner.sol

contracts/dao/StorageStateCommitteeV2.sol

contracts/stake/managers/SeigManagerV1_3.sol

contracts/proxy/ProxyStorage.sol

contracts/common/AuthControlSeigManager.sol

contracts/common/AuthRoleSeigManager.sol

contracts/stake/managers/SeigManagerStorage.sol

contracts/stake/managers/SeigManagerV1_1Storage.sol

contracts/stake/managers/SeigManagerV1_3Storage.sol

contracts/stake/managers/DepositManagerV1_1.sol

contracts/common/AccessibleCommon.sol

contracts/stake/managers/DepositManagerStorage.sol

contracts/stake/managers/DepositManagerV1_1Storage.sol

contracts/layer2/L1BridgeRegistryV1_1.sol

contracts/common/AuthControlL1BridgeRegistry.sol

contracts/common/AuthRoleL1BridgeRegistry.sol

contracts/layer2/L1BridgeRegistryStorage.sol

contracts/layer2/Layer2ManagerV1_1.sol

contracts/layer2/Layer2ManagerStorage.sol

contracts/layer2/OperatorManagerV1_1.sol

contracts/layer2/OperatorManagerStorage.sol

contracts/dao/CandidateAddOnV1_1.sol

contracts/dao/CandidateStorage.sol

contracts/dao/CandidateAddOnStorage.sol

그리고 cloc 결과에 따라 2935 라인을 기준으로 진행할 예정입니다.

cloc \

contracts/proxy/DAOCommitteeProxy2.sol \

contracts/dao/StorageStateCommittee.sol \

contracts/proxy/ProxyStorage2.sol \

contracts/dao/DAOCommittee_V1.sol \

contracts/dao/lib/Agenda.sol \

contracts/dao/DAOCommitteeOwner.sol \

contracts/dao/StorageStateCommitteeV2.sol \

contracts/stake/managers/SeigManagerV1_3.sol \

contracts/proxy/ProxyStorage.sol \

contracts/common/AuthControlSeigManager.sol \

contracts/common/AuthRoleSeigManager.sol \

contracts/stake/managers/SeigManagerStorage.sol \

contracts/stake/managers/SeigManagerV1_1Storage.sol \

contracts/stake/managers/SeigManagerV1_3Storage.sol \

contracts/stake/managers/DepositManagerV1_1.sol \

contracts/common/AccessibleCommon.sol \

contracts/stake/managers/DepositManagerStorage.sol \

contracts/stake/managers/DepositManagerV1_1Storage.sol \

contracts/layer2/L1BridgeRegistryV1_1.sol \

contracts/common/AuthControlL1BridgeRegistry.sol \

contracts/common/AuthRoleL1BridgeRegistry.sol \

contracts/layer2/L1BridgeRegistryStorage.sol \

contracts/layer2/Layer2ManagerV1_1.sol \

contracts/layer2/Layer2ManagerStorage.sol \

contracts/layer2/OperatorManagerV1_1.sol \

contracts/layer2/OperatorManagerStorage.sol \

contracts/dao/CandidateAddOnV1_1.sol \

contracts/dao/CandidateStorage.sol \

contracts/dao/CandidateAddOnStorage.sol

29 text files.

29 unique files.

0 files ignored.

[github.com/AlDanial/cloc](http://github.com/AlDanial/cloc) v 2.02  T=0.02 s (1440.6 files/s, 230144.0 lines/s)

-------------------------------------------------------------------------------

Language                     files          blank        comment           code

-------------------------------------------------------------------------------

Solidity                        29            804            894           2935

-------------------------------------------------------------------------------

SUM:                            29            804            894           2935

-------------------------------------------------------------------------------