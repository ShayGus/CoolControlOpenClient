# SitesResponseData

map of sites

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_id** | [**SiteResponseData**](SiteResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.sites_response_data import SitesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of SitesResponseData from a JSON string
sites_response_data_instance = SitesResponseData.from_json(json)
# print the JSON string representation of the object
print(SitesResponseData.to_json())

# convert the object into a dict
sites_response_data_dict = sites_response_data_instance.to_dict()
# create an instance of SitesResponseData from a dict
sites_response_data_from_dict = SitesResponseData.from_dict(sites_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


