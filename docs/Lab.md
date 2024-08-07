# Lab

A lab that is part of or affiliated with the IGVF consortium.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the metadata object. | [optional] 
**url** | **str** | An external resource with additional information. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**name** | **str** | A short unique name for the lab, current convention is lower cased and hyphen delimited of PI&#39;s first and last name (e.g. john-doe). | [optional] 
**pi** | **str** | Principle Investigator of the lab. | [optional] 
**awards** | **List[str]** | Grants associated with the lab. | [optional] 
**institute_label** | **str** | An abbreviation for the institute the lab is associated with. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the lab. | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from igvf_client.models.lab import Lab

# TODO update the JSON string below
json = "{}"
# create an instance of Lab from a JSON string
lab_instance = Lab.from_json(json)
# print the JSON string representation of the object
print(Lab.to_json())

# convert the object into a dict
lab_dict = lab_instance.to_dict()
# create an instance of Lab from a dict
lab_from_dict = Lab.from_dict(lab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


