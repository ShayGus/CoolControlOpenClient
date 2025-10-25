# SystemControlSwitchesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | requested operation status from the operation status enumeration | 

## Example

```python
from cool_open_client.client.models.system_control_switches_body import SystemControlSwitchesBody

# TODO update the JSON string below
json = "{}"
# create an instance of SystemControlSwitchesBody from a JSON string
system_control_switches_body_instance = SystemControlSwitchesBody.from_json(json)
# print the JSON string representation of the object
print(SystemControlSwitchesBody.to_json())

# convert the object into a dict
system_control_switches_body_dict = system_control_switches_body_instance.to_dict()
# create an instance of SystemControlSwitchesBody from a dict
system_control_switches_body_from_dict = SystemControlSwitchesBody.from_dict(system_control_switches_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


