# UnitControlFansBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fan_mode** | **int** | requested fan mode from the fan modes enumeration | 

## Example

```python
from cool_open_client.client.models.unit_control_fans_body import UnitControlFansBody

# TODO update the JSON string below
json = "{}"
# create an instance of UnitControlFansBody from a JSON string
unit_control_fans_body_instance = UnitControlFansBody.from_json(json)
# print the JSON string representation of the object
print(UnitControlFansBody.to_json())

# convert the object into a dict
unit_control_fans_body_dict = unit_control_fans_body_instance.to_dict()
# create an instance of UnitControlFansBody from a dict
unit_control_fans_body_from_dict = UnitControlFansBody.from_dict(unit_control_fans_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


