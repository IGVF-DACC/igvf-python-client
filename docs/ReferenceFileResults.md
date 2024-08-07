# ReferenceFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ReferenceFile]**](ReferenceFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.reference_file_results import ReferenceFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceFileResults from a JSON string
reference_file_results_instance = ReferenceFileResults.from_json(json)
# print the JSON string representation of the object
print(ReferenceFileResults.to_json())

# convert the object into a dict
reference_file_results_dict = reference_file_results_instance.to_dict()
# create an instance of ReferenceFileResults from a dict
reference_file_results_from_dict = ReferenceFileResults.from_dict(reference_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


