branch :  [https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_6_pause_simpleStakeV1](https://github.com/tokamak-network/tokamak-staking-v2/tree/TSV2_6_pause_simpleStakeV1)

test script :

[https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_6_pause_simpleStakeV1/test/tryToTest/0.simpleStake.js](https://github.com/tokamak-network/tokamak-staking-v2/blob/TSV2_6_pause_simpleStakeV1/test/tryToTest/0.simpleStake.js)

test : 

npx hardhat test test/tryToTest/0.simpleStake.js

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/24c25839-a395-4c80-b80d-8f240430cfdc/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-03_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_12.21.24.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5ATF47O%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCw%2Bs57Wxmj5H5UKMjw0qaLt970E1rP03C6n2y4tWNHLwIgI8WTxHskEtJnAjCcbTvJOcmNz4QjWlIzakOKmnJfhC0q%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDERWpAe60zVJrGXOZCrcA%2BqRUn1K%2BsykWRPLbUEfD9G%2B%2BFXjATqXCmDgnL6%2Fb%2BnMLpUSAkamZsjNh%2FiTSNepCuuzW%2BeOPLJyVPyNqCX6rYadqJTBH2%2FjDRSxGsbQjGW9V6Nuo%2BRf6CAoJtuONQ%2FAYBLwWDaxf32MACaXkZN7lV23Te%2Bg1Jf7rMOkbthimbeRLAgvyGQA7gryqFTslE4gyD0a3H79pTPXY7ToPah1dlQZXLqT5%2Bn%2BMf7t%2BR7dhmwq8NUV9SBpHm5B9r2ozzDYJthwg9kSZlkLAi17c48zb5bVY5Q4FYl%2ByzDSLaKxYbNw8GUfXR3cjaM41C79ysZZvsRZmVSfoRzY0ioidzrHDuElSd38Cak0tFW7CiSWSo6TNqbjZkgKDjkUDVp9HqvTDYclztUcX266Fy3o7i%2BP%2BQ63TaL3Jk46xtbOgWZqgzfaSICFOyAaOZsx0uOWpfMbQxqTMkXhrCCaZD4Sc%2BzuPZgAzL9%2FTNuu1fCGtQa2MP3260kzHc1olqhIkACGJDZLROHaSFvxQLpQ88vnQyigwEUw0ARIsA3zOSanwnQ2gxgJLpz2sbryEUmGLMZXUcDOsIfU3ya1L9s3JhElsmYSOWWAmWEp9Vj%2FPEGj7gA%2FuUQbT7ElpN%2BzoosWFVW3MMLv2cwGOqUBZ9sxjfAeieSc4d6%2BhTffhL1fzYQa%2FrMfdotVnaXEHwq9UxXGirv6Qrnhh5W5AVJCwR4s5zCJKu4s9U0AjquqhPpL5sjlEJkSNMrmwHq%2FuPEmDQ1SqegHKQ0PeLqa4woDcdvUFq6VqTc%2FqWVAfgYTZf3iqnCzk0t94Kt745yLREfqW8twuUt0lJ9Fv2pA%2BTx%2FhESfYt%2FSp1V23FkkySgRkgQTNxyd&X-Amz-Signature=d25654ff70765c36fdaf9800a423c55dce74dd4bb8c69bfcbbaea3213ec68c1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- The pause function can only be executed by admin.
- **When paused, seigniorage is not added even if seignorage is executed.**
- After a pause, the stake , withdraw request , and withdraw process functions are normally executed.
- If you execute unpause, you can receive Seignorage again.

***If you do not want to issue seigniorage to simple stake v1, you can execute an agenda that executes ******`pause`****** by DAO.***