const {expect} = require("chai");
const { ethers } = require("hardhat");

describe("Token Contract", function(){
    it("Deployment should assign the total supply of tokens to the owner", async function (){
        const [owner] = await ethers.getSigners();
        console.log("Signers Object", owner);
        
        const Token=await ethers.getContractFactory("Token"); // instance contract

        const hardhatToken=await Token.deploy(); // deploy contract
        const ownerBalance=await hardhatToken.balanceOf(owner.address); // ownerBalance=10000
        console.log("Owner Address: ", owner.address);

        expect(await hardhatToken.totalSupply()).to.equal(ownerBalance); // totalSupply=10000
    });
});