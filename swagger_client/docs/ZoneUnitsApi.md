# cool_open_client.client.ZoneUnitsApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_units_get**](ZoneUnitsApi.md#zones_zone_id_units_get) | **GET** /zones/{zoneId}/units | get zone units
[**zones_zone_id_units_unit_id_delete**](ZoneUnitsApi.md#zones_zone_id_units_unit_id_delete) | **DELETE** /zones/{zoneId}/units/{unitId} | remove unit from zone
[**zones_zone_id_units_unit_id_post**](ZoneUnitsApi.md#zones_zone_id_units_unit_id_post) | **POST** /zones/{zoneId}/units/{unitId} | add unit to zone

# **zones_zone_id_units_get**
> UnitsResponse zones_zone_id_units_get(x_access_token, zone_id)

get zone units

get zone units

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | 

try:
    # get zone units
    api_response = api_instance.zones_zone_id_units_get(x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneUnitsApi->zones_zone_id_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**|  | 

### Return type

[**UnitsResponse**](UnitsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_units_unit_id_delete**
> Okresponse zones_zone_id_units_unit_id_delete(x_access_token, zone_id, unit_id)

remove unit from zone

remove unit from zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | 
unit_id = 'unit_id_example' # str | 

try:
    # remove unit from zone
    api_response = api_instance.zones_zone_id_units_unit_id_delete(x_access_token, zone_id, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneUnitsApi->zones_zone_id_units_unit_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**|  | 
 **unit_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_units_unit_id_post**
> Okresponse zones_zone_id_units_unit_id_post(x_access_token, zone_id, unit_id)

add unit to zone

add unit to zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneUnitsApi()
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | 
unit_id = 'unit_id_example' # str | 

try:
    # add unit to zone
    api_response = api_instance.zones_zone_id_units_unit_id_post(x_access_token, zone_id, unit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneUnitsApi->zones_zone_id_units_unit_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**|  | 
 **unit_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

