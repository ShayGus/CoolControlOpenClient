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
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.WebsocketApi()

try:
    # Websocket connection endpoint
    api_instance.ws_v2_get()
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

