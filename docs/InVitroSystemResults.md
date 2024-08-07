# InVitroSystemResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[InVitroSystem]**](InVitroSystem.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.in_vitro_system_results import InVitroSystemResults

# TODO update the JSON string below
json = "{}"
# create an instance of InVitroSystemResults from a JSON string
in_vitro_system_results_instance = InVitroSystemResults.from_json(json)
# print the JSON string representation of the object
print(InVitroSystemResults.to_json())

# convert the object into a dict
in_vitro_system_results_dict = in_vitro_system_results_instance.to_dict()
# create an instance of InVitroSystemResults from a dict
in_vitro_system_results_from_dict = InVitroSystemResults.from_dict(in_vitro_system_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


