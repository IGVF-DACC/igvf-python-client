# AnalysisSet

A file set for analyses. Analysis sets represent the results of a computational analysis of raw genomic data or other analyses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**input_file_sets** | **List[str]** | The file set(s) required for this analysis. | [optional] 
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
**samples** | **List[str]** | Samples associated with this analysis set. | [optional] 
**donors** | **List[str]** | The donors of the samples associated with this analysis set. | [optional] 
**file_set_type** | **str** | The level of this analysis set. | [optional] 
**external_image_data_url** | **str** | Links to the external site where images and related data produced by this analysis are stored. | [optional] 
**demultiplexed_samples** | **List[str]** | The sample(s) associated with this analysis set inferred through demultiplexing. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets associated with the samples of this file set. | [optional] 
**data_use_limitation_summaries** | **List[str]** | The data use limitation summaries of institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**controlled_access** | **bool** | The controlled access of the institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**assay_titles** | **List[str]** | Title(s) of assays that produced data analyzed in the analysis set. | [optional] 
**protocols** | **List[str]** | Links to the protocol(s) for conducting the assay on Protocols.io. | [optional] 
**sample_summary** | **str** | A summary of the samples associated with input file sets of this analysis set. | [optional] 
**functional_assay_mechanisms** | **List[str]** | The biological processes measured by the functional assays. | [optional] 
**workflows** | **List[str]** | A workflow for computational analysis of genomic data. A workflow is made up of analysis steps. | [optional] 

## Example

```python
from igvf_client.models.analysis_set import AnalysisSet

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisSet from a JSON string
analysis_set_instance = AnalysisSet.from_json(json)
# print the JSON string representation of the object
print(AnalysisSet.to_json())

# convert the object into a dict
analysis_set_dict = analysis_set_instance.to_dict()
# create an instance of AnalysisSet from a dict
analysis_set_from_dict = AnalysisSet.from_dict(analysis_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


