# SingleCellRnaSeqQualityMetricResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SingleCellRnaSeqQualityMetric]**](SingleCellRnaSeqQualityMetric.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.single_cell_rna_seq_quality_metric_results import SingleCellRnaSeqQualityMetricResults

# TODO update the JSON string below
json = "{}"
# create an instance of SingleCellRnaSeqQualityMetricResults from a JSON string
single_cell_rna_seq_quality_metric_results_instance = SingleCellRnaSeqQualityMetricResults.from_json(json)
# print the JSON string representation of the object
print(SingleCellRnaSeqQualityMetricResults.to_json())

# convert the object into a dict
single_cell_rna_seq_quality_metric_results_dict = single_cell_rna_seq_quality_metric_results_instance.to_dict()
# create an instance of SingleCellRnaSeqQualityMetricResults from a dict
single_cell_rna_seq_quality_metric_results_from_dict = SingleCellRnaSeqQualityMetricResults.from_dict(single_cell_rna_seq_quality_metric_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


