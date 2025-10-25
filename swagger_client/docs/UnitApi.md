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
import cool_open_client.client
from cool_open_client.client.models.unit_response import UnitResponse
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
    api_instance = cool_open_client.client.UnitApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 

    try:
        # get unit
        api_response = await api_instance.units_unit_id_get(origin, referer, x_access_token, unit_id)
        print("The response of UnitApi->units_unit_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitApi->units_unit_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 

### Return type

[**UnitResponse**](UnitResponse.md)

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

# **units_unit_id_put**
> Okresponse units_unit_id_put(origin, referer, x_access_token, unit_id, update_unit_request_body)

update unit

update unit

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.update_unit_request_body import UpdateUnitRequestBody
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
    api_instance = cool_open_client.client.UnitApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    update_unit_request_body = cool_open_client.client.UpdateUnitRequestBody() # UpdateUnitRequestBody | 

    try:
        # update unit
        api_response = await api_instance.units_unit_id_put(origin, referer, x_access_token, unit_id, update_unit_request_body)
        print("The response of UnitApi->units_unit_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitApi->units_unit_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **update_unit_request_body** | [**UpdateUnitRequestBody**](UpdateUnitRequestBody.md)|  | 

### Return type

[**Okresponse**](Okresponse.md)

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

