# TabularFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[TabularFile]**](TabularFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.tabular_file_results import TabularFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of TabularFileResults from a JSON string
tabular_file_results_instance = TabularFileResults.from_json(json)
# print the JSON string representation of the object
print(TabularFileResults.to_json())

# convert the object into a dict
tabular_file_results_dict = tabular_file_results_instance.to_dict()
# create an instance of TabularFileResults from a dict
tabular_file_results_from_dict = TabularFileResults.from_dict(tabular_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


