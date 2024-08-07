# TechnicalSampleResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[TechnicalSample]**](TechnicalSample.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.technical_sample_results import TechnicalSampleResults

# TODO update the JSON string below
json = "{}"
# create an instance of TechnicalSampleResults from a JSON string
technical_sample_results_instance = TechnicalSampleResults.from_json(json)
# print the JSON string representation of the object
print(TechnicalSampleResults.to_json())

# convert the object into a dict
technical_sample_results_dict = technical_sample_results_instance.to_dict()
# create an instance of TechnicalSampleResults from a dict
technical_sample_results_from_dict = TechnicalSampleResults.from_dict(technical_sample_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


