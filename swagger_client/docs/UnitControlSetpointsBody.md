# UnitControlSetpointsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setpoint** | **int** | requested temperature on the same scale the acting user is configured to work with | 

## Example

```python
from cool_open_client.client.models.unit_control_setpoints_body import UnitControlSetpointsBody

# TODO update the JSON string below
json = "{}"
# create an instance of UnitControlSetpointsBody from a JSON string
unit_control_setpoints_body_instance = UnitControlSetpointsBody.from_json(json)
# print the JSON string representation of the object
print(UnitControlSetpointsBody.to_json())

# convert the object into a dict
unit_control_setpoints_body_dict = unit_control_setpoints_body_instance.to_dict()
# create an instance of UnitControlSetpointsBody from a dict
unit_control_setpoints_body_from_dict = UnitControlSetpointsBody.from_dict(unit_control_setpoints_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


