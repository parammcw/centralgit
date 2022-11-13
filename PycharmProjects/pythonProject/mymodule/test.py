"""
const {signTransaction,sendTransaction,prepareTransaction} = require('./index')

async function testing(){
try{
var rawTransaction = await signTransaction(
{
from:"newmadhur.testnet",
to:"madhurrr.testnet",
networkId:"testnet",
value:"1500000000000000000"
},
{
privateKey:"ed25519:3DwGRaAbmU8UBfnvxSgrKKNgELSTR18QPuBNGmicNXd7hhJq86BZ8836xTYXeThhKuYda9gmMD5HGmNAp734KoqQ",
xApiKey:"9iJU9jHvEf8rURIhIdKMB5SLBQMrLWCq37wMg7vL",chainId:"1201"
}
).then(rawTransaction => sendTransaction(
{
chainId:"1201",
xApiKey:"9iJU9jHvEf8rURIhIdKMB5SLBQMrLWCq37wMg7vL",
networkId:"testnet",
rawTransaction:rawTransaction
}
)).then(res => console.log(res))
}
catch(error){
console.log(error)
}
}

testing()
"""
