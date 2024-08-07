# PredictionSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PredictionSet]**](PredictionSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.prediction_set_results import PredictionSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionSetResults from a JSON string
prediction_set_results_instance = PredictionSetResults.from_json(json)
# print the JSON string representation of the object
print(PredictionSetResults.to_json())

# convert the object into a dict
prediction_set_results_dict = prediction_set_results_instance.to_dict()
# create an instance of PredictionSetResults from a dict
prediction_set_results_from_dict = PredictionSetResults.from_dict(prediction_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


