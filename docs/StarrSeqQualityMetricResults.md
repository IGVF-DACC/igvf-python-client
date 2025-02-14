# StarrSeqQualityMetricResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[StarrSeqQualityMetric]**](StarrSeqQualityMetric.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.starr_seq_quality_metric_results import StarrSeqQualityMetricResults

# TODO update the JSON string below
json = "{}"
# create an instance of StarrSeqQualityMetricResults from a JSON string
starr_seq_quality_metric_results_instance = StarrSeqQualityMetricResults.from_json(json)
# print the JSON string representation of the object
print(StarrSeqQualityMetricResults.to_json())

# convert the object into a dict
starr_seq_quality_metric_results_dict = starr_seq_quality_metric_results_instance.to_dict()
# create an instance of StarrSeqQualityMetricResults from a dict
starr_seq_quality_metric_results_from_dict = StarrSeqQualityMetricResults.from_dict(starr_seq_quality_metric_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


