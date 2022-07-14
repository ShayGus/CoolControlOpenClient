# cool_open_client.client.SiteUsersApi

All URIs are relative to *https://api.coolremote.net/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sites_site_id_users_get**](SiteUsersApi.md#sites_site_id_users_get) | **GET** /sites/{siteId}/users | get site users
[**sites_site_id_users_post**](SiteUsersApi.md#sites_site_id_users_post) | **POST** /sites/{siteId}/users | create site user

# **sites_site_id_users_get**
> UsersResponse sites_site_id_users_get(x_access_token, site_id)

get site users

get site users

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteUsersApi()
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # get site users
    api_response = api_instance.sites_site_id_users_get(x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteUsersApi->sites_site_id_users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_access_token** | **str**| access token | 
 **site_id** | **str**|  | 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites_site_id_users_post**
> OkresponseWithId sites_site_id_users_post(body, x_access_token, site_id)

create site user

create site user

### Example
```python
from __future__ import print_function
import time
import cool_open_client.client
from cool_open_client.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = cool_open_client.client.SiteUsersApi()
body = cool_open_client.client.CreateUserRequestBody() # CreateUserRequestBody | 
x_access_token = 'x_access_token_example' # str | access token
site_id = 'site_id_example' # str | 

try:
    # create site user
    api_response = api_instance.sites_site_id_users_post(body, x_access_token, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SiteUsersApi->sites_site_id_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserRequestBody**](CreateUserRequestBody.md)|  | 
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

