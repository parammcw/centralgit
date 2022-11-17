// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract state
{
    uint public age=10;
    constructor() public
    {
        age=15;
    }
    function setAge() public
    {
        age=25;
    }
}
