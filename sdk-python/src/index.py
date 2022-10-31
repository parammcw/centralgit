# importing sys
import sys

sys.path.insert(1, '/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/src/signTransaction')
sys.path.insert(1, '/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration')

# importing the signTransaction function
import index as rawTransaction

# importing the schemaValidator function
import schemaValidator

# importing the getChainId and getChainIdFromChainSymbol function
import common

# importing the schemaValidator function
import initialiseWeb3

import json
# Opening JSON file
file = open('/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration/config.json')
# returns JSON object as a dictionary
config = json.load(file)


def prepareTransaction(apiURL, options):
    print(apiURL)
    print(options)
    # prepareTransaction(options)
    validJson = schemaValidator.validateInput(options);
    if not validJson['valid']:
        return validJson

    try:
        config1 = {
            'method': "post",
            'url': apiURL,
            'data': options,
            'headers': {
                'x-api-key': options['xApiKey']
            }
        }
        print(config1)
        response = axios(config1)
        return response['data']

    except Exception as err:
        return err


def signTransaction(transactionObject, options):
    print(transactionObject)
    print(options)
    # signTransaction(options)
    validJson = schemaValidator.validateInput(options)
    if not validJson['valid']:
        return validJson

    # transactionObject(transactionObject)
    validObject = schemaValidator.validateInput(transactionObject)
    if not validObject['valid']:
        return validObject

    axios.defaults.headers['X-API-KEY'] = options['xApiKey']

    apiURL = config['url']['apiurl'] + '/chain/getpublicrpc/'

    configuration = {}

    chainId = common.getChainId({'chainId': options['chainId'], 'chainSymbol': options['chainSymbol']})
    configuration['params'] = {
        'chainId': chainId
    }

    rpc = axios.get(apiURL, configuration)
    options['rpc'] = rpc['data']['rpc'];
    web3 = initialiseWeb3({'rpc': options['rpc'], 'chainId': chainId, 'key': options['key']});
    transactionObject['value'] = BN(transactionObject['value'])

    try:
        chainName = config['chains'][chainId]['chainName']

    except Exception as err:
        return err

    rawData = rawTransaction['signTransaction' + chainName](web3, transactionObject, options)
    return rawData;


def sendTransaction(options):
    print(options)
    #sendTransaction(options)
    validJson = schemaValidator.validateInput(options)
    if not validJson['valid']:
        return validJson

    try:
        apiURL = config.url.apiurl + '/chain/sendtransaction/';
        params = {
            'method': "post",
            'url': apiURL,
            'data': options,
            'headers': {
                'x-api-key': options['xApiKey']
            }
        }

        transactionHash = axios(params);
        return transactionHash['data'];

    except Exception as err:
        return err
