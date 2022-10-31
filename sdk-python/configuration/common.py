import json
# Opening JSON file
file = open('/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration/config.json')
# returns JSON object as a dictionary
config = json.load(file)

def getChainIdFromChainSymbol(chainSymbol):
    """
    This functions returns the appropriate chainId for the given chainSymbol
    :param chainSymbol:
    :return:
    """
    for chain in config['chains']:
        if config[chain]['chainSymbol'] == chainSymbol:
            return chain

    # Always returning null by default
    return


def getChainId(options):
    """
    This functions returns the appropriate chainId for the given combination of chainId and chainSymbol
    :param options:
    :return:
    """

    chainId = options['chainId']
    chainSymbol = options['chainSymbol'];

    if not chainId and not chainSymbol:
        #By default setting it to EVM based chains
        chainId = "1"
    elif not chainId and chainSymbol:
        #Fetch the equivalent chain ID from the configuration File
        chainId = getChainIdFromChainSymbol(chainSymbol);

    else:
        #By default priority will be given to chainId
        chainId = str(chainId)

    return chainId;