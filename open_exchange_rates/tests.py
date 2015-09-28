from __future__ import unicode_literals

import mock
import json
import unittest
import requests
import urlparse

import client
from exceptions import OpenExchangeRatesInvalidBaseError


def side_effect(*args, **kwargs):

    base = urlparse.parse_qs(args[0])['base'][0]

    response = requests.Response()

    if base == 'EUR':

        response.status_code = 200
        response._content = json.dumps({
            'timestamp': 1398672062,
            'base': 'EUR',
            'rates': {
                'DZD': 108.88854, 'NAD': 14.754583, 'GHS': 3.913803, 'EGP': 9.69261, 'BGN': 1.957726,
                'PAB': 1.385756, 'BOB': 9.576042, 'DKK': 7.467748, 'BWP': 12.188992, 'LBP': 2095.320119,
                'TZS': 2276.773259, 'VND': 29238.056173, 'AOA': 135.566594, 'KHR': 5559.816322,
                'MYR': 4.526931, 'KYD': 1.145428, 'LYD': 1.716092, 'UAH': 15.91834, 'JOD': 0.980985,
                'AWG': 2.470109, 'SAR': 5.197034, 'EUR': 1, 'HKD': 10.744038, 'CHF': 1.219348,
                'GIP': 0.822938, 'BYR': 13868.110255, 'ALL': 140.160167, 'MRO': 410.641633, 'HRK': 7.6142,
                'DJF': 247.46864, 'SZL': 14.760403, 'THB': 44.673932, 'XAF': 656.91159, 'BND': 1.741521,
                'ISK': 155.642518, 'UY': 31.791948, 'NIO': 35.656848, 'LAK': 11150.712925,
                'SYP': 205.181892, 'MAD': 11.241997, 'MZN': 42.916537, 'PHP': 61.703537,
                'ZAR': 14.770657, 'NPR': 134.609744, 'ZWL': 446.705236, 'NGN': 223.070614,
                'CRC': 760.042577, 'AED': 5.090074, 'EEK': 16.109408, 'MWK': 544.940076,
                'LKR': 181.003232, 'PKR': 135.945946, 'HUF': 309.99601, 'BMD': 1.385756, 'LSL': 14.760541,
                'MNT': 2462.025679, 'AMD': 576.526964, 'UGX': 3483.835623, 'QAR': 5.045259,
                'XDR': 0.893756, 'JMD': 152.151803, 'GEL': 2.446926, 'SHP': 0.822938, 'AFN': 78.86993,
                'SBD': 10.102719, 'KPW': 1247.179987, 'TRY': 2.961465, 'BDT': 107.505197,
                'YER': 297.861224, 'HTG': 62.190686, 'XOF': 657.11267, 'MGA': 3281.53841, 'ANG': 2.479089,
                'LRD': 118.482099, 'RWF': 943.752183, 'NOK': 8.329494, 'MOP': 11.0662, 'INR': 83.941504,
                'MXN': 18.193404, 'CZK': 27.450667, 'TJS': 6.750292, 'BTC': 0.0032640058, 'BTN': 83.953436,
                'COP': 2693.728625, 'TMT': 3.949542, 'MUR': 41.732527, 'IDR': 16040.212779,
                'HNL': 26.486057, 'XPF': 119.621994, 'FJD': 2.54545, 'ETB': 26.985483, 'PEN': 3.87679,
                'BZD': 2.786699, 'ILS': 4.81856, 'DOP': 59.806853, 'TWD': 41.947375, 'MDL': 18.715294,
                'BSD': 1.385756, 'SEK': 9.102873, 'ZMK': 7279.478145, 'JEP': 0.822938, 'AUD': 1.490934,
                'SRD': 4.549897, 'CUP': 1.385843, 'CLF': 0.032718, 'BBD': 2.771511, 'KMF': 492.771842,
                'KRW': 1437.118546, 'GMD': 52.797286, 'VEF': 8.717788, 'GTQ': 10.731928, 'CLP': 776.458237,
                'ZMW': 8.69393, 'LTL': 3.454107, 'CDF': 1277.569607, 'XCD': 3.743674, 'KZT': 252.280952,
                'RUB': 49.956958, 'XAG': 0.07040378, 'TTD': 8.949209, 'OMR': 0.53353, 'BRL': 3.110023,
                'MMK': 1334.600376, 'PLN': 4.212851, 'PYG': 6138.698433, 'KES': 120.302677,
                'SVC': 12.125957, 'MKD': 61.677291, 'GBP': 0.822938, 'AZN': 1.086617, 'TOP': 2.578601,
                'MVR': 21.397895, 'VUV': 130.368418, 'GNF': 9646.290517, 'WST': 3.185136,
                'IQD': 1613.573753, 'ERN': 20.720614, 'BAM': 1.958409, 'SCR': 16.528904, 'CAD': 1.528445,
                'CVE': 110.16848, 'KWD': 0.389474, 'BIF': 2149.5609, 'PGK': 3.858894, 'SOS': 1347.8773,
                'SGD': 1.740266, 'UZS': 3158.312381, 'STD': 24569.631583, 'IRR': 35091.487581,
                'CNY': 8.637434, 'SLL': 5969.03326, 'TND': 2.204224, 'GYD': 284.081617, 'MTL': 0.947494,
                'NZD': 1.616812, 'FKP': 0.822938, 'LVL': 0.708936, 'USD': 1.385756, 'KGS': 75.381499,
                'ARS': 11.087513, 'RON': 4.457089, 'RSD': 115.803932, 'BHD': 0.522369, 'JPY': 141.633222,
                'SDG': 7.882825, 'XA': 0.001063
            },
            'license': 'Data sourced from various providers with public-facing APIs; copyright may apply; '
                       'resale is prohibited; no warranties given of any kind. Bitcoin data provided by '
                       'http://coindesk.com. All usage is subject to your acceptance of the License Agreement '
                       'available at: https://openexchangerates.org/license/',
            'disclaimer': 'Exchange rates are provided for informational purposes only, and do not constitute '
                          'financial advice of any kind. Although every attempt is made to ensure quality, NO '
                          'guarantees are given whatsoever of accuracy, validity, availability, or fitness for '
                          'any purpose - please use at your own risk. All usage is subject to your acceptance '
                          'of the Terms and Conditions of Service, available at: '
                          'https://openexchangerates.org/terms/'
        })

    else:

        response.status_code = 400
        response._content = json.dumps({
            'error': True,
            'status': 400,
            'message': 'invalid_base',
            'description': 'Invalid `base` currency [{}] - please make sure you use the standard 3-letter code, '
                           'and that it is supported by the API. Thanks!'.format(base)
        })

    return response


class OpenExchangeRatesClientTestCase(unittest.TestCase):

    def setUp(self):
        super(OpenExchangeRatesClientTestCase, self).setUp()

        self.mock_requests = mock.patch.object(client, 'requests').start()
        self.mock_requests.Session.return_value.get.side_effect = side_effect

        self.client = client.Client('dummy-id')

    def test_success(self):

        self.assertIsInstance(client.Client('dummy-id').get_latest_for_currency('EUR'), dict)

    def test_invalid_base(self):

        with self.assertRaises(OpenExchangeRatesInvalidBaseError):
            client.Client('dummy-id').get_latest_for_currency('ABC')


if __name__ == '__main__':
    unittest.main()
