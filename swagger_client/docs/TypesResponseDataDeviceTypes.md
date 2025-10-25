# TypesResponseDataDeviceTypes

map of type names used in device types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_id** | **str** | type name | [optional] 
**type_object** | [**TypesResponseDataDeviceTypesTypeObject**](TypesResponseDataDeviceTypesTypeObject.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_device_types import TypesResponseDataDeviceTypes

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataDeviceTypes from a JSON string
types_response_data_device_types_instance = TypesResponseDataDeviceTypes.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataDeviceTypes.to_json())

# convert the object into a dict
types_response_data_device_types_dict = types_response_data_device_types_instance.to_dict()
# create an instance of TypesResponseDataDeviceTypes from a dict
types_response_data_device_types_from_dict = TypesResponseDataDeviceTypes.from_dict(types_response_data_device_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


