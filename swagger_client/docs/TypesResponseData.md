# TypesResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temperature_scale** | [**TypesResponseDataTemperatureScale**](TypesResponseDataTemperatureScale.md) |  | [optional] 
**operation_statuses** | [**TypesResponseDataOperationStatuses**](TypesResponseDataOperationStatuses.md) |  | [optional] 
**operation_modes** | [**TypesResponseDataOperationModes**](TypesResponseDataOperationModes.md) |  | [optional] 
**fan_modes** | [**TypesResponseDataFanModes**](TypesResponseDataFanModes.md) |  | [optional] 
**swing_modes** | [**TypesResponseDataSwingModes**](TypesResponseDataSwingModes.md) |  | [optional] 
**week_days** | [**TypesResponseDataWeekDays**](TypesResponseDataWeekDays.md) |  | [optional] 
**permissions** | [**TypesResponseDataPermissions**](TypesResponseDataPermissions.md) |  | [optional] 
**resources** | [**TypesResponseDataResources**](TypesResponseDataResources.md) |  | [optional] 
**roles** | [**TypesResponseDataRoles**](TypesResponseDataRoles.md) |  | [optional] 
**unit_types** | [**TypesResponseDataUnitTypes**](TypesResponseDataUnitTypes.md) |  | [optional] 
**hvac_brands** | [**List[TypesResponseDataHvacBrandsInner]**](TypesResponseDataHvacBrandsInner.md) | array of hvac brands | [optional] 
**device_types** | [**TypesResponseDataDeviceTypes**](TypesResponseDataDeviceTypes.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data import TypesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseData from a JSON string
types_response_data_instance = TypesResponseData.from_json(json)
# print the JSON string representation of the object
print(TypesResponseData.to_json())

# convert the object into a dict
types_response_data_dict = types_response_data_instance.to_dict()
# create an instance of TypesResponseData from a dict
types_response_data_from_dict = TypesResponseData.from_dict(types_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


