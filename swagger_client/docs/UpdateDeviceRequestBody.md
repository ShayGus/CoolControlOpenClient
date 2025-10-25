# UpdateDeviceRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | device name | [optional] 

## Example

```python
from cool_open_client.client.models.update_device_request_body import UpdateDeviceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeviceRequestBody from a JSON string
update_device_request_body_instance = UpdateDeviceRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateDeviceRequestBody.to_json())

# convert the object into a dict
update_device_request_body_dict = update_device_request_body_instance.to_dict()
# create an instance of UpdateDeviceRequestBody from a dict
update_device_request_body_from_dict = UpdateDeviceRequestBody.from_dict(update_device_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


