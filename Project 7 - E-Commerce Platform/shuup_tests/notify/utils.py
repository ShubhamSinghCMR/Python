 
import six


def make_bind_data(variables=None, constants=None):
    if not constants:
        constants = {}
    if not variables:
        variables = {}
    bind_data = {}
    for name, variable in six.iteritems(variables):
        bind_data[name] = {"variable": variable}
    for name, constant in six.iteritems(constants):
        bind_data[name] = {"constant": constant}
    return bind_data
