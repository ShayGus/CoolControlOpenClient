# cool_open_client.client.SiteSystemsApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_systems_get**](SiteSystemsApi.md#sites_site_id_systems_get) | **GET** /sites/{siteId}/systems | get site systems
[**sites_site_id_systems_post**](SiteSystemsApi.md#sites_site_id_systems_post) | **POST** /sites/{siteId}/systems | create site system

# **sites_site_id_systems_get**
> SystemsResponse sites_site_id_systems_get(x_access_token, site_id)

get site systems

get site systems

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteSystemsApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # get site systems
    api_response = api_instance.sites_site_id_systems_get(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteSystemsApi->sites_site_id_systems_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**SystemsResponse**](SystemsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_systems_post**
> OkresponseWithId sites_site_id_systems_post(body, x_access_token, site_id)

create site system

create site system

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteSystemsApi()
body = cool_open_client.client.CreateSystemRequestBody() # CreateSystemRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # create site system
    api_response = api_instance.sites_site_id_systems_post(body, x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteSystemsApi->sites_site_id_systems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSystemRequestBody**](CreateSystemRequestBody.md)|  | 
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

