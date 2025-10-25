# SystemResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | system ID | [optional] 
**name** | **str** | system name | [optional] 
**role** | **object** | caller permissions for this system | [optional] 
**site** | **str** | parent site id | [optional] 
**units** | **List[str]** | array of child unit IDs | [optional] 

## Example

```python
from cool_open_client.client.models.system_response_data import SystemResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemResponseData from a JSON string
system_response_data_instance = SystemResponseData.from_json(json)
# print the JSON string representation of the object
print(SystemResponseData.to_json())

# convert the object into a dict
system_response_data_dict = system_response_data_instance.to_dict()
# create an instance of SystemResponseData from a dict
system_response_data_from_dict = SystemResponseData.from_dict(system_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


