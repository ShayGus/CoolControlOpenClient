# swagger_client.SystemUnitsApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_system_id_units_get**](SystemUnitsApi.md#systems_system_id_units_get) | **GET** /systems/{systemId}/units | get system units
[**systems_system_id_units_unit_id_delete**](SystemUnitsApi.md#systems_system_id_units_unit_id_delete) | **DELETE** /systems/{systemId}/units/{unitId} | remove unit from system
[**systems_system_id_units_unit_id_post**](SystemUnitsApi.md#systems_system_id_units_unit_id_post) | **POST** /systems/{systemId}/units/{unitId} | add unit to system

# **systems_system_id_units_get**
> UnitsResponse systems_system_id_units_get(x_access_token, system_id)

get system units

get system units

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # get system units
    api_response = api_instance.systems_system_id_units_get(x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemUnitsApi->systems_system_id_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 

### Return type

[**UnitsResponse**](UnitsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_units_unit_id_delete**
> Okresponse systems_system_id_units_unit_id_delete(x_access_token, system_id, unit_id)

remove unit from system

remove unit from system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 
unit_id = 'unit_id_example' # str | 

try:
    # remove unit from system
    api_response = api_instance.systems_system_id_units_unit_id_delete(x_access_token, system_id, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemUnitsApi->systems_system_id_units_unit_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 
 **unit_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_units_unit_id_post**
> Okresponse systems_system_id_units_unit_id_post(x_access_token, system_id, unit_id)

add unit to system

add unit to system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 
unit_id = 'unit_id_example' # str | 

try:
    # add unit to system
    api_response = api_instance.systems_system_id_units_unit_id_post(x_access_token, system_id, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemUnitsApi->systems_system_id_units_unit_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 
 **unit_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

