# AnalysisStepResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AnalysisStep]**](AnalysisStep.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.analysis_step_results import AnalysisStepResults

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStepResults from a JSON string
analysis_step_results_instance = AnalysisStepResults.from_json(json)
# print the JSON string representation of the object
print(AnalysisStepResults.to_json())

# convert the object into a dict
analysis_step_results_dict = analysis_step_results_instance.to_dict()
# create an instance of AnalysisStepResults from a dict
analysis_step_results_from_dict = AnalysisStepResults.from_dict(analysis_step_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


