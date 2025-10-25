# ZoneControlModesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | requested operation mode from the operation modes enumeration | 

## Example

```python
from cool_open_client.client.models.zone_control_modes_body import ZoneControlModesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneControlModesBody from a JSON string
zone_control_modes_body_instance = ZoneControlModesBody.from_json(json)
# print the JSON string representation of the object
print(ZoneControlModesBody.to_json())

# convert the object into a dict
zone_control_modes_body_dict = zone_control_modes_body_instance.to_dict()
# create an instance of ZoneControlModesBody from a dict
zone_control_modes_body_from_dict = ZoneControlModesBody.from_dict(zone_control_modes_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


