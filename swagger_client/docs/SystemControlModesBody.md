# SystemControlModesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | requested operation mode from the operation modes enumeration | 

## Example

```python
from cool_open_client.client.models.system_control_modes_body import SystemControlModesBody

# TODO update the JSON string below
json = "{}"
# create an instance of SystemControlModesBody from a JSON string
system_control_modes_body_instance = SystemControlModesBody.from_json(json)
# print the JSON string representation of the object
print(SystemControlModesBody.to_json())

# convert the object into a dict
system_control_modes_body_dict = system_control_modes_body_instance.to_dict()
# create an instance of SystemControlModesBody from a dict
system_control_modes_body_from_dict = SystemControlModesBody.from_dict(system_control_modes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


