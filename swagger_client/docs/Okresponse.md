# Okresponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 

## Example

```python
from cool_open_client.client.models.okresponse import Okresponse

# TODO update the JSON string below
json = "{}"
# create an instance of Okresponse from a JSON string
okresponse_instance = Okresponse.from_json(json)
# print the JSON string representation of the object
print(Okresponse.to_json())

# convert the object into a dict
okresponse_dict = okresponse_instance.to_dict()
# create an instance of Okresponse from a dict
okresponse_from_dict = Okresponse.from_dict(okresponse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


