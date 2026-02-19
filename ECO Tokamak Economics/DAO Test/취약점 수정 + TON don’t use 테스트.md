취약점 수정 전 테스트

1. claim 실행
  1. tx : [https://sepolia.etherscan.io/tx/0x4350a549c177ed6f8caea0221571368ee74d92b49a09bfdefa24c332bdab10a7](https://sepolia.etherscan.io/tx/0x4350a549c177ed6f8caea0221571368ee74d92b49a09bfdefa24c332bdab10a7)
  1. amount : 1,321.232 TON 얻음 (WTON → TON으로 swap 후)
1. claim 이후 
  1. getClaimableActivityReward : 1.6362TON
1. retire 이후
  1. getClaimableActivityReward : 1324.315 TON (claim받을 수 있는 양이 늘어남)
1. ChangeMember 이후
  1. getClaimableActivityReward : 1325.532 TON
1. claim 실행
  1. tx : [https://sepolia.etherscan.io/tx/0x8a40782699c81c179a9df55a755cc3aea6d7fb80ddca4e2d4be947022fbf9eaf](https://sepolia.etherscan.io/tx/0x8a40782699c81c179a9df55a755cc3aea6d7fb80ddca4e2d4be947022fbf9eaf)
  1. amount : 1,325.722 TON
1. claim 이후 
  1. getClaimableActivityReward : 0.646 TON
1. retire → challenge를 통해서 계속해서 공격 가능

취약점 수정 후 테스트

1. claim 실행
  1. getClaimableActivityReward :  92.237 WTON
  1. tx : [https://sepolia.etherscan.io/tx/0x15e0dc75dc56350a509232604a3590b4444f5785241e0977cc261ef7a687902d](https://sepolia.etherscan.io/tx/0x15e0dc75dc56350a509232604a3590b4444f5785241e0977cc261ef7a687902d)
  1. amount : 92.808 WTON
1. claim 이후
  1. getClaimableActivityReward : 0.646 WTON
1. retire 이후
  1. getClaimableActivityReward : 0.951 WTON
1. ChangeMember 이후
  1. getClaimableActivityReward : 0.989 WTON
1. 이상 없음 확인