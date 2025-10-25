# ControlTreeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**ControlTreeResponseData**](ControlTreeResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.control_tree_response import ControlTreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTreeResponse from a JSON string
control_tree_response_instance = ControlTreeResponse.from_json(json)
# print the JSON string representation of the object
print(ControlTreeResponse.to_json())

# convert the object into a dict
control_tree_response_dict = control_tree_response_instance.to_dict()
# create an instance of ControlTreeResponse from a dict
control_tree_response_from_dict = ControlTreeResponse.from_dict(control_tree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


