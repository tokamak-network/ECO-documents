## Draft

[Hollow_Victory_draft.pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/758fd845-0acb-4a27-bafd-319c4e6b36fc/Hollow_Victory_draft.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SDUG2PA%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T044205Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfieQwy12sOolT2huNXRAZBCobg6Fl%2BHEPdNDuFZta7wIhAPEckmSrCNkg4K33Ca3VdU9snAwqObt5F6M93Z7c2N%2FNKv8DCHQQABoMNjM3NDIzMTgzODA1Igzen7Bu6lvlT8S%2BpXIq3AMuX6E8ndBKJFnsoJ6i6x4HA9fGqXAXFU59i9VmjHWhWeXDPJXUzkE5hQsUWXuILVGumeOb7vJCNsh63v1OSLeVcQcgBqVM7%2BYYMhsiFw3neS2E0QONObnaT0h16jsfBbWXHT67B3pnEtXZJVGQcj678jlqtRJrZgrO5G3Jy6BXruIgHDvfeQ01slcu7A77wvipYf40pg1M66aniFDOTQZ8Uev%2Br4MNW%2BmWWdcPabB4DsFgb%2BGgzqcrjoXTopAMp4%2FQTP4Juel5HW4NmRAIVRdFaOlFKFet8nZB1YsK%2BJ%2BJDNScT3I55MkxY65auw96oaAOQaaRXM4%2BhiquyymByslGDeu%2FbJ%2FZyuaZxLNPhOtY3QRyJhnGnY%2FRmfuAUQsXaQToBEkzCu7nt%2FyC3v%2FKzZ7Zsts%2FbkmtkA9QJu4kApPdqQTPK1OWqGztwi9q5ipWa%2FCiWqX5FKxCMKAKFjpZgC05%2BodhMHvJIdX5iaoHOhZQfTJfON%2BldAuPbIXZpcb1OR47Or2phch1WA6j1pKgDVTLyXhsarFLdaqRaZ4EJtYErb5laFH%2Bg9pgcigpLFgztLl626M1X6eNen0B4ETmKGyE3lyxZ39IA03jtDkCyrrPN9fnN5sLi8ZKYj%2Fv%2FDD48NnMBjqkASQBzLswwITTXs%2BhzhrWAfXRUM74C3qzxd5uhG0Vbc2laArxpq8ltDvgcvqjhnJplhh8ENISxKPuMLPcBPr1z3htPHap70gTUKi2dSGnf%2FKmgDPf6AQ4lKYPxwuhC8JtDULqW0CL2vniDracPN5yjMWUJmCsBdJtTBqHb1%2BQX%2Fh0f2QohYtdKPfUvMI6ZdrB53Rjl0vK7%2FGXICRtWt%2Bd%2Bk783pun&X-Amz-Signature=b9d2d58fed2db0df82a9ca1de92e297e2794d7a854dc1fd656901c98d6526e88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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