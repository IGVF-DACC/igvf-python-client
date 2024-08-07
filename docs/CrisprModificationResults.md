# CrisprModificationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[CrisprModification]**](CrisprModification.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.crispr_modification_results import CrisprModificationResults

# TODO update the JSON string below
json = "{}"
# create an instance of CrisprModificationResults from a JSON string
crispr_modification_results_instance = CrisprModificationResults.from_json(json)
# print the JSON string representation of the object
print(CrisprModificationResults.to_json())

# convert the object into a dict
crispr_modification_results_dict = crispr_modification_results_instance.to_dict()
# create an instance of CrisprModificationResults from a dict
crispr_modification_results_from_dict = CrisprModificationResults.from_dict(crispr_modification_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


