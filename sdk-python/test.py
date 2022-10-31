# importing sys
import sys

sys.path.insert(1, '/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/src');

# importing the prepareTransaction # function
import index

apiURL = "https://uat.expand.network"
options = {
    'from': "param.testnet",
    'to': "param.testnet",
    'networkId': "testnet",
    'value': "1500000000000000000"
}

transactionObject = index.prepareTransaction(apiURL, options)

rawTransaction = index.signTransaction({
    'privateKey': "ed25519:3DwGRaAbmU8UBfnvxSgrKKNgELSTR18QPuBNGmicNXd7hhJq86BZ8836xTYXeThhKuYda9gmMD5HGmNAp734KoqQ",
    'xApiKey': "9iJU9jHvEf8rURIhIdKMB5SLBQMrLWCq37wMg7vL",
    'chainId': "1201" ,
    'transactionObject': transactionObject
}, options)

print("rawTransaction:   ", rawTransaction)
index.sendTransaction({
    'chainId': "1201",
    'xApiKey': "9iJU9jHvEf8rURIhIdKMB5SLBQMrLWCq37wMg7vL",
    'networkId': "testnet",
    'rawTransaction': rawTransaction
})