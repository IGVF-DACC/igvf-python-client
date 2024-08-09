# SoftwareVersion

A specific version of a software used for computational analysis. For example, Bowtie2 v2.3.0.

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
**software** | **str** | Unique name of the software package. | [optional] 
**version** | **str** | The version of a particular software. | [optional] 
**download_id** | **str** | The MD5 checksum, SHA-1 commit ID, image hash, or similar permanent identifier of the particular version of software used. | [optional] 
**downloaded_url** | **str** | An external resource to track the version of the software downloaded. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**name** | **str** | A unique identifier for a software version. | [optional] 

## Example

```python
from igvf_client.models.software_version import SoftwareVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersion from a JSON string
software_version_instance = SoftwareVersion.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersion.to_json())

# convert the object into a dict
software_version_dict = software_version_instance.to_dict()
# create an instance of SoftwareVersion from a dict
software_version_from_dict = SoftwareVersion.from_dict(software_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


