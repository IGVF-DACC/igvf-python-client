# PageResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Page]**](Page.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.page_results import PageResults

# TODO update the JSON string below
json = "{}"
# create an instance of PageResults from a JSON string
page_results_instance = PageResults.from_json(json)
# print the JSON string representation of the object
print(PageResults.to_json())

# convert the object into a dict
page_results_dict = page_results_instance.to_dict()
# create an instance of PageResults from a dict
page_results_from_dict = PageResults.from_dict(page_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


