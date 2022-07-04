# swagger_client.DeviceUnitsApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_device_id_units_get**](DeviceUnitsApi.md#devices_device_id_units_get) | **GET** /devices/{deviceId}/units | get device units

# **devices_device_id_units_get**
> UnitsResponse devices_device_id_units_get(x_access_token, device_id)

get device units

get device units

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
device_id = 'device_id_example' # str | 

try:
    # get device units
    api_response = api_instance.devices_device_id_units_get(x_access_token, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceUnitsApi->devices_device_id_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **device_id** | **str**|  | 

### Return type

[**UnitsResponse**](UnitsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
