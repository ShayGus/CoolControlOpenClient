# ZoneControlSwitchesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **int** | requested operation status from the operation status enumeration | 

## Example

```python
from cool_open_client.client.models.zone_control_switches_body import ZoneControlSwitchesBody

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneControlSwitchesBody from a JSON string
zone_control_switches_body_instance = ZoneControlSwitchesBody.from_json(json)
# print the JSON string representation of the object
print(ZoneControlSwitchesBody.to_json())

# convert the object into a dict
zone_control_switches_body_dict = zone_control_switches_body_instance.to_dict()
# create an instance of ZoneControlSwitchesBody from a dict
zone_control_switches_body_from_dict = ZoneControlSwitchesBody.from_dict(zone_control_switches_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


