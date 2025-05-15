# RNASeqKBInfo

The content of the kb-python RNAseq kb_info.json file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**md5sum** | **str** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 

## Example

```python
from igvf_client.models.rna_seq_kb_info import RNASeqKBInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RNASeqKBInfo from a JSON string
rna_seq_kb_info_instance = RNASeqKBInfo.from_json(json)
# print the JSON string representation of the object
print(RNASeqKBInfo.to_json())

# convert the object into a dict
rna_seq_kb_info_dict = rna_seq_kb_info_instance.to_dict()
# create an instance of RNASeqKBInfo from a dict
rna_seq_kb_info_from_dict = RNASeqKBInfo.from_dict(rna_seq_kb_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


