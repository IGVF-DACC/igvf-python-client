# AnalysisSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AnalysisSet]**](AnalysisSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.analysis_set_results import AnalysisSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisSetResults from a JSON string
analysis_set_results_instance = AnalysisSetResults.from_json(json)
# print the JSON string representation of the object
print(AnalysisSetResults.to_json())

# convert the object into a dict
analysis_set_results_dict = analysis_set_results_instance.to_dict()
# create an instance of AnalysisSetResults from a dict
analysis_set_results_from_dict = AnalysisSetResults.from_dict(analysis_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


