# Gene

A gene in the human or mouse genomes. The genes objects in IGVF are imported from GENCODE.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**transcriptome_annotation** | **str** | The annotation and version of the reference resource. | [optional] 
**taxa** | **str** | The species of the organism. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**geneid** | **str** | ENSEMBL GeneID of official nomenclature approved gene. The GeneID does not include the current version number suffix. | [optional] 
**symbol** | **str** | Gene symbol approved by the official nomenclature. | [optional] 
**name** | **str** | The full gene name preferably approved by the official nomenclature. | [optional] 
**synonyms** | **List[str]** | Alternative symbols that have been used to refer to the gene. | [optional] 
**dbxrefs** | **List[str]** | Unique identifiers from external resources. | [optional] 
**locations** | [**List[GeneLocation1]**](GeneLocation1.md) | Gene locations specified using 1-based, closed coordinates for different versions of reference genome assemblies. | [optional] 
**version_number** | **str** | Current ENSEMBL GeneID version number of the gene. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**geneid_with_version** | **str** | The ENSEMBL GeneID concatenated with its version number. | [optional] 

## Example

```python
from igvf_client.models.gene import Gene

# TODO update the JSON string below
json = "{}"
# create an instance of Gene from a JSON string
gene_instance = Gene.from_json(json)
# print the JSON string representation of the object
print(Gene.to_json())

# convert the object into a dict
gene_dict = gene_instance.to_dict()
# create an instance of Gene from a dict
gene_from_dict = Gene.from_dict(gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


