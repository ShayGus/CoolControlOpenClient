# cool_open_client.client.UnitControlApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_unit_id_controls_fan_modes_put**](UnitControlApi.md#units_unit_id_controls_fan_modes_put) | **PUT** /units/{unitId}/controls/fan-modes | set unit fan mode
[**units_unit_id_controls_operation_modes_put**](UnitControlApi.md#units_unit_id_controls_operation_modes_put) | **PUT** /units/{unitId}/controls/operation-modes | set unit operation mode
[**units_unit_id_controls_operation_statuses_put**](UnitControlApi.md#units_unit_id_controls_operation_statuses_put) | **PUT** /units/{unitId}/controls/operation-statuses | set unit operation status
[**units_unit_id_controls_setpoints_put**](UnitControlApi.md#units_unit_id_controls_setpoints_put) | **PUT** /units/{unitId}/controls/setpoints | set unit temperature setpoint
[**units_unit_id_controls_swing_modes_put**](UnitControlApi.md#units_unit_id_controls_swing_modes_put) | **PUT** /units/{unitId}/controls/swing-modes | set unit louver mode


# **units_unit_id_controls_fan_modes_put**
> Okresponse units_unit_id_controls_fan_modes_put(origin, referer, x_access_token, unit_id, unit_control_fans_body)

set unit fan mode

set unit fan mode

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.unit_control_fans_body import UnitControlFansBody
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
    api_instance = cool_open_client.client.UnitControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    unit_control_fans_body = cool_open_client.client.UnitControlFansBody() # UnitControlFansBody | 

    try:
        # set unit fan mode
        api_response = await api_instance.units_unit_id_controls_fan_modes_put(origin, referer, x_access_token, unit_id, unit_control_fans_body)
        print("The response of UnitControlApi->units_unit_id_controls_fan_modes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitControlApi->units_unit_id_controls_fan_modes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **unit_control_fans_body** | [**UnitControlFansBody**](UnitControlFansBody.md)|  | 

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

# **units_unit_id_controls_operation_modes_put**
> Okresponse units_unit_id_controls_operation_modes_put(origin, referer, x_access_token, unit_id, unit_control_modes_body)

set unit operation mode

set unit operation mode

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.unit_control_modes_body import UnitControlModesBody
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
    api_instance = cool_open_client.client.UnitControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    unit_control_modes_body = cool_open_client.client.UnitControlModesBody() # UnitControlModesBody | 

    try:
        # set unit operation mode
        api_response = await api_instance.units_unit_id_controls_operation_modes_put(origin, referer, x_access_token, unit_id, unit_control_modes_body)
        print("The response of UnitControlApi->units_unit_id_controls_operation_modes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitControlApi->units_unit_id_controls_operation_modes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **unit_control_modes_body** | [**UnitControlModesBody**](UnitControlModesBody.md)|  | 

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

# **units_unit_id_controls_operation_statuses_put**
> Okresponse units_unit_id_controls_operation_statuses_put(origin, referer, x_access_token, unit_id, unit_control_switches_body)

set unit operation status

set unit operation status

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.unit_control_switches_body import UnitControlSwitchesBody
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
    api_instance = cool_open_client.client.UnitControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    unit_control_switches_body = cool_open_client.client.UnitControlSwitchesBody() # UnitControlSwitchesBody | 

    try:
        # set unit operation status
        api_response = await api_instance.units_unit_id_controls_operation_statuses_put(origin, referer, x_access_token, unit_id, unit_control_switches_body)
        print("The response of UnitControlApi->units_unit_id_controls_operation_statuses_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitControlApi->units_unit_id_controls_operation_statuses_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **unit_control_switches_body** | [**UnitControlSwitchesBody**](UnitControlSwitchesBody.md)|  | 

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

# **units_unit_id_controls_setpoints_put**
> Okresponse units_unit_id_controls_setpoints_put(origin, referer, x_access_token, unit_id, unit_control_setpoints_body)

set unit temperature setpoint

set unit temperature setpoint

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.unit_control_setpoints_body import UnitControlSetpointsBody
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
    api_instance = cool_open_client.client.UnitControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    unit_control_setpoints_body = cool_open_client.client.UnitControlSetpointsBody() # UnitControlSetpointsBody | 

    try:
        # set unit temperature setpoint
        api_response = await api_instance.units_unit_id_controls_setpoints_put(origin, referer, x_access_token, unit_id, unit_control_setpoints_body)
        print("The response of UnitControlApi->units_unit_id_controls_setpoints_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitControlApi->units_unit_id_controls_setpoints_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **unit_control_setpoints_body** | [**UnitControlSetpointsBody**](UnitControlSetpointsBody.md)|  | 

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

# **units_unit_id_controls_swing_modes_put**
> Okresponse units_unit_id_controls_swing_modes_put(origin, referer, x_access_token, unit_id, unit_control_swings_body)

set unit louver mode

set unit louver mode

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.unit_control_swings_body import UnitControlSwingsBody
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
    api_instance = cool_open_client.client.UnitControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    unit_id = 'unit_id_example' # str | 
    unit_control_swings_body = cool_open_client.client.UnitControlSwingsBody() # UnitControlSwingsBody | 

    try:
        # set unit louver mode
        api_response = await api_instance.units_unit_id_controls_swing_modes_put(origin, referer, x_access_token, unit_id, unit_control_swings_body)
        print("The response of UnitControlApi->units_unit_id_controls_swing_modes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UnitControlApi->units_unit_id_controls_swing_modes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **unit_id** | **str**|  | 
 **unit_control_swings_body** | [**UnitControlSwingsBody**](UnitControlSwingsBody.md)|  | 

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

