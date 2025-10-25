# CreateCustomerRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | customer name | 
**description** | **str** | customer description | [optional] 

## Example

```python
from cool_open_client.client.models.create_customer_request_body import CreateCustomerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCustomerRequestBody from a JSON string
create_customer_request_body_instance = CreateCustomerRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateCustomerRequestBody.to_json())

# convert the object into a dict
create_customer_request_body_dict = create_customer_request_body_instance.to_dict()
# create an instance of CreateCustomerRequestBody from a dict
create_customer_request_body_from_dict = CreateCustomerRequestBody.from_dict(create_customer_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


