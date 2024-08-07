# CuratedSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[CuratedSet]**](CuratedSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.curated_set_results import CuratedSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of CuratedSetResults from a JSON string
curated_set_results_instance = CuratedSetResults.from_json(json)
# print the JSON string representation of the object
print(CuratedSetResults.to_json())

# convert the object into a dict
curated_set_results_dict = curated_set_results_instance.to_dict()
# create an instance of CuratedSetResults from a dict
curated_set_results_from_dict = CuratedSetResults.from_dict(curated_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


