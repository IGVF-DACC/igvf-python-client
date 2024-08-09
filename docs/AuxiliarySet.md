# AuxiliarySet

Auxiliary set is a file set that hosts raw data files (e.g. FASTQs) resulting from sequencing of nucleic acids of a sample that are a proxy to some vital information and necessary for the analysis of an associated measurement set. Auxiliary sets usually would not provide any information about the transcriptome or the genome of the sample in question. For example auxiliary sets would include the sequencing of barcodes that correspond to the elements introduced into cells, or sequencing of guide RNA coding sequences in the cells. The files hosted in the auxiliary sets are relevant for the analysis, but they by themselves are not assessing much of the biology of the sample being analyzed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**accession** | **str** | A unique identifier to be used to reference the object prefixed with IGVF. | [optional] 
**alternate_accessions** | **List[str]** | Accessions previously assigned to objects that have been merged with this object. | [optional] 
**collections** | **List[str]** | Some samples are part of particular data collections. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**revoke_detail** | **str** | Explanation of why an object was transitioned to the revoked status. | [optional] 
**url** | **str** | An external resource with additional information. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**dbxrefs** | **List[str]** | Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file sets. | [optional] 
**samples** | **List[str]** | The sample(s) associated with this file set. | [optional] 
**donors** | **List[str]** | The donors of the samples associated with this auxiliary set. | [optional] 
**file_set_type** | **str** | The category that best describes this auxiliary file set. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_file_set_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**measurement_sets** | **List[str]** | The measurement sets that link to this auxiliary set. | [optional] 

## Example

```python
from igvf_client.models.auxiliary_set import AuxiliarySet

# TODO update the JSON string below
json = "{}"
# create an instance of AuxiliarySet from a JSON string
auxiliary_set_instance = AuxiliarySet.from_json(json)
# print the JSON string representation of the object
print(AuxiliarySet.to_json())

# convert the object into a dict
auxiliary_set_dict = auxiliary_set_instance.to_dict()
# create an instance of AuxiliarySet from a dict
auxiliary_set_from_dict = AuxiliarySet.from_dict(auxiliary_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


