# TissueResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Tissue]**](Tissue.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.tissue_results import TissueResults

# TODO update the JSON string below
json = "{}"
# create an instance of TissueResults from a JSON string
tissue_results_instance = TissueResults.from_json(json)
# print the JSON string representation of the object
print(TissueResults.to_json())

# convert the object into a dict
tissue_results_dict = tissue_results_instance.to_dict()
# create an instance of TissueResults from a dict
tissue_results_from_dict = TissueResults.from_dict(tissue_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


