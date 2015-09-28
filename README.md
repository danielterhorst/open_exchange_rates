# README

An Open Exchange Rates (https://openexchangerates.org/) API client written in Python.

## Installation

* git clone https://github.com/danielterhorst/open_exchange_rates.git
* python setup.py install

Or:

* pip install open_exchange_rates

## Usage

Get all exchange rate for base currency (Enterprise/Unlimited Plan feature):

```python
from open_exchange_rates.client import Client

client = Client(app_id='<your APP ID>')
client.get_latest_for_currency('USD')
```
