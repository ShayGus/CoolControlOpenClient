# swagger_client.AdminsApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admins_customers_post**](AdminsApi.md#admins_customers_post) | **POST** /admins/customers | create customer

# **admins_customers_post**
> CustomerResponse admins_customers_post(x_access_token)

create customer

Create customer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AdminsApi()
x_access_token = 'x_access_token_example' # str | access token

try:
    # create customer
    api_response = api_instance.admins_customers_post(x_access_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsApi->admins_customers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

