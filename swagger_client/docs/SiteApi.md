# cool_open_client.client.SiteApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_delete**](SiteApi.md#sites_site_id_delete) | **DELETE** /sites/{siteId} | delete site
[**sites_site_id_get**](SiteApi.md#sites_site_id_get) | **GET** /sites/{siteId} | get site
[**sites_site_id_put**](SiteApi.md#sites_site_id_put) | **PUT** /sites/{siteId} | update site


# **sites_site_id_delete**
> Okresponse sites_site_id_delete(origin, referer, x_access_token, site_id)

delete site

delete site

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coolremote.net/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cool_open_client.client.Configuration(
    host = "https://api.coolremote.net/api/v2"
)


# Enter a context with an instance of the API client
async with cool_open_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cool_open_client.client.SiteApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    site_id = 'site_id_example' # str | 

    try:
        # delete site
        api_response = await api_instance.sites_site_id_delete(origin, referer, x_access_token, site_id)
        print("The response of SiteApi->sites_site_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteApi->sites_site_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_get**
> SiteResponse sites_site_id_get(origin, referer, x_access_token, site_id)

get site

get site

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.site_response import SiteResponse
from cool_open_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coolremote.net/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cool_open_client.client.Configuration(
    host = "https://api.coolremote.net/api/v2"
)


# Enter a context with an instance of the API client
async with cool_open_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cool_open_client.client.SiteApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    site_id = 'site_id_example' # str | 

    try:
        # get site
        api_response = await api_instance.sites_site_id_get(origin, referer, x_access_token, site_id)
        print("The response of SiteApi->sites_site_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteApi->sites_site_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**SiteResponse**](SiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_put**
> Okresponse sites_site_id_put(origin, referer, x_access_token, site_id, update_site_request_body)

update site

update site

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.update_site_request_body import UpdateSiteRequestBody
from cool_open_client.client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.coolremote.net/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = cool_open_client.client.Configuration(
    host = "https://api.coolremote.net/api/v2"
)


# Enter a context with an instance of the API client
async with cool_open_client.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cool_open_client.client.SiteApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    site_id = 'site_id_example' # str | 
    update_site_request_body = cool_open_client.client.UpdateSiteRequestBody() # UpdateSiteRequestBody | 

    try:
        # update site
        api_response = await api_instance.sites_site_id_put(origin, referer, x_access_token, site_id, update_site_request_body)
        print("The response of SiteApi->sites_site_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteApi->sites_site_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 
 **update_site_request_body** | [**UpdateSiteRequestBody**](UpdateSiteRequestBody.md)|  | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**500** | server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

