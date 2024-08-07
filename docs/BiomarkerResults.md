# BiomarkerResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Biomarker]**](Biomarker.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.biomarker_results import BiomarkerResults

# TODO update the JSON string below
json = "{}"
# create an instance of BiomarkerResults from a JSON string
biomarker_results_instance = BiomarkerResults.from_json(json)
# print the JSON string representation of the object
print(BiomarkerResults.to_json())

# convert the object into a dict
biomarker_results_dict = biomarker_results_instance.to_dict()
# create an instance of BiomarkerResults from a dict
biomarker_results_from_dict = BiomarkerResults.from_dict(biomarker_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


