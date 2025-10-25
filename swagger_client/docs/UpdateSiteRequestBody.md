# UpdateSiteRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | site name | [optional] 
**description** | **str** | site description | [optional] 
**country** | **str** | site country address | [optional] 
**city** | **str** | site city address | [optional] 
**postal_code** | **str** | site postal code address | [optional] 
**address** | **str** | site freetext address | [optional] 
**timezone** | **str** | site timezone | [optional] 

## Example

```python
from cool_open_client.client.models.update_site_request_body import UpdateSiteRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSiteRequestBody from a JSON string
update_site_request_body_instance = UpdateSiteRequestBody.from_json(json)
# print the JSON string representation of the object
print(UpdateSiteRequestBody.to_json())

# convert the object into a dict
update_site_request_body_dict = update_site_request_body_instance.to_dict()
# create an instance of UpdateSiteRequestBody from a dict
update_site_request_body_from_dict = UpdateSiteRequestBody.from_dict(update_site_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


