# CreateZoneRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | zone name | 
**description** | **str** | zone description | [optional] 

## Example

```python
from cool_open_client.client.models.create_zone_request_body import CreateZoneRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateZoneRequestBody from a JSON string
create_zone_request_body_instance = CreateZoneRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateZoneRequestBody.to_json())

# convert the object into a dict
create_zone_request_body_dict = create_zone_request_body_instance.to_dict()
# create an instance of CreateZoneRequestBody from a dict
create_zone_request_body_from_dict = CreateZoneRequestBody.from_dict(create_zone_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


