# SystemsResponseData

dictionary of systems

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_id** | [**SystemResponseData**](SystemResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.systems_response_data import SystemsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SystemsResponseData from a JSON string
systems_response_data_instance = SystemsResponseData.from_json(json)
# print the JSON string representation of the object
print(SystemsResponseData.to_json())

# convert the object into a dict
systems_response_data_dict = systems_response_data_instance.to_dict()
# create an instance of SystemsResponseData from a dict
systems_response_data_from_dict = SystemsResponseData.from_dict(systems_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


