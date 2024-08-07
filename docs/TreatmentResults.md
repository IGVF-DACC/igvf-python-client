# TreatmentResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Treatment]**](Treatment.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.treatment_results import TreatmentResults

# TODO update the JSON string below
json = "{}"
# create an instance of TreatmentResults from a JSON string
treatment_results_instance = TreatmentResults.from_json(json)
# print the JSON string representation of the object
print(TreatmentResults.to_json())

# convert the object into a dict
treatment_results_dict = treatment_results_instance.to_dict()
# create an instance of TreatmentResults from a dict
treatment_results_from_dict = TreatmentResults.from_dict(treatment_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


