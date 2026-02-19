![](images/79e216d0b4da.png)

![](images/10a6aa4e2d56.png)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/f66175c5-aa72-44af-b1fb-f8a28e1fcf6a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULSAULOG%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T052405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZXb7oBD7LP7qzDQIoZbVPZpct1yUI7dlTu6poats5HAiA1CVsQtyIKAUGghgGWbIMWVTv26a%2Bt74ozjdmqYI8AdSr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMb4iFFFtK1nd%2FHQbkKtwDfVZc1lWJu8%2BXlp7YT7Z0uNY6jYrOgma%2BwLr%2FOr0pkHLBC6Rvj014e9pmRQTX5I0ee379kgEua7xblmfG3obJpcMqN22KcTxLMrmOyLS3%2FLsVovmY4sfN%2BgUDKvAW3hxcdVchV2%2BKS1ZafFMQsg%2BRX9U49PUxkcpDw50Lx4blpbL3X2r86zGP2Jv2%2BD8EXP4nBu9%2BEnb3BkBtTquX267BjQknV2i%2FJ4zKvahRckNxvu%2BWYEFLyK00OYG1jqAK%2BsJ04pRQpbK%2BA%2FscX%2FaMOHmRF359dCS1Ed1xRYZLPM%2BUvbN%2BVvY%2B4YCZHr12%2FqxXm1gkmFLJx4uLxuGAo99OuiCejf0iQ13jpr%2FCPHZidtXOKb0USDgUGoYFvgaT0P4Iw8HYPMXPRIhRqsoiH4adg5ZR0EpseplLnWnpJeiPyAYZ1UB2VHEwDhRhGF8AhyWJF69SX%2BMPx%2B1M0Gf5NiSB1kQHXaKx4X4qj5a2QfsWdkllTqXB3cjNg3Oex8diP7Lgjbh4Jj7%2Fd6puAIwEyEYU%2BAM%2FW5KoWKERxYokh6cD2Sx219Crhd8PQ2YVaoRQYyquQYn%2BPv%2Fj%2BqZDeI8IXamsrRhOaW%2FqJDr8awxX%2FYhCb%2FmeK%2B7ycpkgDWo%2F7cIZOJowhfHZzAY6pgHZ6hr2BoT4rGSEISOY4Y7SKSfV8%2FSGSJEWXZwO1PB9Yl5rD%2Ff84ZBz02d741GcX4sdHV%2B2Jq0oPDc800nNPYuuWNglvb6hw8kNm0%2BhGFIwUbfX5ldCF58NCHKbgKTp1T1iBTPxwhkBenO662uBe%2F4My%2FzWQ6WarTE4TJV65%2BCmyba5JQ70l3GYYouf%2Byfx4XxVVTcg64WztkORn78ZtFxENNnhpbod&X-Amz-Signature=c5ff4285fdef3c478ebc85a57810742bd115ec4d23470923acd8b344eb1925d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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