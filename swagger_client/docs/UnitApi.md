# cool_open_client.client.UnitApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_unit_id_get**](UnitApi.md#units_unit_id_get) | **GET** /units/{unitId} | get unit
[**units_unit_id_put**](UnitApi.md#units_unit_id_put) | **PUT** /units/{unitId} | update unit

# **units_unit_id_get**
> UnitResponse units_unit_id_get(origin, referer, x_access_token, unit_id)

get unit

get unit

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitApi()
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # get unit
    api_response = api_instance.units_unit_id_get(origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_unit_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 

### Return type

[**UnitResponse**](UnitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **units_unit_id_put**
> Okresponse units_unit_id_put(body, origin, referer, x_access_token, unit_id)

update unit

update unit

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitApi()
body = cool_open_client.client.UpdateUnitRequestBody() # UpdateUnitRequestBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # update unit
    api_response = api_instance.units_unit_id_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitApi->units_unit_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateUnitRequestBody**](UpdateUnitRequestBody.md)|  | 
 **origin** | **str**|  | [default to https://control.coolremote.net]
 **referer** | **str**|  | [default to https://control.coolremote.net/]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

