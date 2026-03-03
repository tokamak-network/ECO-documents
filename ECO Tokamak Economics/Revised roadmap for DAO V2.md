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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/00d9ae42-65fd-452a-9fc0-21c302d18f49/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3G5JTJL%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T085743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF7QsbcGo3ruxBjzptw0wSHwUS%2FYSPpflF8g02Vsz1xdAiBvt0M1mk0NEBEuyao8cIlctb196WQ7WOH4SG1%2B0CtXlyr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMWmcDRTzZt%2BT1Bd0TKtwDMU9g%2FVAwFZogm61jODwDaEAOhL8NS8qiqxaqqVNMpSLJv9yO3I07cgOn069DpIpxI4eT2vtOJw6Q33RkgTkLLEBE%2FlZZWCtEJQ%2B7fR69Ykz3dFN3kjg%2FrzIQVCV%2FjHUBhdZDfP6Xbmm5%2FpcJ0fnqAAU7hoPiRJappNlScnQLYslcIXCipN4Alfz8ho2zeQolyrvXG41%2F%2Fs2Z0CewVfZAlDw0YbpDZo2IK%2B5W2SFuhsDMh7TljYSPHiBrhtaDfsQjEGqUodlFmaMlZB7prc7iTC3MbDP7hyUeBSEt4VmVmfeRkvbP7HxkINZZ%2FSVbvEjbVO93fMT6aO9V4Fnqu6DHEOXeE%2FhUyz9FuVwZmakZnac5GULVmHvmOkw5SvWi4Se6Yp6WUY%2FPDbwzx%2BLflNBsez4ISz2w87k8x0zg2MZnuUtNW2X%2B2k0RPNB1RKqUo7EVjrVt1TxMGo3w0JGaxAjXYnrXX2FIzuMoUcFDHhBmD%2BW8U2lmdIcVc6wnPJSBlmfYNM88%2FKpQ7%2BmjwZAd8SILgUqXCEbTGGEh8Vhbon1HyinH0nhiVtMKBS42JIIofDbHy7DMo7U4iMKbllL6XR2KkqyU9sRHYjUbSuLz3BK1eZkXThuLMO4gNRfX4aAw9JrbzAY6pgFly9yRgP8GTGIBGD1Uy0%2Bre7hcIGxdgEXKzwcWMBFXxTDcFw1JkYap20UqMV%2FP6Tp44AGmkAmNmeIrxl8noB22OZsAiYiUa4dc%2FA4KnmZUQyuI5gbih%2BEkbmqPbZZSF%2B2CdHNMwic8dIig%2F6Z3JVQUtB3%2BMeAlx9y67N9bHv%2FbSh2uj%2FIOPEko6TPUDQGQ%2Banw7aZ9RYHkNLUUA9juU1bBJezTzyPg&X-Amz-Signature=ffc6c19fd1426e016b152df0029b4d8025c90ca04b8dda5fe294a3eec7deb80e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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