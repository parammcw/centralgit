// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Functions
{
    uint age;
    
    function getter() view public returns(uint)
    {
        return age;
    }
    function setter(uint newage) public
    {
        age=newage;
    }
}
