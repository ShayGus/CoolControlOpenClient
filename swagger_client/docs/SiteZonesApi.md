# cool_open_client.client.SiteZonesApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_zones_get**](SiteZonesApi.md#sites_site_id_zones_get) | **GET** /sites/{siteId}/zones | get site zones
[**sites_site_id_zones_post**](SiteZonesApi.md#sites_site_id_zones_post) | **POST** /sites/{siteId}/zones | create site zone

# **sites_site_id_zones_get**
> ZonesResponse sites_site_id_zones_get(x_access_token, site_id)

get site zones

get site zones

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteZonesApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # get site zones
    api_response = api_instance.sites_site_id_zones_get(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteZonesApi->sites_site_id_zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**ZonesResponse**](ZonesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_zones_post**
> OkresponseWithId sites_site_id_zones_post(body, x_access_token, site_id)

create site zone

create site zone

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteZonesApi()
body = cool_open_client.client.CreateZoneRequestBody() # CreateZoneRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # create site zone
    api_response = api_instance.sites_site_id_zones_post(body, x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteZonesApi->sites_site_id_zones_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateZoneRequestBody**](CreateZoneRequestBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**OkresponseWithId**](OkresponseWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

