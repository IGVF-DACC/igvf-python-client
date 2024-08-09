# Publication

A publication related to IGVF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**attachment** | [**Attachment**](Attachment.md) |  | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**title** | **str** | Title of the publication or communication. | [optional] 
**abstract** | **str** | Abstract of the publication or communication. | [optional] 
**authors** | **str** | The authors of the publication. | [optional] 
**date_published** | **str** | The date the publication or communication was published; must be in YYYY-MM-DD format. | [optional] 
**date_revised** | **str** | The date the publication was revised. | [optional] 
**issue** | **str** | The issue of the publication. | [optional] 
**page** | **str** | Pagination of the reference | [optional] 
**volume** | **str** | The volume of the publication. | [optional] 
**journal** | **str** | The journal of the publication. | [optional] 
**publication_identifiers** | **List[str]** | The publication identifiers associated with this publication object. | [optional] 
**published_by** | **List[str]** | The affiliation of the lab with a larger organization, such as IGVF. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the publication. | [optional] 
**publication_year** | **int** | The year the publication was published. | [optional] 
**samples** | **List[str]** | The samples associated with this publication. | [optional] 
**donors** | **List[str]** | The donors associated with this publication. | [optional] 
**file_sets** | **List[str]** | The file sets associated with this publication. | [optional] 
**workflows** | **List[str]** | The workflows associated with this publication. | [optional] 
**software** | **List[str]** | The software associated with this publication. | [optional] 
**software_versions** | **List[str]** | The software versions associated with this publication. | [optional] 

## Example

```python
from igvf_client.models.publication import Publication

# TODO update the JSON string below
json = "{}"
# create an instance of Publication from a JSON string
publication_instance = Publication.from_json(json)
# print the JSON string representation of the object
print(Publication.to_json())

# convert the object into a dict
publication_dict = publication_instance.to_dict()
# create an instance of Publication from a dict
publication_from_dict = Publication.from_dict(publication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


