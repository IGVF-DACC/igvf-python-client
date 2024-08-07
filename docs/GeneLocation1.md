# GeneLocation1

Gene location specified using 1-based, closed coordinates for a specific version of the reference genome assembly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly** | **str** | The genome assembly to which coordinates relate. e.g. GRCh38. | 
**chromosome** | **str** | The number (or letter) designation for the chromosome, e.g. chr1 or chrX | 
**start** | **int** | The starting coordinate. | 
**end** | **int** | The ending coordinate. | 

## Example

```python
from igvf_client.models.gene_location1 import GeneLocation1

# TODO update the JSON string below
json = "{}"
# create an instance of GeneLocation1 from a JSON string
gene_location1_instance = GeneLocation1.from_json(json)
# print the JSON string representation of the object
print(GeneLocation1.to_json())

# convert the object into a dict
gene_location1_dict = gene_location1_instance.to_dict()
# create an instance of GeneLocation1 from a dict
gene_location1_from_dict = GeneLocation1.from_dict(gene_location1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


