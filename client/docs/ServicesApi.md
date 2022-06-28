# swagger_client.ServicesApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_types_get**](ServicesApi.md#services_types_get) | **GET** /services/types | get system types for enumerations used in protocol

# **services_types_get**
> TypesResponse services_types_get(x_access_token)

get system types for enumerations used in protocol

get system types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get system types for enumerations used in protocol
    api_response = api_instance.services_types_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_types_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**TypesResponse**](TypesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

