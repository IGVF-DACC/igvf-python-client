# PrimaryCellResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PrimaryCell]**](PrimaryCell.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.primary_cell_results import PrimaryCellResults

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryCellResults from a JSON string
primary_cell_results_instance = PrimaryCellResults.from_json(json)
# print the JSON string representation of the object
print(PrimaryCellResults.to_json())

# convert the object into a dict
primary_cell_results_dict = primary_cell_results_instance.to_dict()
# create an instance of PrimaryCellResults from a dict
primary_cell_results_from_dict = PrimaryCellResults.from_dict(primary_cell_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


