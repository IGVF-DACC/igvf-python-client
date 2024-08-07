# SearchResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SearchResultItem]**](SearchResultItem.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.search_results import SearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResults from a JSON string
search_results_instance = SearchResults.from_json(json)
# print the JSON string representation of the object
print(SearchResults.to_json())

# convert the object into a dict
search_results_dict = search_results_instance.to_dict()
# create an instance of SearchResults from a dict
search_results_from_dict = SearchResults.from_dict(search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


