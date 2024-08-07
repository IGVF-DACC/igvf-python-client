# ModelFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ModelFile]**](ModelFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.model_file_results import ModelFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of ModelFileResults from a JSON string
model_file_results_instance = ModelFileResults.from_json(json)
# print the JSON string representation of the object
print(ModelFileResults.to_json())

# convert the object into a dict
model_file_results_dict = model_file_results_instance.to_dict()
# create an instance of ModelFileResults from a dict
model_file_results_from_dict = ModelFileResults.from_dict(model_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


