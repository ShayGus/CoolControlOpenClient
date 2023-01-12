# cool_open_client.client.CustomerUsersApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_users_get**](CustomerUsersApi.md#customers_customer_id_users_get) | **GET** /customers/{customerId}/users | get customer users
[**customers_customer_id_users_post**](CustomerUsersApi.md#customers_customer_id_users_post) | **POST** /customers/{customerId}/users | create customer user

# **customers_customer_id_users_get**
> UsersResponse customers_customer_id_users_get(x_access_token, customer_id)

get customer users

get customer users

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerUsersApi()
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | 

try:
    # get customer users
    api_response = api_instance.customers_customer_id_users_get(x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerUsersApi->customers_customer_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**|  | 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_users_post**
> OkresponseWithId customers_customer_id_users_post(body, x_access_token, customer_id)

create customer user

create customer user

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerUsersApi()
body = cool_open_client.client.CreateUserRequestBody() # CreateUserRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | 

try:
    # create customer user
    api_response = api_instance.customers_customer_id_users_post(body, x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerUsersApi->customers_customer_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequestBody**](CreateUserRequestBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**|  | 

### Return type

[**OkresponseWithId**](OkresponseWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

