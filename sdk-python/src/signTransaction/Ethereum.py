from web3 import Web3


def signTransactionEvm(web3, transactionObject, options):
    """
    Function will sign the transaction payload for ethereum based chains
    """
    print(web3)
    print(transactionObject)
    print(options)
    try:
        signedTransaction = web3.eth.accounts.signTransaction(transactionObject, options['privateKey'])
        return signedTransaction

    except Exception as err:
        return err
