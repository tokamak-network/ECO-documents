To create cost-effective, secure smart contracts, we should master solidity gas optimization techniques. This article is about the practical strategies for Solidity gas optimization. It was referred to the reference articles. 

# **Storage Optimization**

In Solidity, storage optimization is pivotal in managing and reducing gas costs. The basic costs associated with storage operations include 20,000 gas for storing a new variable, 5,000 gas for rewriting an existing variable, and a relatively nominal 200 gas for reading from a storage slot. Interestingly, simply declaring a storage variable without initializing it incurs no gas cost, providing an opportunity for gas savings.

**Minimize on-chain data**

**Efficient data management **

**Updating storage variables:**

**Variable packing:**

**Don’t initialize zero values: **

**Make Solidity values constant where possible**: 

**Use constant and immutable variables for variable that don't change**

** **

# **Refunds**

**Freeing Storage Slots: **

**Using Self Destruct**: 

# **Data Types And Packing**

**Use bytes32 whenever possible because it is the most optimized storage type.** 

**If the length of bytes can be limited, use the lowest amount possible from bytes1 to bytes32**. 

**Using bytes32 is cheaper than using string**.

**Variable packing occurs only in storage — memory and call data are not packed**. 

**You will not save space trying to pack function arguments or local variables.** 

**Storing small numbers in uint8 may not be cheaper.** 

# **Inheritance**

Consider how the use of inheritance over composition can save additional gas.

**Use inheritance**:

**Mind the order: **

# **Memory vs Storage**

**Use storage pointer**

**Try your luck**

# **Mapping vs Array**

**Rule of thumb: **

**When to use mappings**: 

**When to use arrays**: 

# Optimizing Variables

**Optimize variable visibility: **

**Efficient use of global variables: **

**Events for data logging: **

**Streamline return values**: 

**Direct updates to private variables**: 

**Fixed vs dynamic variables: **

**Fixed vs dynamic strings**: 

**Calldata and memory**

# **Function Optimization**

**Use external functions**: 

**Optimize public variables**: 

**Order of functions**: 

**Parameter optimizatio**n: 

**Use of payable functions: **

**Replacing Modifiers with Functions**: 

**Calling a view function**

**Integer overflow/underflow**

**Use revert instead of require**

**Avoid loading too many data in memory**

**Avoid Loops and Complex Computations**

**Precompute Off-Chain When Possible**

# Reference 

[A Comprehensive Guide To Gas And Gas Price In Solidity](https://medium.com/stackanatomy/a-comprehensive-guide-to-gas-and-gas-price-in-solidity-bfb9c00970af)

[Gas Saving Techniques in Solidity](https://dev.to/jamiescript/gas-saving-techniques-in-solidity-324c)

[https://www.infuy.com/blog/7-simple-ways-to-optimize-gas-in-solidity-smart-contracts/](https://www.infuy.com/blog/7-simple-ways-to-optimize-gas-in-solidity-smart-contracts/)