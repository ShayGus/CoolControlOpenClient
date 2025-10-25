# ControlTreeResponseDataCustomersCustomerIdSitesSiteId

single site properties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | site name | [optional] 
**id** | **str** | site id | [optional] 
**role** | **str** | user role for this site | [optional] 
**devices** | **List[int]** | array of associated device IDs | [optional] 
**zones** | **List[int]** | array of associated zone IDs | [optional] 
**systems** | **List[int]** | array of associated system IDs | [optional] 

## Example

```python
from cool_open_client.client.models.control_tree_response_data_customers_customer_id_sites_site_id import ControlTreeResponseDataCustomersCustomerIdSitesSiteId

# TODO update the JSON string below
json = "{}"
# create an instance of ControlTreeResponseDataCustomersCustomerIdSitesSiteId from a JSON string
control_tree_response_data_customers_customer_id_sites_site_id_instance = ControlTreeResponseDataCustomersCustomerIdSitesSiteId.from_json(json)
# print the JSON string representation of the object
print(ControlTreeResponseDataCustomersCustomerIdSitesSiteId.to_json())

# convert the object into a dict
control_tree_response_data_customers_customer_id_sites_site_id_dict = control_tree_response_data_customers_customer_id_sites_site_id_instance.to_dict()
# create an instance of ControlTreeResponseDataCustomersCustomerIdSitesSiteId from a dict
control_tree_response_data_customers_customer_id_sites_site_id_from_dict = ControlTreeResponseDataCustomersCustomerIdSitesSiteId.from_dict(control_tree_response_data_customers_customer_id_sites_site_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


