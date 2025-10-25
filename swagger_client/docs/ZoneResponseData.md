# ZoneResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | zone ID | [optional] 
**name** | **str** | zone name | [optional] 
**role** | **object** | caller permissions for this zone | [optional] 
**site** | **str** | parent site id | [optional] 
**units** | **List[str]** | array of child unit IDs | [optional] 

## Example

```python
from cool_open_client.client.models.zone_response_data import ZoneResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneResponseData from a JSON string
zone_response_data_instance = ZoneResponseData.from_json(json)
# print the JSON string representation of the object
print(ZoneResponseData.to_json())

# convert the object into a dict
zone_response_data_dict = zone_response_data_instance.to_dict()
# create an instance of ZoneResponseData from a dict
zone_response_data_from_dict = ZoneResponseData.from_dict(zone_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


