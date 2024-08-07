# DegronModificationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[DegronModification]**](DegronModification.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.degron_modification_results import DegronModificationResults

# TODO update the JSON string below
json = "{}"
# create an instance of DegronModificationResults from a JSON string
degron_modification_results_instance = DegronModificationResults.from_json(json)
# print the JSON string representation of the object
print(DegronModificationResults.to_json())

# convert the object into a dict
degron_modification_results_dict = degron_modification_results_instance.to_dict()
# create an instance of DegronModificationResults from a dict
degron_modification_results_from_dict = DegronModificationResults.from_dict(degron_modification_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


