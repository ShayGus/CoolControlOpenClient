# cool_open_client.client.ZoneControlApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_controls_fans_put**](ZoneControlApi.md#zones_zone_id_controls_fans_put) | **PUT** /zones/{zoneId}/controls/fans | set zone active fan mode for all units
[**zones_zone_id_controls_modes_put**](ZoneControlApi.md#zones_zone_id_controls_modes_put) | **PUT** /zones/{zoneId}/controls/modes | set zone active operation mode for all units
[**zones_zone_id_controls_setpoints_put**](ZoneControlApi.md#zones_zone_id_controls_setpoints_put) | **PUT** /zones/{zoneId}/controls/setpoints | set zone active temperature setpoint for all units
[**zones_zone_id_controls_switches_put**](ZoneControlApi.md#zones_zone_id_controls_switches_put) | **PUT** /zones/{zoneId}/controls/switches | set zone active operation status for all units

# **zones_zone_id_controls_fans_put**
> Okresponse zones_zone_id_controls_fans_put(body, x_access_token, zone_id)

set zone active fan mode for all units

set zone active fan mode for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneControlApi()
body = cool_open_client.client.ZoneControlFansBody() # ZoneControlFansBody | 
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | zone ID

try:
    # set zone active fan mode for all units
    api_response = api_instance.zones_zone_id_controls_fans_put(body, x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneControlApi->zones_zone_id_controls_fans_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneControlFansBody**](ZoneControlFansBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**| zone ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_controls_modes_put**
> Okresponse zones_zone_id_controls_modes_put(body, x_access_token, zone_id)

set zone active operation mode for all units

set zone active operation mode for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneControlApi()
body = cool_open_client.client.ZoneControlModesBody() # ZoneControlModesBody | 
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | zone ID

try:
    # set zone active operation mode for all units
    api_response = api_instance.zones_zone_id_controls_modes_put(body, x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneControlApi->zones_zone_id_controls_modes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneControlModesBody**](ZoneControlModesBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**| zone ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_controls_setpoints_put**
> Okresponse zones_zone_id_controls_setpoints_put(body, x_access_token, zone_id)

set zone active temperature setpoint for all units

set zone active temperature setpoint for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneControlApi()
body = cool_open_client.client.ZoneControlSetpointsBody() # ZoneControlSetpointsBody | 
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | zone ID

try:
    # set zone active temperature setpoint for all units
    api_response = api_instance.zones_zone_id_controls_setpoints_put(body, x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneControlApi->zones_zone_id_controls_setpoints_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneControlSetpointsBody**](ZoneControlSetpointsBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**| zone ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_controls_switches_put**
> Okresponse zones_zone_id_controls_switches_put(body, x_access_token, zone_id)

set zone active operation status for all units

set zone active operation status for all units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneControlApi()
body = cool_open_client.client.ZoneControlSwitchesBody() # ZoneControlSwitchesBody | 
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | zone ID

try:
    # set zone active operation status for all units
    api_response = api_instance.zones_zone_id_controls_switches_put(body, x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneControlApi->zones_zone_id_controls_switches_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ZoneControlSwitchesBody**](ZoneControlSwitchesBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**| zone ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

