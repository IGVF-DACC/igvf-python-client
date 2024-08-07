# ModelSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ModelSet]**](ModelSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.model_set_results import ModelSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSetResults from a JSON string
model_set_results_instance = ModelSetResults.from_json(json)
# print the JSON string representation of the object
print(ModelSetResults.to_json())

# convert the object into a dict
model_set_results_dict = model_set_results_instance.to_dict()
# create an instance of ModelSetResults from a dict
model_set_results_from_dict = ModelSetResults.from_dict(model_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


