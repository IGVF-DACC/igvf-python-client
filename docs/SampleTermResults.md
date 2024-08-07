# SampleTermResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SampleTerm]**](SampleTerm.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.sample_term_results import SampleTermResults

# TODO update the JSON string below
json = "{}"
# create an instance of SampleTermResults from a JSON string
sample_term_results_instance = SampleTermResults.from_json(json)
# print the JSON string representation of the object
print(SampleTermResults.to_json())

# convert the object into a dict
sample_term_results_dict = sample_term_results_instance.to_dict()
# create an instance of SampleTermResults from a dict
sample_term_results_from_dict = SampleTermResults.from_dict(sample_term_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


