# AuthenticateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**app_id** | **str** |  | [default to 'coolAutomationControl']

## Example

```python
from cool_open_client.client.models.authenticate_request_body import AuthenticateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateRequestBody from a JSON string
authenticate_request_body_instance = AuthenticateRequestBody.from_json(json)
# print the JSON string representation of the object
print(AuthenticateRequestBody.to_json())

# convert the object into a dict
authenticate_request_body_dict = authenticate_request_body_instance.to_dict()
# create an instance of AuthenticateRequestBody from a dict
authenticate_request_body_from_dict = AuthenticateRequestBody.from_dict(authenticate_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


