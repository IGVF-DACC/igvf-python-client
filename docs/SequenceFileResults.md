# SequenceFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SequenceFile]**](SequenceFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.sequence_file_results import SequenceFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceFileResults from a JSON string
sequence_file_results_instance = SequenceFileResults.from_json(json)
# print the JSON string representation of the object
print(SequenceFileResults.to_json())

# convert the object into a dict
sequence_file_results_dict = sequence_file_results_instance.to_dict()
# create an instance of SequenceFileResults from a dict
sequence_file_results_from_dict = SequenceFileResults.from_dict(sequence_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


