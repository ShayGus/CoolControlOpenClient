# UpdateCustomerRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | customer name | 
**description** | **str** | customer description | [optional] 

## Example

```python
from cool_open_client.client.models.update_customer_request_body import UpdateCustomerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCustomerRequestBody from a JSON string
update_customer_request_body_instance = UpdateCustomerRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateCustomerRequestBody.to_json())

# convert the object into a dict
update_customer_request_body_dict = update_customer_request_body_instance.to_dict()
# create an instance of UpdateCustomerRequestBody from a dict
update_customer_request_body_from_dict = UpdateCustomerRequestBody.from_dict(update_customer_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


