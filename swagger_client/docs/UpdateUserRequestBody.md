# UpdateUserRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | user identifier | [optional] 
**temperature_scale** | **int** | user preffered temperature scale from the temperature scale enumeration | [optional] 
**permissions** | **object** | user permissions | [optional] 
**first_name** | **str** | user first name | [optional] 
**last_name** | **str** | user last name | [optional] 
**email** | **str** | user email | [optional] 
**phone** | **str** | user phone number | [optional] 

## Example

```python
from cool_open_client.client.models.update_user_request_body import UpdateUserRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestBody from a JSON string
update_user_request_body_instance = UpdateUserRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestBody.to_json())

# convert the object into a dict
update_user_request_body_dict = update_user_request_body_instance.to_dict()
# create an instance of UpdateUserRequestBody from a dict
update_user_request_body_from_dict = UpdateUserRequestBody.from_dict(update_user_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


