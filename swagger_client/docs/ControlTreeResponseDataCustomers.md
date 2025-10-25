# ControlTreeResponseDataCustomers

dictionary of accessible customers

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | [**ControlTreeResponseDataCustomersCustomerId**](ControlTreeResponseDataCustomersCustomerId.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.control_tree_response_data_customers import ControlTreeResponseDataCustomers

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTreeResponseDataCustomers from a JSON string
control_tree_response_data_customers_instance = ControlTreeResponseDataCustomers.from_json(json)
# print the JSON string representation of the object
print(ControlTreeResponseDataCustomers.to_json())

# convert the object into a dict
control_tree_response_data_customers_dict = control_tree_response_data_customers_instance.to_dict()
# create an instance of ControlTreeResponseDataCustomers from a dict
control_tree_response_data_customers_from_dict = ControlTreeResponseDataCustomers.from_dict(control_tree_response_data_customers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


