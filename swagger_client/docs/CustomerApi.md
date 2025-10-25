# cool_open_client.client.CustomerApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_delete**](CustomerApi.md#customers_customer_id_delete) | **DELETE** /customers/{customerId} | delete customer
[**customers_customer_id_get**](CustomerApi.md#customers_customer_id_get) | **GET** /customers/{customerId} | get customer
[**customers_customer_id_post**](CustomerApi.md#customers_customer_id_post) | **POST** /customers/{customerId} | create customer
[**customers_customer_id_put**](CustomerApi.md#customers_customer_id_put) | **PUT** /customers/{customerId} | update customer


# **customers_customer_id_delete**
> Okresponse customers_customer_id_delete(origin, referer, x_access_token, customer_id)

delete customer

delete customer

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
    api_instance = cool_open_client.client.CustomerApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | customer ID

    try:
        # delete customer
        api_response = await api_instance.customers_customer_id_delete(origin, referer, x_access_token, customer_id)
        print("The response of CustomerApi->customers_customer_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->customers_customer_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

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

# **customers_customer_id_get**
> CustomerResponse customers_customer_id_get(x_access_token, customer_id, origin, referer)

get customer

Get customer

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.customer_response import CustomerResponse
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
    api_instance = cool_open_client.client.CustomerApi(api_client)
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | customer ID
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')

    try:
        # get customer
        api_response = await api_instance.customers_customer_id_get(x_access_token, customer_id, origin, referer)
        print("The response of CustomerApi->customers_customer_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->customers_customer_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **customers_customer_id_post**
> Okresponse customers_customer_id_post(origin, referer, x_access_token, customer_id, create_customer_request_body)

create customer

create customer

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.create_customer_request_body import CreateCustomerRequestBody
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
    api_instance = cool_open_client.client.CustomerApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | customer ID
    create_customer_request_body = cool_open_client.client.CreateCustomerRequestBody() # CreateCustomerRequestBody | properties to update

    try:
        # create customer
        api_response = await api_instance.customers_customer_id_post(origin, referer, x_access_token, customer_id, create_customer_request_body)
        print("The response of CustomerApi->customers_customer_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->customers_customer_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 
 **create_customer_request_body** | [**CreateCustomerRequestBody**](CreateCustomerRequestBody.md)| properties to update | 

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

# **customers_customer_id_put**
> Okresponse customers_customer_id_put(origin, referer, x_access_token, customer_id, update_customer_request_body)

update customer

update customer

### Example


```python
import cool_open_client.client
from cool_open_client.client.models.okresponse import Okresponse
from cool_open_client.client.models.update_customer_request_body import UpdateCustomerRequestBody
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
    api_instance = cool_open_client.client.CustomerApi(api_client)
    origin = 'https://control.coolremote.net' # str |  (default to 'https://control.coolremote.net')
    referer = 'https://control.coolremote.net/' # str |  (default to 'https://control.coolremote.net/')
    x_access_token = 'x_access_token_example' # str | access token
    customer_id = 'customer_id_example' # str | customer ID
    update_customer_request_body = cool_open_client.client.UpdateCustomerRequestBody() # UpdateCustomerRequestBody | properties to update

    try:
        # update customer
        api_response = await api_instance.customers_customer_id_put(origin, referer, x_access_token, customer_id, update_customer_request_body)
        print("The response of CustomerApi->customers_customer_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerApi->customers_customer_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin** | **str**|  | [default to &#39;https://control.coolremote.net&#39;]
 **referer** | **str**|  | [default to &#39;https://control.coolremote.net/&#39;]
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 
 **update_customer_request_body** | [**UpdateCustomerRequestBody**](UpdateCustomerRequestBody.md)| properties to update | 

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

