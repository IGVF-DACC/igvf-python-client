# AnalysisStep

A step in a computational analysis workflow. For example, a sequence alignment step that represents the phase of the computational analysis in which sequenced reads are being aligned to the reference genome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**analysis_step_types** | **List[str]** | The classification of the software. | [optional] 
**step_label** | **str** | Unique lowercased label of the analysis step that includes the relevant assays, the software used, and the purpose of the step, e.g. rampage-grit-peak-calling-step | [optional] 
**title** | **str** | The preferred viewable name of the analysis step, likely the same as the step label. | [optional] 
**workflow** | **str** | The computational workflow in which this analysis step belongs. | [optional] 
**parents** | **List[str]** | The precursor steps. | [optional] 
**input_content_types** | **List[str]** | The content types used as input for the analysis step. | [optional] 
**output_content_types** | **List[str]** | The content types produced as output by the analysis step. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the object. | [optional] 
**name** | **str** | Full name of the analysis step. | [optional] 

## Example

```python
from igvf_client.models.analysis_step import AnalysisStep

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStep from a JSON string
analysis_step_instance = AnalysisStep.from_json(json)
# print the JSON string representation of the object
print(AnalysisStep.to_json())

# convert the object into a dict
analysis_step_dict = analysis_step_instance.to_dict()
# create an instance of AnalysisStep from a dict
analysis_step_from_dict = AnalysisStep.from_dict(analysis_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


