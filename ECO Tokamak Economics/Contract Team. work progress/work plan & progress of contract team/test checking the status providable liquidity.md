![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b0293557-0e38-4a38-838a-e41e94197892/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-12_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.07.42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVI2HXU%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T051456Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGHcaKFGDjIwwWUG0juFF5W08nyUraHHMT3dNFAroGMQIhAKtfvxuOrRnNrAmxuDlujSYRbCH63RFfmsGjHH8HAGR%2FKv8DCHQQABoMNjM3NDIzMTgzODA1Igz5cHbOD5Ud88e4jtkq3ANqZZzNGSh0Q%2BYfUdyXKO4fPW0xhkW3YKVZGviO9fEopk3wRl5zT3XkdcJGDAqc27sFnPqI0bfdZwGs4Si06RK2ugMZMWGMrcSaXhScS%2BaVAbyHa7qiXLqfEjbNFM86%2B1zp%2FSv5eyo3e8oJaqE5my5gh2VRF39MAFCUvvFizIy%2Bxx19%2BPeMQ1aE3hLMgDPwlhapEpGOB%2ByTgS36z8IRBcy9eXp3%2BqmbIQWRr2%2FRiKAiHziog0uSkJvXAbKpcyGe8wBQgRa8vTYrepmhqVk36ryDlWQdFfuXvDtv%2FXt0t57Q0UaGshPsvdTIRZpZoHhdRptRBsGk3Wo8lVqhTdkKQrz%2B9QxkQVQGlAP5%2BmPXLrqr1Mj36S7ZaGT20ksJWxkVj7P8%2BCsYPn%2BGa6%2Froj4X%2FIOxeoVIwnxXmKsbHDlmuZt%2BiIBZ5mmR9jdfMsaR%2BDJvQgSjo%2F6DLGxpgs4FwS2zTGPGpux8dKUDGeMTMp%2BZk%2BoDKEVhg4nLhesdNsP9aGv%2BYVJjK3C8Rdkg9FGczNJvexTP3fJPMJM3r%2F0I9ZrA%2BYEAtf61kgnYkT124DqA63H4QhoaGJD0NS38TrjaMJhO1Ph4PRkBM6bg0R1RPLFLL6sbUL%2BfIapEPe4VMzWtozCG8dnMBjqkAVI45BOtjvMRDd%2FWS4W2y5E%2BeHJvOxEomYOUbSaNY6jwTzdzBwf9TKs9jTSk8NmMfmQKFOnjGlWyKR1LPqRpxxD7UTc%2Bp1McVE4LDqHsT5uXzT3P0lfEq%2FfFdGM6Qed%2FgD%2BjtkjWGqD2PbRsKH71UG4InMlFb0EHdzoBkmSjkZYc2dH%2Fy1ADOH%2Bd0c7JiVBYnM503HMghBVbrBPli8fuNI8HVERf&X-Amz-Signature=d5ac291fb7858c3941a8b6b7df64cb42163c2529d6be10a199258950d132ced3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://app.diagrams.net/#G1TpDw8CHpaubD5xXUXXNFK12v5v7jIXNq](https://app.diagrams.net/#G1TpDw8CHpaubD5xXUXXNFK12v5v7jIXNq)

- L2TransactionHash  를 알고 있을때, L1에서 해당 트랜잭션의 상태를 알고자 한다. 
- 메세지 상태 Message Status READY_TO_PROVE : 3 또는 IN_CHALLENGE_PERIOD: 4 일때, 유동성을 제공할 수 있는 상태로 본다. 
```json
export enum MessageStatus {
  /**
   * Message is an L1 to L2 message and has not been processed by the L2.
   */
  UNCONFIRMED_L1_TO_L2_MESSAGE, // 0

  /**
   * Message is an L1 to L2 message and the transaction to execute the message failed.
   * When this status is returned, you will need to resend the L1 to L2 message, probably with a
   * higher gas limit.
   */
  FAILED_L1_TO_L2_MESSAGE,     // 1

  /**
   * Message is an L2 to L1 message and no state root has been published yet.
	 * L2에서 withdrawTo를 한후, 해당 트랜잭션으로 바로 조회한 상태이다. 아직 L1에 제출되지 않음
   */
  STATE_ROOT_NOT_PUBLISHED,    // 2 

  /**
   * Message is ready to be proved on L1 to initiate the challenge period.
   * L2에서 L1으로 트랜잭션이 제출된 상태로서, 챌린지 기간에 들어갈 수 있는 준비가 된 상태.
   * 아직 검증되지는 않았음. 
   */
  READY_TO_PROVE,     // 3 

  /**
   * Message is a proved L2 to L1 message and is undergoing the challenge period.
   * 메세지가 검증되었으며, 챌린지 기간을 거치고 있는 상태임. 
   */
  IN_CHALLENGE_PERIOD,  // 4 

  /**
   * Message is ready to be relayed.
   * 릴레이될 준비가 된 상태임, DTD기간이 지났으므로, 릴레이될 수 있다. 
   */
  READY_FOR_RELAY,   // 5

  /**
   * Message has been relayed.
   */
  RELAYED,       // 6 
}
```

**example**  

```json
const eventSendMessage = await crossChainMessenger.toCrossChainMessage(response.hash)
console.log(`eventSendMessage : `, eventSendMessage)
const currentStatus = await crossChainMessenger.getMessageStatus(eventSendMessage)
console.log(`**currentStatus** : `, currentStatus)
```