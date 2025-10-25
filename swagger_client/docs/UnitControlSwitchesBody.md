# UnitControlSwitchesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_status** | **int** | requested operation status from the operation status enumeration | 

## Example

```python
from cool_open_client.client.models.unit_control_switches_body import UnitControlSwitchesBody

# TODO update the JSON string below
json = "{}"
# create an instance of UnitControlSwitchesBody from a JSON string
unit_control_switches_body_instance = UnitControlSwitchesBody.from_json(json)
# print the JSON string representation of the object
print(UnitControlSwitchesBody.to_json())

# convert the object into a dict
unit_control_switches_body_dict = unit_control_switches_body_instance.to_dict()
# create an instance of UnitControlSwitchesBody from a dict
unit_control_switches_body_from_dict = UnitControlSwitchesBody.from_dict(unit_control_switches_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


