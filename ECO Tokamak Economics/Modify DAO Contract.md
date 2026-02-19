repo : [https://github.com/tokamak-network/ton-staking-v2/tree/DAOSnapshot](https://github.com/tokamak-network/ton-staking-v2/tree/DAOSnapshot)

# Regarding the DAO Snapshot upgrade

## DAO Snapshot Upgrade Background

To systematically handle proposals and encourage active community participation, the Tokamak DAO has added RFC and Temperature Check stages before the creation of a DAO Agenda in its lifecycle. The Temperature Check stage is conducted on Snapshot, and we plan to upgrade the system by adding an Agenda Memo field when creating a DAO Agenda. This will allow users to input the Snapshot link used for the Temperature Check, so that the background of the Agenda can be easily referenced.

## DAO Snapshot Upgrade Contents

- Functions that change
  - onApprove: Decode the Memo value and pass the information to createAgenda.
  - _decodeAgendaData: Changed to decode Memo values as well
  - _createAgenda: Added a process to save Memo values for AgendaID in storage, taking Memo values as input.
- Add Storage
  - Added mapping storage to allow checking Memo values for AgendaID in DAO Contract

## Check the changed code

- Parts that have been added or changed are highlighted in Bold.

```solidity
//ApproveAndCall
function onApprove(
    address owner,
    address ,
    uint256 ,
    bytes calldata data
) external returns (bool) {
    require(msg.sender == ton, "It's not from TON");
    AgendaCreatingData memory agendaData = _decodeAgendaData(data);
    require(agendaData.target.length != 0, "need target");
    require(agendaData.atomicExecute, "atomicExecute need true");
    require(agendaData.target.length == agendaData.functionBytecode.length, "need same length");
    require(agendaData.votingPeriodSeconds >= agendaManager.minimumVotingPeriodSeconds(), "need over minimumVotingPeriodSeconds");

    for (uint256 i = 0; i < agendaData.target.length; i++) {
        if(agendaData.target[i] == address(daoVault)) {
            bytes memory abc = agendaData.functionBytecode[i];
            bytes memory selector1 = abc.slice(0, 4);

            if (selector1.equal(claimTONBytes)) revert ClaimTONError();
            else if (selector1.equal(claimERC20Bytes)) {
                bytes memory tonaddr = _toBytes(ton);
                bytes memory ercaddr = abc.slice(16, 20);
                bool check3 = ercaddr.equal(tonaddr);
                require(!check3, 'claimERC20 ton dont use');
            } else if (selector1.equal(claimWTONBytes)) {
                revert ClaimWTONError();
            }
        }
    }

    _createAgenda(
        owner,
        agendaData.target,
        agendaData.noticePeriodSeconds,
        agendaData.votingPeriodSeconds,
        agendaData.atomicExecute,
        agendaData.functionBytecode,
        **agendaData.memo**
    );

    return true;
}


function _decodeAgendaData(bytes calldata input)
    internal
    pure
    returns (AgendaCreatingData memory data)
{
    (
	    data.target, 
	    data.noticePeriodSeconds, 
	    data.votingPeriodSeconds, 
	    data.atomicExecute, 
	    data.functionBytecode, 
	    **data.memo
    **) = abi.decode(input, (address[], uint128, uint128, bool, bytes[], string));
}


function _createAgenda(
    address _creator,
    address[] memory _targets,
    uint128 _noticePeriodSeconds,
    uint128 _votingPeriodSeconds,
    bool _atomicExecute,
    bytes[] memory _functionBytecodes,
**    string memory _memo
**)
    internal
    validAgendaManager
    returns (uint256)
{
    // pay to create agenda, burn ton.
    _payCreatingAgendaFee(_creator);

    uint256 agendaID = agendaManager.newAgenda(
        _targets,
        _noticePeriodSeconds,
        _votingPeriodSeconds,
        _atomicExecute,
        _functionBytecodes
    );

**    agendaMemo[agendaID] = _memo;
**
    emit AgendaCreated(
        _creator,
        agendaID,
        _targets,
        _noticePeriodSeconds,
        _votingPeriodSeconds,
        _atomicExecute
    );

    return agendaID;
}


//Add Storage
**mapping(uint256 => string) public agendaMemo;
**
```

# currentAgendaStatus bug fix

## Function Creation Background

During the previous DAO upgrade, after the voting was completed, it was necessary to execute the endAgendaVoting function and generate a transaction in order to properly update the storage for Agendas whose storage had not been changed. To address this, we have added the currentAgendaStatus function, which allows users to accurately check the current status of an Agenda at any time using a view function, without the need to generate a transaction. This addition enables users to view the status of any Agenda directly and conveniently.

## Check the changed code

- Changed to return status value (5,6) when AgendaID is entered as a value greater than the AgendaID currently managed by AgendaManager
- Changed if statement processing section to 5 places
- When an AgendaID value that has not been created is entered
- When Agenda is before NoticeEndTIme
- When Agenda has passed NoticeEndTime but no one has voted
- When Agenda has passed NoticeEndTime and someone has voted and VotingEndTime is set
- When Agenda has passed VoingEndTime after someone has voted

```solidity
function currentAgendaStatus(uint256 _agendaID) external view returns (uint256 currentResult, uint256 cureentStatus) {
    uint256 numAgendas = agendaManager.numAgendas();
    if(numAgendas <=  _agendaID){
        // No Agenda
        // (NO AGENDA, NO AGENDA)
        return (5, 6);
    }

    uint256 noticeEndTime = agendaManager.getAgendaNoticeEndTimeSeconds(_agendaID);
    uint256 votingEndTime = agendaManager.getAgendaVotingEndTimeSeconds(_agendaID);
    
    if (block.timestamp < noticeEndTime) {
        //Notice Time
        //(PENDING, NOTICE)
        return (0, 1);
    } else if (noticeEndTime <= block.timestamp && votingEndTime == 0) {
        //When the NoticeTime has passed but no one has voted
        //(NO CONSENSUS, VOTING)
        currentResult = 4;
        cureentStatus = 2;
        return (currentResult, cureentStatus);
    } else if (noticeEndTime <= block.timestamp &&  block.timestamp <= votingEndTime) {
        //When the NoticeTime has passed and someone has voted, but voting has not ended
        (uint256 result,) = agendaManager.getAgendaResult(_agendaID);
        cureentStatus = 2;
        return (result, cureentStatus);
    } else if (votingEndTime < block.timestamp && votingEndTime != 0) {
        //Results after votingEndTime has passed
        (uint256 yes, uint256 no, uint256 abstain) = agendaManager.getVotingCount(_agendaID);
        if (quorum <= yes) {
            // yes
            (uint256 result, bool executed) = agendaManager.getAgendaResult(_agendaID);
            currentResult = result;
            if (executed) {
                cureentStatus = 4;
            } else {
                cureentStatus = 3;
            }
            return (currentResult, cureentStatus);
        } else if (quorum <= no) {
            // no (REJECT, ENDED)
            currentResult = 2;
            cureentStatus = 5;
            return (currentResult, cureentStatus);
        } else if (quorum <= abstain) {
            // (DISMISS, ENDED)
            currentResult = 3;
            cureentStatus = 5;
            return (currentResult, cureentStatus);
        } else {
            // (NO CONSENSUS, ENDED)
            currentResult = 4;
            cureentStatus = 5;
            return (currentResult, cureentStatus);
        }
    }

}
```

# How to Test

## On Sepolia

```solidity
//blockNumber: 8323710
npx hardhat test test/agenda/29.currentAgendaViewTest-sepolia.js
```

## On Mainnet

```solidity
//blockNumber:22355050
npx hardhat test test/agenda/30.currentAgendaViewTest-mainnet.js
```

# Deploy & CreateAgedna the Contract

## On Sepolia

```solidity
//Deployed Contract
DAOCommittee_V2 0xF955b73431ba9B411E41A13Bf29787BCD087FA6E

//Create Agenda
tx : https://sepolia.etherscan.io/tx/0x8ce7ab0412fc6c9a5f7dcde6b56c212b52e5714ede0ea6f6e41a79c3a13485b1

//Execute Agenda
tx : https://sepolia.etherscan.io/tx/0x59fc5d95f9bb71590bd41a4d2442e94d34d05199188d3e31978a89480e7ddac6
```