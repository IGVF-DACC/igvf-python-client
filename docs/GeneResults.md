# GeneResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Gene]**](Gene.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.gene_results import GeneResults

# TODO update the JSON string below
json = "{}"
# create an instance of GeneResults from a JSON string
gene_results_instance = GeneResults.from_json(json)
# print the JSON string representation of the object
print(GeneResults.to_json())

# convert the object into a dict
gene_results_dict = gene_results_instance.to_dict()
# create an instance of GeneResults from a dict
gene_results_from_dict = GeneResults.from_dict(gene_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


