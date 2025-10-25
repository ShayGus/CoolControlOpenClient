# cool_open_client.client.AuthenticationApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_authenticate_post**](AuthenticationApi.md#users_authenticate_post) | **POST** /users/authenticate | authenticate


# **users_authenticate_post**
> OkresponseWithToken users_authenticate_post(authenticate_request_body)

authenticate

get access token

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.authenticate_request_body import AuthenticateRequestBody
from cool_open_client.client.models.okresponse_with_token import OkresponseWithToken
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
    api_instance = cool_open_client.client.AuthenticationApi(api_client)
    authenticate_request_body = cool_open_client.client.AuthenticateRequestBody() # AuthenticateRequestBody | 

    try:
        # authenticate
        api_response = await api_instance.users_authenticate_post(authenticate_request_body)
        print("The response of AuthenticationApi->users_authenticate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->users_authenticate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticate_request_body** | [**AuthenticateRequestBody**](AuthenticateRequestBody.md)|  | 

### Return type

[**OkresponseWithToken**](OkresponseWithToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | parameter error |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

