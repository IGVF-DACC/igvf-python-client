# ModelSet

A file set grouping files that represent trained predictive models. Model file sets contain data files that could be used by predictive modeling software to generate predictions or annotations of genomic features such as genomic variants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**input_file_sets** | **List[str]** | The file set(s) that served as inputs for the derivation of this model set. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**accession** | **str** | A unique identifier to be used to reference the object prefixed with IGVF. | [optional] 
**alternate_accessions** | **List[str]** | Accessions previously assigned to objects that have been merged with this object. | [optional] 
**collections** | **List[str]** | Some samples are part of particular data collections. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**revoke_detail** | **str** | Explanation of why an object was transitioned to the revoked status. | [optional] 
**url** | **str** | An external resource with additional information. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**dbxrefs** | **List[str]** | Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file sets. | [optional] 
**control_type** | **str** | The type of control this file set represents. | [optional] 
**samples** | **List[str]** | The sample(s) associated with this file set. | [optional] 
**donors** | **List[str]** | The donor(s) associated with this file set. | [optional] 
**file_set_type** | **str** | The category that best describes this predictive model set. | [optional] 
**model_name** | **str** | The custom lab name given to this predictive model set. | [optional] 
**model_version** | **str** | The semantic version number for this predictive model set. | [optional] 
**prediction_objects** | **List[str]** | The objects this predictive model set is targeting. | [optional] 
**model_zoo_location** | **str** | The link to the model on the Kipoi repository. | [optional] 
**assessed_genes** | **List[str]** | A list of genes assessed in this model set. | [optional] 
**external_input_data** | **str** | A tabular file with links to external data utilized for this model. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets associated with the samples of this file set. | [optional] 
**data_use_limitation_summaries** | **List[str]** | The data use limitation summaries of institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**controlled_access** | **bool** | The controlled access of the institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**externally_hosted** | **bool** |  | [optional] 
**software_versions** | **List[str]** | The software versions used to produce this predictive model. | [optional] 

## Example

```python
from igvf_client.models.model_set import ModelSet

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSet from a JSON string
model_set_instance = ModelSet.from_json(json)
# print the JSON string representation of the object
print(ModelSet.to_json())

# convert the object into a dict
model_set_dict = model_set_instance.to_dict()
# create an instance of ModelSet from a dict
model_set_from_dict = ModelSet.from_dict(model_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


