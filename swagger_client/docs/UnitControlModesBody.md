# UnitControlModesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_mode** | **int** | requested operation mode from the operation modes enumeration | 

## Example

```python
from cool_open_client.client.models.unit_control_modes_body import UnitControlModesBody

# TODO update the JSON string below
json = "{}"
# create an instance of UnitControlModesBody from a JSON string
unit_control_modes_body_instance = UnitControlModesBody.from_json(json)
# print the JSON string representation of the object
print(UnitControlModesBody.to_json())

# convert the object into a dict
unit_control_modes_body_dict = unit_control_modes_body_instance.to_dict()
# create an instance of UnitControlModesBody from a dict
unit_control_modes_body_from_dict = UnitControlModesBody.from_dict(unit_control_modes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


