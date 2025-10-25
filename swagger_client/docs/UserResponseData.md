# UserResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | user ID | [optional] 
**username** | **str** | user identifier | [optional] 
**email** | **str** | user email | [optional] 
**phone** | **str** | user phone number | [optional] 
**role** | **object** | caller permissions for this user | [optional] 
**permissions** | **object** | user permissions | [optional] 

## Example

```python
from cool_open_client.client.models.user_response_data import UserResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseData from a JSON string
user_response_data_instance = UserResponseData.from_json(json)
# print the JSON string representation of the object
print(UserResponseData.to_json())

# convert the object into a dict
user_response_data_dict = user_response_data_instance.to_dict()
# create an instance of UserResponseData from a dict
user_response_data_from_dict = UserResponseData.from_dict(user_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


