# ZoneControlFansBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | requested fan mode from the fan modes enumeration | 

## Example

```python
from cool_open_client.client.models.zone_control_fans_body import ZoneControlFansBody

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneControlFansBody from a JSON string
zone_control_fans_body_instance = ZoneControlFansBody.from_json(json)
# print the JSON string representation of the object
print(ZoneControlFansBody.to_json())

# convert the object into a dict
zone_control_fans_body_dict = zone_control_fans_body_instance.to_dict()
# create an instance of ZoneControlFansBody from a dict
zone_control_fans_body_from_dict = ZoneControlFansBody.from_dict(zone_control_fans_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


