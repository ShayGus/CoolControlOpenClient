# CreateSystemRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | system name | 
**description** | **str** | system description | [optional] 

## Example

```python
from cool_open_client.client.models.create_system_request_body import CreateSystemRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSystemRequestBody from a JSON string
create_system_request_body_instance = CreateSystemRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateSystemRequestBody.to_json())

# convert the object into a dict
create_system_request_body_dict = create_system_request_body_instance.to_dict()
# create an instance of CreateSystemRequestBody from a dict
create_system_request_body_from_dict = CreateSystemRequestBody.from_dict(create_system_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


