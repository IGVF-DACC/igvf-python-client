# User

A user of IGVF data portal who is a member or affiliate member of IGVF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the metadata object. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**email** | **str** | The email associated with the user&#39;s account. | [optional] 
**first_name** | **str** | The user&#39;s first (given) name. | [optional] 
**last_name** | **str** | The user&#39;s last (family) name. | [optional] 
**lab** | **str** | Lab user is primarily associated with. | [optional] 
**submits_for** | **List[str]** | Labs user is authorized to submit data for. | [optional] 
**groups** | **List[str]** | Additional access control groups | [optional] 
**viewing_groups** | **List[str]** | The group that determines which set of data the user has permission to view. | [optional] 
**job_title** | **str** | The role of the user in their lab or organization. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the object. | [optional] 
**title** | **str** | The full name of the user. | [optional] 

## Example

```python
from igvf_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


