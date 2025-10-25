# ControlTreeResponseDataCustomersCustomerId

single customer properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | customer name | [optional] 
**id** | **str** | customer id | [optional] 
**role** | **str** | user role for this customer | [optional] 
**sites** | [**ControlTreeResponseDataCustomersCustomerIdSites**](ControlTreeResponseDataCustomersCustomerIdSites.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.control_tree_response_data_customers_customer_id import ControlTreeResponseDataCustomersCustomerId

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTreeResponseDataCustomersCustomerId from a JSON string
control_tree_response_data_customers_customer_id_instance = ControlTreeResponseDataCustomersCustomerId.from_json(json)
# print the JSON string representation of the object
print(ControlTreeResponseDataCustomersCustomerId.to_json())

# convert the object into a dict
control_tree_response_data_customers_customer_id_dict = control_tree_response_data_customers_customer_id_instance.to_dict()
# create an instance of ControlTreeResponseDataCustomersCustomerId from a dict
control_tree_response_data_customers_customer_id_from_dict = ControlTreeResponseDataCustomersCustomerId.from_dict(control_tree_response_data_customers_customer_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


