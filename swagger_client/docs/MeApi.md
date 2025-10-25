# cool_open_client.client.MeApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_me_get**](MeApi.md#users_me_get) | **GET** /users/me | get me
[**users_me_tree_get**](MeApi.md#users_me_tree_get) | **GET** /users/me/tree | get my control tree


# **users_me_get**
> UserResponse users_me_get(origin, referer, x_access_token)

get me

get me

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.user_response import UserResponse
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
    api_instance = cool_open_client.client.MeApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token

    try:
        # get me
        api_response = await api_instance.users_me_get(origin, referer, x_access_token)
        print("The response of MeApi->users_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->users_me_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 

### Return type

[**UserResponse**](UserResponse.md)

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
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me_tree_get**
> ControlTreeResponse users_me_tree_get(origin, referer, x_access_token)

get my control tree

get my control tree

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.control_tree_response import ControlTreeResponse
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
    api_instance = cool_open_client.client.MeApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token

    try:
        # get my control tree
        api_response = await api_instance.users_me_tree_get(origin, referer, x_access_token)
        print("The response of MeApi->users_me_tree_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->users_me_tree_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 

### Return type

[**ControlTreeResponse**](ControlTreeResponse.md)

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
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

