@Unknown 

# URL

[https://simple-staking-v2-one.vercel.app/staking](https://simple-staking-v2-one.vercel.app/staking)

- L1 sepolia testnet에서 수행

# Scope 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/7d05fa1a-f5ad-4716-abd7-5bd467654284/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MZBHIZD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T041407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnBTs327KjoH3nNC5SSAs1gnProncdrgQSz%2BaLokke2AiEA9Vqols%2FsqcQLb55imgpmLtqnh4pMZZVonJS6XFC6Dl8q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDLExSpAMzZYrE%2BEVcyrcA2WFUtvnKsdfn8DdqfvnVPl34m3vuI3I9c2ULf07WQPxfjgJcypOHIE7ZKdaFRhJwy4bVUE9NurPWW1jnrXzqhH4hCI31veLxi0vmJ20UmqRUVNp%2Bh5aWZmnLqQDHFqes9TFo5osV4BTR8qEtG9MQ8e7wktGZlwqluadhUkYMLq7HtNlVvnfe6ZfrxR0HW%2FoqXKEFf%2Fv%2FWuiY82i4itXOFKsHs%2FfE%2BUnGGahyThf3qmGrdzH6UUn56Apf9hcHhMlXDytOsXyO3X4vWOPlOoSejWw6pMHiPdEoNFTcsYV5MQ4Kcq0XoEMN6YFW4uoU4RGGLzATozbNVoBfn2QRaaWiW3HNV84JH%2FT9pe64S2QQfKItPh%2FPu0w9sWd%2FA43KjTiuU3EEwbhpV6h%2FBvwgi7veAT%2BPlzTFB3DGkuN3ruC7U7TmAS80qGv1%2FTE9i4JL0vfsKBBsd8K2d0cVkt2iObAciLb%2FJrnAKe849nAAtQ0USeiSN3lnZ9U%2BiNPWHzc4T%2F8AoSLUTgy82lLECDxG6%2FTQ%2Fq61vXP04jD0l5ygRdHwXAnCsRcH22VYlc2Dmkg5HjWMcEhI%2BvkonSc7FbCXSU8AoHDrjGz6VJL9Cuz795CmCHQ6W9zZuDVPlQPCLWBMMLv2cwGOqUBbXAuuNvWEsfl875F2eA7iR4gfB2TDwmGbQIn%2F29LTJODXnGhDfU%2FVi4iDNXyzLRLuyXC%2F8nUb1%2BralT0fGPSdsJqR9sKMfE4FXPgXWjiWstWbxbYRi3KxOkJMbwYA56jJFik%2FY1OfrC3Z5wFHiYIZN0JaJ5GJh%2F%2BFHtK3ubH1HN6%2BLqF%2FZM82uZ7%2FP0xTuBavcadtoT7LZ2qA6QdpYY60Ny2ydoZ&X-Amz-Signature=60f14e50c4dea87ce5f510b747f0516c79a3d416f979ba5258d09c7f93b60583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Titan_Test1 오퍼레이터의 Withdraw 버튼을 누른후 나오는 기능들에 대한 QA를 요청합니다.
1. 위의 L2 탭에 대한 QA는 추후 요청 예정

# 1. Result

withdraw 기능 테스트 → 테스트가 가능한 5개 operator 대상

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/829348ad-4284-47dd-804a-1d251814b323/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MZBHIZD%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T041407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAnBTs327KjoH3nNC5SSAs1gnProncdrgQSz%2BaLokke2AiEA9Vqols%2FsqcQLb55imgpmLtqnh4pMZZVonJS6XFC6Dl8q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDLExSpAMzZYrE%2BEVcyrcA2WFUtvnKsdfn8DdqfvnVPl34m3vuI3I9c2ULf07WQPxfjgJcypOHIE7ZKdaFRhJwy4bVUE9NurPWW1jnrXzqhH4hCI31veLxi0vmJ20UmqRUVNp%2Bh5aWZmnLqQDHFqes9TFo5osV4BTR8qEtG9MQ8e7wktGZlwqluadhUkYMLq7HtNlVvnfe6ZfrxR0HW%2FoqXKEFf%2Fv%2FWuiY82i4itXOFKsHs%2FfE%2BUnGGahyThf3qmGrdzH6UUn56Apf9hcHhMlXDytOsXyO3X4vWOPlOoSejWw6pMHiPdEoNFTcsYV5MQ4Kcq0XoEMN6YFW4uoU4RGGLzATozbNVoBfn2QRaaWiW3HNV84JH%2FT9pe64S2QQfKItPh%2FPu0w9sWd%2FA43KjTiuU3EEwbhpV6h%2FBvwgi7veAT%2BPlzTFB3DGkuN3ruC7U7TmAS80qGv1%2FTE9i4JL0vfsKBBsd8K2d0cVkt2iObAciLb%2FJrnAKe849nAAtQ0USeiSN3lnZ9U%2BiNPWHzc4T%2F8AoSLUTgy82lLECDxG6%2FTQ%2Fq61vXP04jD0l5ygRdHwXAnCsRcH22VYlc2Dmkg5HjWMcEhI%2BvkonSc7FbCXSU8AoHDrjGz6VJL9Cuz795CmCHQ6W9zZuDVPlQPCLWBMMLv2cwGOqUBbXAuuNvWEsfl875F2eA7iR4gfB2TDwmGbQIn%2F29LTJODXnGhDfU%2FVi4iDNXyzLRLuyXC%2F8nUb1%2BralT0fGPSdsJqR9sKMfE4FXPgXWjiWstWbxbYRi3KxOkJMbwYA56jJFik%2FY1OfrC3Z5wFHiYIZN0JaJ5GJh%2F%2BFHtK3ubH1HN6%2BLqF%2FZM82uZ7%2FP0xTuBavcadtoT7LZ2qA6QdpYY60Ny2ydoZ&X-Amz-Signature=44ea56eff6c2c81ec6ddb83579f26bb12dffcb027bbfe38df624413b258305b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Operator로 Candidate_jason 선택 시

### Operator로 Eugene 선택시

### Operator로 Titan_Test1 선택 시

### Operator로 Test_member 선택시

### Operator로 Contract_team_DAOv2 선택시

# 2. QA buget

1. 지급기준 ([QA policy](/00a62bf844134cc3b1489190f7fc9877#4662abf08c064e6e86c09eb9b434fadd)) 
  1. 개선사항 (에러, 개선건의 등) 건당 10 TON
1. 개선사항 : 19건
  1. 기능별 테스트(unstake, withdraw 등) : 12건 
  1. Operator별 테스트 : 7건
1. PI 요청 : 190 TON (19건 x 10 TON)