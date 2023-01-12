# cool_open_client.client.CustomersApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_get**](CustomersApi.md#customers_get) | **GET** /customers | get my customers

# **customers_get**
> CustomersResponse customers_get(x_access_token)

get my customers

Get all the customers caller has permissions to see

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomersApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # get my customers
    api_response = api_instance.customers_get(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->customers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**CustomersResponse**](CustomersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

