# NoResultsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | [optional] 
**graph** | **List[object]** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**clear_filters** | **str** |  | [optional] 
**columns** | [**Dict[str, NoResultsResponseColumnsValue]**](NoResultsResponseColumnsValue.md) |  | [optional] 
**facet_groups** | [**List[NoResultsResponseFacetGroupsInner]**](NoResultsResponseFacetGroupsInner.md) |  | [optional] 
**facets** | [**List[NoResultsResponseFacetsInner]**](NoResultsResponseFacetsInner.md) |  | [optional] 
**filters** | [**List[NoResultsResponseFiltersInner]**](NoResultsResponseFiltersInner.md) |  | [optional] 
**notification** | **str** |  | [optional] 
**sort** | [**Dict[str, NoResultsResponseSortValue]**](NoResultsResponseSortValue.md) |  | [optional] 
**title** | **str** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from igvf_client.models.no_results_response import NoResultsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NoResultsResponse from a JSON string
no_results_response_instance = NoResultsResponse.from_json(json)
# print the JSON string representation of the object
print(NoResultsResponse.to_json())

# convert the object into a dict
no_results_response_dict = no_results_response_instance.to_dict()
# create an instance of NoResultsResponse from a dict
no_results_response_from_dict = NoResultsResponse.from_dict(no_results_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


