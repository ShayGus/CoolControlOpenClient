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
> Okresponse units_unit_id_controls_fan_modes_put(body, origin, referer, x_access_token, unit_id)

set unit fan mode

set unit fan mode

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitControlApi()
body = cool_open_client.client.UnitControlFansBody() # UnitControlFansBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit fan mode
    api_response = api_instance.units_unit_id_controls_fan_modes_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_fan_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlFansBody**](UnitControlFansBody.md)|  | 
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

# **units_unit_id_controls_operation_modes_put**
> Okresponse units_unit_id_controls_operation_modes_put(body, origin, referer, x_access_token, unit_id)

set unit operation mode

set unit operation mode

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitControlApi()
body = cool_open_client.client.UnitControlModesBody() # UnitControlModesBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit operation mode
    api_response = api_instance.units_unit_id_controls_operation_modes_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_operation_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlModesBody**](UnitControlModesBody.md)|  | 
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

# **units_unit_id_controls_operation_statuses_put**
> Okresponse units_unit_id_controls_operation_statuses_put(body, origin, referer, x_access_token, unit_id)

set unit operation status

set unit operation status

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitControlApi()
body = cool_open_client.client.UnitControlSwitchesBody() # UnitControlSwitchesBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit operation status
    api_response = api_instance.units_unit_id_controls_operation_statuses_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_operation_statuses_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSwitchesBody**](UnitControlSwitchesBody.md)|  | 
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

# **units_unit_id_controls_setpoints_put**
> Okresponse units_unit_id_controls_setpoints_put(body, origin, referer, x_access_token, unit_id)

set unit temperature setpoint

set unit temperature setpoint

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitControlApi()
body = cool_open_client.client.UnitControlSetpointsBody() # UnitControlSetpointsBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit temperature setpoint
    api_response = api_instance.units_unit_id_controls_setpoints_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_setpoints_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSetpointsBody**](UnitControlSetpointsBody.md)|  | 
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

# **units_unit_id_controls_swing_modes_put**
> Okresponse units_unit_id_controls_swing_modes_put(body, origin, referer, x_access_token, unit_id)

set unit louver mode

set unit louver mode

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.UnitControlApi()
body = cool_open_client.client.UnitControlSwingsBody() # UnitControlSwingsBody | 
origin = 'https://control.coolremote.net' # str |  (default to https://control.coolremote.net)
referer = 'https://control.coolremote.net/' # str |  (default to https://control.coolremote.net/)
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit louver mode
    api_response = api_instance.units_unit_id_controls_swing_modes_put(body, origin, referer, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_swing_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSwingsBody**](UnitControlSwingsBody.md)|  | 
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

