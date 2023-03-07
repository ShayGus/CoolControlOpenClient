# cool_open_client.client.SystemApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_system_id_delete**](SystemApi.md#systems_system_id_delete) | **DELETE** /systems/{systemId} | delete system
[**systems_system_id_get**](SystemApi.md#systems_system_id_get) | **GET** /systems/{systemId} | get system
[**systems_system_id_put**](SystemApi.md#systems_system_id_put) | **PUT** /systems/{systemId} | update system

# **systems_system_id_delete**
> Okresponse systems_system_id_delete(origin, referer, x_access_token, system_id)

delete system

delete system

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemApi()
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # delete system
    api_response = api_instance.systems_system_id_delete(origin, referer, x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->systems_system_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_get**
> SystemResponse systems_system_id_get(origin, referer, x_access_token, system_id)

get system

get system

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemApi()
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # get system
    api_response = api_instance.systems_system_id_get(origin, referer, x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->systems_system_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 

### Return type

[**SystemResponse**](SystemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_put**
> Okresponse systems_system_id_put(body, origin, referer, x_access_token, system_id)

update system

update system

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemApi()
body = cool_open_client.client.UpdateSystemRequestBody() # UpdateSystemRequestBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # update system
    api_response = api_instance.systems_system_id_put(body, origin, referer, x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->systems_system_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSystemRequestBody**](UpdateSystemRequestBody.md)|  | 
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

