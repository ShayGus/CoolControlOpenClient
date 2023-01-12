# cool_open_client.client.MeApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_me_get**](MeApi.md#users_me_get) | **GET** /users/me | get me
[**users_me_tree_get**](MeApi.md#users_me_tree_get) | **GET** /users/me/tree | get my control tree

# **users_me_get**
> UserResponse users_me_get(x_access_token)

get me

get me

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.MeApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get me
    api_response = api_instance.users_me_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_get: %s\n" % e)
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

# **users_me_tree_get**
> ControlTreeResponse users_me_tree_get(x_access_token)

get my control tree

get my control tree

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.MeApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my control tree
    api_response = api_instance.users_me_tree_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->users_me_tree_get: %s\n" % e)
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

