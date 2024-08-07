# TabularFile

A file containing textual data with a tabular structure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlled_access** | **bool** | Boolean value, indicating the file being controlled access, if true. | [optional] 
**anvil_url** | **str** | URL linking to the controlled access file that has been deposited at AnVIL workspace. | [optional] 
**assembly** | **str** | Genome assembly applicable for the tabular data. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**file_format_type** | **str** | The subtype of bed files. | [optional] 
**transcriptome_annotation** | **str** | The annotation and version of the reference resource. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**accession** | **str** | A unique identifier to be used to reference the object prefixed with IGVF. | [optional] 
**alternate_accessions** | **List[str]** | Accessions previously assigned to objects that have been merged with this object. | [optional] 
**collections** | **List[str]** | Some samples are part of particular data collections. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**revoke_detail** | **str** | Explanation of why an object was transitioned to the revoked status. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**analysis_step_version** | **str** | The analysis step version of the file. | [optional] 
**content_md5sum** | **str** | The MD5sum of the uncompressed file. | [optional] 
**content_type** | **str** | The type of content in the file. | [optional] 
**dbxrefs** | **List[str]** | Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file objects. | [optional] 
**derived_from** | **List[str]** | The files participating as inputs into software to produce this output file. | [optional] 
**file_format** | **str** | The file format or extension of the file. | [optional] 
**file_format_specifications** | **List[str]** | Document that further explains the file format. | [optional] 
**file_set** | **str** | The file set that this file belongs to. | [optional] 
**file_size** | **int** | File size specified in bytes. | [optional] 
**md5sum** | **str** | The md5sum of the file being transferred. | [optional] 
**submitted_file_name** | **str** | Original name of the file. | [optional] 
**upload_status** | **str** | The upload/validation status of the file. | [optional] 
**validation_error_detail** | **str** | Explanation of why the file failed the automated content checks. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the tabular file. | [optional] 
**integrated_in** | **List[str]** | Construct library set(s) that this file was used for in insert design. | [optional] 
**input_file_for** | **List[str]** | The files which are derived from this file. | [optional] 
**gene_list_for** | **List[str]** | File Set(s) that this file is a gene list for. | [optional] 
**loci_list_for** | **List[str]** | File Set(s) that this file is a loci list for. | [optional] 
**href** | **str** | The download path to obtain file. | [optional] 
**s3_uri** | **str** | The S3 URI of public file object. | [optional] 
**upload_credentials** | **object** | The upload credentials for S3 to submit the file content. | [optional] 

## Example

```python
from igvf_client.models.tabular_file import TabularFile

# TODO update the JSON string below
json = "{}"
# create an instance of TabularFile from a JSON string
tabular_file_instance = TabularFile.from_json(json)
# print the JSON string representation of the object
print(TabularFile.to_json())

# convert the object into a dict
tabular_file_dict = tabular_file_instance.to_dict()
# create an instance of TabularFile from a dict
tabular_file_from_dict = TabularFile.from_dict(tabular_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


