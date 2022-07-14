# cool_open_client.client.ZoneApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zones_zone_id_delete**](ZoneApi.md#zones_zone_id_delete) | **DELETE** /zones/{zoneId} | delete zone
[**zones_zone_id_get**](ZoneApi.md#zones_zone_id_get) | **GET** /zones/{zoneId} | get zone
[**zones_zone_id_put**](ZoneApi.md#zones_zone_id_put) | **PUT** /zones/{zoneId} | update zone

# **zones_zone_id_delete**
> Okresponse zones_zone_id_delete(x_access_token, zone_id)

delete zone

delete zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneApi()
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | 

try:
    # delete zone
    api_response = api_instance.zones_zone_id_delete(x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->zones_zone_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_get**
> ZoneResponse zones_zone_id_get(x_access_token, zone_id)

get zone

get zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneApi()
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | 

try:
    # get zone
    api_response = api_instance.zones_zone_id_get(x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->zones_zone_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **zone_id** | **str**|  | 

### Return type

[**ZoneResponse**](ZoneResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **zones_zone_id_put**
> Okresponse zones_zone_id_put(body, x_access_token, zone_id)

update zone

update zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.ZoneApi()
body = cool_open_client.client.UpdateZoneRequestBody() # UpdateZoneRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
zone_id = 'zone_id_example' # str | zone ID

try:
    # update zone
    api_response = api_instance.zones_zone_id_put(body, x_access_token, zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ZoneApi->zones_zone_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateZoneRequestBody**](UpdateZoneRequestBody.md)|  | 
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

