# PhenotypeTermResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PhenotypeTerm]**](PhenotypeTerm.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.phenotype_term_results import PhenotypeTermResults

# TODO update the JSON string below
json = "{}"
# create an instance of PhenotypeTermResults from a JSON string
phenotype_term_results_instance = PhenotypeTermResults.from_json(json)
# print the JSON string representation of the object
print(PhenotypeTermResults.to_json())

# convert the object into a dict
phenotype_term_results_dict = phenotype_term_results_instance.to_dict()
# create an instance of PhenotypeTermResults from a dict
phenotype_term_results_from_dict = PhenotypeTermResults.from_dict(phenotype_term_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


