# cool_open_client.client.DevicesApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices_get**](DevicesApi.md#devices_get) | **GET** /devices | get my devices

# **devices_get**
> DevicesResponse devices_get(origin, referer, x_access_token)

get my devices

get my devices

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.DevicesApi()
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my devices
    api_response = api_instance.devices_get(origin, referer, x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

