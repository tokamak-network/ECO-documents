**index**

### Storage Layout

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/28fa6a65-bf01-4a15-ab77-4084fb5f7983/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNQXNFBK%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T093941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaHKNuUvruVxCVf8t4CnX3yVavf9akxD%2BCfj6nV0prrQIgRJKuXCB7lXM8YchFLdvaKgiFXRXW22Nt3YVbwtrwQ1oq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDDjnIoABRXrfFFucuircA2VQPaDHQJnm8Ttbj68JX7OmWKF43%2BgCqu67Md5tSv5yrRuV5jLVM8k2GhFkl%2Fn37A36NpIl96zJ3P4v8HQQpIwS93wn9E4PeMZf%2B6oPVJa2lwMJ6sBI5sJEDpgxkT46RaLEQu2yl5Ybe%2BcKQYZtltQ9fhY7%2Fu%2B8KUWTxldNwsP9ArTywUYcQbF9JaSjgxnTU7azDkchx64VmYWNCgXF6X1j8e%2BJMri1wpYV6YdVhJrIXn3QGcdleLfTrusGRnAp1wJsec0hBShXLZcghTpxi5PXm5I6B%2BHeDmCw%2FxI%2B5Squeyz2u8VJSeqLag2NmbQ%2Bhee3jGrGl4AvwoQBizHwxS%2BCY93QWJiEvYoyZVHIl5PN5LCJ7Uy4X35XYcH66xQBjvwS6d0vg%2BvVVCXoyZNPFfFRFv7J%2B84LiYBnF00ytSLsIjILGqKI%2B%2B9A3QATi9%2BbsKbqw1CywSeP2whmDr5viHwctCpdd0bNMjd7QZeOvu30dovDdQr%2B7c4e0WyJdDArqeeRr69kVzIlfJC3lFM74SLcHV22FNjHKlm45AHjZx8Yxz2nXPv4FltvXBlp8hoFT%2Bw%2FubqXSVm1fdSxg2qcxLAGE0RKlbQrI70jSEbMgAM8A6ezJ89m5UTayn%2FlMOeY28wGOqUBdPf%2FqykZEdDHEM6qVobSwv75LsQXueFfD2AkSu4XiT%2BDaBltMPkXfx0at2ZlZWSa9kTUuGDR%2FYhHQd8Dlk6vvAfqZH%2FkxpXncSx08oNRSeWU2yiPVbk0LF1HmBV7m6k6CzlKEAQq2g6IyCYF%2FH9qDFLk5%2FE%2FgN578MMGDnBKXpVFfdVvMwPPAOBpEByqYVX%2B0VcZJCXRIQlZeNc1wKR%2F4vvqwURR&X-Amz-Signature=28a62da6a72a1d637a88e20f6e85988301464f5812184c14295dce0b1cb08aaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> ***DAOCommitteeProxy2, DAOCommitteeOwner, 그리고 DAOCommittee_V1 컨트랙트의 storage layout은 모두 동일하다.***

1. *`ton`*
1. *`daoVault`*
1. *`agendaManager`*
1. *`candidateFactory`**: *
1. *`layer2Registry`*
1. *`seigManager`*
1. *candidates*
1. *members*
1. *maxMember*
1. *_candidateInfos*
1. *quorum*
1. *activityRewardPerSecond*
1. *_roles*
1. *_supportedInterfaces*
1. *`_implementation`*
1. *_oldCandidateInfos*
1. *`wton`*
1. *`layer2Manager`*
1. *`candidateAddOnFactory`*
1. *`proxyImplementation`*
1. *`aliveImplementation`*
1. *`selectorImplementation`*
1. *blacklist*
1. *privateLayer2*
1. *cooldown*
1. *cooldownTime*

> *주소는 **`address`**로 표시한다.*

### Functions

1. `removeFromBlacklist`:
1. `createCandidate`: 

[[DAOCommittee Upgrade History]]

[[DAOCommitteeProxy & DAOCommitteeProxy2]]