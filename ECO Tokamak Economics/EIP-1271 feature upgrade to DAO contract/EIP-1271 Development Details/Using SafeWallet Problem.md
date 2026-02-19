# SafeWallet SDK관련 문제

1. MultiSigWallet의 Owner들 중 2명이상 Sign을 해야되는데 이 경우 혼자서 하는 경우가 아니면 SignData를 주고 받아야함
1. 현재 Sepolia기준으로 SDK와 Front의 코드가 통합되지 않아서 생기는 오류가 있습니다. 배포하는 Contract버전이 다르고 Sign Confirm을 제대로 해도 Front에서는 제대로 되지 않았다는 오류가 발생합니다. (Sign confirm의 값과 Front에서 보이는 값이 다름) → 이 오류로 인해서 Front에서는 Contract에서 Sign시 Front에서 execute가 불가능해서 따로 signature값을 기억했다가 execute를 호출해줘야합니다.
1. 현재 Sepolia기준으로 Contract와 SDK의 코드도 통합되지 않았음, 1.3.0, 1.4.1 버전에는 MAGICVALUE가 0x20c13b0b이고 1.5.0버전 부터는 0x1626ba7e이고 버전은 1.3.0, 1.4.1, 1.5.0 이렇게 쓰이고 있는 것 같음 (어떤 버전을 쓸껀지에 따라서 Contract 코드가 달라져야함)

결론

1. 어떤식으로 SafeWallet을 생성하고 해당 버전은 어떤 버전인지 확인 필요
1. contract가 Sign을 했을때 잘못된 Sign값을 기억하기 때문에 Front에서 execute에러가 나는데 사용자들이 어떤식으로 execute하게 할 것인지 생각 필요 → 스크립트 제공으로 해결
1. MultiSigWallet의 Owner들이 어떤식으로 사용되는지에 대한 이해 필요 (PRIVATE KEY관리를 한명이 할것인지 여러명에서 할 것인지) → 스크립트 제공으로 해결
1. Safe쪽에 해당 이슈 공유하고 이슈 해결할 수 있도록 건의

내가 만든 Signature (82로 만들어서 통과)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d0915d88-fb66-4545-a768-2c57ad7a9b37/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DAUU3T6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCpncBzCj%2F6O0wR%2Ba51I77qtBJ%2FWx0BsACd6GO7csx2wIhAM1pXyJG6SJ76UWSr1RvQy3bIiCbcFfl0RxDncDFPeVtKv8DCHQQABoMNjM3NDIzMTgzODA1IgxBlenl1kMUPtlICiAq3AMWV6CFlIEZZP6ypgSDs1iICLUL0JJCvg8Kua%2BHkdhzIPTDmcSqhNbSlMkBmcQdov2L0ujYoyhkfcVOyJ38tPVlgMt4z6HGdg6bqEmwGndKQS4xkW60A0aDURmBZ4EnbOU3k8UHzEcHMX9Sj7AduFs4kO%2B2yuOEBeC9IDgwjpj80rgbAyj81vTXa8I5GH2WfKnGWFEDzyJ85D8iL%2FGUijCK9%2FN8L%2FvvsMiiceYVcG2QrK4TTzJx2Rurqdok5TMATSD4yHL5r6tL%2FijRm1SwY4QvSJ9TWup7I1MlEfZFhh1jkaAtB48MBgv8ArwtTODIw3mQZKpdEWB1MgicNcySP5nKAnW6KndKDbKzGBaTp7qRJxZZYKbEjbNKjxlZm0WJJBNhIj920zcHwGN%2FXj2RwhVp%2B35vquRRrGy92rpn5tOKnxnWmzNEnW2PZmJZnaZY0dT9d%2BLB3rWn37J%2BI9qfc%2F9QfXitmlDO8P5NZ3MBHh6PqJODOQbZUhr3o2EDsCyU1mmso9YLJGhL6Oe8BN9WA2cjkthKskHGtYP6Lns57zoK1PzkuZUX3uRQs0k33rXOvrBTlAMRqAwYJ2hGiGbsfcBcLV7AivAMayQyYCwtsmZX2nnbhsbx83BbnE9vijDE79nMBjqkAQtpR8CxpoXOsyTyMs18jXTnzySOcteyrmt2ORIaCou9DAwuDCffTBbq3K1pts6Dd46IBvqKX7ClSJkVLBINl%2BwWNnwq5Z5cjJagBtwhqkThl%2FhrmhY5BolFYRZWVmUlsulqVY0hCzPgWYFEkf5kL%2BIzOQFFY2WOpCK%2BSetixN%2FodOflOAe8SgH8uPFUQBRspKJUFg6o4xepABFz%2FsfKPMSUBVf6&X-Amz-Signature=8c34a78d9f013dc4422e775b7296b0deb94f149eaef086ba1a3f4857fc68406c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Front에서 보여지는 Signature (41로 보여져서 이것을 실행시킬때 에러가 남)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/5648faf0-51bb-4529-a1fc-eed4d173f07f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DAUU3T6%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCpncBzCj%2F6O0wR%2Ba51I77qtBJ%2FWx0BsACd6GO7csx2wIhAM1pXyJG6SJ76UWSr1RvQy3bIiCbcFfl0RxDncDFPeVtKv8DCHQQABoMNjM3NDIzMTgzODA1IgxBlenl1kMUPtlICiAq3AMWV6CFlIEZZP6ypgSDs1iICLUL0JJCvg8Kua%2BHkdhzIPTDmcSqhNbSlMkBmcQdov2L0ujYoyhkfcVOyJ38tPVlgMt4z6HGdg6bqEmwGndKQS4xkW60A0aDURmBZ4EnbOU3k8UHzEcHMX9Sj7AduFs4kO%2B2yuOEBeC9IDgwjpj80rgbAyj81vTXa8I5GH2WfKnGWFEDzyJ85D8iL%2FGUijCK9%2FN8L%2FvvsMiiceYVcG2QrK4TTzJx2Rurqdok5TMATSD4yHL5r6tL%2FijRm1SwY4QvSJ9TWup7I1MlEfZFhh1jkaAtB48MBgv8ArwtTODIw3mQZKpdEWB1MgicNcySP5nKAnW6KndKDbKzGBaTp7qRJxZZYKbEjbNKjxlZm0WJJBNhIj920zcHwGN%2FXj2RwhVp%2B35vquRRrGy92rpn5tOKnxnWmzNEnW2PZmJZnaZY0dT9d%2BLB3rWn37J%2BI9qfc%2F9QfXitmlDO8P5NZ3MBHh6PqJODOQbZUhr3o2EDsCyU1mmso9YLJGhL6Oe8BN9WA2cjkthKskHGtYP6Lns57zoK1PzkuZUX3uRQs0k33rXOvrBTlAMRqAwYJ2hGiGbsfcBcLV7AivAMayQyYCwtsmZX2nnbhsbx83BbnE9vijDE79nMBjqkAQtpR8CxpoXOsyTyMs18jXTnzySOcteyrmt2ORIaCou9DAwuDCffTBbq3K1pts6Dd46IBvqKX7ClSJkVLBINl%2BwWNnwq5Z5cjJagBtwhqkThl%2FhrmhY5BolFYRZWVmUlsulqVY0hCzPgWYFEkf5kL%2BIzOQFFY2WOpCK%2BSetixN%2FodOflOAe8SgH8uPFUQBRspKJUFg6o4xepABFz%2FsfKPMSUBVf6&X-Amz-Signature=f1eba3d60f3b53e2a5f0ce1c4e395cfc47dbf83df1c378b2155b0ce76417c711&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# SafeWallet Contract관련 문제

1. SafeWallet의 Signature를 복구하는 방식이 EIP-1271표준을 따르지 않는 문제가 있었습니다.
1. SafeWallet에서 제공하는 SafeTxHash를 사용하여서 Signature을 복구하였을때 signer가 제대로 복구되지 않는 현상을 발견하였습니다.

해결

1. SafeWallet Contract, SDK를 분석하여서 EIP-1271표준을 따르지 않는 signature복구 과정 확인
1. SDK를 분석하여 SafeTxHash값이 아닌 어떤 Hash값으로 서명하는지 확인