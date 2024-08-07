# WholeOrganismResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[WholeOrganism]**](WholeOrganism.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.whole_organism_results import WholeOrganismResults

# TODO update the JSON string below
json = "{}"
# create an instance of WholeOrganismResults from a JSON string
whole_organism_results_instance = WholeOrganismResults.from_json(json)
# print the JSON string representation of the object
print(WholeOrganismResults.to_json())

# convert the object into a dict
whole_organism_results_dict = whole_organism_results_instance.to_dict()
# create an instance of WholeOrganismResults from a dict
whole_organism_results_from_dict = WholeOrganismResults.from_dict(whole_organism_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


