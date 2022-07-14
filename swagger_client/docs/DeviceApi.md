# cool_open_client.client.DeviceApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_device_id_delete**](DeviceApi.md#devices_device_id_delete) | **DELETE** /devices/{deviceId} | delete device
[**devices_device_id_get**](DeviceApi.md#devices_device_id_get) | **GET** /devices/{deviceId} | get device
[**devices_device_id_put**](DeviceApi.md#devices_device_id_put) | **PUT** /devices/{deviceId} | update device

# **devices_device_id_delete**
> Okresponse devices_device_id_delete(x_access_token, device_id)

delete device

delete device

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.DeviceApi()
x_access_token = 'x_access_token_example' # str | access token
device_id = 'device_id_example' # str | 

try:
    # delete device
    api_response = api_instance.devices_device_id_delete(x_access_token, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_device_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **device_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_device_id_get**
> DeviceResponse devices_device_id_get(x_access_token, device_id)

get device

get device

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.DeviceApi()
x_access_token = 'x_access_token_example' # str | access token
device_id = 'device_id_example' # str | 

try:
    # get device
    api_response = api_instance.devices_device_id_get(x_access_token, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_device_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **device_id** | **str**|  | 

### Return type

[**DeviceResponse**](DeviceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_device_id_put**
> Okresponse devices_device_id_put(body, x_access_token, device_id)

update device

update device

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.DeviceApi()
body = cool_open_client.client.UpdateDeviceRequestBody() # UpdateDeviceRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
device_id = 'device_id_example' # str | 

try:
    # update device
    api_response = api_instance.devices_device_id_put(body, x_access_token, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->devices_device_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateDeviceRequestBody**](UpdateDeviceRequestBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **device_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

