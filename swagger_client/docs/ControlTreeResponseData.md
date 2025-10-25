# ControlTreeResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customers** | [**ControlTreeResponseDataCustomers**](ControlTreeResponseDataCustomers.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.control_tree_response_data import ControlTreeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTreeResponseData from a JSON string
control_tree_response_data_instance = ControlTreeResponseData.from_json(json)
# print the JSON string representation of the object
print(ControlTreeResponseData.to_json())

# convert the object into a dict
control_tree_response_data_dict = control_tree_response_data_instance.to_dict()
# create an instance of ControlTreeResponseData from a dict
control_tree_response_data_from_dict = ControlTreeResponseData.from_dict(control_tree_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


