# UpdateSystemRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | system name | [optional] 
**description** | **str** | system description | [optional] 

## Example

```python
from cool_open_client.client.models.update_system_request_body import UpdateSystemRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSystemRequestBody from a JSON string
update_system_request_body_instance = UpdateSystemRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateSystemRequestBody.to_json())

# convert the object into a dict
update_system_request_body_dict = update_system_request_body_instance.to_dict()
# create an instance of UpdateSystemRequestBody from a dict
update_system_request_body_from_dict = UpdateSystemRequestBody.from_dict(update_system_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


