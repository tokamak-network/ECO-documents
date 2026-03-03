## Draft

[Hollow_Victory_draft.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/758fd845-0acb-4a27-bafd-319c4e6b36fc/Hollow_Victory_draft.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGF4GMLI%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T091636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCOxrvJ79eXyeKPr4ZTq4aewZoBtMrpxbjaGr8HSqEyxgIhAINksgKfdYJctLxhWk0K9YR62kOP46dbA3LwFro4%2Fi5zKv8DCHoQABoMNjM3NDIzMTgzODA1Igy6Ps%2FutOCvJOA3qg0q3ANEMl2a%2FrsVEPUAKtONptR1CWDRWpM3tlGP50VpeA1prs73neDGbjWiah21mXRGUZcmnR7lRde6UdKVPSY4YWsMUZYFKjQjCfHRCF%2F%2BQIx9GhjwiWOfMHfngdJ%2Bn1w9FCFKIOtDs0Xk3IFtEbCOpFYmfrkIPuNfl0oRoY411eo2t80TKYr50BeUG%2FhFcfD9u%2BwJoz0d3hATVe4tuwbSd4STPJm7EovkkYneStuZDRoL%2FmLtiUcaJ1iNzECbN0O0JCsfE7zGH8QVARpqHdsm5V4UY0%2FNa9TfL4wWFCaSVxDav2XpCXmkAevcQdfBlDvL28JBdwMX168nP0L2yh0q4avGseS1sbVAPRj%2FdX7cYydrq1CvP2EcNJprdlxz6mE1BrbQVuhFMJ4dC3PqAdYAQKGfLxuz5miW2sg%2FpFlIuEn%2BOTIZS4jTFJ9L2eAKw7C09tEfp0NrEVw0qmt%2F4nKz0BRf7Hfl1HlQoIio%2FoB62Xhbki6gXGYE5%2BO8ZEjirMrf8RjzfbaubCSQNEJRw3%2F0fmbbr5PflnwXm0mJyNL2Yj0zuIXqJ%2FCD3sbZOj0XNXUX%2FhQq3uBjCBVopFspr1Oompz%2F68DFyyOKGHmiVCZV%2FItC1F%2FaKycGHpi5RDpeoDDsmNvMBjqkAb1EDlEIDcz13sEmiegoyEluycE8ACbMb7X56%2FJo8cX1yx7IgLZjlsrHPtKYCtS5ZO7WTmSBVFmeEDe86dqFivXanYCES14Wr3%2FiRCHGW0Bh3KoU7LJ1sDhmzvSDWemN%2BTNSrVIVaZZNlbn7fzaMbhM8NXWMc8vAVMVmT5NfNL958Bf5Bk4Pu74%2B53powenQfU7cNzkE9wS%2BdnSALnDVOVFIthRn&X-Amz-Signature=6b40fdb5d5f907e41664299db2b2ea674327c1ea51ba3c97c958dff6c0b71904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1. Let’s assume there’re multiple validators
1. Validators can create a dispute game as a smart contract
1. In the dispute game contract, they try to find a state change that is disagreed and make a decision by executing the state change
1. An attacker or a defender should response in a time limit. If not, the participant loses the game.
1. A winner takes the opponent’s deposit. For a validator, the prize money is the proposer’s deposit
1. If there’re mutliple disputes for one state change by a malicious proposer, the first dispute game winner takes the proposer’s deposit. That is, first-come-first-served.
1. But this doesn’t mean that the proposer should response first to the first dispute game
1. The proposer can deal with mutliple dispute games without a specific order in each game’s response time limit
1. This structure causes a serious problem: The malicious proposer doesn’t need to lose the deposit (nearly) at all
1. If there are mutliple validators, the proposer can negotiate to the validators. If there can be only one winner among the validators, the proposer can suggest to get bribe by the condition that he can finish one validators dispute faster than the others
1. If you’re a validator and your dispute doesn’t finish first, then you don’t get any reward. Therefore, the malicious proposer is very advantegeous in this negotiation.
1. Game thoeretically, the equilibrium is that the proposer doesn’t pay at all. In other words, a validator should pay the proposer all the deposit to make one’s dispute finished first
1. Even if many validators are not rational, if this is a decentralized validator environment, the proposer can own a validator account and he can dispute himself not to lose deposit (The deposit moves to the attacker’s validator account from the proposer’s account)


### References

[Link](https://github.com/code-423n4/2024-07-optimism/blob/main/packages/contracts-bedrock/src/dispute/FaultDisputeGame.sol)

[https://docs.arbitrum.io/how-arbitrum-works/bold/bold-economics-of-disputes](https://docs.arbitrum.io/how-arbitrum-works/bold/bold-economics-of-disputes)