# DeviceResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | device ID | [optional] 
**serial** | **str** | device serial number | [optional] 
**role** | **object** | caller permissions for this device | [optional] 
**site** | **str** | parent site id | [optional] 
**units** | **List[str]** | array of child unit IDs | [optional] 
**is_connected** | **bool** | defines whether device connected | [optional] 

## Example

```python
from cool_open_client.client.models.device_response_data import DeviceResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceResponseData from a JSON string
device_response_data_instance = DeviceResponseData.from_json(json)
# print the JSON string representation of the object
print(DeviceResponseData.to_json())

# convert the object into a dict
device_response_data_dict = device_response_data_instance.to_dict()
# create an instance of DeviceResponseData from a dict
device_response_data_from_dict = DeviceResponseData.from_dict(device_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


