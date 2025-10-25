# UnitControlSwingsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**swing_mode** | **int** | requested operation status from the swing mode enumeration | 

## Example

```python
from cool_open_client.client.models.unit_control_swings_body import UnitControlSwingsBody

# TODO update the JSON string below
json = "{}"
# create an instance of UnitControlSwingsBody from a JSON string
unit_control_swings_body_instance = UnitControlSwingsBody.from_json(json)
# print the JSON string representation of the object
print(UnitControlSwingsBody.to_json())

# convert the object into a dict
unit_control_swings_body_dict = unit_control_swings_body_instance.to_dict()
# create an instance of UnitControlSwingsBody from a dict
unit_control_swings_body_from_dict = UnitControlSwingsBody.from_dict(unit_control_swings_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


