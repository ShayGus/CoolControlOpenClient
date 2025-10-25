# cool_open_client.client.CustomerSitesApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_sites_get**](CustomerSitesApi.md#customers_customer_id_sites_get) | **GET** /customers/{customerId}/sites | get customer sites
[**customers_customer_id_sites_post**](CustomerSitesApi.md#customers_customer_id_sites_post) | **POST** /customers/{customerId}/sites | create customer site


# **customers_customer_id_sites_get**
> SitesResponse customers_customer_id_sites_get(origin, referer, x_access_token, customer_id)

get customer sites

get customer sites

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.sites_response import SitesResponse
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
    api_instance = cool_open_client.client.CustomerSitesApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | 

    try:
        # get customer sites
        api_response = await api_instance.customers_customer_id_sites_get(origin, referer, x_access_token, customer_id)
        print("The response of CustomerSitesApi->customers_customer_id_sites_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSitesApi->customers_customer_id_sites_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**|  | 

### Return type

[**SitesResponse**](SitesResponse.md)

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

# **customers_customer_id_sites_post**
> OkresponseWithId customers_customer_id_sites_post(origin, referer, x_access_token, customer_id, create_site_request_body)

create customer site

create customer site

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.create_site_request_body import CreateSiteRequestBody
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
    api_instance = cool_open_client.client.CustomerSitesApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | customer ID
    create_site_request_body = cool_open_client.client.CreateSiteRequestBody() # CreateSiteRequestBody | 

    try:
        # create customer site
        api_response = await api_instance.customers_customer_id_sites_post(origin, referer, x_access_token, customer_id, create_site_request_body)
        print("The response of CustomerSitesApi->customers_customer_id_sites_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerSitesApi->customers_customer_id_sites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 
 **create_site_request_body** | [**CreateSiteRequestBody**](CreateSiteRequestBody.md)|  | 

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

