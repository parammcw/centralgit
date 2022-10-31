# importing sys
import sys
sys.path.insert(1, '/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration')
# importing the getChainId and getChainIdFromChainSymbol function
import common

import json
# Opening JSON file
file = open('/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration/config.json')
# returns JSON object as a dictionary
config = json.load(file)

import json
# Opening JSON file
file = open('/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration/errorMessage.json')
# returns JSON object as a dictionary
errorMessage = json.load(file)

# Import the multiple different web3 libraries
from web3 import Web3 as evmWeb

invalidChainId = {
    'error': errorMessage['error']['message']['invalidChainId'],
    'code': errorMessage['error']['code']['invalidInput']
}

def initialiseWeb3(data):
    """
    Initialise a web3 depending on the chain Id or chain Symbol
    :param data:
    :return:
    """

    chainId = common.getChainId({
        'chainId': data.chainId,
        'chainSymbol': data.chainSymbol
    })

    try:
        rpc = data['rpc'] or config['chains'][chainId]['rpc']
        chainName = config['chains'][chainId]['chainName']

    except Exception as err:
        return invalidChainId

    if chainName == 'Evm':
        web3 = evmWeb(rpc)

    return web3

