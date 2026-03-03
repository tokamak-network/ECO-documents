![](images/8e77b04c5c17.png)

![](images/1675b1681f3f.png)

***storage slots:***

1. *ton*
1. *daoVault*
1. *agendaManager*
1. *candidateFactory*
1. *layer2Registry*
1. *seigManager*
1. *candidates*
1. *members*
1. *maxMember*
1. *_candidateInfos*
1. *quorum*
1. *activityRewardPerSecond*
1. *_roles*
1. *_supportedInterfaces*
1. *pauseProxy(1), ****_implementation****(20)*

1. *_oldCandidateInfos*
1. *wton*
1. *layer2Manager*
1. *candidateAddOnFactory*
1. ***proxyImplementation***
1. ***selectorImplementation***
1. *blacklist*
1. *privateLayer2*
1. *cooldown*
1. *cooldownTime*

***—> No storage collision! ***💥

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f66175c5-aa72-44af-b1fb-f8a28e1fcf6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2XFRV5F%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T095712Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQClx9rFe%2BZywKQvAeyM9iNLsG9CXK9y1Nsxy3xQkhIp8gIhALEIQapsuO9mxvocQhUQeDi0tCyWEOZHyo3M2iYpu7XxKv8DCHoQABoMNjM3NDIzMTgzODA1IgwFf9VOMF8px5F4%2B%2Bkq3AM1GsPHnFVSjX0KWGlMrXNiW8YOXgKcDMSJi%2FfWxjOYzPrnIEO52zhuS%2F3nVFoHEK5snPlepxJvCx0DHIIDA7KLsFRaJ%2F4GTUUNgSpvz2APt%2Fa4synR%2Fbp51ZMOjB5uhP2l6KZor0KHfHPatdwxQKszBWNkhI2bsGtQkm%2FhMmxjQ1DembQxl03ur%2FF98lXw39TmEdneLfjqtU5%2FV%2BdYZPiarQeg6DvepAUV4t49vSS72zjKAv0bB1%2FaTv4%2BsX2AFDlV4%2B3h5y7LHUlEeg4njVPZKgHFbmY4tfY27UTtkjHz20hcElgrarK6saP3Ug66jBJ%2FOE%2BjSGxAQkyVrSDRzT8EIduAwIaVZy57lISI3lFKbBA%2B3W7PAFlyuIjgkndbzXS%2BXjegI47iUKCXfTD9MVl0EBDv4QvZhwLEeLyUZSIKVmsppXHT8lULmJ8Vc8bkN3RHdeNHsLWK6U5RkYqat0AD6hJod9Ymz1tMklCJYYNnftV1mdbGbG85nMeLXDBgmg4Kik7BrLLsBrqEEFdLpgGxisUEaR5lniW7%2FaFjrxRT5yISA3Bx61a9KVf3RmqiRVj8OVGkagLj%2Fbx0pHT%2FcvYaH3zAkbw%2Ffuspgw03vg7%2B7lPwLkN2f4KM31OB3TChmdvMBjqkAej4tYLwlRdHrrMO7kdvi%2F8OORADWKGuZSJ20%2F72DWmu6wKVpyu9LRTTVHzAfOxM0q5DCWL1UKsEycp3AkvnIJNcF8qcPSA2B%2BLNTpgioBMYYlYHO4yfkZuv%2F4EoQ7E%2FV7WiuT0hO67mdJtjkBGZl5GHWMewAA7bgbEdAoyfPKW2o%2B41hAHYmM8a8%2BDVpkSm7n7p5gLWQkeGUD1snI2eohI6rmYA&X-Amz-Signature=6df913e912ae9059164b217836b98bb32bb61c89749362d1ffe57a5530350eda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```solidity
*function getSelectorImplementation2(bytes4 _selector) 
    public view returns (address impl) 
{
****    // 1. 셀렉터별 매핑 확인****
    address selectImp = selectorImplementation[_selector];
    
****    // 2. 매핑이 없으면 → 기본 구현체 반환****
    if (selectImp == address(0)) 
        return proxyImplementation[0];

****    // 3. 매핑이 있고 살아있으면 → 해당 구현체 반환****
    else if (aliveImplementation[selectImp]) {
        return selectImp;
    } 
    
****    // 4. 매핑이 있지만 죽었으면 → 기본 구현체 반환****
    else 
        return proxyImplementation[0];
}*
```