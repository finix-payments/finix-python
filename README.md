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
# fetch 5 payment instruments and print id of each
payment_instruments = client.payment_instruments.list(limit=5)
for single_instrument in payment_instruments:
    print(single_instrument.id)

# fetch the next 5 payment instruments and print type of the first one
next_five_instruments = payment_instruments.list_next()
print(next_five_instruments[0].type)
```

Here is an example of catching exceptions:
```python
try:
    client.payment_instruments.get('this_is_invalid_id')

except finix.ApiException as e:
    # print basic http information of the exception
    print(e.status)
    print(e.reason)
    print(e.headers)
    # print message of each error in the http response body
    for err in e.body:
        print (err.message)
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
