# CreateUserRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | user identifier | 
**password** | **str** | user password | 
**temperature_scale** | **int** | user preffered temperature scale from the temperature scale enumeration | 
**permissions** | **object** | user permissions | 
**first_name** | **str** | user first name | [optional] 
**last_name** | **str** | user last name | [optional] 
**email** | **str** | user email | [optional] 
**phone** | **str** | user phone number | [optional] 

## Example

```python
from cool_open_client.client.models.create_user_request_body import CreateUserRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequestBody from a JSON string
create_user_request_body_instance = CreateUserRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateUserRequestBody.to_json())

# convert the object into a dict
create_user_request_body_dict = create_user_request_body_instance.to_dict()
# create an instance of CreateUserRequestBody from a dict
create_user_request_body_from_dict = CreateUserRequestBody.from_dict(create_user_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


