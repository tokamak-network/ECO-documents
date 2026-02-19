# **Introduction**

When the Titan Network service is closed, the remaining assets on the Titan network can be withdrawn from the Ethereum network.
Withdrawal is possible through the UI web service, or users can also withdraw their assets through Etherscan.

This document explains how to withdraw assets through Etherscan.

The titan_new-generate-assets.json document provides hashes that can be claimed for a specific asset.  

**Step 1. In the "titan_new-generate-assets.json" file, search for your address in the data area corresponding to the desired token name.**

**Step 2. Copy the l1Token address, amount, and hash values corresponding to your address from the “generate-assets3.json” file.**

If you look up the address 0x796C1f28c777b8a5851D356EBbc9DeC2ee51137F, 

If you search below,

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/c36aedb0-2f37-4836-97d4-381f460ecee3/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-12-23_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.28.56.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4OCP7XO%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T042128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB2vw6ID1HXANLSXl3L831sdV8Boyz0pXsChXwkvzB47AiAM2M%2FmTmJNK7h3O%2BLGnKCWwkgoog3j9Z1PMIRkCMqyLSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMQ%2F2CEuYLSdQrZjw2KtwDtN%2FHLsWRV%2BS5aIHb3JuOQ7icMxXOS4Ha1NJEl0NhByerPQzAF5Cih%2BmRNWgnJwq2YyEZKKl87OK8A7H3NAf3ky71%2Bm5YQxdT3SuN7lZNX25kw2gmVAJ7vSZQIsR87TS%2FvhMLCEV8WO1suGrlVTrEwJxAVFSqrLfRvuV4uo7QMRZW38%2BqwldNlGZehOwHyC533hy3g%2BwWj%2F96Qr%2Bsv7ViAKDCWJkIANeEx7AfvrGJDuQ9mHozxSCCaF2ba19cJ%2FS7inB6mX%2Br6kZ%2B81VPzXvRIayUf2lYf2cByiku1syOkT6P1HesqgyRbIXkgTbKPjs9SgLVOq10QpBPzlLlUTTE4Iucyz%2B9inBV3SX9guUFbM8euSxHI9HoieHTq%2FZGC19sMsvVEGFnuKod2ZUDxG%2B7YrPS1hywuECVxartz4%2FUhQhbkkYnlksZzuNebjf2jnesjSrXEmiuhNvYyqpi4X0Xl1%2B0Zwr%2FSYqiX0aem7jH4%2FAXDoXbIUr%2Byd758ewTL0dJBNT7Y8jDKCqevIsV8xGIvvhCTFx%2FtNK5%2Ff1eDo7gp6VuO9%2B%2FeOek48ajYFUHflgc52z2Ei%2Fp5lTSPUM9NxfQCRt37MWMWlWOHQ7vS8PATuNhLdQlS%2FKo16%2BxEPcwzPDZzAY6pgHenQU7gBd3kpHA4XmGwLDBJIPspLDLi1rcSUHwr5dBKLwfCJdjqEyNy50%2F2Rd7RzWxNgFkmA%2BtXi%2BV6l5cGQgwpjK%2BRLQzyEUstTccKVKhDKQZKr8CuwxEZI%2F2u4Gc7NJYTGdamaWU0mOMqroYjcx1FY07l%2BUejhWivg%2FWA12F%2FTU2gNmF%2FOK7%2Fo8N1ZyekgW%2FvusoKdVB0xhDldiOwWUnI%2BhUk%2FAe&X-Amz-Signature=406e6e0bb14b81279a46336c5abecc173ce00374606c39f00b0509a800f34f1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

To convert the amount (77075825179826438) from wei to Ether (decimals 18), divide by 10^18, so you can claim 0.077075825179826438 ETH. 

 

**Step 3. Check if you can claim the token with the hash.**

- Contract: L1StandardBridge ([link](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#readProxyContract))
- Function: [claimState](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#readProxyContract#F2)
  - Hash (string): Hash value retrieved in Step 2
- Return (bool): <u>*A claim is possible only if the searched value is false*</u>. If it is true, a claim has already been made.  ** **

**Step 4. Look up the contract position that stores the claim information.**

- Contract: L1StandardBridge ([link](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#readProxyContract))
- Function: [getForcePosition](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#readProxyContract#F6)
  - _hash (string): Hash value retrieved in Step 2
- Return (address):  **the contract position address **

**Step 5.  Claim **

You can claim one asset or multiple assets at once.

- Connect your account into etherscan clicking `Connect to Web3`.


**Step 5-1.  Claiming a single asset**

Go to the [L1StandardBridge contract ](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#writeProxyContract)in ethersacn and click `Contract` → `Write as Proxy`.

- Contract: L1StandardBridge  
- Function: [forceWithdrawClaim](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#writeProxyContract#F11)
  - _position (address): The contract position address returned in step 4
  - _hash (string): hash retrieved in step 2
  - _token  (address): l1Token retrieved in step 2
  - _amount (uint256): amount retrieved in step 2
  - _address (address): claimer retrieved in step 2

After entering the parameters, click the write button to execute the transaction.

![](images/b7d9156c6b06.png)

**Step 5-2.  Claiming multiple assets at once
**Go to the [L1StandardBridge contract ](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#writeProxyContract)in ethersacn and click `Contract` → `Write as Proxy`.

- Contract: L1StandardBridge  
![](images/ed777db3ea65.png)

  - Function: [forceWithdrawClaimAll](https://etherscan.io/address/0x59aa194798Ba87D26Ba6bEF80B85ec465F4bbcfD#writeProxyContract#F12)
    - params :  
Enter each asset claim information as an array in the form of
{address position, string hashed, address token,uint amount,address getAddress}
  - examples 
** **When claiming two assets, (1) TON and (2) ETH, enter as in (3).

    - (1) TON search results
```json
 "l1Token": "0xa30fe40285B8f5c0457DbC3B7C8A280373c40044",
 "l2Token": "0x7c6b91D9Be155A6Db01f749217d76fF02A7227F2",
 "tokenName": "Tokamak Network Token",
  
 "claimer": "0x757de9c340c556b56f62efae859da5e08baae7a2",
 "amount": "996000000000000000",
 "hash": "0x7d4ad43c4eb5152ab242a8eacacba53b20e06cff3a6533f6ce15cfcf03e2176d"
 
 
 getForcePosition:  0x1a7dFF905E30d36578b6b2aC46089dEc51531067
```
    - (2) ETH search results
```json
"l1Token": "0x0000000000000000000000000000000000000000",
"l2Token": "0xDeadDeAddeAddEAddeadDEaDDEAdDeaDDeAD0000",
"tokenName": "Ether",

"claimer": "0x757de9c340c556b56f62efae859da5e08baae7a2",
"amount": "105899999967584534",
"hash": "0x946fda2cf90bda4739dce26cf41c16776e462618b3752e9645a05bb5512e2781"
 
 
getForcePosition:  0x1a7dFF905E30d36578b6b2aC46089dEc51531067
```
    - (3) Input values 
```json
[{position:'0x1a7dFF905E30d36578b6b2aC46089dEc51531067',hashed:'0x7d4ad43c4eb5152ab242a8eacacba53b20e06cff3a6533f6ce15cfcf03e2176d',token:'0xa30fe40285B8f5c0457DbC3B7C8A280373c40044',amount:'996000000000000000',getAddress:'0x757de9c340c556b56f62efae859da5e08baae7a2'},{position:'0x1a7dFF905E30d36578b6b2aC46089dEc51531067',hashed:'0x946fda2cf90bda4739dce26cf41c16776e462618b3752e9645a05bb5512e2781',token:'0x0000000000000000000000000000000000000000',amount:'105899999967584534',getAddress:'0x757de9c340c556b56f62efae859da5e08baae7a2'}]
```