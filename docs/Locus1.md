# Locus1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly** | **str** | The genome assembly to which coordinates relate (e.g., GRCh38). | 
**chromosome** | **str** | The number (or letter) designation for the chromosome, e.g. chr1 or chrX | 
**start** | **int** | The 1-based, closed (inclusive) starting coordinate. | 
**end** | **int** | The 1-based, closed (inclusive) ending coordinate. | 

## Example

```python
from igvf_client.models.locus1 import Locus1

# TODO update the JSON string below
json = "{}"
# create an instance of Locus1 from a JSON string
locus1_instance = Locus1.from_json(json)
# print the JSON string representation of the object
print(Locus1.to_json())

# convert the object into a dict
locus1_dict = locus1_instance.to_dict()
# create an instance of Locus1 from a dict
locus1_from_dict = Locus1.from_dict(locus1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


