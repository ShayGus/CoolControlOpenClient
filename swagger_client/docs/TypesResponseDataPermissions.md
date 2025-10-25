# TypesResponseDataPermissions

map of permission names used in permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permission** | **str** | permission name | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_permissions import TypesResponseDataPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataPermissions from a JSON string
types_response_data_permissions_instance = TypesResponseDataPermissions.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataPermissions.to_json())

# convert the object into a dict
types_response_data_permissions_dict = types_response_data_permissions_instance.to_dict()
# create an instance of TypesResponseDataPermissions from a dict
types_response_data_permissions_from_dict = TypesResponseDataPermissions.from_dict(types_response_data_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


