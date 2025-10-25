# OkresponseWithTokenData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | access token | [optional] 

## Example

```python
from cool_open_client.client.models.okresponse_with_token_data import OkresponseWithTokenData

# TODO update the JSON string below
json = "{}"
# create an instance of OkresponseWithTokenData from a JSON string
okresponse_with_token_data_instance = OkresponseWithTokenData.from_json(json)
# print the JSON string representation of the object
print(OkresponseWithTokenData.to_json())

# convert the object into a dict
okresponse_with_token_data_dict = okresponse_with_token_data_instance.to_dict()
# create an instance of OkresponseWithTokenData from a dict
okresponse_with_token_data_from_dict = OkresponseWithTokenData.from_dict(okresponse_with_token_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


