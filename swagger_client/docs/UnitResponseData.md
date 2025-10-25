# UnitResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | unit ID | [optional] 
**name** | **str** | system name | [optional] 
**device** | **str** | parent device id | [optional] 
**is_connected** | **bool** | Is unit connected | [optional] 
**supported_operation_statuses** | **List[int]** | Supported operation statuses | [optional] 
**supported_operation_modes** | **List[int]** | Supported operation modes | [optional] 
**supported_fan_modes** | **List[int]** | Supported fan modes | [optional] 
**supported_swing_modes** | **List[int]** | Supported swing modes | [optional] 
**temperature_limits** | [**UnitResponseDataTemperatureLimits**](UnitResponseDataTemperatureLimits.md) |  | [optional] 
**brand** | **int** |  | [optional] 
**active_setpoint** | **int** |  | [optional] 
**ambient_temperature** | **int** |  | [optional] 
**active_operation_status** | **int** |  | [optional] 
**active_operation_mode** | **int** |  | [optional] 
**active_fan_mode** | **int** |  | [optional] 
**active_swing_mode** | **int** |  | [optional] 
**filter** | **bool** |  | [optional] 
**enable_cool_mode** | **bool** |  | [optional] 
**enable_heat_mode** | **bool** |  | [optional] 
**enable_auto_mode** | **bool** |  | [optional] 
**is_half_c_degree_enabled** | **bool** |  | [optional] 

## Example

```python
from cool_open_client.client.models.unit_response_data import UnitResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UnitResponseData from a JSON string
unit_response_data_instance = UnitResponseData.from_json(json)
# print the JSON string representation of the object
print(UnitResponseData.to_json())

# convert the object into a dict
unit_response_data_dict = unit_response_data_instance.to_dict()
# create an instance of UnitResponseData from a dict
unit_response_data_from_dict = UnitResponseData.from_dict(unit_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


