# CreateSiteRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | site name | 
**description** | **str** | site description | [optional] 
**country** | **str** | site country address | [optional] 
**city** | **str** | site city address | [optional] 
**postal_code** | **str** | site postal code address | [optional] 
**address** | **str** | site freetext address | [optional] 
**timezone** | **str** | site timezone | 

## Example

```python
from cool_open_client.client.models.create_site_request_body import CreateSiteRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSiteRequestBody from a JSON string
create_site_request_body_instance = CreateSiteRequestBody.from_json(json)
# print the JSON string representation of the object
print(CreateSiteRequestBody.to_json())

# convert the object into a dict
create_site_request_body_dict = create_site_request_body_instance.to_dict()
# create an instance of CreateSiteRequestBody from a dict
create_site_request_body_from_dict = CreateSiteRequestBody.from_dict(create_site_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


