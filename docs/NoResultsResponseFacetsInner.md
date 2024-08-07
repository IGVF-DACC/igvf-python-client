# NoResultsResponseFacetsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**terms** | [**List[NoResultsResponseFacetsInnerTermsInner]**](NoResultsResponseFacetsInnerTermsInner.md) |  | [optional] 
**total** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**appended** | **bool** |  | [optional] 
**open_on_load** | **bool** |  | [optional] 

## Example

```python
from igvf_client.models.no_results_response_facets_inner import NoResultsResponseFacetsInner

# TODO update the JSON string below
json = "{}"
# create an instance of NoResultsResponseFacetsInner from a JSON string
no_results_response_facets_inner_instance = NoResultsResponseFacetsInner.from_json(json)
# print the JSON string representation of the object
print(NoResultsResponseFacetsInner.to_json())

# convert the object into a dict
no_results_response_facets_inner_dict = no_results_response_facets_inner_instance.to_dict()
# create an instance of NoResultsResponseFacetsInner from a dict
no_results_response_facets_inner_from_dict = NoResultsResponseFacetsInner.from_dict(no_results_response_facets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


