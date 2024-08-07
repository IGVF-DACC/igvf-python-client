# AnalysisStepVersionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AnalysisStepVersion]**](AnalysisStepVersion.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.analysis_step_version_results import AnalysisStepVersionResults

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStepVersionResults from a JSON string
analysis_step_version_results_instance = AnalysisStepVersionResults.from_json(json)
# print the JSON string representation of the object
print(AnalysisStepVersionResults.to_json())

# convert the object into a dict
analysis_step_version_results_dict = analysis_step_version_results_instance.to_dict()
# create an instance of AnalysisStepVersionResults from a dict
analysis_step_version_results_from_dict = AnalysisStepVersionResults.from_dict(analysis_step_version_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


