# PredictionSet

A file set of computational predictions. Prediction sets contain results of analyses to predict functions or traits of genomic features.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file_sets** | **List[str]** | The file set(s) required for this prediction set. | [optional] 
**small_scale_loci_list** | **List[object]** | A small scale (&lt;&#x3D;100) list of specific chromosomal region(s) whose functionality is investigated in this prediction set. This property describes the input variables of the prediction set. For example, this list consists of the genetic variants whose functionality is predicted in this prediction set. | [optional] 
**large_scale_loci_list** | **str** | A large scale list (&gt;100) of specific chromosomal regions whose functionality is investigated in this prediction set. This property describes the input variables of the prediction set. For example, this list consists of the genetic variants whose functionality is predicted in this prediction set. | [optional] 
**small_scale_gene_list** | **List[str]** | The specific, small scale list of (&lt;&#x3D;100) gene(s) whose functionality is investigated in this prediction set. This property describes the input variables of the prediction set. For example, this list consists of the genes whose expression level is predicted in this prediction set. It differs from assessed_genes (see more information under assessed_genes). | [optional] 
**large_scale_gene_list** | **str** | The large scale list of (&gt;100 genes) whose functionality is investigated in this prediction set. This property describes the input variables of the prediction set. For example, this list consists of the genes whose expression level is predicted in this prediction set. It differs from assessed_genes (see more information under assessed_genes). | [optional] 
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
**samples** | **List[str]** | The sample(s) associated with this file set. | [optional] 
**donors** | **List[str]** | The donor(s) associated with this file set. | [optional] 
**file_set_type** | **str** | The category that best describes this prediction set. | [optional] 
**scope** | **str** | The scope or scale that this prediction set is designed to target. If the scope is across gene(s) or loci, these will need to be specified in the genes or loci property. | [optional] 
**assessed_genes** | **List[str]** | A list of gene(s) assessed in this prediction set. This property is used to describe the gene(s) being investigated, especially how the input variables in the prediction set affect some critical functionality of the gene(s). For example, the effect could be predicted from genetic variants on the binding affinity of a transcription factor encoded by a gene (assessed_genes). It differs from small_scale_gene_list and large_scale_gene_list, as these are used when the input variables of the prediction set are genes. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the prediction set. | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_file_set_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 

## Example

```python
from igvf_client.models.prediction_set import PredictionSet

# TODO update the JSON string below
json = "{}"
# create an instance of PredictionSet from a JSON string
prediction_set_instance = PredictionSet.from_json(json)
# print the JSON string representation of the object
print(PredictionSet.to_json())

# convert the object into a dict
prediction_set_dict = prediction_set_instance.to_dict()
# create an instance of PredictionSet from a dict
prediction_set_from_dict = PredictionSet.from_dict(prediction_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


