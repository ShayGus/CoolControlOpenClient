# UpdateZoneRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | zone name | [optional] 
**description** | **str** | zone description | [optional] 

## Example

```python
from cool_open_client.client.models.update_zone_request_body import UpdateZoneRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateZoneRequestBody from a JSON string
update_zone_request_body_instance = UpdateZoneRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateZoneRequestBody.to_json())

# convert the object into a dict
update_zone_request_body_dict = update_zone_request_body_instance.to_dict()
# create an instance of UpdateZoneRequestBody from a dict
update_zone_request_body_from_dict = UpdateZoneRequestBody.from_dict(update_zone_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


