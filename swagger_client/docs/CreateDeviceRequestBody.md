# CreateDeviceRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | device name | [optional] 
**serial** | **str** | serial number of the device | 
**pin** | **str** | device pin | 

## Example

```python
from cool_open_client.client.models.create_device_request_body import CreateDeviceRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceRequestBody from a JSON string
create_device_request_body_instance = CreateDeviceRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateDeviceRequestBody.to_json())

# convert the object into a dict
create_device_request_body_dict = create_device_request_body_instance.to_dict()
# create an instance of CreateDeviceRequestBody from a dict
create_device_request_body_from_dict = CreateDeviceRequestBody.from_dict(create_device_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


