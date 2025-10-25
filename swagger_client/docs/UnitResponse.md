# UnitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**UnitResponseData**](UnitResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.unit_response import UnitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnitResponse from a JSON string
unit_response_instance = UnitResponse.from_json(json)
# print the JSON string representation of the object
print(UnitResponse.to_json())

# convert the object into a dict
unit_response_dict = unit_response_instance.to_dict()
# create an instance of UnitResponse from a dict
unit_response_from_dict = UnitResponse.from_dict(unit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


