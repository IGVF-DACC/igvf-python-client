# MeasurementSet

Measurement set is a file set that hosts raw data files (e.g. FASTQs) resulting from sequencing of a library prepared from the nucleic acids of the sample that is the main target of the assay. For example sequencing of accessible regions in the genome, or sequencing of the transcriptome of the sample. The assay can either be bulk or single cell type. The sample specific raw sequencing results will be captured in the measurement sets. The files in the measurement sets are specific to the sample being investigated. See auxiliary sets for files that are not a direct result of sequencing the sample under investigation.

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
**donors** | **List[str]** | The donors of the samples associated with this measurement set. | [optional] 
**file_set_type** | **str** | The category that best describes this measurement set. | [optional] 
**assay_term** | **str** | The assay used to produce data in this measurement set. | [optional] 
**protocols** | **List[str]** | Links to the protocol(s) for conducting the assay on Protocols.io. | [optional] 
**preferred_assay_title** | **str** | The custom lab preferred label for the experiment performed in this measurement set. | [optional] 
**multiome_size** | **int** | The number of datasets included in the multiome experiment this measurement set is a part of. | [optional] 
**control_file_sets** | **List[str]** | File sets that can serve as scientific controls for this measurement_set. | [optional] 
**sequencing_library_types** | **List[str]** | Description of the libraries sequenced in this measurement set. | [optional] 
**auxiliary_sets** | **List[str]** | The auxiliary sets of files produced alongside raw data from this measurement set. | [optional] 
**external_image_url** | **str** | Links to the external site where images produced by this measurement are stored. | [optional] 
**targeted_genes** | **List[str]** | A list of genes targeted in this assay. For example, TF ChIP-seq attempts to identify binding sites of a protein encoded by a specific gene. In CRISPR FlowFISH, the modified samples are sorted based on expression of a specific gene. This property differs from small_scale_gene_list in Construct Library Set, which describes genes targeted by the content integrated in the constructs (such as guide RNAs.) | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_file_set_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**related_multiome_datasets** | **List[str]** | Related datasets included in the multiome experiment this measurement set is a part of. | [optional] 

## Example

```python
from igvf_client.models.measurement_set import MeasurementSet

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSet from a JSON string
measurement_set_instance = MeasurementSet.from_json(json)
# print the JSON string representation of the object
print(MeasurementSet.to_json())

# convert the object into a dict
measurement_set_dict = measurement_set_instance.to_dict()
# create an instance of MeasurementSet from a dict
measurement_set_from_dict = MeasurementSet.from_dict(measurement_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


