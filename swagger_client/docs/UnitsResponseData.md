# UnitsResponseData

dictionary of units

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit_id** | [**UnitResponseData**](UnitResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.units_response_data import UnitsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UnitsResponseData from a JSON string
units_response_data_instance = UnitsResponseData.from_json(json)
# print the JSON string representation of the object
print(UnitsResponseData.to_json())

# convert the object into a dict
units_response_data_dict = units_response_data_instance.to_dict()
# create an instance of UnitsResponseData from a dict
units_response_data_from_dict = UnitsResponseData.from_dict(units_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


