# cool_open_client.client.AuthenticationApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_authenticate_post**](AuthenticationApi.md#users_authenticate_post) | **POST** /users/authenticate | authenticate

# **users_authenticate_post**
> OkresponseWithToken users_authenticate_post(body)

authenticate

get access token

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.AuthenticationApi()
body = cool_open_client.client.AuthenticateRequestBody() # AuthenticateRequestBody | 

try:
    # authenticate
    api_response = api_instance.users_authenticate_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->users_authenticate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthenticateRequestBody**](AuthenticateRequestBody.md)|  | 

### Return type

[**OkresponseWithToken**](OkresponseWithToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

