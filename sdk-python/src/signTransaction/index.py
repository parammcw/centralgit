# importing sys
import sys

sys.path.insert(1, '/centralgit/sdk-python/src/signTransaction')

# importing the signTransaction function
import Ethereum


def signTransactionEvm(web3, transactionObject, options):
    print(web3)
    print(transactionObject)
    print(options)
    rawData = Ethereum.signTransactionEvm(web3, transactionObject, options)
    return rawData