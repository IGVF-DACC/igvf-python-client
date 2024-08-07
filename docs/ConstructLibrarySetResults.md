# ConstructLibrarySetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ConstructLibrarySet]**](ConstructLibrarySet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.construct_library_set_results import ConstructLibrarySetResults

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructLibrarySetResults from a JSON string
construct_library_set_results_instance = ConstructLibrarySetResults.from_json(json)
# print the JSON string representation of the object
print(ConstructLibrarySetResults.to_json())

# convert the object into a dict
construct_library_set_results_dict = construct_library_set_results_instance.to_dict()
# create an instance of ConstructLibrarySetResults from a dict
construct_library_set_results_from_dict = ConstructLibrarySetResults.from_dict(construct_library_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


