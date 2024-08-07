# AccessKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | Description of the access key. | [optional] 
**status** | **str** |  | [optional] 
**user** | **str** | The user that is assigned to this access key. | [optional] 
**access_key_id** | **str** | An access key. | [optional] 
**secret_access_key_hash** | **str** | A secret access key. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the object. | [optional] 

## Example

```python
from igvf_client.models.access_key import AccessKey

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKey from a JSON string
access_key_instance = AccessKey.from_json(json)
# print the JSON string representation of the object
print(AccessKey.to_json())

# convert the object into a dict
access_key_dict = access_key_instance.to_dict()
# create an instance of AccessKey from a dict
access_key_from_dict = AccessKey.from_dict(access_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


