# MpraQualityMetricResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[MpraQualityMetric]**](MpraQualityMetric.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.mpra_quality_metric_results import MpraQualityMetricResults

# TODO update the JSON string below
json = "{}"
# create an instance of MpraQualityMetricResults from a JSON string
mpra_quality_metric_results_instance = MpraQualityMetricResults.from_json(json)
# print the JSON string representation of the object
print(MpraQualityMetricResults.to_json())

# convert the object into a dict
mpra_quality_metric_results_dict = mpra_quality_metric_results_instance.to_dict()
# create an instance of MpraQualityMetricResults from a dict
mpra_quality_metric_results_from_dict = MpraQualityMetricResults.from_dict(mpra_quality_metric_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


