# OpenReadingFrame

Protein-encoding open reading frames (ORF)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**orf_id** | **str** | Open reading frame ID. | [optional] 
**genes** | **List[str]** | ENSEMBL GeneIDs of official nomenclature approved genes. The GeneIDs do not include the current version number suffix. | [optional] 
**protein_id** | **str** | ENSEMBL ProteinID of official nomenclature approved protein. The ProteinID does not include the current version number suffix. | [optional] 
**dbxrefs** | **List[str]** | Unique identifiers from the hORFeome database | [optional] 
**pct_identical_protein** | **float** | The percentage of identical matches to Ensembl protein. | [optional] 
**pct_coverage_protein** | **float** | The percentage of ORF covered by Ensembl protein. | [optional] 
**pct_coverage_orf** | **float** | The percentage of Ensembl protein covered by ORF. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from igvf_client.models.open_reading_frame import OpenReadingFrame

# TODO update the JSON string below
json = "{}"
# create an instance of OpenReadingFrame from a JSON string
open_reading_frame_instance = OpenReadingFrame.from_json(json)
# print the JSON string representation of the object
print(OpenReadingFrame.to_json())

# convert the object into a dict
open_reading_frame_dict = open_reading_frame_instance.to_dict()
# create an instance of OpenReadingFrame from a dict
open_reading_frame_from_dict = OpenReadingFrame.from_dict(open_reading_frame_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


