## 3.0.0 - 2022-07-29
* Supported API Version: **2022-02-01**
* Payment instruments API:
  * Removed the endpoint '**_create_payment_instrument_verification_** '.
  * Added the endpoint '**_list_updates_by_payment_instrument_id_** ' 
* Improve list endpoints experience:
  * List endpoints now return a FinixList. 
    * FinixList supports list-like behavior such as index access together with easier pagination control using method list_next() to fetch resources from the next page
    * A `list_next()` function will fetch the next set of resources.
    * You can check if there are more resources to fetch with `has_more` variable.
* Improved exception handling:
  * Previously, the json data was returned as the error. Now there is a ErrorList exception that behaves like a list and contains FinixErrors with all kinds of possible error fields.
* Added default versioning header: 
  * A FinixClient now automatically uses the latest version of Finix APIs. You no longer need to manually configure the versioning header.
* Added underscore to mark internal attributes and methods as private.
* Re-organized and improved the test suite.

## 2.0.0 - 2022-07-15
* Supported API Version: 2022-02-01
* Complete rewrite from previous deprecated library.
