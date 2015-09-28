class OpenExchangeRatesError(Exception):
    pass


class OpenExchangeRatesNotFoundError(OpenExchangeRatesError):
    """ Client requested a non-existent resource """
    pass


class OpenExchangeRatesMissingAppIdError(OpenExchangeRatesError):
    """ Client did not provide an App ID """
    pass


class OpenExchangeRatesInvalidAppIdError(OpenExchangeRatesError):
    """ Client provided an invalid App ID """
    pass


class OpenExchangeRatesNotAllowedError(OpenExchangeRatesError):
    """ Client doesn't have permission to access requested route/feature """
    pass


class OpenExchangeRatesAccessRestrictedError(OpenExchangeRatesError):
    """ Access restricted for reason given in 'description' """
    pass


class OpenExchangeRatesAccessRestrictedOverUseError(OpenExchangeRatesError):
    """ Access restricted for repeated over-use """
    pass


class OpenExchangeRatesInvalidBaseError(OpenExchangeRatesError):
    """ Client requested rates for an unsupported base currency """
    pass
