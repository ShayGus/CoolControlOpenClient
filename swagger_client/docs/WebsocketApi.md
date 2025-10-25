# cool_open_client.client.WebsocketApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ws_v2_get**](WebsocketApi.md#ws_v2_get) | **GET** /ws/v2 | Websocket connection endpoint


# **ws_v2_get**
> ws_v2_get()

Websocket connection endpoint

Websocket connection endpoint

### Example


```python
import cool_open_client.client
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
    api_instance = cool_open_client.client.WebsocketApi(api_client)

    try:
        # Websocket connection endpoint
        await api_instance.ws_v2_get()
    except Exception as e:
        print("Exception when calling WebsocketApi->ws_v2_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

