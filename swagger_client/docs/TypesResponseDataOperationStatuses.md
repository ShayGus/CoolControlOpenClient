# TypesResponseDataOperationStatuses

map of supported operation status enums

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | operation status name | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_operation_statuses import TypesResponseDataOperationStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataOperationStatuses from a JSON string
types_response_data_operation_statuses_instance = TypesResponseDataOperationStatuses.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataOperationStatuses.to_json())

# convert the object into a dict
types_response_data_operation_statuses_dict = types_response_data_operation_statuses_instance.to_dict()
# create an instance of TypesResponseDataOperationStatuses from a dict
types_response_data_operation_statuses_from_dict = TypesResponseDataOperationStatuses.from_dict(types_response_data_operation_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


