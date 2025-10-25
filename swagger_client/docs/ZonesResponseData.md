# ZonesResponseData

dictionary of zones

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_id** | [**ZoneResponseData**](ZoneResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.zones_response_data import ZonesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ZonesResponseData from a JSON string
zones_response_data_instance = ZonesResponseData.from_json(json)
# print the JSON string representation of the object
print(ZonesResponseData.to_json())

# convert the object into a dict
zones_response_data_dict = zones_response_data_instance.to_dict()
# create an instance of ZonesResponseData from a dict
zones_response_data_from_dict = ZonesResponseData.from_dict(zones_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


