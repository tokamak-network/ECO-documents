[Sample]
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [ ] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [ ] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking |  |  |  |
| Unstaking |  |  |  |
| Restake |  |  |  |
| Withdraw |  |  |  |
| Calculator |  |  |  |
| Update Seigniorage |  |  |  |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Justin
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 3 | Works but has UI update issues - staked amount doesn't refresh automatically after transaction. |
| Unstaking | Y | 2 | Allows unstaking more than staked amount leading to failed transactions. No failure notifications shown. UI doesn't update after successful unstake. |
| Restake | Y | 2 | Only supports restaking all unstaked amounts at once via redepositMulti. No option to use sequential redeposit. |
| Withdraw | Y | 1 | no warning about 14-day wait, no pending amount display, L2 withdrawal locks users out if they unstake first. Missing L2 network info. |
| Calculator | Y | 5 | Simulator works well |
| Update Seigniorage | Y | 3 | Functions but has grammar error ("Seigniorage is updated X" should be "was updated at block X"). Block number doesn't update in UI after transaction. |
| Claim(If you have L2) | Y | 2 | No L2 network information (RPC, explorer, chain ID). Users can't verify or access their L2 funds. Unclear seigniorage terminology. |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

 ETC: Network validation only works for mainnet, not other networks.

Nam
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation(Ubuntu 24.04 on WSL)**

```javascript

➜  staking-community-version git:(internal-test) ✗ node -v
v20.16.0
➜  staking-community-version git:(internal-test) ✗ pnpm -v
10.7.0             
```

  - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
  - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
    1. But the terminal shows this error

```javascript

 ✓ Ready in 1318ms
 ○ Compiling / ...
 ✓ Compiled / in 12.6s (8676 modules)
 ⚠ Unsupported metadata viewport is configured in metadata export in /. Please move it to viewport export instead.
Read more: https://nextjs.org/docs/app/api-reference/functions/generate-viewport
 ⚠ Unsupported metadata viewport is configured in metadata export in /. Please move it to viewport export instead.
Read more: https://nextjs.org/docs/app/api-reference/functions/generate-viewport
 ⨯ src/components/modal/WalletModal.tsx (279:24) @ window
 ⨯ ReferenceError: window is not defined
    at WalletModal (./src/components/modal/WalletModal.tsx:348:28)
digest: "1297123957"
  277 |         mx="auto"
  278 |         position={'absolute'}
> 279 |         right={(Number(window.innerWidth) - 1150) /2 }
      |                        ^
  280 |       >
  281 |         {
  282 |           (!chainSupported || (chainId && chainId !== Number(DEFAULT_NETWORK))) ? (
 GET / 500 in 13169ms
 ○ Compiling /[contractAddress] ...
 ✓ Compiled /[contractAddress] in 6.9s (8840 modules)
 ⚠ Unsupported metadata viewport is configured in metadata export in /favicon.ico. Please move it to viewport export instead.
Read more: https://nextjs.org/docs/app/api-reference/functions/generate-viewport
 ⨯ src/components/modal/WalletModal.tsx (279:24) @ window
 ⨯ ReferenceError: window is not defined
    at WalletModal (./src/components/modal/WalletModal.tsx:348:28)
digest: "1297123957"
  277 |         mx="auto"
  278 |         position={'absolute'}
> 279 |         right={(Number(window.innerWidth) - 1150) /2 }
      |                        ^
  280 |       >
  281 |         {
  282 |           (!chainSupported || (chainId && chainId !== Number(DEFAULT_NETWORK))) ? (
 ⚠ Unsupported metadata viewport is configured in metadata export in /favicon.ico. Please move it to viewport export instead.
Read more: https://nextjs.org/docs/app/api-reference/functions/generate-viewport
 GET /favicon.ico 500 in 7575ms

```



2. And in the front-end side, we are looping to call the RPC → The RPC is DDOS-ed 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/a3090dda-8a1c-471f-addc-872e8595def4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2K2O353%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLD3cflh80Ua78THakmwWOJccassXfCmf4x5aQ2vbFGAiEA5eSUgFFuWLQBGZY6rkanzTWPtW6GrTGqpYCA3w%2F3h04q%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDLOLFWpK%2BkrxJ4F45ircA1pmvV0WOimJVCdNhDAPDy8BD2k22SLBVtjkfFobXU2DUOXas%2FyOcQiOBhjo7qmuwKguuLA7A%2BREqdYtSZ%2BNniJqXvoJvGk93%2FjKdaFIeQmkxCWJKyz2kXx53MooKsB%2B9R9bEoZA6Y0jSrN85lVSMBy%2F5dKJgzG3u0wDmdr8rsdcoiPvCGEIEdf5KZrAtnvrKMmDdXxv8EglVwySThzeSk1VgHfgsYHnLEdA4sk6hkWWEz6Hx9kA72rWHuWNUoJgS9ev%2BKz9Wv0HXEs6L72ceBBp0q3yORtBduBX%2FfNjk2S5oEHxzVfyk9WUTZzP21zCikIZ5N2PDLULBkyMaEqMxT4hbuJ5aPH0dtOz4GM0SnOf9Dqb2U5Zf5UoNwha0Y%2FSPQO4Mjc2jm972o9ERcToOBDg1v8PZ6pG53WHtdQ5LrqPSCpnswyWbtCOvgv%2BMzMe1qIc%2BbynmNtk9O9cCZr6PbVgZg1kLwaYejt3%2BiRR7hoYzY6xN%2FXrXPVw2XgY52Opf8IauVi2oaiywuihXjZ2MHPgPRbnFAB4Q01wFv6h0tnpiB5y1gR%2FnwYuaCCLU7tEvhTsfLATkdo1DM%2Fyy4UCSaB3zVyhFK2QJXI2pZ1fdMknQl5CuLUlWPZGC6zHMOXE2swGOqUB9h0fQcgiI7%2Btow1Ystb5Q%2F4mCI%2BPRZWpj6posihMBZnXCFQApIGedu07veLRJEpK88runeo6xLrIjQwJuBRk7JXPpIjT%2BO3HyPfVuChialG%2FpgNxrYc%2B%2F730pJ%2BoMByYLd10GGjvKhj543CercjxLMhNOCQXUCNtktnefvObh2KkiXW35KPjjJBV7KZCt91a3TNyKt0HevxPbYd7eGG3pnfdNxDL&X-Amz-Signature=bd32aeeb435df0ab8da138d52a339d20ef3dd11efd8728de6d6708102454ce6f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

    1. This error is shown on the console log

```javascript
TypeError: Do not know how to serialize a BigInt
    at JSON.stringify (<anonymous>)
    at setState (index.js:82:48)
    at updateState (index.js:49:9)
    at eval (index.js:38:17)
    at eval (index.js:8268:15)
    at sendEndOfBatchNotifications (index.js:4303:11)
    at endBatch (index.js:4352:5)
    at eval (index.js:4404:7)
    at Object.enqueueExecution (index.js:891:3)
    at eval (index.js:4403:18)
    at commitHookEffectListMount (react-dom.development.js:21102:23)
    at commitHookPassiveMountEffects (react-dom.development.js:23154:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23259:11)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23256:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
    at recursivelyTraversePassiveMountEffects (react-dom.development.js:23237:7)
    at commitPassiveMountOnFiber (react-dom.development.js:23370:9)
```


4. 

I staked two times:

    - 1 TON: [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0x3303edc2ab783456f43326d84aa1824c5037b71fcc6bfe071eb4cd33b3872e9a)
    - 10 TON: [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0xb58e2def73c0e12fb91b01c9801ecbb5bcac83814361609a1240a9040b47eb7b)


But the UI shows `10.99` TON can be re-staked → I can’t update to `11 TON` → So if i click the button `Restake` I will receive 10.99 TON, not 11 TON.

`Unstake` shows `11 TON` → Expected result


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/8b05ccde-fed6-489f-a53b-c7684af366a6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2K2O353%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHLD3cflh80Ua78THakmwWOJccassXfCmf4x5aQ2vbFGAiEA5eSUgFFuWLQBGZY6rkanzTWPtW6GrTGqpYCA3w%2F3h04q%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDLOLFWpK%2BkrxJ4F45ircA1pmvV0WOimJVCdNhDAPDy8BD2k22SLBVtjkfFobXU2DUOXas%2FyOcQiOBhjo7qmuwKguuLA7A%2BREqdYtSZ%2BNniJqXvoJvGk93%2FjKdaFIeQmkxCWJKyz2kXx53MooKsB%2B9R9bEoZA6Y0jSrN85lVSMBy%2F5dKJgzG3u0wDmdr8rsdcoiPvCGEIEdf5KZrAtnvrKMmDdXxv8EglVwySThzeSk1VgHfgsYHnLEdA4sk6hkWWEz6Hx9kA72rWHuWNUoJgS9ev%2BKz9Wv0HXEs6L72ceBBp0q3yORtBduBX%2FfNjk2S5oEHxzVfyk9WUTZzP21zCikIZ5N2PDLULBkyMaEqMxT4hbuJ5aPH0dtOz4GM0SnOf9Dqb2U5Zf5UoNwha0Y%2FSPQO4Mjc2jm972o9ERcToOBDg1v8PZ6pG53WHtdQ5LrqPSCpnswyWbtCOvgv%2BMzMe1qIc%2BbynmNtk9O9cCZr6PbVgZg1kLwaYejt3%2BiRR7hoYzY6xN%2FXrXPVw2XgY52Opf8IauVi2oaiywuihXjZ2MHPgPRbnFAB4Q01wFv6h0tnpiB5y1gR%2FnwYuaCCLU7tEvhTsfLATkdo1DM%2Fyy4UCSaB3zVyhFK2QJXI2pZ1fdMknQl5CuLUlWPZGC6zHMOXE2swGOqUB9h0fQcgiI7%2Btow1Ystb5Q%2F4mCI%2BPRZWpj6posihMBZnXCFQApIGedu07veLRJEpK88runeo6xLrIjQwJuBRk7JXPpIjT%2BO3HyPfVuChialG%2FpgNxrYc%2B%2F730pJ%2BoMByYLd10GGjvKhj543CercjxLMhNOCQXUCNtktnefvObh2KkiXW35KPjjJBV7KZCt91a3TNyKt0HevxPbYd7eGG3pnfdNxDL&X-Amz-Signature=61e61e14f7f1731e11db1d63642a1cf13c7258df88e8cb4a0ab3980ebd5a5f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. When I click `Withdraw L2`, in the first time, I executed the withdrawal transaction successfully: [Sepolia Transaction Hash: 0x37d5d314df... | Etherscan](https://sepolia.etherscan.io/tx/0x37d5d314dfe96ad1cb4c4ad1eeeb8e5af316494de5f6041242f3c75b33bde371)
But the UI still shows 11 TON can withdraw. If I click to Withdraw to L2 again, Metamask will show this transaction can fails

Same with the Unstake page. `11 TON` shows and the button `Unstake` is enabled, but if i do that, the transaction fails.
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | y |  |  |
| Unstaking | y |  |  |
| Restake | y |  |  |
| Withdraw | y |  |  |
| Calculator |  |  |  |
| Update Seigniorage | y |  |  |
| Claim(If you have L2) | y |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Chiko
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation (Ubuntu 24.04)**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 3 | I should refresh every time to get the updated staked amount |
| Unstaking | Y | 3 |  |
| Restake | Y | 3 |  |
| Withdraw | Y | 3 |  |
| Calculator | Y | 5 |  |
| Update Seigniorage | Y | 5 |  |
| Claim(If you have L2) | Y | 3 |  |
  1. Terminal Errors
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/6aac4d41-bf1a-49cb-be83-ed06f90e4d2b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPO3F2YP%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BI73s8tjZOgrn8Dh1VKRDgwA0t0D9lMQbkwJ2mzcgOwIhAOA26jnZdMrn80lA1U9HMqAKHP5VcQxfFFwS9WzmHG%2BRKv8DCHcQABoMNjM3NDIzMTgzODA1IgxuA7%2Fpuk%2FaMSjCc04q3APCeO9y7ZPTcECwyInV3MaGEZcy2tpe45iDq7pxMg6lQfrj0RQMY0fT1jOyHkIIM%2BzhZF%2FFXcspAVEONQVzzcO4J7zZVka4id2ClBR0eRDxE1PwchCtgHzEPfPyM%2BtTKOcAh2KDgkduCZFbauHlxOcsTPOGzy3K5mym1LHzIsCHC%2FPZseFtSEWFNIx%2FRJAfMe55uxgECQpFA8OSJU8bQA6ky%2FbGJpJM4vTr68oNSig808rFv71gUiOmU0%2FxAxErxfuc5y6AaLMl1RoVPQsZ3Iqx4OcZBVd8m4EIsalmRV66QuTtn21abiSChFhK81O9a7nBZJhgxNeL24dGGrjE4ZMAo1xel8EQZolU%2FQzNAQyJM0TCfEt4qdwa6yfx0aZlfOTiFM4UM4hs%2Fv7EVLT6GIEb2GxfirlX8pUZCyWlT5ycYqSmCQ2Ddj4gnZDk7KAq3XokdMpxzIpIKocpA5VxHNK6s2GwE7zkTpNQbdoF6Gne7pufyuSDOf05LlEg5CjlwQrmtOp%2Fao%2Fm58ZEh8yLJk6VtX8Y1Kma1FrsDnU1oJ8IGUNS2zSVrgiJhS2ov23cilYtlpg8DklhMg0oLUEFjwbqaZWgtTmKodMW0yVtTVEFQwALKmO3b3FR%2B%2FfZ6DDDw9rMBjqkAcfGfgkGBkw6EXA8f%2FgQmFbgC9iw9kyu1114O%2BPEXtVdqu8yoIVyuNaOlR8qOOsL7oDndcyfdLLvaPKL1TrmTcv2wJYLXGIYMw6CXTirAe5J0mlJDa0VlCNFDuQTWQFfyANTvobMfJO%2B5IJlzsT7D04B2%2B4oLGVAt4N18XD%2BeAOgOrkOKs35MGAN%2FDIgWakMZYBP0waqgWwBohmA%2BzAdLErdeNtw&X-Amz-Signature=0521e60c5fcd1c3efdd5997abf283b40d0070f9016855fccea48981c5ac4be38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)
  1. Staking test
    1. Staked 600 TON : [Sepolia Transaction Hash: 0x47fc148301... | Etherscan](https://sepolia.etherscan.io/tx/0x47fc1483018a56b0007000e885cdedb44ba43efeb139b30e3386d67f062c7a56)
    1. Unstaked 600 TON: [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0xeab16ab25860cb949f3054598e037b62be1b51c87039a62f7dfa7c9289adde52)
    1. Restaked 600 TON: [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0xbf746cfc851a4abb4290ace21f02417534ba89df6c6d00129099fab41335715d)
    1. Update Seigniorage: [sepolia.etherscan.io](https://sepolia.etherscan.io/tx/0x8cbbe82edaceef560bf2fc89a8e70e029586ec380965e04486769b74ea4edfae)
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Ale
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 5 |  |
| Unstaking | Y | 4 |  |
| Restake | Y | 5 |  |
| Withdraw | Y | 3 | It felt less user-friendly because I couldn't tell when a withdrawal would be available. However, if it's a community edition running in an unpredictable environment, that's understandable.  |
| Calculator | Y | 5 |  |
| Update Seigniorage | Y | 5 |  |
| Claim(If you have L2) | N |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [x] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`I think it'd be more helpful if it has some trouble shooting for cases you can expect normally.`

Suhyeon
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 5 |  |
| Unstaking | Y | 5 |  |
| Restake | Y | 5 |  |
| Withdraw | Y | 3 | I’m not sure I used it honestly. I couldn’t withdraw TON cause it didn’t pass 14 days |
| Calculator | Y | 5 | It’s very easy to use but there’re limited choices for duration |
| Update Seigniorage | Y | 5 |  |
| Claim(If you have L2) | N |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [x] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

<u>The below command didn’t work for me.
git clone tokamak-network/staking-community-version</u>

Kyle
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking |  |  |  |
| Unstaking |  |  |  |
| Restake |  |  |  |
| Withdraw |  |  |  |
| Calculator |  |  |  |
| Update Seigniorage |  |  |  |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Harvey
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 5 |  |
| Unstaking | Y | 5 |  |
| Restake | Y | 5 |  |
| Withdraw | Y | 3 | Withdrawing from the ETH chain is fine.
However, when withdrawing to the L2 chain, I cannot know where the TON went.
I wish there was a way to check the TON. |
| Calculator | Y | 5 |  |
| Update Seigniorage | Y | 5 |  |
| Claim(If you have L2) | N |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Mehdi
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** macbook pro M3 pro 36go arm64

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No 
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 4 | the updated staked amount is not displayed dynamically (we have to refresh). |
| Unstaking | Y | 3 | The unstaked amount (amount that just got unstaked) is not displayed. We should add it somewhere. |
| Restake | Y | 3 | Users shouod be able to restake a part of the amount. Currently, users are enforced to restake the total unstaked amount. |
| Withdraw |  |  |  |
| Calculator | Y | 4 | The recalculate button is misleading. I would suggest to call this button “back” |
| Update Seigniorage | Y | 5 | No comment |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [x] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`We should mention which branch to use`

Theo
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** Macbook Pro, Apple M1 Max, 32GB, arm64

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [ ] Yes
- [x] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [x] Yes → *Please specify: *
- [ ] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 5 | Dev page: Webpage cannot fetch staked amount and account balance immediately (need to refresh the page) |
| Unstaking | Y | 5 |  |
| Restake | Y | 5 |  |
| Withdraw | Y | 5 | Suggestion to change the menu name: Withdraw - L2 -> **Move to L2** or **Withdraw and deposit L2**

The concept of withdrawing assets staked with L1 to L2 is not easily understood. A more direct expression would reduce confusion. |
| Calculator | Y |  |  |
| Update Seigniorage | Y |  |  |
| Claim(If you have L2) | N |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Shailu
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [x] Yes → *Please specify:*
- [ ] Although I didn’t faced any issue to run the ui on my local using npm run dev command but i got error while creating a local production build
 

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/feaa0325-bca3-4f81-81d5-c798d5d13eaf/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZVPNH77%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQX%2FmtfU3d4ECLHOmJpu77DlB8i0WTXsqWskamWYotVwIgEXZ4af2y5t%2Bb5N2CXAoq%2Bn4M9EnJvYSicNFaGfbMpDMq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDPJlDFsNxhTQXE%2B6lCrcA8uXDx0ox4tHj9FJXAEjXJvOPDlxjHMpUyOr%2BNS70j9IOTVIHd1202BHUgKfYi4%2BDv%2FOpyUmcmon9fSYUBOOyBlVSTuerjlzGwbElx0JK1nZsBxjxXFWw%2BYYlsY1LVEaTAl%2Bq6Z0sAZLZBLyAO4Yt8G2QDNBdtG5mpKz0yH7FdR%2F02sWELN4TxHt5DIx24HWRMwHtW8ExDjB6qR8RUAQZWAZhHeEWv6%2B%2FK9p1Q%2FeI3T%2FhLrj5J6u5xbYHw9iM748WCoLrawnCCH5gBbhgZ942WTGAlWhG4OueruNk1andNQdrY3oUgFJnGyu9RnRjKWKyTqQZe5tHJ%2BJgYWnhtZCPwrRdSG69DnUvd162Kfsl1Yr%2Bo4Hr9jneiSDVpYUJU4cuMpy7by8S4MQYjeOINA%2FmEbZQKJ%2BT6Ax%2BknBZAkuaMNPLP%2BD0EJbifHSIbTg6teIUuRGvi6MvJ5c1OnLbRl%2BoxC7i5mJrgLoVUfiUpHmOsJaIjahREZXmJ5YX39v6Xc48k%2BSdgarFhPPSC0vVtjZ9IaRvC%2BqVIUrPcwEY%2FAo8acRJ7aNtFz57iuokvsTSxOpWwwjK52VHQf763gc3i1HFQJc4darfKqNSHiOvuT7VD6dW15ZlBlq%2F88l%2FoyuMJTE2swGOqUB8mNQfmhdHTCtxLiIIgFee9igisgU5Fe%2BcAKQjNAEVg8qV1WwWBvxBxEkFVYztqnsB5RZMfBVu9XLbXgXB5YzbudD34HZsgiR9%2FtDLyDlq331BKvkcT1biNO7hghXKw%2BA7zcOVlDjwCyUa3wzNdtusSM663CXce4o1HPBOroaYo6iO8umRb%2BKtFWwZFQt%2BB3ElDCW0eNt1zXHiNxbSGyXmLuOpsNP&X-Amz-Signature=879991f4d7f3ff61828314de506e1c479cf2589052b463ec020532054916356f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] One suggestion about the ui which i would like to give is that the continuous scroll which is good in styling perspective, I didn’t find that user friendly. I was initially scrolling through that to find my operator thinking it’s at the bottom and then realizing that it’s a continuous scroll 😅.
One more thing which i would like to add is that the ui could also be more screen adaptive so that depending on the screen size everything could be displayed in a single screen without the scoll as on my laptop i’m getting a scroll bar at the right side.


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/dd34bf21-5550-40b9-81ad-6a0d2fb340a7/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZVPNH77%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQX%2FmtfU3d4ECLHOmJpu77DlB8i0WTXsqWskamWYotVwIgEXZ4af2y5t%2Bb5N2CXAoq%2Bn4M9EnJvYSicNFaGfbMpDMq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDPJlDFsNxhTQXE%2B6lCrcA8uXDx0ox4tHj9FJXAEjXJvOPDlxjHMpUyOr%2BNS70j9IOTVIHd1202BHUgKfYi4%2BDv%2FOpyUmcmon9fSYUBOOyBlVSTuerjlzGwbElx0JK1nZsBxjxXFWw%2BYYlsY1LVEaTAl%2Bq6Z0sAZLZBLyAO4Yt8G2QDNBdtG5mpKz0yH7FdR%2F02sWELN4TxHt5DIx24HWRMwHtW8ExDjB6qR8RUAQZWAZhHeEWv6%2B%2FK9p1Q%2FeI3T%2FhLrj5J6u5xbYHw9iM748WCoLrawnCCH5gBbhgZ942WTGAlWhG4OueruNk1andNQdrY3oUgFJnGyu9RnRjKWKyTqQZe5tHJ%2BJgYWnhtZCPwrRdSG69DnUvd162Kfsl1Yr%2Bo4Hr9jneiSDVpYUJU4cuMpy7by8S4MQYjeOINA%2FmEbZQKJ%2BT6Ax%2BknBZAkuaMNPLP%2BD0EJbifHSIbTg6teIUuRGvi6MvJ5c1OnLbRl%2BoxC7i5mJrgLoVUfiUpHmOsJaIjahREZXmJ5YX39v6Xc48k%2BSdgarFhPPSC0vVtjZ9IaRvC%2BqVIUrPcwEY%2FAo8acRJ7aNtFz57iuokvsTSxOpWwwjK52VHQf763gc3i1HFQJc4darfKqNSHiOvuT7VD6dW15ZlBlq%2F88l%2FoyuMJTE2swGOqUB8mNQfmhdHTCtxLiIIgFee9igisgU5Fe%2BcAKQjNAEVg8qV1WwWBvxBxEkFVYztqnsB5RZMfBVu9XLbXgXB5YzbudD34HZsgiR9%2FtDLyDlq331BKvkcT1biNO7hghXKw%2BA7zcOVlDjwCyUa3wzNdtusSM663CXce4o1HPBOroaYo6iO8umRb%2BKtFWwZFQt%2BB3ElDCW0eNt1zXHiNxbSGyXmLuOpsNP&X-Amz-Signature=e5a72a9657583c62be2d55039754e22d6b05891b9d4e3c108b36170cf5c9454f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

I also checked this for other screens like ipads and this pattern exists for those too - 


![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/54fed8f0-e861-46db-9ed9-2b4e07eaf3b9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZVPNH77%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQX%2FmtfU3d4ECLHOmJpu77DlB8i0WTXsqWskamWYotVwIgEXZ4af2y5t%2Bb5N2CXAoq%2Bn4M9EnJvYSicNFaGfbMpDMq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDPJlDFsNxhTQXE%2B6lCrcA8uXDx0ox4tHj9FJXAEjXJvOPDlxjHMpUyOr%2BNS70j9IOTVIHd1202BHUgKfYi4%2BDv%2FOpyUmcmon9fSYUBOOyBlVSTuerjlzGwbElx0JK1nZsBxjxXFWw%2BYYlsY1LVEaTAl%2Bq6Z0sAZLZBLyAO4Yt8G2QDNBdtG5mpKz0yH7FdR%2F02sWELN4TxHt5DIx24HWRMwHtW8ExDjB6qR8RUAQZWAZhHeEWv6%2B%2FK9p1Q%2FeI3T%2FhLrj5J6u5xbYHw9iM748WCoLrawnCCH5gBbhgZ942WTGAlWhG4OueruNk1andNQdrY3oUgFJnGyu9RnRjKWKyTqQZe5tHJ%2BJgYWnhtZCPwrRdSG69DnUvd162Kfsl1Yr%2Bo4Hr9jneiSDVpYUJU4cuMpy7by8S4MQYjeOINA%2FmEbZQKJ%2BT6Ax%2BknBZAkuaMNPLP%2BD0EJbifHSIbTg6teIUuRGvi6MvJ5c1OnLbRl%2BoxC7i5mJrgLoVUfiUpHmOsJaIjahREZXmJ5YX39v6Xc48k%2BSdgarFhPPSC0vVtjZ9IaRvC%2BqVIUrPcwEY%2FAo8acRJ7aNtFz57iuokvsTSxOpWwwjK52VHQf763gc3i1HFQJc4darfKqNSHiOvuT7VD6dW15ZlBlq%2F88l%2FoyuMJTE2swGOqUB8mNQfmhdHTCtxLiIIgFee9igisgU5Fe%2BcAKQjNAEVg8qV1WwWBvxBxEkFVYztqnsB5RZMfBVu9XLbXgXB5YzbudD34HZsgiR9%2FtDLyDlq331BKvkcT1biNO7hghXKw%2BA7zcOVlDjwCyUa3wzNdtusSM663CXce4o1HPBOroaYo6iO8umRb%2BKtFWwZFQt%2BB3ElDCW0eNt1zXHiNxbSGyXmLuOpsNP&X-Amz-Signature=b7214aed39134f26faf23d0361803cd3541aa54a96a3e064080311841c92fa51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Like what i would say is if we are going for continous scroll. Then we should try to figure out ways in which the ui on different screen could be seen in a single page without scroll and the continous scroll which we have on the ui it’s size is adjusted according to the screen. I think this would be more user friendly.

- [ ] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 3 | I tried a few iterations - First i staked 10 TONS, Unstaked the same and then again staked 100 TONS. In these cases the staked amount didn’t got updated on the ui. I had to refresh and reconnect the wallet to see that |
| Unstaking | Y | 3 | The unstaked amount was not reflected on the ui immediately |
| Restake | Y | 3 | I was not able to change the Restaked amount if it’s something which user can’t change then we can change the colour tone of the amount to show that it’s static. The amount after restaking did not changed. And once i had restaked still the restaking amount was visible there, I think once user restakes this should also gets reset along with the button (Like what happens when user unstakes) |
| Withdraw | Y |  |  |
| Calculator | Y | 5 |  |
| Update Seigniorage | Y |  |  |
| Claim(If you have L2) | N |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

James
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [ ] Yes → *Please specify:*
- [x] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Yes | 5 | I tried stake several times, first I tried with 1.3 TON and noticed that 1.29 is staked. Next time, staked 1200 TON and restake as well as unstake the features were working well. Need some improved UX. |
| Unstaking | Yes | 4 | Validation should be done on the Frontend before Smart Contract function is called |
| Restake | Yes | 4 |  |
| Withdraw |  |  |  |
| Calculator | Yes | 5 |  |
| Update Seigniorage | Yes |  |  |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Victor
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** Ubuntu x86_64

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [x] Yes → *Please specify:*
- [ ] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking |  |  |  |
| Unstaking |  |  |  |
| Restake |  |  |  |
| Withdraw |  |  |  |
| Calculator |  |  |  |
| Update Seigniorage |  |  |  |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [ ] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

`_____________________________________________________`

Aryan
> Note: You may refer to your above testing feedback and include relevant links to support your responses in this questionnaire.

**Device Model & OS:** 

  1. **Setup and Installation**
    - **Was the installation process straightforward?**
- [x] Yes
- [ ] Somewhat
- [ ] No
    - **Did you face any issues while setting up community version?**
- [x] Yes → *Please specify:*


Issue 1:

I was successfully able to run `npm run dev`, but even being connected to the Sepolia network, I continued receiving a pop-up to switch to sepolia.

Initially, my MetaMask account was connected to the Ethereum mainnet. When I accessed the website, it requested a switch to the Sepolia network, which I did manually within MetaMask. Even after switching to Sepolia, the pop-up continued to appear.

[File](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/17a5b267-fdea-430c-9620-a965dd70fe23/Screen_Recording_2025-05-30_at_11.01.03_AM.mov?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXRHNOE7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMfdFEI3rY3%2FLNIzQsE7af3%2F1iMVF7TMV7zo46KM1HNwIgJNLeP57l8I6r%2BfZdSXGMHBKeUkpUYFf0FPmHLX081VYq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDDxHX%2FMaodUlkk1X%2ByrcA%2B9FYfqg8R99H9HUWKvH%2BPo6nFMbWNOKydbYtn2QgSiEDZww8ZA%2BEHUcvTtNsakwCUO7VgyW4i4bWVa5OS2CQlHTgZq6pLay0mBwOqT6koeNIBWrXdDZebobuBLkWYgrtxJ4FGMrHV9W6ngvRiZ2dQEufHVLrjNMuMW4VBOEkdUF00EJyAwmoyKUVb2GmdtYdALHJiVgcTPX1TWp4dJmwUidP0zK9QyGiF4vcnWaOVIJ4oQF8Ba3BddtJJ%2F54vMMMMbabSrimc3bUt1w6FIPZre2U%2BHz8QgWU3Plyou2VxqPzXI15nF9cK1GkjAEwcXxv9haV3C2e7%2FEauGa0qP0cplJtBemeipW%2ByG4AC0vFZgONLlTPYbkNfwhITJZktbY5q8etIqymMVFpI1NSq4fgqwOXrNsJdfoWJ%2BXsO2vbbi2Aa2JVLetGYiHJnoNClfOxaL539WBb4t%2FaffPrme7vSynx7hxtS7JJYNnyI0Rf%2FJ9vWpIYDIFj8%2F%2BxiHbWM%2FchJd%2F24kmx2AWUKS1CHBnXfckMvq13WKhlHClkts53mre32rjZ308hDZTI%2B%2Bhd%2FZJq%2FVaU%2BgkQHNXRB3%2FjeulwezWZszZxja35RKzlajHjBvivVHJehy5Ll5plpTYMIjE2swGOqUB6bdj%2F4tCz3dt9e3s7dp3aiAFW8Pqjbniwy%2F659Vxk67eY1P%2BFQs6vRPC7eqporDyqu90mqJ3g0n0qV6ULWRgix%2FNUL4z%2FgQIRxiXlrqfG4xHOsu9msPr7bU71IZvL5bLQW1Nb6%2Fwhu4W3KjjShec4HE01phwe%2Bvi84Xp%2B0u9oEg4Cb4vFU6CPTi0z1HiB4yZLkwz516N8hyTtwKPxWLzJU15maHg&X-Amz-Signature=da57fa6006f6a6f17b8b680e989847e9ec2516bcd4e17e4e07de58989146fa98&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Issue 2:

I ran the command npm run build and it failed.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/d2e2348d-c87f-4f8a-b87a-c493d28c6474/Screenshot_2025-05-30_at_11.31.51_AM.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXRHNOE7%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T055323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDMfdFEI3rY3%2FLNIzQsE7af3%2F1iMVF7TMV7zo46KM1HNwIgJNLeP57l8I6r%2BfZdSXGMHBKeUkpUYFf0FPmHLX081VYq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDDxHX%2FMaodUlkk1X%2ByrcA%2B9FYfqg8R99H9HUWKvH%2BPo6nFMbWNOKydbYtn2QgSiEDZww8ZA%2BEHUcvTtNsakwCUO7VgyW4i4bWVa5OS2CQlHTgZq6pLay0mBwOqT6koeNIBWrXdDZebobuBLkWYgrtxJ4FGMrHV9W6ngvRiZ2dQEufHVLrjNMuMW4VBOEkdUF00EJyAwmoyKUVb2GmdtYdALHJiVgcTPX1TWp4dJmwUidP0zK9QyGiF4vcnWaOVIJ4oQF8Ba3BddtJJ%2F54vMMMMbabSrimc3bUt1w6FIPZre2U%2BHz8QgWU3Plyou2VxqPzXI15nF9cK1GkjAEwcXxv9haV3C2e7%2FEauGa0qP0cplJtBemeipW%2ByG4AC0vFZgONLlTPYbkNfwhITJZktbY5q8etIqymMVFpI1NSq4fgqwOXrNsJdfoWJ%2BXsO2vbbi2Aa2JVLetGYiHJnoNClfOxaL539WBb4t%2FaffPrme7vSynx7hxtS7JJYNnyI0Rf%2FJ9vWpIYDIFj8%2F%2BxiHbWM%2FchJd%2F24kmx2AWUKS1CHBnXfckMvq13WKhlHClkts53mre32rjZ308hDZTI%2B%2Bhd%2FZJq%2FVaU%2BgkQHNXRB3%2FjeulwezWZszZxja35RKzlajHjBvivVHJehy5Ll5plpTYMIjE2swGOqUB6bdj%2F4tCz3dt9e3s7dp3aiAFW8Pqjbniwy%2F659Vxk67eY1P%2BFQs6vRPC7eqporDyqu90mqJ3g0n0qV6ULWRgix%2FNUL4z%2FgQIRxiXlrqfG4xHOsu9msPr7bU71IZvL5bLQW1Nb6%2Fwhu4W3KjjShec4HE01phwe%2Bvi84Xp%2B0u9oEg4Cb4vFU6CPTi0z1HiB4yZLkwz516N8hyTtwKPxWLzJU15maHg&X-Amz-Signature=f87418377f3aeff1d8e860ec07a6984e6affb153685d30831b0433f21726d907&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- [ ] No
  1. **Feature Usage**
Please mark if you used the feature and rate your experience from 1–5 (1 = poor, 5 = excellent). Please feel free to add any new row, if you want to provide additional experience

| Feature | Used? (Y/N) | Ease of Usage Rating (1–5) | Comments |
| --- | --- | --- | --- |
| Staking | Y | 4 | The Ui took some time to reflect the Staked Amount. Even after Unstaking my Staked Amount has not been changed. |
| Unstaking | Y | 3 | no comment |
| Restake | Y | 3 | I could only deposit the unstaked amount, not a part of the unstake amount |
| Withdraw |  |  |  |
| Calculator | Y | 5 | no comment |
| Update Seigniorage | Y | 4 | no comment |
| Claim(If you have L2) |  |  |  |
  1. **Documentation & UX**
  - **Was the **[**Setup Guide**](https://github.com/tokamak-network/staking-community-version?tab=readme-ov-file#staking-community-version-setup-guide)** helpful?**
- [x] Very helpful
- [ ] Somewhat helpful
- [ ] Not helpful

Do you have any suggestions for improving the Setup guide?

# Types of Issues

## Build error

## Hydration error

## Configuration

## Disable the button when unstake

## Reset the input amount when changing the action

## Update staked amount after sending the transaction

## Account change button is not working on wallet modal

## Cannot update information after changing account

## Do not know how to serialize a BigInt error in console

## Build error (copy-to-clipboard)

## Fix Input UI

## Related with SDK update reward part Staking 

## Withdraw warning

## Missing L2 information

## Withdraw L2 position

## Incorrect message about update seigniorage

## Total Staked show 0 during loading instead of loading indicator

## **Candidate clickable area extends too far causing unintended navigation**

## **Network switch functionality triggered without wallet connection**