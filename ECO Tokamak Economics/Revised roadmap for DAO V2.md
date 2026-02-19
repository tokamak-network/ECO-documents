1. The original way, not using SYB scores: 

```solidity
number of votes = sqrt(TON_balance)
```

1. The vote only contributes if the user has score > x:

```solidity
number of votes = bool(score >= x) * sqrt(TON_balance)
```

*(here bool() is a function that returns 1 if the condition is true and 0 otherwise)*

 3. The vote is weighted by the score of the account: 

```solidity
number of votes = score * sqrt(TON_balance)
```

### Timeline of SYB

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/00d9ae42-65fd-452a-9fc0-21c302d18f49/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TR7ALF3U%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T042316Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD43iXaNljMjfA8Wz5wqUChlgOFdVNm2RGereRGqWQ%2B4QIhAOy24cw1HharMGKXm8%2BrdGHIJlJ3vL9%2B7HLvq%2Biksa%2BZKv8DCHQQABoMNjM3NDIzMTgzODA1IgypTL5QZM9cGLaf0JIq3APw9bMAfcyzUvlzy7DVDjB0wbIrQ4uM3ay9dPhGD1uMfjtiSag0WISF7wSzGbFbm0V82%2FukD9wT8ivxB7NRc%2FNq3%2BzpKnieqZVk2q3ew2c5%2BD%2BsoOhIhChoR0OPboYnZ9gvXqJAKy5SZClKf%2BGitYyWznVlkKchkVQ3WScHe3k%2BLkx2gddlJOeY7qJ1GBOFidkl55At6IV9wE9cHtWo366zj22J2e7d9nF%2B39mZmxVvgzg2UajS1Kpg%2F3HNlbhbWMVkjAaRCL%2BH9pbdBVf%2BW0SeQX%2BROtMYeSoQhi9SDW7begYsfyc2fHN0bdWDvfZBOpEQg5r0ri4hzuL03%2FzGF%2F8inFaDpgI%2FfnjwiR%2BRCnSFe4qPPpt7iaZdU5haRDfv9dmJIE2y3E4xwZS97HxQueI%2Bs%2F5zonuErsELR1XeYGvva2mPpfIwxC7vRozCPAWfl1YMLqI1zQvTASH6CUzmSNslkDERb5AGoOpl%2BcZsNaBtEUKN%2B%2BkFPw4q3F4dpBWwBUdY48qI2KAGQ1Pvf5rJ7XPUVM9ywpJesJePTR8JiKiggL8gwycS9H5ceBawGg53XPW4jhjYTJZzDqbdPcjht7ZfqM6QWMuZgJQmtwmTogeJ1tjxUrLA01bfdNk2RjDS8dnMBjqkAXieWM0Lf5Gv7T08QRG2yoHpkWZS17IvHo%2FMQCssUxO%2BdHokQqha6rnyWa5u%2BZVdcHOx0tc3Q571ob7uYZPwwYAjDjfXy2YokuuPC3EFBl58SNll%2BeAk9gYkETsncfgVDfwLq9f0e6BQcX%2BNquEoo0ynCzwuvn0XrymmQSizFfPejoMoB6ZimvkGM%2BTvD%2FxE3fT6yUQkurqvnxPND6f8Ug3CmE6L&X-Amz-Signature=530af943755c7b989c79bb1d00a66d262d4675472092042ce9fd00b4d8eb2ed4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Original Plan

| **Category** | **Subcategory** |  |
| --- | --- | --- |
| **Added use of Snapshot and forum** | **Open community version v1.0 + community guide**: Include documentation for new agenda creation via Snapshot and forum | Early Q2, 2025 |
| **Improvement of proposal interface** | **Open community version v2.0**: Add support for arbitrary code execution | End Q2, 2025 |
| **Apply the security council** | **Open community version v3.0**: Remove EOA from DAOCommittee Proxy, implement security council, enhance contract security, and define security council roles | Q4, 2025 |

### Revised Plan

| **Category** | **Subcategory** |  |
| --- | --- | --- |
| **Policy Document including PoU** | Policy document(v1.0 + Security council + Proof of Uniqueness based Snapshot) | Q3, 2025 |
| **Added use of Snapshot and forum** | **Open community version v1.0 + community guide**: Include documentation for new agenda creation via Snapshot and forum | End Q4, 2025 |
| **Improvement of proposal interface** | **Open community version v2.0**: Add support for arbitrary code execution | End Q4, 2025 |
| **Apply the security council** | **Open community version v3.0**: Remove EOA from DAOCommittee Proxy, implement security council, enhance contract security, and define security council roles | End Q4, 2025 |