# AnalysisStepVersion

A step version in a computational analysis workflow.

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
**analysis_step** | **str** | The analysis step which this version belongs to. | [optional] 
**software_versions** | **List[str]** | The software versions used in this analysis step versions. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the object. | [optional] 

## Example

```python
from igvf_client.models.analysis_step_version import AnalysisStepVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStepVersion from a JSON string
analysis_step_version_instance = AnalysisStepVersion.from_json(json)
# print the JSON string representation of the object
print(AnalysisStepVersion.to_json())

# convert the object into a dict
analysis_step_version_dict = analysis_step_version_instance.to_dict()
# create an instance of AnalysisStepVersion from a dict
analysis_step_version_from_dict = AnalysisStepVersion.from_dict(analysis_step_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


