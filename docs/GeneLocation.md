# GeneLocation

Gene location specified using 1-based, closed coordinates for a specific version of the reference genome assembly.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | The starting coordinate. | 
**end** | **int** | The ending coordinate. | 
**chromosome** | **str** | The number (or letter) designation for the chromosome, e.g. chr1 or chrX | 
**assembly** | **str** | The genome assembly to which coordinates relate. e.g. GRCh38. | 

## Example

```python
from igvf_client.models.gene_location import GeneLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GeneLocation from a JSON string
gene_location_instance = GeneLocation.from_json(json)
# print the JSON string representation of the object
print(GeneLocation.to_json())

# convert the object into a dict
gene_location_dict = gene_location_instance.to_dict()
# create an instance of GeneLocation from a dict
gene_location_from_dict = GeneLocation.from_dict(gene_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


