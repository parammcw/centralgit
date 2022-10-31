"""
For the functions under chain category,
the validation is set on the function level
For example, for funciton getBlock() the request will be same, regardless of the chain ID and symbol
Whereas for all the other category, validations are broken one level down, i.e. to the protocol level
"""

jsonSchema = {
    'allErrors': True,
    'strict': True,
    'useDefaults': True
}