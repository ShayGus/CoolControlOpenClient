# swagger_client.SiteApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_delete**](SiteApi.md#sites_site_id_delete) | **DELETE** /sites/{siteId} | delete site
[**sites_site_id_get**](SiteApi.md#sites_site_id_get) | **GET** /sites/{siteId} | get site
[**sites_site_id_put**](SiteApi.md#sites_site_id_put) | **PUT** /sites/{siteId} | update site

# **sites_site_id_delete**
> Okresponse sites_site_id_delete(x_access_token, site_id)

delete site

delete site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # delete site
    api_response = api_instance.sites_site_id_delete(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->sites_site_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_get**
> SiteResponse sites_site_id_get(x_access_token, site_id)

get site

get site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # get site
    api_response = api_instance.sites_site_id_get(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->sites_site_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_put**
> Okresponse sites_site_id_put(body, x_access_token, site_id)

update site

update site

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SiteApi()
body = swagger_client.UpdateSiteRequestBody() # UpdateSiteRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # update site
    api_response = api_instance.sites_site_id_put(body, x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteApi->sites_site_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateSiteRequestBody**](UpdateSiteRequestBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

