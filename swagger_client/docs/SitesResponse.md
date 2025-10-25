# SitesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | success status | [optional] 
**data** | [**SitesResponseData**](SitesResponseData.md) |  | [optional] 

## Example

```python
from cool_open_client.client.models.sites_response import SitesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SitesResponse from a JSON string
sites_response_instance = SitesResponse.from_json(json)
# print the JSON string representation of the object
print(SitesResponse.to_json())

# convert the object into a dict
sites_response_dict = sites_response_instance.to_dict()
# create an instance of SitesResponse from a dict
sites_response_from_dict = SitesResponse.from_dict(sites_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


