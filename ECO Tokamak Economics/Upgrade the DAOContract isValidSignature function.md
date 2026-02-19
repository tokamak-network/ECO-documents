# Title*

Added signature verification function to DAO contracts

# **Author*******

Harvey

# **Summary*******

Since a DAO contract does not have a private key, it cannot sign messages.

By implementing the isValidSignature(_hash, _signature) function, the DAO contract can verify the validity of a signature and act as one of the signers in a SafeWallet.

# **Background & Motivation*******

When creating an L2 chain using the TRH-SDK, if that L2 chain participates in TON Staking, it will affect seigniorage distribution. 

Therefore, TokamakDAO must participate in the L1 contract and key authority management of the L2 chain. Any changes that could impact TON-Staking seigniorage must be reviewed and approved by TokamakDAO before implementation.
This structure is not intended to guarantee the operational quality of the L2 chain, but serves as a minimum safeguard to prevent negative impacts on TON-Staking seigniorage.

Therefore, TokamakDAO needs to be registered as a Signer in SafeWallet to manage key permissions and L1Contracts on L2 chains created using TRH-SDK. We propose an update to verify the validity of signatures as a Signer. This can be achieved by implementing the isValidSignature(hash, signature) function in the signing contract, which can then be called to verify the validity of the signature.

# **Proposal Details**

## **Specification*******

```bash
//add storage
address public multiSigWallet; 

bytes4 private constant MAGICVALUE = 0x20c13b0b;
bytes4 private constant INVALID_SIGNATURE = 0xffffffff;

bytes32 public constant SAFE_MSG_TYPEHASH = 0x60b3cbf8b4a223d68d641b3b6ddf9a298e7f33710cf3d3a9d1146b5a6150fbca;
bytes32 private constant DOMAIN_SEPARATOR_TYPEHASH = 0x47e79534a245952e8b16893a336b85a3d9ea9fa8c573f3d803afb92a79469218;

//add functions
/**
 * @notice Signature validation according to SafeWallet Method
 * @dev Validates signatures from MultiSigWallet owners (DAO Contract Owner)
 * @dev Safe Wallet can use this when DAO Contract is one of its signers
 * @param _hash Hash that was signed
 * @param _signature Signature data (multiple signatures from MultiSigWallet owners)
 * @return magicValue SafeWallet magic value
 */
function isValidSignature(
    bytes memory _hash,
    bytes memory _signature
) external view returns (bytes4 magicValue) {
    require(_signature.length >= 130, 'bad sig len');
    if (multiSigWallet == address(0)) {
        return INVALID_SIGNATURE;
    }
    require(
        hasRole(DEFAULT_ADMIN_ROLE, multiSigWallet),
        'multisig not admin'
    );
    bytes memory messageData = encodeMessageDataForSafe(_hash);
    bytes32 messageHash = keccak256(messageData);
    if (_validateSignatures(messageHash, _signature)) {
        return MAGICVALUE;
    }
    return INVALID_SIGNATURE;
}

/**
 * @notice Verify multiple signatures from MultiSigWallet owners
 * @dev Validates signatures from DAO Contracts MultiSigWallet owners
 * @param _hash Hash that was signed
 * @param _signature Concatenated signature data from MultiSigWallet owners
 * @return true if valid signatures meet MultiSigWallet threshold
 */
function _validateSignatures(
    bytes32 _hash,
    bytes memory _signature
) internal view returns (bool) {
    uint256 requiredSigs = IMultiSigWallet(multiSigWallet).numConfirmationsRequired();
    uint256 sigCount = _signature.length / 65;
    
    if (sigCount < requiredSigs) return false;

    address[] memory signers = new address[](sigCount);
    uint256 validSigs = 0;

    for (uint256 i = 0; i < sigCount; i++) {
        bytes memory sigPart = _signature.slice(i * 65, 65);
        address signer = _recoverSigner(_hash, sigPart);

        if (isOwner(signer) && !_isDuplicate(signers, signer, i)) {
            signers[i] = signer;
            validSigs++;
        }
    }

    if (requiredSigs <= validSigs ) {
        return true;
    } else {
        return false;
    }
}

/**
 * @notice Recovers signer address from ECDSA signature
 * @param _hash Hash that was signed
 * @param _signature Signature data (65 bytes)
 * @return signer Signer address
 */
function _recoverSigner(
    bytes32 _hash,
    bytes memory _signature
) internal pure returns (address signer) {
    bytes32 r;
    bytes32 s;
    uint8 v;

    assembly {
        r := mload(add(_signature, 32))
        s := mload(add(_signature, 64))
        v := byte(0, mload(add(_signature, 96)))
    }

    // Prevent signature malleability
    require(
        uint256(s) <= 0x7FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF5D576E7357A4501DDFE92F46681B20A0,
        "bad sig 's' value"
    );

    require(v == 31 || v == 32, "bad sig 'v' value");

    // Create Ethereum signed message hash
    bytes32 ethSignedMessageHash = keccak256(
        abi.encodePacked('\x19Ethereum Signed Message:\n32', _hash)
    );
    signer = ecrecover(ethSignedMessageHash, v - 4, r, s);

    require(signer != address(0), 'Invalid signer');
    return signer;
}

function encodeMessageDataForSafe(bytes memory message) public view returns (bytes memory) {
    bytes32 safeMessageHash = keccak256(abi.encode(SAFE_MSG_TYPEHASH, keccak256(message)));
    return abi.encodePacked(bytes1(0x19), bytes1(0x01), domainSeparator(), safeMessageHash);
}

function domainSeparator() public view returns (bytes32) {
    return keccak256(abi.encode(DOMAIN_SEPARATOR_TYPEHASH, getChainId(), this));
}

function getChainId() public view returns (uint256) {
    uint256 id;
    // solhint-disable-next-line no-inline-assembly
    assembly {
        id := chainid()
    }
    return id;
}

/**
 * @notice Check for duplicate signers
 * @param signers Array of signer addresses
 * @param signer Address to check
 * @param currentIndex Current index in the array
 * @return true if duplicate found
 */
function _isDuplicate(
    address[] memory signers,
    address signer,
    uint256 currentIndex
) internal pure returns (bool) {
    for (uint256 i = 0; i < currentIndex; i++) {
        if (signers[i] == signer) return true;
    }
    return false;
}

/**
 * @notice Verify that you are the owner of MultiSigWallet
 * @param _address Enter address
 * @return true True if the owner of MultiSigWallet
 */
function isOwner(address _address) public view returns (bool) {
    return IMultiSigWallet(multiSigWallet).isOwner(_address);
}

/**
 * @notice Sets MultiSigWallet address (onlyOwner)
 * @dev MultiSigWallet becomes the DAO Owner and its owners signatures are validated via EIP-1271
 * @param _multiSigWallet New MultiSigWallet address
 */
function setMultiSigWallet(
    address _multiSigWallet
) external onlyOwner nonZero(_multiSigWallet) {
    address oldWallet = multiSigWallet;
    require(
        hasRole(DEFAULT_ADMIN_ROLE, _multiSigWallet),
        'not admin'
    );
    multiSigWallet = _multiSigWallet;
    emit MultiSigWalletSet(oldWallet, _multiSigWallet);
}
```

The isValidSignature method can be called to validate a given signature. This method generates a signature based on a nonce generated by SafeWallet.

This function is not a standard ERC-1271 function and supports hashes and signatures generated by SafeWallet.

Since the parameters differ from the standard ERC-1271 function, additional standard ERC-1271 upgrades are possible. However, this upgrade does not include this part.

## Backwards Compatibility

This upgrade is backwards compatible with previous work by only adding the isValidSignature function rather than modifying the functionality of the previous DAOContract.

## **Reference Implementation**

Example implementation of a contract calling the isValidSignature() function on an external   contract

```bash
 function callDAOisValidSignature(
    address _addr,
    bytes calldata _hash,
    bytes calldata _signature
  ) public view {
    bytes4 result = IDAO(_addr).isValidSignature(_hash, _signature);
    require(result == 0x20c13b0b, "INVALID_SIGNATURE");
  }
```

# **Expected Impact*******

When this feature is applied to TokamakDAO, TokamakDAO will be designated as one of the Signers of SafeWallet, allowing it to vote for or against transactions generated in SafeWallet.

This update will increase the utility and influence of TokamakDAO.

And since the view function is added, there is no problem with the security of the TokamakDAO Contract.

# **Security Considerations**

The isValidSignature function is a view function, so it doesn't alter storage. Therefore, once a signature is valid, it remains valid forever. This means that when generating hash values, you need to manage them using a timestamp or nonce.

To import and use the updated isValidSignature function, we recommend managing the hash value within the contract.