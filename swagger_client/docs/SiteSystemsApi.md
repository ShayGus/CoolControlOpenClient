# cool_open_client.client.SiteSystemsApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_systems_get**](SiteSystemsApi.md#sites_site_id_systems_get) | **GET** /sites/{siteId}/systems | get site systems
[**sites_site_id_systems_post**](SiteSystemsApi.md#sites_site_id_systems_post) | **POST** /sites/{siteId}/systems | create site system


# **sites_site_id_systems_get**
> SystemsResponse sites_site_id_systems_get(origin, referer, x_access_token, site_id)

get site systems

get site systems

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.systems_response import SystemsResponse
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
    api_instance = cool_open_client.client.SiteSystemsApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    site_id = 'site_id_example' # str | 

    try:
        # get site systems
        api_response = await api_instance.sites_site_id_systems_get(origin, referer, x_access_token, site_id)
        print("The response of SiteSystemsApi->sites_site_id_systems_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSystemsApi->sites_site_id_systems_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**SystemsResponse**](SystemsResponse.md)

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

# **sites_site_id_systems_post**
> OkresponseWithId sites_site_id_systems_post(origin, referer, x_access_token, site_id, create_system_request_body)

create site system

create site system

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.create_system_request_body import CreateSystemRequestBody
from cool_open_client.client.models.okresponse_with_id import OkresponseWithId
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
    api_instance = cool_open_client.client.SiteSystemsApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    site_id = 'site_id_example' # str | 
    create_system_request_body = cool_open_client.client.CreateSystemRequestBody() # CreateSystemRequestBody | 

    try:
        # create site system
        api_response = await api_instance.sites_site_id_systems_post(origin, referer, x_access_token, site_id, create_system_request_body)
        print("The response of SiteSystemsApi->sites_site_id_systems_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SiteSystemsApi->sites_site_id_systems_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 
 **create_system_request_body** | [**CreateSystemRequestBody**](CreateSystemRequestBody.md)|  | 

### Return type

[**OkresponseWithId**](OkresponseWithId.md)

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

