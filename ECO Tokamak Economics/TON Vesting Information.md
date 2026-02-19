# Vesting Contract

> [!note]
> 📌 **The vesting contract outlines the how 50,000,000 TON is allocated into various vault.** Each vault has its own unique token and can be exchanged for TON at a specified swap ratio. The vault also specifies the authorized individuals who can access the tokens, as well as the unlock schedule.
> There is a special vault called MarketingTON that does not have unlock schedule and allows for swapping beyond a predetermined amount. However, it's important to note that this does not result in the creation of additional TON. Any surplus swap amount is deducted from the claimable amount in other vaults. In other words, the total claimable amount from all the vaults remains fixed at 50,000,000 TON.

- Medium article about Vesting model: [medium link](https://medium.com/onther-tech/tokamak-network-token-economics-en-kr-97f105ef8517)
- Medium article about Vesting contract: [medium link](https://medium.com/onther-tech/ton-token-vesting-system-29588659260)
- Vesting repo : 

[Link](https://github.com/tokamak-network/presale-contracts)

## [SeedTON](https://etherscan.io/address/0x6c1e75ce98f67e15587388f633d8c7ae8f2c399f)

## [PrivateTON](https://etherscan.io/address/0xa4eac2a2eaff4a43e31b336406a6d618725032cc)

## [**StrategicTON**](https://etherscan.io/address/0x9ab783adc9958f578cb4b126187592e2d9072a2d)

## [Team](https://etherscan.io/address/0x07599893969f5a4851d149ed14dbeba886811afb)[**TON**](https://etherscan.io/address/0x07599893969f5a4851d149ed14dbeba886811afb)

## [Advisor](https://etherscan.io/address/0x7c65182dd2ec55d3d91d16e2e69eebe251a5f1a2)[**TON**](https://etherscan.io/address/0x7c65182dd2ec55d3d91d16e2e69eebe251a5f1a2)

## [Marketing](https://etherscan.io/address/0xe3a87a9343D262F5f11280058ae807B45aa34669)[**TON**](https://etherscan.io/address/0xe3a87a9343D262F5f11280058ae807B45aa34669)

## [Business](https://etherscan.io/address/0x774bb5875072dea0a41f8d4ea90adc36270cc98e)[**TON**](https://etherscan.io/address/0x774bb5875072dea0a41f8d4ea90adc36270cc98e)

## [Reserve](https://etherscan.io/address/0xd1f04aad6582f6034f4e5709f2c09b147f3376c5)[**TON**](https://etherscan.io/address/0xd1f04aad6582f6034f4e5709f2c09b147f3376c5)

## [DAOTON](https://etherscan.io/address/0x08368cf6c32f5ca0ac80f7bc9da768fc775e9cd7)

# Swap Contract

> [!note]
> 📌 The policy for swapping vault tokens to TON (Tokamak Network Token) is stored in Ethereum network. **The token swap contract applies rules for the vault token’s circulating supply, timing of coin circulation, and allocation of newly circulated coins. **Because these rules are defined in the smart contract, nobody, including the system's developers, can change the contract or its rules.

- [VestingSwapper](https://etherscan.io/address/0x25c31c6f764c11fbe62b72e83a149771d6d70a61) (Seed**TON**, Private**TON**, Strategic**TON, **Marketing**TON)**
- [Swapper](https://etherscan.io/address/0x8db1fdfda8d1024f8a5b5dced5ec1918435f2fc8) (Marketing**TON, **Team**TON, **Advisor**TON, **Business**TON, **Reserve**TON, **DAO**TON)**

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/fc262c27-4d4e-4d76-add6-c384f76e55f8/SwapDiagram.svg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC75VK6I%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T040012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwB1JLsuTUmB%2BT0laJNIx%2FgI4301TUXK3xa9cuefI7VAIhAOn4WiDl2uHtOtUGMI9n0HTjityLnS41KDQmRckt7JzZKv8DCHQQABoMNjM3NDIzMTgzODA1Igw6GcFqiMKWP44S22Iq3ANqGaOtAOVvWY8hxRYZaq%2FhzxOEDC61Z95x7jn%2BPWNUwWoV3BmxzmjM1gosFprSRY%2FmrTS1QjSBZr0W2KByyUM6LhWLXGh5WYn9h%2B6nBSA9jnR5uo58YYyIZHoqAvBk8J4eTJTC2MZ12TP0TpE982hsBWveBCzQyo3RTlk0BY8XY%2FcIUCFAFFWazRzksUsN2P07VGkG7t6ovfm1FZiV%2FKh%2F2J%2BI9ahosBo%2FRplRZ6MohBc6AIebYtxMhG65ZDl9P6GIL9xotyhHkl7u3XZf6XBP8mqbWmkKFUwCdhqRGbsd8nlAC0gvDivqMtEpgt4l6WMNGtMR65X6vQxfd5WY5DJDUmM1MMxnKVc%2BvRHou5g3cgtoWh7qhE51goMsqA85m9O2uIx2Dr2ObaEj8nFCVDR6WYdmW%2FnKUF%2BUXWuxptXw29aWlu1dD5yADb7%2B0vI0hq8LD3XiNW9i8Xo%2FPLmeD7P0mi4gjzTMAi4K2F7ZnmRYD7a%2FXt2iP%2B1nm%2Bknw2gj0PRSidUU541a9Z0iWIpAzdrVQ%2BiTtorROrlPD7R6UVy9dsPPbQHav6DEKvkWIIKfh0pV7jDYsXqjpOAUhmAmC8IF2f4nGfFxTIwbT6FJxdMF5Kb27Td3qdFq0iQnoDCc8NnMBjqkAVZLPx7Pq0i3CBIAHxQznKHgW7TaCn5pHCRr3jvWwc24gKAeWRaOy042NanJDeSMyGgH4cqxQwXs8lTTRJm53HyFfhpBF8oxTI3sDG7hrEIXwSoen4aWEHsoaGj9rGHzIz6vBx7tLzz2727Iue7LCfemkBKfOmeKn6Vlas9%2FnZafvC5Pml%2F7FUm0v8kO3EhJlwK3IsQcktZvg0nUo8Hsa%2F%2BSaHRy&X-Amz-Signature=c838b03a0b4089cc76ac992ba464d002da0cdc59fdcf70ec422fd296f4b114fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)