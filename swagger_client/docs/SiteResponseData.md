# SiteResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | site ID | [optional] 
**name** | **str** | site name | [optional] 
**description** | **str** | site description | [optional] 
**country** | **str** | site address - country | [optional] 
**city** | **str** | site address - city | [optional] 
**postal_code** | **str** | site address - postal code | [optional] 
**address** | **str** | site address - freeform text | [optional] 
**timezone** | **str** | site timezone | [optional] 
**customer** | **str** | parent customer id | [optional] 
**devices** | **List[str]** | array of child device IDs | [optional] 
**zones** | **List[str]** | array of child zone IDs | [optional] 
**systems** | **List[str]** | array of child system IDs | [optional] 
**role** | **object** | caller permissions for this site | [optional] 

## Example

```python
from cool_open_client.client.models.site_response_data import SiteResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SiteResponseData from a JSON string
site_response_data_instance = SiteResponseData.from_json(json)
# print the JSON string representation of the object
print(SiteResponseData.to_json())

# convert the object into a dict
site_response_data_dict = site_response_data_instance.to_dict()
# create an instance of SiteResponseData from a dict
site_response_data_from_dict = SiteResponseData.from_dict(site_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


