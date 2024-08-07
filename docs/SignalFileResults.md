# SignalFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SignalFile]**](SignalFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.signal_file_results import SignalFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of SignalFileResults from a JSON string
signal_file_results_instance = SignalFileResults.from_json(json)
# print the JSON string representation of the object
print(SignalFileResults.to_json())

# convert the object into a dict
signal_file_results_dict = signal_file_results_instance.to_dict()
# create an instance of SignalFileResults from a dict
signal_file_results_from_dict = SignalFileResults.from_dict(signal_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


