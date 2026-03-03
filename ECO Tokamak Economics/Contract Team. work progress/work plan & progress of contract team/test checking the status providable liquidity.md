![](https://prod-files-secure.s3.us-west-2.amazonaws.com/64903c51-687e-448d-8297-662b977d8aa9/b0293557-0e38-4a38-838a-e41e94197892/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-05-12_%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB_11.07.42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z33GLUN%2F20260219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260219T094810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2BX4VsBYFIcH4avGvPA95Jm687B3uwEXAUJT7qwafRQwIhAPzkGm5JWuS%2FupnU3%2F4CXi5U8LbuqDSTBLVoKYOAKGFYKv8DCHoQABoMNjM3NDIzMTgzODA1IgzFCsZCicImj9QeGN4q3AO%2BUgPrFSFvovno3AC06g4PU8ZNR8q9fX67vKewnNNz7fltkOfBvwjMZDm58U3T2FjcpIpI7h9wTwxCHsHXmkFtzfq7fV2ik%2BsOkDMAbdafxEZPiOpB0OdeNsca8OrMIg08HpKut1sZ%2BFV9pKZdeBwiWqDyXwIAkbY%2FL%2FNMjutystgL2koIV2utB0LYBSlGL5A5Eqrh8EsKmr1ArzJtCamYrYgGz5Fg2kxr%2BNhwvJaUqeCLVCDEQiCWMdhV3WFP%2B8Wf40IamSxsacrUPuNY360UMv4K7sMBs2ik2bb2X2D7xuTKI7gJeCjIsCAyLxrBWmNfy1ia361QgCOv7Y902o2a5vqeAve%2FjDJi4UGTNIHa8OX7r9rJ1%2BzDeBGazaSeV3%2B5HjqN9K5GxuN5c4QIBEIgkz9FWH8%2F0Sji17VnQ9VZcN0IXkKTDJJyhlCvDYSdZFQTJiPTPNw9jwqjF7O9dnEV0nYrBP4vIMXOr2jBwZeIIYrNUY0Drgq8aXSaRlON5rRUtxzFeWDdT0kEbnpYe6nZOGUuSx8QvAjpUMLQaHSCbsbNi9Q0yYtfa1kepHIAR7ryVUNUnJmKcf9MtBvQpAYXKERO0npkX4dYMhODS4JexwyeW%2FHMxFTuBm9qMTCjmdvMBjqkAShlMT0RfBrzCz5JZvR6pqu5Cob5vCcY5LSOpLATHf%2BzRPcoI9LxWWhJJT2US%2BRHJGrRg75sQN0TsXNtcET9DIIqbVctc1l6%2BIbzCZjef77RC8vBsoeqCqTWYmGL9uGJrs7H%2F1599WZ3WCQM%2Fipp2BoKPhyz1c8HF5xDSvxL1yzVSYW%2F1jkRwi%2B%2BH%2BVVo048C4h4UKaRLuEDlPM29TNW%2BVuMme2s&X-Amz-Signature=07d001ec545bba94f80f761fb88f0d9d300c3cb326a5b71eed18307976cad4f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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