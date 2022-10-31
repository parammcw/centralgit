# Copyright 2022 The CmLab Authors
# This file is part of the expand Library.

import json
# Opening JSON file
file = open('/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration/errorMessage.json')
# returns JSON object as a dictionary
errorMessage = json.load(file)

# Standard JSON schema for the complete adaptor program
# Including all the functions
import sys
sys.path.insert(1, '/home/param/PycharmProjects/pythonProject/centralgit/sdk-python/configuration')

# importing the signTransaction function
import schema


def validateInput(options):
    """
    This functions validate the given options as per the schema
    Returns the validate response as of following
    {
        "valid": false,
        "message" : {
           "error": {
              missingProperty: 'address'
           }
        }
       "code" : 401
     }
    :param options:
    :return:
    """

    print(options)
    validate = schema.jsonSchema
    valid = False
    error = validate['allErrors'] if not valid else None
    response = {'valid': valid}

    if not valid:
        response['message'] = error
        response['code'] = errorMessage['error']['code']['invalidInput']

    return response