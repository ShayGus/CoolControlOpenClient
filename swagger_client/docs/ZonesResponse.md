# ZonesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**ZonesResponseData**](ZonesResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.zones_response import ZonesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ZonesResponse from a JSON string
zones_response_instance = ZonesResponse.from_json(json)
# print the JSON string representation of the object
print(ZonesResponse.to_json())

# convert the object into a dict
zones_response_dict = zones_response_instance.to_dict()
# create an instance of ZonesResponse from a dict
zones_response_from_dict = ZonesResponse.from_dict(zones_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


