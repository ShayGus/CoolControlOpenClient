# TypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**TypesResponseData**](TypesResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.types_response import TypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponse from a JSON string
types_response_instance = TypesResponse.from_json(json)
# print the JSON string representation of the object
print(TypesResponse.to_json())

# convert the object into a dict
types_response_dict = types_response_instance.to_dict()
# create an instance of TypesResponse from a dict
types_response_from_dict = TypesResponse.from_dict(types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


