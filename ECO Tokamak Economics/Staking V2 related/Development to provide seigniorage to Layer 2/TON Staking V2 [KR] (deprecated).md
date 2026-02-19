TON Staking v2 는 V2 백서의 내용을 반영하기 위한 개발이므로,  [백서](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2)를 먼저 읽고 오시기 바랍니다. 

V2에는 V1에는 존재하지 않는 L2 시퀀서라는 개념이 도입되었으며,  새로 발행되는 톤 시뇨리지의 일부를 L2 시퀀서에게 분배하는 내용이 추가된 내용입니다.  V2는 기존  V1 컨트랙에서 보강된 시스템이기 때문에, V1에 존재하는 컨트랙일 경우, 업그레이드하여 구현합니다.  따라서 본 글을 읽으시는 독자는 V1 시스템을 알고 있어야 합니다.  톤스테이킹 V1에 대해서 더 자세히 알고 싶은 분은 [미디움 글](https://medium.com/tokamak-network/looking-into-tokamak-networks-staking-contract-7d5f9fa057e7)을 참고하시기 바랍니다. 

# V2에서 변경하는 사항들  

## 시뇨리지 분배의 변화 

V2에서는  발행된 시뇨리지에서 톤의 총 발행량과  L2 레이어의 톤 유동성의 비율만큼의 시뇨리지를 L2 시퀀서에게 지급합니다.  (백서 참고) 

![V1 의 시뇨리지 분배](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6e2a8516-0927-4c97-8fe1-393a9582e2b1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.49.36.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=5b51c64d60ae46e04150d8d1e28564f63e2501bf709d13570fff12b889dc73d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![V2의 시뇨리지 분배 ](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/367faed2-b282-46f3-b4ad-0225993e226d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.50.15.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=5b1c62276e8d92efd6eef1517376fbe91588e38de29b37c2652f1c3737ab95f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Layer2Candidate 추가  

V1에서는 DAOCandidate Layer2 가 존재하였습니다. DAOCandidate 는 다오의 위원회가 될 수 있는 Layer2 입니다.

V2에서 추가되는 Layer2Candidate는 DAOCandidate의 모든 기능을 상속받아 다오의 위원회가 될 수 있음과 동시에 Layer2의 시퀀서가 시뇨리지를 받을 수 있습니다.    

## 스테이킹 금액을 즉시 Layer2 유동성으로 사용 가능합니다. 

Layer2Candidate 에서 추가된 기능으로, 해당 Layer2의 독자적인 예치 기능을 언스테이킹 기능과 연계하여,  인출과 동시에 L2에 예치하는(withdrawAndDepositL2) 함수를 제공합니다.   

withdrawAndDepositL2 함수는 스테이킹 금액을 언스테이킹하면서 동시에 Layer2에 예치하는 기능입니다. 이 기능이 V1과 비교했을때의 강점은 언스테이킹 요청 후 대기 시간없이(대기블록 : .. 블록, 약 2주)  바로 언스테이킹이 가능하다는데 있습니다.  함수 실행 즉시 L1에 묶인 자금을 L2  유동성으로 사용할 수 있습니다.  

## Layer2Candidate 의 L2시퀀서에게 시뇨리지 제공 중지할 수 있는 메커니즘을 제공합니다.     

레이어2 시퀀서에게 시뇨리지를 부여하는 기능은 토카막 이코노미의 큰 권한을 부여받은 것입니다. 그런데, 이러한 레이어2가 토카막 이코노미에 적절한 역할을 하지 못한다고 판단될 경우, 시뇨리지 위원회는 해당 Layer2Candidate의 시퀀서에게 부여되는 시뇨리지를 중지할 수 있습니다. 

## Layer2Candidate 의 L2시퀀서에게 시뇨리지 제공 중지 취소를 할 수 있습니다. 

 Layer2Candidate의 시뇨리지 중지의 복구는 타당한 이유 및 개선이 있다고 판단될 경우, 시뇨리지 위원회에 의해 다시 중지취소가 가능합니다. 

# TON Stake Contracts    

## TON Stake V1 Contracts

V1 의 컨트랙트는 아래와 같이 구성되어 있다. DAOCandidate는 DAOCommittee를 통해 생성을 할 수 있으며, 생성된 daoCandiate가 Layer2Registry를 통해 등록되고, SeigManager에 등록되면서, DAOCandidate와 매핑되는 AutoCoinage가 생성된다. AutoCoinage 는 스테이킹 금액을 관리하면서, 복리이자를 지급하기 위한 로직을 보유한다. 때문에 각 레이어 (DAOCandidate) 마다 별도의 AutoCoinage 가 생성된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/441dce2f-f4da-4ee4-91bc-580afd7df8a6/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.28.06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=9263e3bb1a552f5d61db0ba262b8a3d85f3bd8086cf4a6796cb9aed70531d27e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## TON Stake V2 Contracts

V2는 V1의 구성을 유지하면서 Layer2Candidate가 추가되었다. 컨트랙트 구성은 아래 그림과 같다. V1에 비해 다소 복잡해보인다. 그러나 파란색 부분의 컨트랙이 추가되었고 기존 구성에는 전혀 변경사항이 없음을 알 수 있다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/070e303e-b4d5-4dbc-a889-8b1dd711c26e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-21_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.04.54.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=b11ae30224ed3c9fc7b859b34b1b7909fca6c753872c76fcc7933015c165e362&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

먼저 이해하고 넘어가야 할것은 Layer2를 L1에서 어떻게 확인할 것인가에 대한 문제이다. 우리가 현재 타켓으로 하고 있는 Layer2는 옵티미즘 롤업이다. 옵티미즘의 레이어2를 먼저 적용하고, 다른 레이어도 적용될수 있도록 컨트랙 업그레이가 가능하게 제작한다.  옵티미즘 레이어2는 legacy버전과 배드락 버전이 있다. 처음 적용 대상은 옵티미즘 레거시 버전과 옵티미즘 배드락버전 중 L2 nativeToken이 톤인경우로 제한한다는 것을 기억해주길 바란다.  옵티미즘 배드락 버전에는 SystemConfig 컨트랙에 L1컨트랙의 정보와 환경설정이 담겨있다. 따라서 SystemConfig의 주소를 Layer2를 구별할 수 있는 주소로 사용할 것이다. 레거시 버전의 경우에는 SystemConfig가 존재하지 않기 때문에, legacySystemConfig 컨트랙을 별도 만들었다. 레거시 레이어2의 경우는 legacySystemConfig 컨트랙을 배포하여, 이 주소를 해당 Layer2를 구별할 수 있는 주소록 사용해야 한다. 

아래 Contract 파트에서 파란색 컨트랙에 대해 하나씩 설명하도록 하겠다. 

# Use case 

## For registrant of L2Registry

L2Registry 컨트랙에 registrant 권한을 가진 계정은 Layer2 의 고유한 정보를 보유하고 있는 SystemConfig를 등록할 수 있다. SystemConfig를 등록한다는 것은 해당 레이어2가 문제가 없는 레이어2라는 것을 확인했다는 의미이다.  등록된 SystemConfig의 레이어2만 Layer2Candidate로 등록될 수 있다.  Layer2Candidate 로 등록이 되고 나서야 해당 시퀀서가 시뇨리지를 받을 수 있게 된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/985596ab-ea70-4120-a54a-83b21d6573ac/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.07.19.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=09961daeeceaf9fbeb83294fb3e5518543cdde61e9b130668e9980c7b1e1690e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For everyone 

누구나 L2Registry에 등록된 SystemConfig에 대해서 Layer2Candidate를 등록할 수 있다. Layer2Candidate 등록시에는 오퍼레이터 계정으로 최소 예치금 이상을 예치하여야 하므로, 최소예치금에 해당하는 톤을 같이 제공해야 한다. 현재 서비스 기준으로는 최소 1000.1 TON을 제공해야 한다.  ‘Layer2Candidate 등록’ 기능을 통해 Operator, Layer2Candidate, Coinage 컨트랙이 생성된다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fafadd66-1b57-4f77-8a51-018f178ea306/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.41.57.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=7311a4826d641aab1a25162758d8de5f4231b6eaab842ae7208a65f6db53eca8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For staker in Layer2Candidate

Layer2Candidate 에 스테이킹한 사용자는 WithdrawAndDepositL2 기능을 통해 스테이킹을 금액 인출과 동시에 인출된 금액을 해당 Layer2 에 예치하는 기능을 수행할 수 있습니다. 이때 스테이킹 금액을 인출할때 대기시간없이 바로 인출 및 L2 예치가 됩니다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/45aec071-04e4-491f-86b3-7377a85dc221/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.25.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=1ba8f33d10b49ed49113b09bfe5e84420996f8ca8c4e4bd0c02817da4466e268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## For seigniorageCommittee

심플 스테이킹 V2는 Layer2를 운영하는 Layer2Candidate의 시퀀서에게 톤 시뇨리지를 발급하는 이코노미를 설계했습니다. 그러나 Layer2를 실제로 운영하지 않거나  불합리하게 시뇨리지를 할당받는 행위 등을 발견할 즉시 해당 레이어2의 시퀀서에게 톤 시뇨리지 발급을 중지할 수 있는 기능이 있어야 합니다. 

 L2Registry 컨트랙에 정의된 시뇨리지 위원회 계정을 만들었습니다. 시뇨리지 위원회는 레이어2 시퀀서에 대한 시뇨리지 발급 중지 또는 발급 중지 취소 기능을 수행할 수 있습니다.  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/68a7f248-5364-44d9-9165-a9dd06fd7908/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.44.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=289e64908a94ea35aabd0f77fd73f11b7c566513f8b18980b6cceda00811ab6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Sequence Diagrams   

## Register Layer2Candidate 

Layer2Candidate를 등록할때에는 해당 레이어의 오퍼레이터 이름으로 최소 예치금액 이상을 예치해야 합니다. 

Layer2Candidate를 등록시. Layer2의 환경설정 정보를 보유하고 있는 SystemConfig 컨트랙 주소를 제시해야 합니다. 또한 입력하는 SystemConfig는 등록 전에 L2Registry에 등록되어 있어야 합니다. ( L2Registry에 등록하는 권한은 L2Registry의 Registrant 권한을 보유한 계정만 등록이 가능합니다. ) 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/04f3c312-7fb4-438d-b3b7-fa8fbf23d939/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_10.36.58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=6b63327adc010c9a5dce7193b98e1ce80cc3de8cd7fe4ddae5d5a5b83ffadddf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Withdraw And Deposit L2 

Layer2Candidate 에 스테이킹한 사용자는 스테이킹한 금액을 즉시 출금하면서, Layer2에 예치할 수 있습니다. 

  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c6654014-150b-4263-9ffb-4816dce85214/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_1.49.12.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=dbfbc29bc2e5838a19f3c88e116c49f1a54684b89648a4cc1f5d6cdea37ee888&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Stop distributing a seigniorage to the L2 sequencer

시뇨리지 위원회는  특정 레이어2가 시뇨리지를 받기에 불합리하다고 판단될때, 해당 레이어2의 시퀀서에게 배분하는 시뇨리지 발급을 중지할 수 있습니다. 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/e2a30ff0-83d1-4da5-ab23-9fbc2867bb08/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.10.46.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=be124de561462c567a237ba85a0d04966648cba40a9591302c54db8dffc92229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Cancel stopping distributing a seigniorage to the L2 sequencer

시뇨리지 위원회는  특정 레이어2의 시퀀서에게 배분하는 시뇨리지 발급을 중지했던 것을 취소하여, 다시 시뇨리지를 지급할 수 있습니다.  

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8df2043b-66cb-4060-94f4-4a86ab9626ea/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-06-26_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.11.00.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO43MMKQ%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7%2BWg6s%2BSWuXo3ufX6DU71%2BVKL812OzmCQmGQK%2BPaf5AIgPxBBOqGZm0yKF1MiI9ZuLFMVZUSCuRrzc%2BDeZZc%2FxSMq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGlf%2B20FDGUK6zNEYCrcA6Ih4Foa03l3j2zZZPLaN6Cxrma8NWprDlBhNDY79tjWhd9QKbwm7DmU7gjRpCPenZzqn4QRg59Nmsx19JFRbyh54OWP9pqCVEGK6204a8u0hMRZdfLVjUKn7Cp8tjANilmngf5CBABPtriGUmbEC1PIEnhd6Xmp%2FYQX6w7UN6244lBEEtHx4Rm8ta04fpOKVh0Pn0tsVmDopCDLyfNiYZVFMBSC61WM4jZTjgF0PofSbaYDFC4XaPdWiTi3G5rzLdfcsSShlOT9yiRNX78A%2BOHL2JktUD9gM0ncQFW4Jgef4OsKtrwVOXeMMzuYwx6TZ61dQlEs%2BVun%2BYLwMytju70t6MdCckcbTHe78PdzXn%2FVQwiexDLF3WJ%2BQBSeIF8SODU5J2tJEib%2BR4tz0yk%2Faw6FbDgnSkM7G9MbijaVIoT1NKPVkwdLE%2FeYat%2Fx31xy9zx6qm06qkYDmzHlSbE2vREanZQ%2BnvdywXObS56d4qS0c7En9r9881eQG7W4rJ07XpX8XB6aZVDwcsFm%2Bg%2BrnEKFXW%2FdELdsFOCIzPV5y2R46d63DKDKlA25XxS6pV5LJy55%2FTq%2FRqe1Q9PestxpKgo1Bn7mPyptMQCgGaodp6P23BsJ2rclElW5tHTcMKLw2cwGOqUBUK9cKuGfb5zDqRiQ965qz0hQpJzqUPwCF%2B891Xaub2w3b5feNxo%2BmUi1yznQalyj0rroY6PodQQTKte3fXZM5C6UYEp0cbpth7oBR23to1KeLW0r%2BIODmU3LxW5rs15XNADWXNMfrDdrLYD9F%2F4Oy3rAbjkTbr92NJ1WVv7HKUAh8Hedsr%2FYdEnZ%2F%2BSG7bE7GnHtrRiIO77GAxK2%2BHmzcV8tkW3g&X-Amz-Signature=0fe2ede9ad1bdbd7ada37cffab861324ead1d84f8d3cc30ba751845883aec7ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Contract Details 

## L2Registry

- 개요
  - 토카막 네트웤에서 운영되는 레이어2의 SystemConfig 컨트랙 주소가 등록된  컨트랙입니다. 
  -  타이탄, 타노스는 어드민에 의해 수동으로 SystemConfig를 입력합니다. 
  - on-demand L2에서 생성된 컨트랙은 컨트랙 생성시 자동으로 등록됩니다.  
  - 기존에 심플스테이킹에 Layer2Registry가 존재하여 구별을 주고자 L2Registry 로 이름을 정했다. 
  - 추후 다른 레이어(ex, zk-EVM) 지원을 고려하여 프록시로 구성하여 업그레이드 가능해야 한다.  
- 권한 
  - **Owner **:  오너는 로직 업그레이드 권한을 갖으며, 매니저를 지정할 수 있다. 
  - **Manager** : 재단은 MANAGER_ROLE 을 보유하고 있고, 매니저는 오퍼레이터를 등록하거나 제거할 수 있다.  SeigniorageCommittee
  - Registrant:  on-demand-L2 오픈시, L2를 실제 배포하는 서버의 EOA에게 REGISTRANT_ROLE 을 주어야 한다. 
- 스토리지 
```javascript
address public layer2Manager;
address public seigManager;
address public ton;
address public seigniorageCommittee;
    
/// systemConfig - type (0:empty, 1: optimism legacy, 2: optimism bedrock native TON)
mapping (address => uint8) public systemConfigType;

/// For registered bridges, set to true.
mapping (address => bool) public l1Bridge;

/// For registered portals, set to true.
mapping (address => bool) public portal;

/// Set the layer where seigniorage issuance has been suspended to true.
mapping (address => bool) public rejectSystemConfig; 
```
- 이벤트 
```javascript
 event SetAddresses(address _layer2Manager, address _seigManager, address _ton);
event SetSeigniorageCommittee(address _seigniorageCommittee);

/**
 * @notice  Event occurs when registering SystemConfig
 * @param   systemConfig  the systemConfig address
 * @param   type_         0: none, 1: legacy, 2: bedrock with nativeTON
 */
event RegisteredSystemConfig(address systemConfig, uint8 type_);

/**
 * @notice  Event occurs when an account with registrant privileges changes the layer 2 type.
 * @param   systemConfig  the systemConfig address
 * @param   type_         0: none, 1: legacy, 2: bedrock with nativeTON
 */
event ChangedType(address systemConfig, uint8 type_);

/**
 * @notice  Event occurs when onlySeigniorageCommittee stops issuing seigniorage
 *          to the layer 2 sequencer of a specific systemConfig.
 * @param   _systemConfig  the systemConfig address
 */
event RejectedLayer2Candidate(address _systemConfig);

/**
 * @notice  Event occurs when onlySeigniorageCommittee cancels stoping issuing seigniorage
 *          to the layer 2 sequencer of a specific systemConfig.
 * @param   _systemConfig  the systemConfig address
 */
event RestoredLayer2Candidate(address _systemConfig);

```
- 주요 Transaction Functions 
  - function rejectLayer2Candidate(address _systemConfig)  external onlySeigniorageCommittee() 
```solidity
/**
 * @notice Stop issuing seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function rejectLayer2Candidate(
    address _systemConfig
)  external onlySeigniorageCommittee() 
```
  - function restoreLayer2Candidate(address _systemConfig)  external onlySeigniorageCommittee() 
```solidity
/**
 * Restore cancel stoping seigniorage to the layer 2 sequencer of a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function restoreLayer2Candidate(
    address _systemConfig
)  external onlySeigniorageCommittee() 
```
  - function registerSystemConfigByManager(address _systemConfig, uint8 _type)  external onlyManager 
```solidity
/**
 * @notice Registers Layer2 for a specific systemConfig by the manager.
 * @param _systemConfig  the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function registerSystemConfigByManager(address _systemConfig, uint8 _type)  external  onlyManager  

```
  - function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyRegistrant
```solidity
/**
 * @notice Registers Layer2 for a specific systemConfig by Registrant.
 * @param _systemConfig the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function registerSystemConfig(address _systemConfig, uint8 _type)  external  onlyRegistrant  

```
  -  function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant
```solidity
/**
 * @notice Changes the Layer2 type for a specific systemConfig by Registrant.
 * @param _systemConfig the systemConfig address
 * @param _type          1: legacy, 2: bedrock with nativeTON
 */
function changeType(address _systemConfig, uint8 _type)  external  onlyRegistrant 
```
- 주요 View Functions 
  -  function layer2TVL(address _systemConfig) public view returns (uint256 amount)
```solidity
/**
 * @notice View the liquidity of Layer2 TON for a specific systemConfig.
 * @param _systemConfig the systemConfig address
 */
function layer2TVL(address _systemConfig) public view returns (uint256 amount)
```
  - function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid)
```solidity
/**
 * @notice Check whether a specific systemConfig can be registered as a type.
 * @param _systemConfig the systemConfig address
 * @param _type         1: legacy, 2: bedrock with nativeTON
 */
function availableForRegistration(address _systemConfig, uint8 _type) public view returns (bool valid)
  
```

## OperatorFactory

- 개요
DAOCommittee 에 Layer2Candidate가 멤버로 등록될때 Layer2Candidate의 오퍼레이터 주소가 매핑의 키값으로 등록되기 때문에 오퍼레이터 주소가 변경되어서는 안된다.  그러나 L2레이어(SystemConfig)의 오퍼레이터는 언제든지 바뀔수 있기 때문에 Operator 컨트랙을 만들었다.  Operator 컨트랙은 SystemConfig 컨트랙에 매핑되는 컨트랙이다. 즉, SystemConfig (L2레이어) 컨트랙 주소로 Operator 컨트랙의 주소를 생성하여야 한다.    추후 로직 변경 가능성이 있으므로, 프록시로 구현하였다. 
- 권한 
  - 오너 : 오너는 배포되는 오퍼레이터의 로직을 설정할 수 있다.  
- 스토리지
```javascript
address public operatorImplementation;
address public depositManager;
address public ton;
address public wton;
address public layer2Manager;
```
- 이벤트
```javascript
/**
 * @notice Event occurs when set the addresses
 * @param depositManager    the depositManager address
 * @param ton               TON address
 * @param wton              WTON
 * @param layer2Manager     the layer2Manager address
 */
event SetAddresses(address depositManager, address ton, address wton, address layer2Manager);

/**
 * @notice Event occured when change the operator implementaion address
 * @param newOperatorImplementation the operator implementaion address
 */
event ChangedOperatorImplementaion(address newOperatorImplementation);

/**
 * @notice Event occured when create the Operator Contract
 * @param systemConfig  the systemConfig address
 * @param owner         the owner address
 * @param manager       the manager address
 * @param operator      the operator address
 */
event CreatedOperator(address systemConfig, address owner, address manager, address operator);

```
- 주요  Transaction 함수 
  - function changeOperatorImplementaion(address newOperatorImplementation) external onlyOwner 
```solidity
/**
 * @notice Change the operator implementaion address by Owner
 * @param newOperatorImplementation the operator implementaion address
 */
function changeOperatorImplementaion(address newOperatorImplementation) external onlyOwner  
```
  -  function createOperator(address systemConfig) external returns (address operator)
```solidity
/**
 * @notice  Create an Operator Contract, and return its address.
 *          return revert if the account is already deployed.
 *          Note. Only Layer2Manager Contract can be called.
 *          When creating the Layer2Candidate, create an Operator contract
 *          that is mapped to SystemConfig.
 * @param systemConfig  the systemConfig address
 */
function createOperator(address systemConfig) external returns (address operator) {
 
```
- 주요 View 함수 
  - function getAddress(address systemConfig) public view returns (address) 
```solidity
/**
 * @notice  Returns the operator contract address matching systemConfig.
 * @param systemConfig  the systemConfig address
 */
function getAddress(address systemConfig) public view returns (address) 
```

## Operator

- 개요
  - Operator 컨트랙은 추후 Layer2에서 다중 시퀀서(오퍼레이터)를 지원할 가능성이 있다는 것을 염두에 두고 설계되어야 한다.  따라서 업그레이드 가능한 구조로 설계된다. 
  - Layer2Candidate 는 DAOCandidate의 모든 기능을 상속받았다. DAOCandidate의 onlyCandidate 의 정의 
    - **Operator.isOperator(msg.sender)** 가 true은 계정을 의미하며, operator 권한을 가진 계정은 Layer2Candidate의 오퍼레이터 함수를 사용할수 있게 한다.
- 권한 
  - owner 
    - 프록시 오너로서, 로직을 업그레이드 할 수 있다.
    - 프록시 오너는 재단이 보유한다. 
    - 매니저를 변경할 수 있다. 
    - 오퍼레이터를 추가/삭제할 수 있다. 
  - manager 
    - 관리자 권한은 오퍼레이터 등록 및 제거 할 수 있다. 최초 배포시 SystemConfig의 오너를 manager 로 지정한다. 
    - 추후 SystemConfig의 오너가 변경될때, transferManager 를 이용하여 manager를 변경해야 한다. (SystemConfig.owner 가 manager를 가져갈 수 있는 인터페이스를 제공한다. )  
  - operator  (onlyCandidate)
    - 오퍼레이터 권한을 보유한다. 다오멤버의 함수를 사용할 수 있다. 
    - onlyCandidate : **Operator.isOperator(msg.sender)**  == true 인 계정이다. 
    - DAOCandidate에서 상속받은 onlyCandidate가 사용할 수 있는 함수는 오퍼페이터가 실행할 수 있다. 
      - changeMember 함수 → Operator 컨트랙이 다오의 멤버가 된다. 
      - retireMember 함수 → Operator 컨트랙이 다오 멤버에서 사임한다. 
      - castVote 함수  → Operator 컨트랙 이름으로 안건에 투표한다. 
      - claimActivityReward 함수 → 리워드는 Operator 컨트랙이 받는다.  
- 스토리지
```javascript
address public systemConfig;
address public layer2Manager;
address public depositManager;
address public ton;
address public wton;

address public manager;
mapping(address => bool) public operator;
```
- 이벤트
```javascript
/**
* @notice Event occurs when the transfer manager
* @param previousManager   the previous manager address
* @param newManager        the new manager address
*/
event TransferredManager(address previousManager, address newManager);

/**
* @notice Event occurs when adding the operator
* @param operator  the operator address
*/
event AddedOperator(address operator);

/**
* @notice Event occurs when deleting the operator
* @param operator  the operator address
*/
event DeletedOperator(address operator);

/**
* @notice Event occurs when setting the addresses
* @param _layer2Manager    the _layer2Manager address
* @param _depositManager   the _depositManager address
* @param _ton              the TON address
* @param _wton             the WTON address
*/
event SetAddresses(address _layer2Manager, address _depositManager, address _ton, address _wton);

/**
* @notice Event occurs when the claim token
* @param token     the token address, if token address is address(0), it is ETH
* @param caller    the caller address
* @param to        the address received token
* @param amount    the received token amount
*/
event Claimed(address token, address caller, address to, uint256 amount);

```
- 주요  Transaction 함수 
  - function claimETH() external onlyOwnerOrManager 
```javascript
/**
 * @notice  Give ETH to a manager through the manager(or owner) claim
 */
function claimETH() external onlyOwnerOrManager
```
  - function claimERC20(address token, uint256 amount) external onlyOwnerOrManager 
```javascript
/**
 * @notice  Give ERC20 to a manager through the manager(or owner) claim
 * @param token     the token address
 * @param amount    the amount claimed token
 */
function claimERC20(address token, uint256 amount) external onlyOwnerOrManager
```
  - function depositByLayer2Canddiate(uint256 amount) external onlyLayer2Candidate 
```javascript
/**
 * @notice Deposit wton amount to DepositManager as named Layer2
 * @param amount    the deposit wton amount (ray)
 */
function depositByLayer2Canddiate(uint256 amount) external onlyLayer2Candidate 
```
  - function claimByLayer2Candidate(uint256 amount) external onlyLayer2Candidate 
```javascript
/**
* @notice Claim WTON to a manager
* @param amount    the deposit wton amount (ray)
*/
function claimByLayer2Candidate(uint256 amount) external onlyLayer2Candidate
```
- 주요 View 함수 
  - function acquireManager() external
```javascript
/**
 * @notice acquire administrator privileges.
 */
function acquireManager() external 
```
  - function isOperator(address addr) public view returns (bool)
```javascript
/**
 * @notice Returns true if the operator has permission.
 * @param addr the address to check
 */
function isOperator(address addr) public view returns (bool)
```
  - function checkL1Bridge() public view returns (bool result, address l1Bridge, address portal, address l2Ton) 
```javascript
/**
 * @notice Returns the availability status of Layer 2, L1 bridge address, portal address, and L2TON address.
 * @return result   the availability status of Layer 2
 * @return l1Bridge the L1 bridge address
 * @return portal   the L1 portal address
 * @return l2Ton    the L2 TON address
 *                  L2TON address is 0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000,
 *                  In this case, the native token of Layer 2 is TON.
 */
function checkL1Bridge() public view returns (bool result, address l1Bridge, address portal, address l2Ton) {
  
```

## Layer2Manager 

- 개요
  - Layer2 시퀀서가 시뇨리지를 받기 위해서는 SystemConfig 주소를  Layer2Manager에 등록해야 합니다. 
  - 시뇨리지 분배시, Layer2의 시퀀서들에게 지급되는 시뇨리지를 Layer2Manager에게 지급합니다. 따라서 Layer2Manager 는 Layer2Candidate 의 시뇨리지 정산 전까지 해당 시뇨리지를 보유하게 됩니다.      
- 권한 
  - Owner** **:  오너는 로직 업그레이드 권한을 갖으며, 설정값들을 설정할 수 있다.  
- 스토리지
```javascript
struct OperatorInfo {
    address systemConfig;
    address layer2Candidate;
}

struct SystemConfigInfo {
    uint8 stateIssue; // status for giving seigniorage ( 0: none, 1: registered, 2: paused )
    address operator;
}

address public l2Register;
address public operatorFactory;
address public ton;
address public wton;
address public dao;
address public depositManager;
address public seigManager;
address public swapProxy;

/// The minimum TON deposit amount required when creating a Layer2Candidate.
/// Due to calculating swton, It is recommended to set 
/// DepositManager's minimum deposit + 0.1 TON
uint256 public minimumInitialDepositAmount;  

/// systemConfig - SystemConfigInfo
mapping (address => SystemConfigInfo) public systemConfigInfo;

/// operator - OperatorInfo
mapping (address => OperatorInfo) public operatorInfo;

```
- 이벤트
```javascript
/**
 * @notice Event occurs when setting the minimum initial deposit amount
 * @param _minimumInitialDepositAmount the inimum initial deposit amount
 */
event SetMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount);

/**
 * @notice Event occurs when registering Layer2Candidate
 * @param systemConfig      the systemConfig address
 * @param wtonAmount        the wton amount depositing when registering Layer2Canddiate
 * @param memo              the name of Layer2Canddiate
 * @param operator          a opperator contract address
 * @param layer2Candidate   a layer2Candidate address
 */
event RegisteredLayer2Candidate(address systemConfig, uint256 wtonAmount, string memo, address operator, address layer2Candidate);

/**
 * @notice Event occurs when pausing the layer2 candidate
 * @param systemConfig      the systemConfig address
 * @param _layer2           the layer2 address
 */
event PausedLayer2Candidate(address systemConfig, address _layer2);

/**
 * @notice Event occurs when pausing the layer2 candidate
 * @param systemConfig      the systemConfig address
 * @param _layer2           the layer2 address
 */
event UnpausedLayer2Candidate(address systemConfig, address _layer2);
```
- 주요  Transaction 함수 
  - function registerLayer2Candidate(address systemConfig, uint256 amount, bool flagTon, string calldata memo) external
```javascript
/**
 * @notice Register the Layer2Candidate
 * @param systemConfig     systemConfig's address
 * @param amount           transfered amount
 * @param flagTon          if true, amount is ton, otherwise it it wton
 * param memo             layer's name
 */
function registerLayer2Candidate(
    address systemConfig,
    uint256 amount,
    bool flagTon,
    string calldata memo
)
    external
```
  - function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool)
```javascript
/// @notice ERC20 Approve callback
/// @param owner    Account that called approveAndCall
/// @param spender  OnApprove function contract address
/// @param amount   Approved amount
/// @param data     Data used in OnApprove contract
/// @return bool    true
function onApprove(address owner, address spender, uint256 amount, bytes calldata data) external returns (bool)
```
  - function pauseLayer2Candidate(address systemConfig) external onlyL2Register ifFree 
```javascript
/**
 * @notice Pause the layer2 candidate
 * @param systemConfig the systemConfig address
 */
function pauseLayer2Candidate(address systemConfig) external onlyL2Register ifFree 
```
  - function unpauseLayer2Cnadidate(address systemConfig) external onlyL2Register ifFree 
```solidity
/**
 * @notice Unpause the layer2 candidate
 * @param systemConfig the systemConfig address
 */
function unpauseLayer2Cnadidate(address systemConfig) external onlyL2Register ifFree 
```
  - function updateSeigniorage(address systemConfig, uint256 amount) external onlySeigManger 
```javascript
/**
* @notice When executing update seigniorage, the seigniorage is settled to the Operator of Layer 2.
* @param systemConfig the systemConfig address
* @param amount the amount to give a seigniorage
*/
function updateSeigniorage(address systemConfig, uint256 amount) external onlySeigManger 
```
  - function setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)  external  onlyOwner 
```javascript
/**
* @notice  Set the minimum TON deposit amount required when creating a Layer2Candidate.
*          Due to calculating swton, it is recommended to set DepositManager's minimum deposit + 0.1 TON
* @param   _minimumInitialDepositAmount the minimum initial deposit amount
*/
function setMinimumInitialDepositAmount(uint256 _minimumInitialDepositAmount)  external  onlyOwner 
```

 

- 주요 View 함수 
  - function systemConfigOfOperator(address _oper) external view returns (address) 
```javascript
/**
 * @notice View the systemConfig address of the operator address.
 * @param _oper     the operator address
 * @return          the systemConfig address
 */
function systemConfigOfOperator(address _oper) external view returns (address) 
```
  - function operatorOfSystemConfig(address _sys) external view returns (address) 
```javascript
/**
 * @notice View the operator address of the systemConfig address.
 * @param _sys      the systemConfig address
 * @return          the operator address
 */
function operatorOfSystemConfig(address _sys) external view returns (address) 
```
  - function layer2CandidateOfOperator(address _oper) external view returns (address)
```javascript
/**
 * @notice  View the layer2Candidate address of the operator address.
 * @param _oper     the operator address
 * @return          the layer2Candidate address
 */
function layer2CandidateOfOperator(address _oper) external view returns (address) 
```
  - function issueStatusLayer2(address _sys) external view returns (uint8)
```javascript
/**
 * @notice View the status of seigniorage provision for Layer 2 corresponding to SystemConfig.
 * @param _sys      the systemConfig address
 * @return          the status of seigniorage provision for Layer 2
 *                  ( 0: none , 1: registered, 2: paused )
 */
function issueStatusLayer2(address _sys) external view returns (uint8) 
```
  - function checkLayer2TVL(address _systemConfig) public view returns (bool result, uint256 amount) 
```javascript
/**
 * @notice  Check Layer 2’s TON liquidity related information
 * @param _systemConfig the syatemConfig address
 * @return result       whether layer 2 TON liquidity can be checked
 * @return amount       the layer 2's TON amount (total value liquidity)
 */
function checkLayer2TVL(address _systemConfig) public view returns (bool result, uint256 amount)
```
  - function checkL1Bridge(address _systemConfig) public view returns (bool result, address l1Bridge, address portal, address l2Ton) 
```javascript
/**
 * @notice Layer 2 related information search
 * @param _systemConfig     the systemConfig address
 * @return result           whether Layer2 information can be searched
 * @return l1Bridge         the L1 bridge address
 * @return portal           the optimism portal address
 * @return l2Ton            the L2 TON address
 */
function checkL1Bridge(address _systemConfig) public view returns (bool result, address l1Bridge, address portal, address l2Ton)

```

## Layer2ContractFactory 

- 개요
  - Layer2Candiate 를 생성하는 컨트랙입니다. 
- 권한 
  - Owner** **:  오너는 로직 업그레이드 권한을 갖으며, 설정값들을 설정할 수 있다.  
- 스토리지
```javascript
address public depositManager;
address public daoCommittee;
address public layer2CandidateImp;
address public ton;
address public wton;

address public onDemandL2Registry;
```
- 이벤트
```javascript
/**
 * @notice  Event that occurs when a Candidate is created
 * @param sender            the sender address
 * @param layer2            the layer2 address
 * @param operator          the operator address
 * @param isLayer2Candidate whether it is Layer2Candidate
 * @param name              the name of Layer2
 * @param committee         the committee address
 * @param seigManager       the seigManager address
 */
event DeployedCandidate(
    address sender,
    address layer2,
    address operator,
    bool isLayer2Candidate,
    string name,
    address committee,
    address seigManager
);
```
- 주요  Transaction 함수 
  - function deploy(address _sender, string memory _name, address _committee, address _seigManager) public onlyDAOCommittee  returns (address)
```solidity
/**
* @notice Deploy the candidate contract
* @param _sender       the sender address
* @param _name         the name of layer2
* @param _committee    the committee address
* @param _seigManager  the seigManager address
* @return              the created candidate address
*/
function deploy(
  address _sender,
  string memory _name,
  address _committee,
  address _seigManager
)
  public onlyDAOCommittee
  returns (address)
```

## Layer2Contract 

- 개요
  - 심플스테이킹(톤 스테이킹)의 기본기능(예치, 업데이트시뇨리지-이자지급, 출금 기능)을 지원한다. 
  - DAOCandidate에서 할 수 있는 다오 멤버 기능을 지원한다. 
  - 업데이트 시뇨리지 실행시, Layer2Candidate의 시퀀서(오퍼레이터)가 시뇨리지를 받을 수 있다.
- 권한 
  - Owner : 오너는 로직 업그레이드 권한을 갖으며, 설정값을 초기화 할 수 있다.
  - onlyCandidate : Layer2Candidate 에 매칭되는 Operator 컨트랙의 오퍼레이터 권한을 갖는 계정 
```javascript
 modifier onlyCandidate() {
      require(IOperateContract(candidate).isOperator(msg.sender),
      "sender is not an operator");
      _;
  }
```
- 스토리지
```solidity
    mapping(bytes4 => bool) internal _supportedInterfaces;
    bool public isLayer2Candidate;
    address public candidate;
    string public memo;

    address public committee;
    address public seigManager;
    address ton;
    address wton;
```
- 이벤트
```javascript
event Initialized(address _operateContract, string memo, address committee, address seigManager);
event SetMemo(string _memo);
```
- 주요  Transaction 함수 
  - function changeMember(uint256 _memberIndex) external  onlyCandidate   returns (bool)
```javascript
/// @notice Try to be a member
/// @param _memberIndex The index of changing member slot
/// @return Whether or not the execution succeeded
function changeMember(uint256 _memberIndex)
    external
    onlyCandidate
    returns (bool)
```
  - function retireMember() external onlyCandidate returns (bool)
```javascript
/// @notice Retire a member
/// @return Whether or not the execution succeeded
function retireMember() external onlyCandidate returns (bool) 
```
  - function castVote(uint256 _agendaID,  uint256 _vote, string calldata  _comment ) external  onlyCandidate
```javascript
/// @notice Vote on an agenda
/// @param _agendaID The agenda ID
/// @param _vote voting type
/// @param _comment voting comment
function castVote(
    uint256 _agendaID,
    uint256 _vote,
    string calldata _comment
)
    external
    onlyCandidate
```
  - function claimActivityReward() external  onlyCandidate
```javascript
/**
 * @notice Claim an activity reward
 */
function claimActivityReward()
    external
    onlyCandidate
```
  - function updateSeigniorage() external returns (bool) 
```javascript
/// @notice Call updateSeigniorage on SeigManager
/// @return Whether or not the execution succeeded
function updateSeigniorage() external returns (bool)
```
  - function updateSeigniorage(uint256 afterCall) public returns (bool) 
```javascript
/// @notice Call updateSeigniorage on SeigManager
/// @param afterCall    After running update seigniorage, option to run additional functions
///                     0: none, 1: claim, 2: staking
/// @return             Whether or not the execution succeeded
function updateSeigniorage(uint256 afterCall) public returns (bool) 
```
- 주요 View 함수
  -  function totalStaked() external  view returns (uint256 totalsupply)
```javascript
/// @notice Retrieves the total staked balance on this candidate
/// @return totalsupply Total staked amount on this candidate
function totalStaked()
    external
    view
    returns (uint256 totalsupply)
```
  - function stakedOf(address _account)  external  view returns (uint256 amount)
```javascript
/// @notice Retrieves the staked balance of the account on this candidate
/// @param _account Address being retrieved
/// @return amount The staked balance of the account on this candidate
function stakedOf(
    address _account
)
    external
    view
    returns (uint256 amount)
```

## SeigManagerV1_3 

- 개요
  - Layer2Candidate의 업데이트 시뇨리지 실행시, layer2의 TON TVL에 따라  Layer2 시퀀서에게 시뇨리지를 지급해야 하며, 지급되는 시뇨리지는 Operator 컨트랙에게 정산됩니다.  
  - Operator 컨트랙의 오퍼레이터권한을 갖는 시퀀서가 Layer2Candidate 의  업데이트 시뇨리지 실행(시뇨리지 분배시)시, 청구 및 스테이킹 옵션을 선택해서, 시뇨리지 정산과 동시에 청구 또는 스테이킹 기능을  같이 실행할 수 있습니다.  
  - L2 시퀀서에게 분배되는 시뇨리지 분배로직은 [V2 백서](https://github.com/tokamak-network/papers/blob/master/cryptoeconomics/tokamak-cryptoeconomics-en.md#222-ton-staking-v2)의 시뇨리지 배분 규칙에 따라 이루어진다. 
  - V1에서 이미 SeigManager 가 배포되어 운영되고 있으므로, 다른 기능은 변경없이 업데이트 시뇨리지 함수만  SeigManagerV1_3에 변경된 로직으로 실행되도록 한다. 
  - 업데이트 시뇨리지 함수실행시 Layer2에게 제공하는 시뇨리지를 관리하기 위한 스토리지를 추가한다. 
- 권한 
  - 
- 추가된 스토리지
```javascript
struct Layer2Reward {
    uint256 layer2Tvl;
    uint256 initialDebt;
}

/// L2Registry address
address public l2Registry;

/// Layer2Manager address
address public layer2Manager;

/// layer2 seigs start block
uint256 public layer2StartBlock;

uint256 public l2RewardPerUint;  // ray unit .1e27

/// total layer2 TON TVL
uint256 public totalLayer2TVL;

/// layer2 reward information for each layer2.
mapping (address => Layer2Reward) public layer2RewardInfo;

```
- 삭제된 이벤트 
업데이트 시뇨리지 실행시 발생하던 SeigGiven 이벤트가 삭제되었다. 

```javascript
event SeigGiven(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig);
```
- 추가된 이벤트
업데이트 시뇨리지 실행시 아래 SeigGiven2 이벤트가 추가 발생한다. 

```javascript
/**
 * Event that occurs when seigniorage is distributed when update seigniorage is executed
 * @param layer2        The layer2 address
 * @param totalSeig     Total amount of seigniorage issued
 * @param stakedSeig    Seigniorage equal to the staking ratio of ton total 
 *                      supply in total issued seigniorage
 * @param unstakedSeig  Total issued seigniorage minus stakedSeig
 * @param powertonSeig  Seigniorage distributed to powerton
 * @param daoSeig       Seigniorage distributed to dao
 * @param pseig         Seigniorage equal to relativeSeigRate ratio 
 *                      from unstakedSeig amount
 *                      Seigniorage given to stakers = stakedSeig + pseig
 * @param l2TotalSeigs  Seigniorage distributed to L2 sequencer
 * @param layer2Seigs   Seigniorage currently settled (give) 
 *                      to layer2Candidate's operator contract
 */
event SeigGiven2(address indexed layer2, uint256 totalSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 pseig, uint256 l2TotalSeigs, uint256 layer2Seigs);

```
- 주요  Transaction 함수 
  - function excludeFromSeigniorage (address _layer2) external returns (bool) onlyLayer2Manager
```javascript
/**
* @notice Exclude the layer2 in distributing a seigniorage
* @param _layer2     the layer2 address
*/
function excludeFromSeigniorage (address _layer2)
external
returns (bool)
```
  - function updateSeigniorageOperator() external  returns (bool)  onlyCandidate
```javascript
/**
* @notice Distribute the issuing seigniorage.
*         If caller is a Layer2Candidate, the seigniorage is settled to the L2 Operator.
*/
function updateSeigniorageOperator()
external
returns (bool)
```
  - function updateSeigniorage() external  returns (bool)  onlyCandidate
```javascript
/**
* @notice Distribute the issuing seigniorage.
*/
function updateSeigniorage()
external
returns (bool)
```
  - function updateSeigniorageLayer(address layer2) external returns (bool) 
```javascript
/**
* @notice Distribute the issuing seigniorage on layer2.
*/
function updateSeigniorageLayer(address layer2) external returns (bool) 
```
- 주요 View 함수 
  - function getOperatorAmount(address layer2) external view returns (uint256)  
```javascript
/**
* @notice Query the staking amount held by the operator
*/
function getOperatorAmount(address layer2) external view returns (uint256) 
```
  -  function estimatedDistribute(uint256 blockNumber, address layer2, bool _isSenderOperator)  external view returns (uint256 maxSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 relativeSeig, uint256 l2TotalSeigs, uint256 layer2Seigs)
```javascript
/**
* @notice Estimate the seigniorage to be distributed
* @param blockNumber         The block number
* @param layer2              The layer2 address
* @param _isSenderOperator   Whether sender is operator of layer2
* @return maxSeig            Total amount of seigniorage occurring in that block
* @return stakedSeig         the amount equals to the staking ratio in TON total supply
*                            in total issuing seigniorage
* @return unstakedSeig       MaxSeig minus stakedSeig
* @return powertonSeig       the amount calculated to be distributed to Powerton
* @return daoSeig            the amount calculated to be distributed to DAO
* @return relativeSeig       the amount equal to relativeSeigRate ratio from unstakedSeig amount
* @return l2TotalSeigs       the amount calculated to be distributed to L2 sequencer
* @return layer2Seigs        the amount currently to be settled (give)  to layer2Candidate's operator contract
*/
function estimatedDistribute(uint256 blockNumber, address layer2, bool _isSenderOperator)
external view
returns (uint256 maxSeig, uint256 stakedSeig, uint256 unstakedSeig, uint256 powertonSeig, uint256 daoSeig, uint256 relativeSeig, uint256 l2TotalSeigs, uint256 layer2Seigs) 
```

## DepositManagerV1_1 

- 개요
  - Layer2Candidate 의 경우라면 톤스테이킹출금을 하면서, 동시에 해당 Layer2에 예치할 수 있는 기능 (withdrawAndDepositL2) 을 지원한다. 이 때에는 출금시 지연시간 없이 즉시 출금 후, L1에 예치된다. 
  - Layer2Candidate가 아닌 레이어에 withdrawAndDepositL2 함수를 요청할때는 에러를 발생한다. 
  -  DepositManagerProxy에 기존 로직은 그대로 두고, withdrawAndDepositL2 함수만 추가되도록 한다. 
- 스토리지
```javascript
address public ton;
uint32 public minDepositGasLimit; /// not used
```
- 이벤트
```javascript
/**
 * @notice Event that occurs when calling the withdrawAndDepositL2 function
 * @param layer2    The layer2 address
 * @param account   The account address
 * @param amount    The amount of withdrawal and deposit L2
 */
event WithdrawalAndDeposited(address indexed layer2, address account, uint256 amount);

```
- 주요  Transaction 함수 
  - function withdrawAndDepositL2(address layer2, uint256 amount) external ifFree returns (bool) 

```javascript
/**
 * @notice Withdrawal from L1 and deposit to L2
 * @param layer2    The layer2 address
 * @param amount    The amount to be withdrawal and deposit L2. ()`amount` WTON in RAY)
 */
function withdrawAndDepositL2(address layer2, uint256 amount) external ifFree returns (bool) 
```