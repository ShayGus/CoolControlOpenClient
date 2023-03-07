# cool_open_client.client.SystemControlApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**systems_system_id_controls_modes_put**](SystemControlApi.md#systems_system_id_controls_modes_put) | **PUT** /systems/{systemId}/controls/modes | set system active operation mode for all units
[**systems_system_id_controls_switches_put**](SystemControlApi.md#systems_system_id_controls_switches_put) | **PUT** /systems/{systemId}/controls/switches | set system active operation status for all units

# **systems_system_id_controls_modes_put**
> Okresponse systems_system_id_controls_modes_put(body, origin, referer, x_access_token, system_id)

set system active operation mode for all units

set system active operation mode for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemControlApi()
body = cool_open_client.client.SystemControlModesBody() # SystemControlModesBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # set system active operation mode for all units
    api_response = api_instance.systems_system_id_controls_modes_put(body, origin, referer, x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemControlApi->systems_system_id_controls_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemControlModesBody**](SystemControlModesBody.md)|  | 
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

# **systems_system_id_controls_switches_put**
> Okresponse systems_system_id_controls_switches_put(body, origin, referer, x_access_token, system_id)

set system active operation status for all units

set system active operation status for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SystemControlApi()
body = cool_open_client.client.SystemControlSwitchesBody() # SystemControlSwitchesBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
system_id = 'system_id_example' # str | 

try:
    # set system active operation status for all units
    api_response = api_instance.systems_system_id_controls_switches_put(body, origin, referer, x_access_token, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemControlApi->systems_system_id_controls_switches_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SystemControlSwitchesBody**](SystemControlSwitchesBody.md)|  | 
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

