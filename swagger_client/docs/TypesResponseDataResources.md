# TypesResponseDataResources

map of resource names used in permissions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | resource name | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_resources import TypesResponseDataResources

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataResources from a JSON string
types_response_data_resources_instance = TypesResponseDataResources.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataResources.to_json())

# convert the object into a dict
types_response_data_resources_dict = types_response_data_resources_instance.to_dict()
# create an instance of TypesResponseDataResources from a dict
types_response_data_resources_from_dict = TypesResponseDataResources.from_dict(types_response_data_resources_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


