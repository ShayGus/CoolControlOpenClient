# BadResponse404


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**message** | **str** | text message describing the error | [optional] 

## Example

```python
from cool_open_client.client.models.bad_response404 import BadResponse404

# TODO update the JSON string below
json = "{}"
# create an instance of BadResponse404 from a JSON string
bad_response404_instance = BadResponse404.from_json(json)
# print the JSON string representation of the object
print(BadResponse404.to_json())

# convert the object into a dict
bad_response404_dict = bad_response404_instance.to_dict()
# create an instance of BadResponse404 from a dict
bad_response404_from_dict = BadResponse404.from_dict(bad_response404_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


