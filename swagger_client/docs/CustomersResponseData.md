# CustomersResponseData

map of customers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | [**CustomerResponseData**](CustomerResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.customers_response_data import CustomersResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomersResponseData from a JSON string
customers_response_data_instance = CustomersResponseData.from_json(json)
# print the JSON string representation of the object
print(CustomersResponseData.to_json())

# convert the object into a dict
customers_response_data_dict = customers_response_data_instance.to_dict()
# create an instance of CustomersResponseData from a dict
customers_response_data_from_dict = CustomersResponseData.from_dict(customers_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


