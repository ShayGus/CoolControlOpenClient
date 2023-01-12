# cool_open_client.client.CustomerSitesApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_sites_get**](CustomerSitesApi.md#customers_customer_id_sites_get) | **GET** /customers/{customerId}/sites | get customer sites
[**customers_customer_id_sites_post**](CustomerSitesApi.md#customers_customer_id_sites_post) | **POST** /customers/{customerId}/sites | create customer site

# **customers_customer_id_sites_get**
> SitesResponse customers_customer_id_sites_get(x_access_token, customer_id)

get customer sites

get customer sites

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerSitesApi()
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | 

try:
    # get customer sites
    api_response = api_instance.customers_customer_id_sites_get(x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerSitesApi->customers_customer_id_sites_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**|  | 

### Return type

[**SitesResponse**](SitesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_sites_post**
> OkresponseWithId customers_customer_id_sites_post(body, x_access_token, customer_id)

create customer site

create customer site

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerSitesApi()
body = cool_open_client.client.CreateSiteRequestBody() # CreateSiteRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | customer ID

try:
    # create customer site
    api_response = api_instance.customers_customer_id_sites_post(body, x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerSitesApi->customers_customer_id_sites_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSiteRequestBody**](CreateSiteRequestBody.md)|  | 
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

### Return type

[**OkresponseWithId**](OkresponseWithId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

