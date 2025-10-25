# TypesResponseDataDeviceTypesTypeObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | device name | [optional] 
**short_name** | **str** | device short name | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_device_types_type_object import TypesResponseDataDeviceTypesTypeObject

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataDeviceTypesTypeObject from a JSON string
types_response_data_device_types_type_object_instance = TypesResponseDataDeviceTypesTypeObject.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataDeviceTypesTypeObject.to_json())

# convert the object into a dict
types_response_data_device_types_type_object_dict = types_response_data_device_types_type_object_instance.to_dict()
# create an instance of TypesResponseDataDeviceTypesTypeObject from a dict
types_response_data_device_types_type_object_from_dict = TypesResponseDataDeviceTypesTypeObject.from_dict(types_response_data_device_types_type_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


