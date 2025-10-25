# ZoneResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**ZoneResponseData**](ZoneResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.zone_response import ZoneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneResponse from a JSON string
zone_response_instance = ZoneResponse.from_json(json)
# print the JSON string representation of the object
print(ZoneResponse.to_json())

# convert the object into a dict
zone_response_dict = zone_response_instance.to_dict()
# create an instance of ZoneResponse from a dict
zone_response_from_dict = ZoneResponse.from_dict(zone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


