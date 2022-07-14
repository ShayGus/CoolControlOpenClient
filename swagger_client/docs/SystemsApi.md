# cool_open_client.client.SystemsApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_get**](SystemsApi.md#systems_get) | **GET** /systems | get my systems

# **systems_get**
> SystemsResponse systems_get(x_access_token)

get my systems

get my systems

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemsApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my systems
    api_response = api_instance.systems_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->systems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**SystemsResponse**](SystemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

