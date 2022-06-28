# swagger_client.SiteDevicesApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_devices_get**](SiteDevicesApi.md#sites_site_id_devices_get) | **GET** /sites/{siteId}/devices | get site devices
[**sites_site_id_devices_post**](SiteDevicesApi.md#sites_site_id_devices_post) | **POST** /sites/{siteId}/devices | add device to site

# **sites_site_id_devices_get**
> DevicesResponse sites_site_id_devices_get(x_access_token, site_id)

get site devices

get site devices

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteDevicesApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # get site devices
    api_response = api_instance.sites_site_id_devices_get(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteDevicesApi->sites_site_id_devices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**DevicesResponse**](DevicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_devices_post**
> OkresponseWithId sites_site_id_devices_post(body, x_access_token, site_id)

add device to site

add device to site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteDevicesApi()
body = swagger_client.CreateDeviceRequestBody() # CreateDeviceRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # add device to site
    api_response = api_instance.sites_site_id_devices_post(body, x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteDevicesApi->sites_site_id_devices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateDeviceRequestBody**](CreateDeviceRequestBody.md)|  | 
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

