# CustomerResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | customer ID | [optional] 
**name** | **str** | customer name | [optional] 
**description** | **str** | customer descriptions | [optional] 
**role** | **object** | caller permissions for this customer | [optional] 
**sites** | **List[str]** | array of child site IDs | [optional] 

## Example

```python
from cool_open_client.client.models.customer_response_data import CustomerResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerResponseData from a JSON string
customer_response_data_instance = CustomerResponseData.from_json(json)
# print the JSON string representation of the object
print(CustomerResponseData.to_json())

# convert the object into a dict
customer_response_data_dict = customer_response_data_instance.to_dict()
# create an instance of CustomerResponseData from a dict
customer_response_data_from_dict = CustomerResponseData.from_dict(customer_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


