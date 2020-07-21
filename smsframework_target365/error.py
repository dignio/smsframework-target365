from smsframework.exc import *


class Target365ProviderError(ProviderError):
    """ Custom Target365 errors """

    def __init__(self, message=''):
        super(Target365ProviderError, self).__init__(message)
