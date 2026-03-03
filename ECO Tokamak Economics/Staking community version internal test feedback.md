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

![](images/b3f06e8fd1d6.png)

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


![](images/37e988ede94c.png)
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
![](images/b8a0f543b796.png)
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
 

![](images/997232f11b1c.png)

- [ ] One suggestion about the ui which i would like to give is that the continuous scroll which is good in styling perspective, I didn’t find that user friendly. I was initially scrolling through that to find my operator thinking it’s at the bottom and then realizing that it’s a continuous scroll 😅.
One more thing which i would like to add is that the ui could also be more screen adaptive so that depending on the screen size everything could be displayed in a single screen without the scoll as on my laptop i’m getting a scroll bar at the right side.


![](images/1a7e897d85f6.png)

I also checked this for other screens like ipads and this pattern exists for those too - 


![](images/b031dfc07be7.png)

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

[File](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/17a5b267-fdea-430c-9620-a965dd70fe23/Screen_Recording_2025-05-30_at_11.01.03_AM.mov?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XILYGN4U%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T102801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGsHpBBaDO%2BAe%2BaK0Sm0WfI8WRoIW4xUpg8a5aqjh846AiBeZknxZn6Yr4BC1O4seys8vPOgXK888qsj1%2B2RNlU2ryr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMoImBK1eoTVjli6OYKtwD67LmOLQsJtNDofzXA2vRLX56UwpSrOgD9p6Bpo%2FmuEtBCBn7c9atErm9HTh53ICNdhmu9wGVn7myUweA%2BT%2FeXHcUrnCLkVP961mvC4%2BvES1KEMbctEdksWngoFA1NUOtI7rlpV10XvSmrsILZGo1aTjgm%2BuKOH7A9UA0YlsDD7Nob88No5BhVcAFbt%2FfObZINd5lPAlp%2FnJUvkV0fveiUD9aJMQf2W3%2BD8ASoJg1LBtSsxQN2yxO3L0z2Gc3k064Zl9RLbCQ4CwAbqevzhILUqA7qZeyXtNZ9pULX%2B%2BTAO8XB2WLMel7eeRCyfSZluDVk5xgwmi55%2BWTklU6H%2FDpogX17ZakHD8cBkP%2BNFabDwF1mtf%2B8vu9i1BmZc1X4UEe%2FjXVEujUtgWh9Ed%2FVLoYkzqHBaP7n%2FQWtMb5PCaJ6ABIkRWcE0wqE5S%2BGII0xo9Ps2cdbhVbo1NEYEiU40p1V9Tg%2BV%2BJksZtzlzEbsJxQzc%2B5oBFmmcEDIsq6jmkeVg8uV8xxI1%2BE6AahF6uPBMa%2Bo2nNPaqDv5KK8UI632vffvQSYsg%2FLL%2BUvxWe2Lxx9vy3BUn8DkNygMxzi6OYQMERjM0HW2svePFHjhDZB0T3tfs0p6jhIo54YCbY70w2ZnbzAY6pgHl%2FIJf%2FJMxW6IWyP8dbhm8xiVvW2sMYzKQk2nh2K5G7laEy6iHNki0JO1FXPS2reykQFbVh%2B4A4yNOOMMJg2OMGGscisei3lOkuHf87SSluYtd3jTHUJobtmnLJ5rGuNJjrDDbfBy92Esvy3aZTuY99A4f6EQ2RNrQtmatsPZRe7alUzTAFLYbMOXLE3gDc1KfC48A8dZ0dFOZjXHqM5KQc1LBN9OL&X-Amz-Signature=4e40e710ad02103a1f5c18c0e7d526b9f1c513d99aaed2e012a06c454b0d6868&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

Issue 2:

I ran the command npm run build and it failed.

![](images/90d925bb2797.png)

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

Related Issue

## Hydration error

### Related Issue

- #30, #25, #23

### How to fix it

- Try to find hydrate point and fix it

## Configuration

### Related Issue

- #29, 

## Disable the button when unstake

### Related Issue

- #27, #16, # 9

### Happend

- unstake button is active when don’t have staked amount
- If I input larger than staked amount, unstake button should be disabled on UI but it's able to unstake(but fails on contract)

### How to fix

- update condition for unstake button
- If input unstake amount more than staked amount, it will be turn in to staked amount

## Reset the input amount when changing the action

### Related Issue

- #28, 

### How to fix it

- reset input value after change action

## Update staked amount after sending the transaction

### Related Issue

- #26, #10

### Happend

- After a successful stake transaction, the UI updates are inconsistent. While "Unclaimed Staking Reward" automatically updates without page refresh, "Your Staked Amount" remains at 0 and requires manual page refresh to display the correct staked amount.

### How to fix it

- update staked amount after send transaction

## Account change button is not working on wallet modal

### Related Issue

- #24,  #3

### Happend

1. Connect MetaMask wallet to the Tokamak staking service
1. Open the Account modal
1. Observe "Connected with MetaMask" text with a "Change" button
1. Click the "Change" button
1. Notice that nothing happens

### How to fix it

- Fix wallet view when clicking the change button in the wallet modal
- But, currently, there is only metamask support, so blocked the change button.

## Cannot update information after changing account

### Related Issue

- #23, 

### Happend

- When I change my account in the middle, the data from my previous account is displayed, and even though it is an account that has not staked, it is displayed on the screen as an unstakeable amount.

### How to solve it

- Add event listener for change account

## Do not know how to serialize a BigInt error in console

### Related Issue

- #21, 

## Build error (copy-to-clipboard)

### Related Issue

- #20, 

## Fix Input UI

### Related Issue

- #19, 

### Happend

- The button is overlapping the input area when I put 0.000

### How to fix it

- adjust parameters

## Related with SDK update reward part Staking 

### Related Issue

- #18, #8

### Happend

- After successfully executing an updateSeigniorage transaction, the UI does not reflect the new block number. While the console shows "Refresh result: Success" (from useTx.ts:170), the displayed text "Seigniorage is updated 8410146." remains unchanged and does not update to the new block number.
- The spinner has never been done and takes a lot of rpc calls.

### How to solve it

- replace SDK related value to hook

## Withdraw warning

### Related Issue

- #14, 

### Happend

- The Withdraw tab lacks information about withdrawal requirements and pending unstaked amounts. The contract provides multiple functions to track withdrawal requests, but none of this data is displayed in the UI. Users cannot see their pending withdrawals or when they become available.
- Missing withdrawal warning(unstake)

### How to fix it

- add warning message

## Missing L2 information

### Related Issue

- #12, 

### Happend

- Need tooltips for `Sequencer seigniorage` section

### How to fix it

- Add tooltip

## Withdraw L2 position

### Related Issue

- #11, 

### Happend

- The current tab order and dropdown structure creates confusion about the withdrawal process. "Withdraw L2" is positioned after "Unstake" in the UI flow, implying that unstaking is required before L2 withdrawal. However, Withdraw L2 can be executed directly without unstaking, while only Withdraw Ethereum requires the unstake + 14-day waiting period.
- 

### How to fix it

- Add tooltip to unstake button

## Incorrect message about update seigniorage

### Related Issue

- #7, 

### Happend

- The text "Seigniorage is updated 8410146" has incorrect English grammar. The sentence is missing a preposition and proper structure to indicate that seigniorage was updated at block number 8410146..

### How to fix it

- update text

## Total Staked show 0 during loading instead of loading indicator

### Related Issue

- #6, 

### Happend

- When the page is loading, the "Total staked" field displays "0.0 TON" instead of showing a loading indicator. This creates confusion as it appears there are no staked tokens when the data is actually still being fetched.

### How to fix it

- add loading indicator

## **Candidate clickable area extends too far causing unintended navigation**

### Related Issue

- #4, 

### Happend

- The clickable area for each candidate in the list extends far beyond the visible content, covering what appears to be empty space. This causes unintended navigation when users click on seemingly empty areas for scrolling or other interactions

### How to fix it

- add fit-content attribute to width

## **Network switch functionality triggered without wallet connection**

### Related Issue

- # 2, #15 

### Happend

- The "Switch to Sepolia" button is displayed and functional even when no wallet is connected. Clicking the button shows a "Switched network" notification despite no wallet being connected to switch networks on.
- It says I need to switch Sepolia even tho my wallet is already there.
- Text doesn't seem to be good to recognize.

### How to fix it

- I used `useChainId` hooks in wagmi before. But it cannot catch changed network id. So, I changed it to using `ethereum.on` method.