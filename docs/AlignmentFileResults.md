# AlignmentFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AlignmentFile]**](AlignmentFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.alignment_file_results import AlignmentFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of AlignmentFileResults from a JSON string
alignment_file_results_instance = AlignmentFileResults.from_json(json)
# print the JSON string representation of the object
print(AlignmentFileResults.to_json())

# convert the object into a dict
alignment_file_results_dict = alignment_file_results_instance.to_dict()
# create an instance of AlignmentFileResults from a dict
alignment_file_results_from_dict = AlignmentFileResults.from_dict(alignment_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


