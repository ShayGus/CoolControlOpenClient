# OkresponseWithToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**OkresponseWithTokenData**](OkresponseWithTokenData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.okresponse_with_token import OkresponseWithToken

# TODO update the JSON string below
json = "{}"
# create an instance of OkresponseWithToken from a JSON string
okresponse_with_token_instance = OkresponseWithToken.from_json(json)
# print the JSON string representation of the object
print(OkresponseWithToken.to_json())

# convert the object into a dict
okresponse_with_token_dict = okresponse_with_token_instance.to_dict()
# create an instance of OkresponseWithToken from a dict
okresponse_with_token_from_dict = OkresponseWithToken.from_dict(okresponse_with_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


