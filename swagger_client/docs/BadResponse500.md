# BadResponse500


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**message** | **str** | text message describing the error | [optional] 

## Example

```python
from cool_open_client.client.models.bad_response500 import BadResponse500

# TODO update the JSON string below
json = "{}"
# create an instance of BadResponse500 from a JSON string
bad_response500_instance = BadResponse500.from_json(json)
# print the JSON string representation of the object
print(BadResponse500.to_json())

# convert the object into a dict
bad_response500_dict = bad_response500_instance.to_dict()
# create an instance of BadResponse500 from a dict
bad_response500_from_dict = BadResponse500.from_dict(bad_response500_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


