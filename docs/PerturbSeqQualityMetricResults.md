# PerturbSeqQualityMetricResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PerturbSeqQualityMetric]**](PerturbSeqQualityMetric.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.perturb_seq_quality_metric_results import PerturbSeqQualityMetricResults

# TODO update the JSON string below
json = "{}"
# create an instance of PerturbSeqQualityMetricResults from a JSON string
perturb_seq_quality_metric_results_instance = PerturbSeqQualityMetricResults.from_json(json)
# print the JSON string representation of the object
print(PerturbSeqQualityMetricResults.to_json())

# convert the object into a dict
perturb_seq_quality_metric_results_dict = perturb_seq_quality_metric_results_instance.to_dict()
# create an instance of PerturbSeqQualityMetricResults from a dict
perturb_seq_quality_metric_results_from_dict = PerturbSeqQualityMetricResults.from_dict(perturb_seq_quality_metric_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


