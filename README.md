# Finix Python Library

This is the official Finix Python library

## Installation
### Prerequisites
- Python>=3.6

### install from PyPI:
```
pip install --upgrade finix
```

### install from source:
```
python setup.py install
```



## Using the Library
### Initialization
```python
import finix
from finix.configuration import Environment, Configuration
from finix.models import *        
# finix.models is intended for wildcard import, feel safe to import all predefined models at once

config = Configuration(
    username = 'ENTER_YOUR_USERNAME',
    password = 'ENTER_YOUR_PASSWORD',
    environment = Environment.SANDBOX
)

client = finix.FinixClient(config)
```
### Specify API version
To access the latest version of Finix API, you need to manually set the versioning header as shown below. Otherwise, requests will go to the oldest version of Finix API.
```python
client.set_default_header('Finix-Version','2022-02-01')
```

### Example APIs
Here is an example of creating a transfer:
```python
request = CreateTransferRequest(
    merchant='MUeDVrf2ahuKc9Eg5TeZugvs',
    currency = Currency("USD"),
    amount = 12345,
    source = 'PIe2YvpcjvoVJ6PzoRPBK137',
    tags = Tags(
        category = 'sale'
    )
)

transfer = client.transfers.create(create_transfer_request=request)
```

Here is an example of listing payment instruments:
```python
# fetch a list of 5 resources with default pagination
payment_instrument_list = client.payment_instruments.list(limit=5)

# print type of the first payment instrument from the fetched list
print(payment_instrument_list.embedded['payment_instruments'][0]['type'])
```


## Supported APIs
- Transfers
- Authorizaitons
- Identities
- Merchants
- Payment Instruments
- Instrument Updates
- Balance Transfers
- Devices
- Disputes
- Files
- Settlements
- Webhooks
- Verifications
- Merchant Profiles
- Fee Profiles
