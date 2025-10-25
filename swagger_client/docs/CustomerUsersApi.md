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
import cool_open_client.client
from cool_open_client.client.models.users_response import UsersResponse
from cool_open_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coolremote.net/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cool_open_client.client.Configuration(
    host = "https://api.coolremote.net/api/v2"
)


# Enter a context with an instance of the API client
async with cool_open_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cool_open_client.client.CustomerUsersApi(api_client)
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | 

    try:
        # get customer users
        api_response = await api_instance.customers_customer_id_users_get(x_access_token, customer_id)
        print("The response of CustomerUsersApi->customers_customer_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_users_post**
> OkresponseWithId customers_customer_id_users_post(x_access_token, customer_id, create_user_request_body)

create customer user

create customer user

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.create_user_request_body import CreateUserRequestBody
from cool_open_client.client.models.okresponse_with_id import OkresponseWithId
from cool_open_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coolremote.net/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cool_open_client.client.Configuration(
    host = "https://api.coolremote.net/api/v2"
)


# Enter a context with an instance of the API client
async with cool_open_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cool_open_client.client.CustomerUsersApi(api_client)
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | 
    create_user_request_body = cool_open_client.client.CreateUserRequestBody() # CreateUserRequestBody | 

    try:
        # create customer user
        api_response = await api_instance.customers_customer_id_users_post(x_access_token, customer_id, create_user_request_body)
        print("The response of CustomerUsersApi->customers_customer_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerUsersApi->customers_customer_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**|  | 
 **create_user_request_body** | [**CreateUserRequestBody**](CreateUserRequestBody.md)|  | 

### Return type

[**OkresponseWithId**](OkresponseWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

