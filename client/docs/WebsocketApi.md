# swagger_client.WebsocketApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_get**](WebsocketApi.md#root_get) | **GET** / | Websocket connection endpoint

# **root_get**
> root_get()

Websocket connection endpoint

Websocket connection endpoint

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsocketApi()

try:
    # Websocket connection endpoint
    api_instance.root_get()
except ApiException as e:
    print("Exception when calling WebsocketApi->root_get: %s\n" % e)
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

