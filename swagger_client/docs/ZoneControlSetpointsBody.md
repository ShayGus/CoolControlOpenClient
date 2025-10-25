# ZoneControlSetpointsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setpoint** | **int** | requested temperature on the same scale the acting user is configured to work with | 

## Example

```python
from cool_open_client.client.models.zone_control_setpoints_body import ZoneControlSetpointsBody

# TODO update the JSON string below
json = "{}"
# create an instance of ZoneControlSetpointsBody from a JSON string
zone_control_setpoints_body_instance = ZoneControlSetpointsBody.from_json(json)
# print the JSON string representation of the object
print(ZoneControlSetpointsBody.to_json())

# convert the object into a dict
zone_control_setpoints_body_dict = zone_control_setpoints_body_instance.to_dict()
# create an instance of ZoneControlSetpointsBody from a dict
zone_control_setpoints_body_from_dict = ZoneControlSetpointsBody.from_dict(zone_control_setpoints_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


