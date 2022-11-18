/** @type import('hardhat/config').HardhatUserConfig */
require("@nomiclabs/hardhat-waffle")

const ALCHEMY_API_KEY = "CZLVYMBIq_c78jRGxRZijgmWGVrP4AE0";
const GOERLI_PRIVATE_KEY = "a04a58bdc18ee3a66f7462ef05ca01729d42316c311339e2f88dd318cc9cf526";

module.exports = {
  solidity: "0.8.17",
  networks: {
    goerli: {
      url: `https://eth-goerli.g.alchemy.com/v2/${ALCHEMY_API_KEY}`,
      accounts:[`0x${GOERLI_PRIVATE_KEY}`],
    },
  },
};
