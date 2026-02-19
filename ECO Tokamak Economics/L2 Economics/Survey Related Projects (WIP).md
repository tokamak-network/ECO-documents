Author: Suhyeon

Date: 2025-08-01

This page aims to compare Layer 2 projects taking similar approaches with Tokamak

## Overview

| 프로젝트 이름 | 토큰 | 스테이킹 및 시퀀서 보안 접근 | 설명 및 상태 |
| --- | --- | --- | --- |
| **Espresso** | ESP (추정) | 공유 시퀀서 네트워크에 PoS 스테이킹 적용. 노드 운영자와 스테이커가 슬래싱 메커니즘으로 보안 유지하며, 시퀀싱 권한 경매와 BFT 합의 지원. | 여러 L2 롤업 간 공유 시퀀서로 인터오퍼러빌리티 강조. 2025년 Mainnet 0(허가형)에서 PoS 퍼미션리스로 전환 중. ICO vesting 길어 투기적 리스크 있음. |
| **Starknet** | STRK | PoS 스타일 스테이킹으로 탈중앙화 시퀀서 운영. 최소 20,000 STRK 필요, 위임 가능하며 슬래싱 적용. Liquid Staking(stSTRK) 지원. | ZK 롤업 기반 L2로 v0.14 멀티 시퀀서 도입. 2025년 v3 스테이킹 완료 예정, 월 언락 스케줄로 공급 압력 있음. APY 약 7.35%. |
| **Metis** | METIS | PoS 스타일 스테이킹으로 탈중앙화된 시퀀서 네트워크 운영. 슬래싱 메커니즘과 LST(Liquid Staking Tokens) 보상 지원. | 이더리움 L2 중 최초로 탈중앙화 시퀀서를 구현한 프로젝트. 여러 시퀀서 노드가 경쟁하며, METIS 스테이킹으로 보안 유지. 2025년 현재 메인넷 운영 중이며, Vitalik Buterin의 어머니 관련 프로젝트로도 유명. |
| **Morph** | MORPH (예정) | 탈중앙화 시퀀서 네트워크에 PoS 스테이킹 적용. 노드 운영자와 스테이커가 수수료 공유. | Optimistic Rollup 기반 L2로, Holesky 테스트넷에서 탈중앙화 시퀀서를 시연. 2025년 메인넷 전환 예정으로, 효율성과 비용 절감을 강조. |
| **Eclipse** | ECL (예정) | 시퀀서 스테이킹과 탈중앙화. 홀더가 앱 지원 스테이킹으로 보상 획득. | Solana VM(SVM)을 Ethereum 보안과 결합한 L2. 시퀀서 스테이킹으로 사기 증명(fraud-proof) 지원. 2025년 메인넷 출시, 10,000 TPS 목표. |
| **Movement** | MOVE (예정) | 공유 시퀀서(M1)에 PoS 스테이킹. 탈중앙화 노드 네트워크로 업타임 강화. | Move 언어 기반 모듈러 L2 네트워크. M1 공유 시퀀서가 여러 체인에 분산 처리. 2025년 160K TPS 지원 로드맵. |
| **Aztec** | AZTEC (예정) | Fernet 프로토콜로 탈중앙화 시퀀서 구현. PoS 스테이킹과 프라이버시 증명 결합. | 프라이버시 중심 ZK L2. 2025년 분산 시퀀서 시스템 도입으로, 다른 L2 중 유일하게 탈중앙화 시퀀서 보유(현재 기준). |
| **Taiko** | TAIKO | 기반 롤업(based rollup)으로 Ethereum L1 validators를 시퀀서로 활용. PoS 스테이킹으로 L1 보안 레버리지. | ZK-EVM 기반 L2. 2025년 Fusaka 포크에서 FOCIL(Forced Inclusion Lists)로 약한 검열 문제 해결. |
| **Astria** | ASTRIA (예정) | 공유 시퀀서 네트워크에 PoS 스테이킹. 여러 롤업 간 중립적 순서화. | 모듈러 공유 시퀀서 프로젝트. Espresso와 유사하게 Polygon, Offchain Labs와 협력. 2025년 메인넷 준비 중. |
| **Ten Protocol** | TEN | POBI(Proof of Block Inclusion)로 탈중앙화 시퀀서. TEE(Trusted Execution Environment)와 PoS 결합. | 프라이버시 중심 L2. 여러 Aggregator가 경쟁하며, 2025년 MEV 최소화와 공정성 강조. |

## Comparison

| 카테고리 | 프로젝트 예시 | 주요 메커니즘 | 효율성/안정성 포인트 | 2025년 상태 및 리스크 |
| --- | --- | --- | --- | --- |
| **공유 모델** | Espresso, Astria | PoS 스테이킹 + 공유 네트워크 (HotShot/CometBFT) | 여러 롤업 공유로 비용 절감, 상호운용성 ↑ | 퍼미션리스 전환 중; 네트워크 실패 시 다중 영향 |
| **단일 모델** | Starknet, Metis | PoS 스테이킹 + 자체 시퀀서 풀 (ZK/Optimistic) | 특화 최적화로 안정성 ↑, 맞춤 보안 | v3 업그레이드/ DSEQ Reboot; 스케일링 비용 ↑ |
| **L1 레버리지** | Eclipse, Taiko | L1 validators 레버리지 + 하이브리드 스테이킹 | L1 보안 상속으로 복잡성 ↓ | 메인넷 출시/포크 업그레이드; L1 의존성 취약 |