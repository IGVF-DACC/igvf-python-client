# PseudobulkSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PseudobulkSet]**](PseudobulkSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.pseudobulk_set_results import PseudobulkSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of PseudobulkSetResults from a JSON string
pseudobulk_set_results_instance = PseudobulkSetResults.from_json(json)
# print the JSON string representation of the object
print(PseudobulkSetResults.to_json())

# convert the object into a dict
pseudobulk_set_results_dict = pseudobulk_set_results_instance.to_dict()
# create an instance of PseudobulkSetResults from a dict
pseudobulk_set_results_from_dict = PseudobulkSetResults.from_dict(pseudobulk_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


