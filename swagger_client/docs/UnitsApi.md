# cool_open_client.client.UnitsApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_get**](UnitsApi.md#units_get) | **GET** /units | get my units

# **units_get**
> UnitsResponse units_get(origin, referer, x_access_token)

get my units

get my units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitsApi()
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my units
    api_response = api_instance.units_get(origin, referer, x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitsApi->units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 

### Return type

[**UnitsResponse**](UnitsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

