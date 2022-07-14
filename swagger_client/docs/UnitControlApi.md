# cool_open_client.client.UnitControlApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**units_unit_id_controls_fans_put**](UnitControlApi.md#units_unit_id_controls_fans_put) | **PUT** /units/{unitId}/controls/fans | set unit fan mode
[**units_unit_id_controls_modes_put**](UnitControlApi.md#units_unit_id_controls_modes_put) | **PUT** /units/{unitId}/controls/modes | set unit operation mode
[**units_unit_id_controls_setpoints_put**](UnitControlApi.md#units_unit_id_controls_setpoints_put) | **PUT** /units/{unitId}/controls/setpoints | set unit temperature setpoint
[**units_unit_id_controls_swings_put**](UnitControlApi.md#units_unit_id_controls_swings_put) | **PUT** /units/{unitId}/controls/swings | set unit louver mode
[**units_unit_id_controls_switches_put**](UnitControlApi.md#units_unit_id_controls_switches_put) | **PUT** /units/{unitId}/controls/switches | set unit operation status

# **units_unit_id_controls_fans_put**
> Okresponse units_unit_id_controls_fans_put(body, x_access_token, unit_id)

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
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit fan mode
    api_response = api_instance.units_unit_id_controls_fans_put(body, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_fans_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlFansBody**](UnitControlFansBody.md)|  | 
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

# **units_unit_id_controls_modes_put**
> Okresponse units_unit_id_controls_modes_put(body, x_access_token, unit_id)

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
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit operation mode
    api_response = api_instance.units_unit_id_controls_modes_put(body, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlModesBody**](UnitControlModesBody.md)|  | 
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
> Okresponse units_unit_id_controls_setpoints_put(body, x_access_token, unit_id)

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
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit temperature setpoint
    api_response = api_instance.units_unit_id_controls_setpoints_put(body, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_setpoints_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSetpointsBody**](UnitControlSetpointsBody.md)|  | 
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

# **units_unit_id_controls_swings_put**
> Okresponse units_unit_id_controls_swings_put(body, x_access_token, unit_id)

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
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit louver mode
    api_response = api_instance.units_unit_id_controls_swings_put(body, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_swings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSwingsBody**](UnitControlSwingsBody.md)|  | 
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

# **units_unit_id_controls_switches_put**
> Okresponse units_unit_id_controls_switches_put(body, x_access_token, unit_id)

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
x_access_token = 'x_access_token_example' # str | access token
unit_id = 'unit_id_example' # str | 

try:
    # set unit operation status
    api_response = api_instance.units_unit_id_controls_switches_put(body, x_access_token, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UnitControlApi->units_unit_id_controls_switches_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnitControlSwitchesBody**](UnitControlSwitchesBody.md)|  | 
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

