## 4.0.0 - 2022-09-09
* Supported API Version: **2022-02-01**
* Added support for the following APIs: 
    * Onboarding Forms
    * Compliance Forms
* Updated filter params 
* Renamed `download_file` endpoint in `files_api` to `download` 
* Renamed `upload_file` endpoint in `files_api` to `upload` 
* Added `list_by_payment_instrument_id` endpoint in `verifications_api`
* Fixed type with `list_associated_identities` endpoint 
* Added designated models for associated identity: `create_associated_identity`, `associated_identity`, `associated_identity_entity`, `create_associated_identity_request_entity`, `create_associated_identity_request_entity_business_address`, `create_associated_identity_request_entity_dob`, `create_associated_identity_request_entity_incorporation_date`, ``create_associated_identity_request_entity_personal_address`
* Added model `additional_buyer_charges`, `get_device_query_params`, `transfer_links`, `transfer_links_destination`, `transfer_links_disputes`, `transfer_links_fees`, `transfer_links_fee_profile`, `transfer_links_parent`, `transfer_links_payment_instruments`, `transfer_links_reversals`, `transfer_links_source`, `update_identity_request_entity_personal_address`, `update_merchant_profile_request`, `verification_links`, `verification_links_application`, `verification_links_merchant`
* Removed model `input_details`
* Updated Enums
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
