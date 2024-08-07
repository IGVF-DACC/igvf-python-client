# AssayTermResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AssayTerm]**](AssayTerm.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.assay_term_results import AssayTermResults

# TODO update the JSON string below
json = "{}"
# create an instance of AssayTermResults from a JSON string
assay_term_results_instance = AssayTermResults.from_json(json)
# print the JSON string representation of the object
print(AssayTermResults.to_json())

# convert the object into a dict
assay_term_results_dict = assay_term_results_instance.to_dict()
# create an instance of AssayTermResults from a dict
assay_term_results_from_dict = AssayTermResults.from_dict(assay_term_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


