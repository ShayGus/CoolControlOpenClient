# cool_open_client.client.CustomerApi

All URIs are relative to *https://api.coolremote.net/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customers_customer_id_delete**](CustomerApi.md#customers_customer_id_delete) | **DELETE** /customers/{customerId} | delete customer
[**customers_customer_id_get**](CustomerApi.md#customers_customer_id_get) | **GET** /customers/{customerId} | get customer
[**customers_customer_id_post**](CustomerApi.md#customers_customer_id_post) | **POST** /customers/{customerId} | create customer
[**customers_customer_id_put**](CustomerApi.md#customers_customer_id_put) | **PUT** /customers/{customerId} | update customer

# **customers_customer_id_delete**
> Okresponse customers_customer_id_delete(x_access_token, customer_id)

delete customer

delete customer

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerApi()
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | customer ID

try:
    # delete customer
    api_response = api_instance.customers_customer_id_delete(x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_customer_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_get**
> CustomerResponse customers_customer_id_get(x_access_token, customer_id)

get customer

Get customer

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerApi()
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | customer ID

try:
    # get customer
    api_response = api_instance.customers_customer_id_get(x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_customer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

### Return type

[**CustomerResponse**](CustomerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_post**
> Okresponse customers_customer_id_post(body, x_access_token, customer_id)

create customer

create customer

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerApi()
body = cool_open_client.client.CreateCustomerRequestBody() # CreateCustomerRequestBody | properties to update
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | customer ID

try:
    # create customer
    api_response = api_instance.customers_customer_id_post(body, x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_customer_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCustomerRequestBody**](CreateCustomerRequestBody.md)| properties to update | 
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customers_customer_id_put**
> Okresponse customers_customer_id_put(body, x_access_token, customer_id)

update customer

update customer

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.CustomerApi()
body = cool_open_client.client.UpdateCustomerRequestBody() # UpdateCustomerRequestBody | properties to update
x_access_token = 'x_access_token_example' # str | access token
customer_id = 'customer_id_example' # str | customer ID

try:
    # update customer
    api_response = api_instance.customers_customer_id_put(body, x_access_token, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerApi->customers_customer_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateCustomerRequestBody**](UpdateCustomerRequestBody.md)| properties to update | 
 **x_access_token** | **str**| access token | 
 **customer_id** | **str**| customer ID | 

### Return type

[**Okresponse**](Okresponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

