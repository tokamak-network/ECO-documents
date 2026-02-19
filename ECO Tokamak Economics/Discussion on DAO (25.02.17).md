## Hammer Audit feedback about issue62

1. [https://github.com/tokamak-network/ton-staking-v2/issues/62](https://github.com/tokamak-network/ton-staking-v2/issues/62)
1. 내용
  1. 멤버들 중 제일 TON 스테이킹이 많이되어있는 멤버가 retire 후 challange를 통해서 다른 멤버의 index에 들어간 후 비어있는 index에 TON 스테이킹이 적게외어있는 candidate들을 Member로 등록시킬 수 있습니다.
  1. 악용가능성
    1. 아젠다에 대한 투표하기전 해당 작업을 하여서 아젠다에 대한 투표권 자신이 다 가질 수 있습니다.
    1. MemberReward를 차지할 수 있습니다.

## DAOv2 정책

1. [[Lifecycle of  TIP (KR)]] 
1. 내용
  1. 위의 현재 DAO 아젠다 투표에 대한 정책 변경은 필요없을지?
  1. 변경을 한다면 Jason님이 초기에 적어준 정책으로 업그레이드도 가능해보입니다.
1. 문제점
  1. 기존 DAOAgendaManager Contract는 Proxy가 아니여서 업그레이드가 불가능하여 새로 배포하여야합니다.
  1. DAO Contract 업그레이드 하는 일정을 잡아 놓지않았습니다.

## 미팅결과

1. Hammer Audit Feedback
  1. Zena : 취약점이 존재 하므로 수정해야합니다.
  1. 수정안 
    1. retire → 일정시간동안 challange 금지
    1. 추가 고민 해보기 (25년 2월 18일 or 19일 Kevin Feedback)
1. DAOv2 정책
  1. 지금 DAO 투표 시스템을 변경할 필요는 없음
1. 