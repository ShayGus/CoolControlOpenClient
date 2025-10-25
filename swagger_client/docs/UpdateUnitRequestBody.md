# UpdateUnitRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | unit name | [optional] 
**type** | **int** | unit type from the unit type enumeration | [optional] 
**supported_switch_modes** | **List[int]** | operation status the unit supports - array of integers from the operation status enumeration | [optional] 
**supported_modes** | **List[int]** | operation modes the unit supports - array of integers from the operation modes enumeration | [optional] 
**supported_fan_modes** | **List[int]** | fan modes the unit supports - array of integers from the fan modes enumeration | [optional] 
**supported_swing_modes** | **List[int]** | swing modes the unit supports - array of integers from the swing modes enumeration | [optional] 
**temperature_limits** | **object** | TBD | [optional] 

## Example

```python
from cool_open_client.client.models.update_unit_request_body import UpdateUnitRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUnitRequestBody from a JSON string
update_unit_request_body_instance = UpdateUnitRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUnitRequestBody.to_json())

# convert the object into a dict
update_unit_request_body_dict = update_unit_request_body_instance.to_dict()
# create an instance of UpdateUnitRequestBody from a dict
update_unit_request_body_from_dict = UpdateUnitRequestBody.from_dict(update_unit_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


