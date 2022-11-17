// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract local
{
    string name="Param";

    function store() pure public returns(uint)
    {
        string memory name1="Param";
        uint age=11;
        return age;
    }
}
