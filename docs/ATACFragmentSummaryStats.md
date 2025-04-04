# ATACFragmentSummaryStats



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**md5sum** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 

## Example

```python
from igvf_client.models.atac_fragment_summary_stats import ATACFragmentSummaryStats

# TODO update the JSON string below
json = "{}"
# create an instance of ATACFragmentSummaryStats from a JSON string
atac_fragment_summary_stats_instance = ATACFragmentSummaryStats.from_json(json)
# print the JSON string representation of the object
print(ATACFragmentSummaryStats.to_json())

# convert the object into a dict
atac_fragment_summary_stats_dict = atac_fragment_summary_stats_instance.to_dict()
# create an instance of ATACFragmentSummaryStats from a dict
atac_fragment_summary_stats_from_dict = ATACFragmentSummaryStats.from_dict(atac_fragment_summary_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


