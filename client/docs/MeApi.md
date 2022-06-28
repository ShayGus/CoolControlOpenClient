# swagger_client.MeApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**me_get**](MeApi.md#me_get) | **GET** /me | get me
[**me_tree_get**](MeApi.md#me_tree_get) | **GET** /me/tree | get my control tree

# **me_get**
> UserResponse me_get(x_access_token)

get me

get me

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get me
    api_response = api_instance.me_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->me_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **me_tree_get**
> ControlTreeResponse me_tree_get(x_access_token)

get my control tree

get my control tree

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my control tree
    api_response = api_instance.me_tree_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->me_tree_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**ControlTreeResponse**](ControlTreeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

