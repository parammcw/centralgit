const {expect} = require("chai");

describe("Token Contract", function(){
    let Token;
    let hardhatToken;
    let owner;
    let addr1;
    let addr2;
    let addrs;

    beforeEach(async function (){
        [owner, addr1, addr2, ...addrs] = await ethers.getSigners();
        Token=await ethers.getContractFactory("Token"); // instance contract
        hardhatToken=await Token.deploy(); // deploy contract
    });

    describe("Deployment", function (){
        it("Should set the right owner", async function (){
            expect(await hardhatToken.owner()).to.equal(owner.address);
        });
        it("Should assign the total supply of tokens to the owner", async function (){
            const ownerBalance=await hardhatToken.balanceOf(owner.address); // ownerBalance=10000
            expect(await hardhatToken.totalSupply()).to.equal(ownerBalance); // totalSupply=10000
        });
    });

    describe("Transactions", function (){
        it("Should transfer tokens between accounts", async function (){
            // owner account to addr1
            await hardhatToken.transfer(addr1.address,5);
            const addr1Balance = await hardhatToken.balanceOf(addr1.address);
            expect(addr1Balance).to.equal(5);
            // addr1 account to addr2
            await hardhatToken.connect(addr1).transfer(addr2.address,5);
            const addr2Balance = await hardhatToken.balanceOf(addr2.address);
            expect(addr2Balance).to.equal(5);
        });
        it("Should fail if sender does not have enough tokens", async function () {
            const initialOwnerBalance = await hardhatToken.balanceOf(owner.address)  //10000
            await expect(hardhatToken.connect(addr1).transfer(owner.address,1)).to.be.revertedWith("Not enough tokens");
            expect(await hardhatToken.balanceOf(owner.address)).to.equal(initialOwnerBalance);
        });
        it("Should update balances after transfers", async function (){
            const initialOwnerBalance = await hardhatToken.balanceOf(owner.address);
            await hardhatToken.transfer(addr1.address,5);
            await hardhatToken.transfer(addr2.address,10);

            const finalOwnerBalance = await hardhatToken.balanceOf(owner.address);
            expect(finalOwnerBalance).to.equal(initialOwnerBalance-15);

            const addr1Balance = await hardhatToken.balanceOf(addr1.address);
            expect(addr1Balance).to.equal(5);

            const addr2Balance = await hardhatToken.balanceOf(addr2.address);
            expect(addr2Balance).to.equal(10);
        });
    });
});    