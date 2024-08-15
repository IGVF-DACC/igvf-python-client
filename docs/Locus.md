# Locus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** | The 1-based, closed (inclusive) starting coordinate. | 
**end** | **int** | The 1-based, closed (inclusive) ending coordinate. | 
**chromosome** | **str** | The number (or letter) designation for the chromosome, e.g. chr1 or chrX | 
**assembly** | **str** | The genome assembly to which coordinates relate (e.g., GRCh38). | 

## Example

```python
from igvf_client.models.locus import Locus

# TODO update the JSON string below
json = "{}"
# create an instance of Locus from a JSON string
locus_instance = Locus.from_json(json)
# print the JSON string representation of the object
print(Locus.to_json())

# convert the object into a dict
locus_dict = locus_instance.to_dict()
# create an instance of Locus from a dict
locus_from_dict = Locus.from_dict(locus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


