# TypesResponseDataHvacBrandsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | hvac type id | [optional] 
**type** | **str** | Brand type | [optional] 
**name** | **str** | Brand Name | [optional] 
**is_water_heater** | **bool** | Is the device water heater | [optional] 
**has_booster** | **bool** | Does the device has booster | [optional] 

## Example

```python
from cool_open_client.client.models.types_response_data_hvac_brands_inner import TypesResponseDataHvacBrandsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TypesResponseDataHvacBrandsInner from a JSON string
types_response_data_hvac_brands_inner_instance = TypesResponseDataHvacBrandsInner.from_json(json)
# print the JSON string representation of the object
print(TypesResponseDataHvacBrandsInner.to_json())

# convert the object into a dict
types_response_data_hvac_brands_inner_dict = types_response_data_hvac_brands_inner_instance.to_dict()
# create an instance of TypesResponseDataHvacBrandsInner from a dict
types_response_data_hvac_brands_inner_from_dict = TypesResponseDataHvacBrandsInner.from_dict(types_response_data_hvac_brands_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


