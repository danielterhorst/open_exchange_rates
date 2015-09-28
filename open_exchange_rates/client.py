from __future__ import unicode_literals

import logging
import httplib
import operator

from requests.adapters import HTTPAdapter
import requests

from .exceptions import OpenExchangeRatesAccessRestrictedError, OpenExchangeRatesAccessRestrictedOverUseError, \
    OpenExchangeRatesInvalidAppIdError, OpenExchangeRatesInvalidBaseError, OpenExchangeRatesMissingAppIdError, \
    OpenExchangeRatesNotAllowedError, OpenExchangeRatesNotFoundError


logger = logging.getLogger(__name__)


class Client(object):

    API_URL_PREFIX = 'https://openexchangerates.org/api'
    API_URL_LATEST = '{}/latest.json?app_id={{}}&base={{}}'.format(API_URL_PREFIX)

    HTTP_CODE_ERROR_MAP = {
        (httplib.NOT_FOUND, 'not_found'): OpenExchangeRatesNotFoundError,
        (httplib.UNAUTHORIZED, 'missing_app_id'): OpenExchangeRatesMissingAppIdError,
        (httplib.UNAUTHORIZED, 'invalid_app_id'): OpenExchangeRatesInvalidAppIdError,
        (httplib.UNAUTHORIZED, 'not_allowed'): OpenExchangeRatesNotAllowedError,
        (httplib.FORBIDDEN, 'access_restricted'): OpenExchangeRatesAccessRestrictedError,
        (429, 'access_restricted'): OpenExchangeRatesAccessRestrictedOverUseError,
        (httplib.BAD_REQUEST, 'invalid_base'): OpenExchangeRatesInvalidBaseError
    }

    def __init__(self, app_id):

        self.app_id = app_id

        # Provides cookie persistence, connection-pooling, and configuration.
        self.session = requests.Session()

        # Create an requests HTTP adapter and set number of retries to attempt
        adapter = HTTPAdapter()
        adapter.max_retries = 5

        # Register transport adapter for given URL prefix and enable connection retrying.
        self.session.mount(self.API_URL_PREFIX, adapter=adapter)

    def get_latest_for_currency(self, iso_name):
        """ Get latest exchange rate for given base currency """
        return self.execute(self.API_URL_LATEST.format(self.app_id, iso_name))['rates']

    def execute(self, url):
        """ Generic execute method to perform API call and handle errors. """

        response = self.session.get(url, timeout=5)

        content_json = response.json()

        # If we get an HTTP error code, raise an exception
        if response.status_code in map(operator.itemgetter(0), self.HTTP_CODE_ERROR_MAP.keys()):

            # Get the exception based on the HTTP status and error message
            exception_class = self.HTTP_CODE_ERROR_MAP[(response.status_code, content_json.get('message'))]

            # Raise it with the description (if available)
            raise exception_class(content_json.get('description'))

        return content_json
