# AuxiliarySetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AuxiliarySet]**](AuxiliarySet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.auxiliary_set_results import AuxiliarySetResults

# TODO update the JSON string below
json = "{}"
# create an instance of AuxiliarySetResults from a JSON string
auxiliary_set_results_instance = AuxiliarySetResults.from_json(json)
# print the JSON string representation of the object
print(AuxiliarySetResults.to_json())

# convert the object into a dict
auxiliary_set_results_dict = auxiliary_set_results_instance.to_dict()
# create an instance of AuxiliarySetResults from a dict
auxiliary_set_results_from_dict = AuxiliarySetResults.from_dict(auxiliary_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


