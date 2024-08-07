# LabResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Lab]**](Lab.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.lab_results import LabResults

# TODO update the JSON string below
json = "{}"
# create an instance of LabResults from a JSON string
lab_results_instance = LabResults.from_json(json)
# print the JSON string representation of the object
print(LabResults.to_json())

# convert the object into a dict
lab_results_dict = lab_results_instance.to_dict()
# create an instance of LabResults from a dict
lab_results_from_dict = LabResults.from_dict(lab_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


