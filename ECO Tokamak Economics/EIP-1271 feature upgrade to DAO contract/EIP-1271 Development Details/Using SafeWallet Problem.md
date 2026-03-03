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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d0915d88-fb66-4545-a768-2c57ad7a9b37/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GG4QM3H%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAmZAupud4iYyvfE2Rf1rUG6dUkaPyzfGOC%2FY31UemuAiBtGqtp%2FlIRpMOm8DkAp2BtbPwexIUAbd%2FkFI%2FkQGn5LSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMejRIO11LEGCzOdSXKtwDaJJRzexejoWHP8TznN6Of28PAcXt8Fo8DkDdFjDltVPwv%2FZHAbykCYl1bVx%2FnidXXPdi1TtZD%2FcXpgjd9dLy8mIeZW3IA4uZXUh%2FoCHmqLABYk5kQHUJvjtV1HnZY8%2BkN8aEq%2FhjZmx59ZnUgDP%2BHHEyFlyYwu29rdsit%2FakI4mI1yBCw%2BgcPRyK5K%2FwmIf2Mt37wo7%2BfMZnXzCYezzdKZ9A5tJ0idXwG%2FH7lfiT27dtaH8svTjVBFZdtMmDdjKq1Fg1M2IxPzDILN6C6vGiZyOGiSq0TBTmW5zKc%2Foh73ggHWcqhzEaCl6sn%2FOGBKoqf%2BbJu%2ByMDTMSjvU7kZQDqB98AHQHvq7jy1egUCGuJj1Kz72%2Fv2GzG2CehzYcWWy18yOet2ei5MVLkGw9VSphcq8CSTR8aBBSWwW1RjsSBxghZZqO8ydCBP7YPe%2BD3VH8LRaT%2Fw25SXAr8Tl3r4ynqCNJLrIzRdVIKDELJos4U3zO4qQxOjMzVwB%2BiSf453Ulf%2BMPPPd7IOpi4qdg72LfWlTNQrzuXB3GyiNufrT9CzNCseiBMHVtiQIUhinBtMpHiZjSaRGKeY1q2zeYjW7Fv7o%2BzeeNKO5Dg5xF%2FI0LuxKKD0XaUg77HOF%2FyaUwpJnbzAY6pgHthj70bWfg33Nh09iCkv9TdMne3Y8jErJDN4DjU7EvzjXmJDOptDsBytvZIx78rwAaqR7La5OWqlOzB7ZCccGwLIZibwHHa9OUdO1L9QS0GukXCzWIab28qlWztK7gzhGxiJ%2BiusfNBtotTlQvGjvqWSz0ZaWL7aUGttMDQWthfyRZ0Yonv9suDeh1yHaE1%2FH04Nw2vgXay9P545v7sK9NLA5DxIqb&X-Amz-Signature=969c118b3df6d8153eabd267ba698b9c108d4eafe48fcb67ffd01383af7dc045&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Front에서 보여지는 Signature (41로 보여져서 이것을 실행시킬때 에러가 남)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/5648faf0-51bb-4529-a1fc-eed4d173f07f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GG4QM3H%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGAmZAupud4iYyvfE2Rf1rUG6dUkaPyzfGOC%2FY31UemuAiBtGqtp%2FlIRpMOm8DkAp2BtbPwexIUAbd%2FkFI%2FkQGn5LSr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMejRIO11LEGCzOdSXKtwDaJJRzexejoWHP8TznN6Of28PAcXt8Fo8DkDdFjDltVPwv%2FZHAbykCYl1bVx%2FnidXXPdi1TtZD%2FcXpgjd9dLy8mIeZW3IA4uZXUh%2FoCHmqLABYk5kQHUJvjtV1HnZY8%2BkN8aEq%2FhjZmx59ZnUgDP%2BHHEyFlyYwu29rdsit%2FakI4mI1yBCw%2BgcPRyK5K%2FwmIf2Mt37wo7%2BfMZnXzCYezzdKZ9A5tJ0idXwG%2FH7lfiT27dtaH8svTjVBFZdtMmDdjKq1Fg1M2IxPzDILN6C6vGiZyOGiSq0TBTmW5zKc%2Foh73ggHWcqhzEaCl6sn%2FOGBKoqf%2BbJu%2ByMDTMSjvU7kZQDqB98AHQHvq7jy1egUCGuJj1Kz72%2Fv2GzG2CehzYcWWy18yOet2ei5MVLkGw9VSphcq8CSTR8aBBSWwW1RjsSBxghZZqO8ydCBP7YPe%2BD3VH8LRaT%2Fw25SXAr8Tl3r4ynqCNJLrIzRdVIKDELJos4U3zO4qQxOjMzVwB%2BiSf453Ulf%2BMPPPd7IOpi4qdg72LfWlTNQrzuXB3GyiNufrT9CzNCseiBMHVtiQIUhinBtMpHiZjSaRGKeY1q2zeYjW7Fv7o%2BzeeNKO5Dg5xF%2FI0LuxKKD0XaUg77HOF%2FyaUwpJnbzAY6pgHthj70bWfg33Nh09iCkv9TdMne3Y8jErJDN4DjU7EvzjXmJDOptDsBytvZIx78rwAaqR7La5OWqlOzB7ZCccGwLIZibwHHa9OUdO1L9QS0GukXCzWIab28qlWztK7gzhGxiJ%2BiusfNBtotTlQvGjvqWSz0ZaWL7aUGttMDQWthfyRZ0Yonv9suDeh1yHaE1%2FH04Nw2vgXay9P545v7sK9NLA5DxIqb&X-Amz-Signature=fe93ee8ebeb3bcc453ff86d5c40b7c123465e909295fe272c6b95381c6713ee8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# SafeWallet Contract관련 문제

1. SafeWallet의 Signature를 복구하는 방식이 EIP-1271표준을 따르지 않는 문제가 있었습니다.
1. SafeWallet에서 제공하는 SafeTxHash를 사용하여서 Signature을 복구하였을때 signer가 제대로 복구되지 않는 현상을 발견하였습니다.

해결

1. SafeWallet Contract, SDK를 분석하여서 EIP-1271표준을 따르지 않는 signature복구 과정 확인
1. SDK를 분석하여 SafeTxHash값이 아닌 어떤 Hash값으로 서명하는지 확인