# MultiplexedSampleResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[MultiplexedSample]**](MultiplexedSample.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.multiplexed_sample_results import MultiplexedSampleResults

# TODO update the JSON string below
json = "{}"
# create an instance of MultiplexedSampleResults from a JSON string
multiplexed_sample_results_instance = MultiplexedSampleResults.from_json(json)
# print the JSON string representation of the object
print(MultiplexedSampleResults.to_json())

# convert the object into a dict
multiplexed_sample_results_dict = multiplexed_sample_results_instance.to_dict()
# create an instance of MultiplexedSampleResults from a dict
multiplexed_sample_results_from_dict = MultiplexedSampleResults.from_dict(multiplexed_sample_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


