# cool_open_client.client.SitesApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_get**](SitesApi.md#sites_get) | **GET** /sites | get my sites

# **sites_get**
> SitesResponse sites_get(x_access_token)

get my sites

get my sites

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SitesApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my sites
    api_response = api_instance.sites_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->sites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**SitesResponse**](SitesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

