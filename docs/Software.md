# Software

A software used for computational  analysis. For example, Bowtie2 alignment software.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**name** | **str** | Unique name of the software package; a lowercase version of the title. | [optional] 
**title** | **str** | The preferred viewable name of the software. | [optional] 
**source_url** | **str** | An external resource to the codebase. | [optional] 
**used_by** | **List[str]** | The component(s) of the IGVF consortium that utilize this software. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**versions** | **List[str]** | A list of versions that have been released for this software. | [optional] 

## Example

```python
from igvf_client.models.software import Software

# TODO update the JSON string below
json = "{}"
# create an instance of Software from a JSON string
software_instance = Software.from_json(json)
# print the JSON string representation of the object
print(Software.to_json())

# convert the object into a dict
software_dict = software_instance.to_dict()
# create an instance of Software from a dict
software_from_dict = Software.from_dict(software_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


