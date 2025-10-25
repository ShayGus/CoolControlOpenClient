# OkresponseWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**OkresponseWithIdData**](OkresponseWithIdData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.okresponse_with_id import OkresponseWithId

# TODO update the JSON string below
json = "{}"
# create an instance of OkresponseWithId from a JSON string
okresponse_with_id_instance = OkresponseWithId.from_json(json)
# print the JSON string representation of the object
print(OkresponseWithId.to_json())

# convert the object into a dict
okresponse_with_id_dict = okresponse_with_id_instance.to_dict()
# create an instance of OkresponseWithId from a dict
okresponse_with_id_from_dict = OkresponseWithId.from_dict(okresponse_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


