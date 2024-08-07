# DegronModification

A degron modification that can induce degradation of a protein.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**sources** | **List[str]** | The originating lab(s) or vendor(s). | [optional] 
**lot_id** | **str** | The lot identifier provided by the originating lab or vendor. | [optional] 
**product_id** | **str** | The product or catalog identifier provided following deposition to addgene.org. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
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
**activated** | **bool** | A boolean indicating whether the modification has been activated by a chemical agent. | [optional] 
**activating_agent_term_id** | **str** | The CHEBI identifier for the activating agent of the modification. | [optional] 
**activating_agent_term_name** | **str** | The CHEBI name for the activating agent of the modification. | [optional] 
**modality** | **str** | The purpose or intended effect of a modification. | [optional] 
**degron_system** | **str** | The type of degron system implemented. | [optional] 
**tagged_proteins** | **List[str]** | The tagged proteins which are targeted for degradation. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**biosamples_modified** | **List[str]** | The biosamples which have been modified with this modification. | [optional] 

## Example

```python
from igvf_client.models.degron_modification import DegronModification

# TODO update the JSON string below
json = "{}"
# create an instance of DegronModification from a JSON string
degron_modification_instance = DegronModification.from_json(json)
# print the JSON string representation of the object
print(DegronModification.to_json())

# convert the object into a dict
degron_modification_dict = degron_modification_instance.to_dict()
# create an instance of DegronModification from a dict
degron_modification_from_dict = DegronModification.from_dict(degron_modification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


