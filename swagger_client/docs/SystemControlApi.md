# cool_open_client.client.SystemControlApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_system_id_controls_modes_put**](SystemControlApi.md#systems_system_id_controls_modes_put) | **PUT** /systems/{systemId}/controls/modes | set system active operation mode for all units
[**systems_system_id_controls_switches_put**](SystemControlApi.md#systems_system_id_controls_switches_put) | **PUT** /systems/{systemId}/controls/switches | set system active operation status for all units


# **systems_system_id_controls_modes_put**
> Okresponse systems_system_id_controls_modes_put(origin, referer, x_access_token, system_id, system_control_modes_body)

set system active operation mode for all units

set system active operation mode for all units

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.system_control_modes_body import SystemControlModesBody
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
    api_instance = cool_open_client.client.SystemControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    system_id = 'system_id_example' # str | 
    system_control_modes_body = cool_open_client.client.SystemControlModesBody() # SystemControlModesBody | 

    try:
        # set system active operation mode for all units
        api_response = await api_instance.systems_system_id_controls_modes_put(origin, referer, x_access_token, system_id, system_control_modes_body)
        print("The response of SystemControlApi->systems_system_id_controls_modes_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControlApi->systems_system_id_controls_modes_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 
 **system_control_modes_body** | [**SystemControlModesBody**](SystemControlModesBody.md)|  | 

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

# **systems_system_id_controls_switches_put**
> Okresponse systems_system_id_controls_switches_put(origin, referer, x_access_token, system_id, system_control_switches_body)

set system active operation status for all units

set system active operation status for all units

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.system_control_switches_body import SystemControlSwitchesBody
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
    api_instance = cool_open_client.client.SystemControlApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    system_id = 'system_id_example' # str | 
    system_control_switches_body = cool_open_client.client.SystemControlSwitchesBody() # SystemControlSwitchesBody | 

    try:
        # set system active operation status for all units
        api_response = await api_instance.systems_system_id_controls_switches_put(origin, referer, x_access_token, system_id, system_control_switches_body)
        print("The response of SystemControlApi->systems_system_id_controls_switches_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SystemControlApi->systems_system_id_controls_switches_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **system_id** | **str**|  | 
 **system_control_switches_body** | [**SystemControlSwitchesBody**](SystemControlSwitchesBody.md)|  | 

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

