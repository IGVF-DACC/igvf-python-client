# Award

A grant providing financial support for a scientific project. For example, HG012076 supporting \"Single-cell Mapping Center for Human Regulatory Elements and Gene Activity.\"

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
**title** | **str** | The grant name from the NIH database, if applicable. | [optional] 
**name** | **str** | The official grant number from the NIH database, if applicable | [optional] 
**start_date** | **str** | The date when the award begins. | [optional] 
**end_date** | **str** | The date when the award concludes. | [optional] 
**pis** | **List[str]** | Principal Investigator(s) of the grant. | [optional] 
**contact_pi** | **str** | The contact Principal Investigator of the grant. | [optional] 
**project** | **str** | The collection of biological data related to a single initiative, originating from a consortium. | [optional] 
**viewing_group** | **str** | The group that determines which set of data the user has permission to view. | [optional] 
**component** | **str** | The project component the award is associated with. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the award. | [optional] 

## Example

```python
from igvf_client.models.award import Award

# TODO update the JSON string below
json = "{}"
# create an instance of Award from a JSON string
award_instance = Award.from_json(json)
# print the JSON string representation of the object
print(Award.to_json())

# convert the object into a dict
award_dict = award_instance.to_dict()
# create an instance of Award from a dict
award_from_dict = Award.from_dict(award_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


