// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

struct Meassurement {
    string temperature;
    string humidity;
}

/**
 * @title IoTDevice
 */
contract IoTDevice {

    address private owner;
    Meassurement[] meassurements;

    // modifier to check if caller is owner
    modifier isOwner() {
        // If the first argument of 'require' evaluates to 'false', execution terminates and all
        // changes to the state and to Ether balances are reverted.
        // This used to consume all gas in old EVM versions, but not anymore.
        // It is often a good idea to use 'require' to check if functions are called correctly.
        // As a second argument, you can also provide an explanation about what went wrong.
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    /**
     * @dev Set contract deployer as owner
     */
    constructor() {
        owner = msg.sender; // 'msg.sender' is sender of current call, contract deployer for a constructor
    }


    function addMeassurement(string calldata temperature, string calldata humidity) public isOwner {
        // Instantiate new data set
        Meassurement memory new_data;
        new_data.temperature = temperature;
        new_data.humidity = humidity;
        
        // Add new dataset to state
        meassurements.push(new_data);
        
    }

    /**
     * @dev Return owner address 
     * @return address of owner
     */
    function getOwner() external view returns (address) {
        return owner;
    }

    function getMeassurements() external view returns (Meassurement [] memory) {
        return meassurements;
    }
} 
