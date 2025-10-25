# UnitsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**UnitsResponseData**](UnitsResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.units_response import UnitsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnitsResponse from a JSON string
units_response_instance = UnitsResponse.from_json(json)
# print the JSON string representation of the object
print(UnitsResponse.to_json())

# convert the object into a dict
units_response_dict = units_response_instance.to_dict()
# create an instance of UnitsResponse from a dict
units_response_from_dict = UnitsResponse.from_dict(units_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


