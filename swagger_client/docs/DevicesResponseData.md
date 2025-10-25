# DevicesResponseData

dictionary of devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | [**DeviceResponseData**](DeviceResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.devices_response_data import DevicesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesResponseData from a JSON string
devices_response_data_instance = DevicesResponseData.from_json(json)
# print the JSON string representation of the object
print(DevicesResponseData.to_json())

# convert the object into a dict
devices_response_data_dict = devices_response_data_instance.to_dict()
# create an instance of DevicesResponseData from a dict
devices_response_data_from_dict = DevicesResponseData.from_dict(devices_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


