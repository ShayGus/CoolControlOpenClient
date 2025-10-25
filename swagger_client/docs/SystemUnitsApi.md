# cool_open_client.client.SystemUnitsApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_system_id_units_get**](SystemUnitsApi.md#systems_system_id_units_get) | **GET** /systems/{systemId}/units | get system units
[**systems_system_id_units_unit_id_delete**](SystemUnitsApi.md#systems_system_id_units_unit_id_delete) | **DELETE** /systems/{systemId}/units/{unitId} | remove unit from system
[**systems_system_id_units_unit_id_post**](SystemUnitsApi.md#systems_system_id_units_unit_id_post) | **POST** /systems/{systemId}/units/{unitId} | add unit to system


# **systems_system_id_units_get**
> UnitsResponse systems_system_id_units_get(origin, referer, x_access_token, system_id)

get system units

get system units

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.units_response import UnitsResponse
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
    api_instance = cool_open_client.client.SystemUnitsApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    system_id = 'system_id_example' # str | 

    try:
        # get system units
        api_response = await api_instance.systems_system_id_units_get(origin, referer, x_access_token, system_id)
        print("The response of SystemUnitsApi->systems_system_id_units_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemUnitsApi->systems_system_id_units_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 

### Return type

[**UnitsResponse**](UnitsResponse.md)

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

# **systems_system_id_units_unit_id_delete**
> Okresponse systems_system_id_units_unit_id_delete(origin, referer, x_access_token, system_id, unit_id)

remove unit from system

remove unit from system

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
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
    api_instance = cool_open_client.client.SystemUnitsApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    system_id = 'system_id_example' # str | 
    unit_id = 'unit_id_example' # str | 

    try:
        # remove unit from system
        api_response = await api_instance.systems_system_id_units_unit_id_delete(origin, referer, x_access_token, system_id, unit_id)
        print("The response of SystemUnitsApi->systems_system_id_units_unit_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemUnitsApi->systems_system_id_units_unit_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_system_id_units_unit_id_post**
> Okresponse systems_system_id_units_unit_id_post(origin, referer, x_access_token, system_id, unit_id)

add unit to system

add unit to system

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
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
    api_instance = cool_open_client.client.SystemUnitsApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    system_id = 'system_id_example' # str | 
    unit_id = 'unit_id_example' # str | 

    try:
        # add unit to system
        api_response = await api_instance.systems_system_id_units_unit_id_post(origin, referer, x_access_token, system_id, unit_id)
        print("The response of SystemUnitsApi->systems_system_id_units_unit_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemUnitsApi->systems_system_id_units_unit_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
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

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

