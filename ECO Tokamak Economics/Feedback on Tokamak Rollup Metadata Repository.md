- Seminar ppt : [link](https://docs.google.com/presentation/d/1gCKN7XGDL_aYNKlHseZD4PUoocNxwbjlR0y1sH3CuIY/edit?slide=id.p1#slide=id.p1) , [voice](https://drive.google.com/drive/folders/1dOkWy_XA1-kB3MtdaqCy1JM1YrNXy8bt)
- video of registering a rollup: [link](https://drive.google.com/drive/folders/1Zdt5b7ndzCo7itZKnntzn-aefVe7yAmD) 
- Guide Documents:
  - [Development Setup](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/docs/development-setup.md#-setup) 
  - [Registration Guide](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/docs/registration-guide.md#rollup-registration-guide) 
  - [Metadata Schema](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/schemas/example-rollup-metadata.json)
  - [Generate Signature](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/docs/registration-guide.md#step-4-generate-sequencer-signature) 
  - [PR Process](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/docs/pr-process.md#pull-request-process) 
  - [Validation](https://github.com/tokamak-network/tokamak-rollup-metadata-repository/blob/main/docs/validation-system.md#validation-system) 

# Feedbacks 

Sample 
- [ ] ..
- [ ] .. 

- Theo
The opinions on building an L2 contract verification system using metadata you mentioned in the seminar

  1. **On-chain verification is possible** because the metadata includes the RPC address and the deployed contract address.
  1. In order to verify whether the codehash has been changed, a procedure is needed to store the original codehash that has not been changed in the contract and compare it, and **I think that additional contract development and deployment are required for this.**
  1. If verification is performed using the method of [no.2](/20fd96a400a3808197b3fabedd6c4e05#211d96a400a38034b118d4cb39746eaa), the method of verifying whether the contract has been changed based on the codehash is the **same as the L1 contract verification logic currently under review.**
  1. What is the difference from the L1 contract verification logic? I think it would be good to discuss it together.
  1. I enjoyed your today’s seminar. Thank you so much.