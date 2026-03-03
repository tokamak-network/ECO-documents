branch :  [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_6_pause_simpleStakeV1](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_6_pause_simpleStakeV1)

test script :

[https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_6_pause_simpleStakeV1/test/tryToTest/0.simpleStake.js](https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_6_pause_simpleStakeV1/test/tryToTest/0.simpleStake.js)

test : 

npx hardhat test test/tryToTest/0.simpleStake.js

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/24c25839-a395-4c80-b80d-8f240430cfdc/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.21.24.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQTBZLOC%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCFXQ8hg9MlxwaFhqc1LBnhmTbxiqzLphlNM2sFHaN0GAIhANgKIlMJKupY6Z%2FEKNbZiNUJLtCDO2uQ3JgzlQ42rAYvKv8DCHoQABoMNjM3NDIzMTgzODA1IgxYuBOJ6hnOvSBpyDYq3AO1uSufnFevYf%2FMIWs6duBcYHSwj5LvjqmmDWPjLw9CVmb1SBX%2FrThod3Ao0xI3s8gQ6LkNGGj6yptDKpHusLS6Mexn31MLVf%2BlfUqubP2d7xnH7%2FpDZct88Knt8c2XB2ataSkD1pQ7Dd9NSByMFsBueKtn1u11BtDA00pp7pOpa3Vt9xgOocVrKJB9vNPKJuuRoveXfF2oEwDQYlNgi%2B3PUNrTe74gSpO2ETHXvmA1446j6pCoajK2UEVbwHW73l%2F8j9dE5T7tk%2FgGrgitMngeD%2FGPt8YqN30GJaKqmKlAIP3mQ%2BaFSEyUC7Jv8v4IxK%2FDuDVgxzZYtfCjZpi31GXZglBkoaY3rp6WSCs0veI0ne54DzMBb%2BFJEiloIKUtyIMPTrUFLTOYlRzXIifv9hTVM%2Bt6ufgwlX6jXrYntovbAGyUPkNKvU%2FMjQK4k%2FOfncoik%2FKRPmzBOTopTrK81whtKIajcwkwrHqDNBEreDSyPmYjHC%2B4%2BJzVM7397WxzfGt%2BEA9oX1NWcaiRm5K%2By7%2BPn7%2BTeCmrXx%2B3AanvbATLldYcVw7cvb6s39tQ1GLXfuLn1KkuWvVBggrp2H46WgkH4AYL9MfbCFaaRr11%2Bzdpb6OqXRQfFYx73imvhTCLmtvMBjqkAWjOTGY7IgBVY8tjf9%2BWbuxFaLoL2SrCp8FhNO1psxtPan2mnKimX7QGNiKTNvdBf8ZGA0EkRD97KJojc7n29PjiB5ZcRLsQzaBUV%2FJ21bbLy97tJcJPLjp2NIWvwgbRoooCYIdBKea6NA9xvfM6SMb9Cf%2FWFGtv1I0r5wkRxNSg5Bqdq4V2RLyXv6kz%2B%2F2tmdvOfttsgagCrd%2Fcl89v6Yz7AMqO&X-Amz-Signature=b15e9049fa7da3db45f488efba09cb0b5679f37161dcda1bbfd761446516fbb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- The pause function can only be executed by admin.
- **When paused, seigniorage is not added even if seignorage is executed.**
- After a pause, the stake , withdraw request , and withdraw process functions are normally executed.
- If you execute unpause, you can receive Seignorage again.

***If you do not want to issue seigniorage to simple stake v1, you can execute an agenda that executes ******`pause`****** by DAO.***