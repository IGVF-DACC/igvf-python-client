# MatrixFile

A file containing quantification data in a multi-dimension format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**reference_files** | **List[str]** | Link to the reference files used to generate this file. | [optional] 
**filtered** | **bool** | Indicates whether the file has gone through some filtering step, for example, removal of PCR duplicates or filtering based on significance calling. | [optional] 
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
**derived_manually** | **bool** | A boolean indicating whether the file has been dervided manually without automated computational methods. | [optional] 
**file_format** | **str** | The file format or extension of the file. | [optional] 
**file_format_specifications** | **List[str]** | Documents that describe the file format and fields of this file. | [optional] 
**file_set** | **str** | The file set that this file belongs to. | [optional] 
**file_size** | **int** | File size specified in bytes. | [optional] 
**md5sum** | **str** | The md5sum of the file being transferred. | [optional] 
**submitted_file_name** | **str** | Original name of the file. | [optional] 
**upload_status** | **str** | The upload/validation status of the file. | [optional] 
**validation_error_detail** | **str** | Explanation of why the file failed the automated content checks. | [optional] 
**checkfiles_version** | **str** | The Checkfiles GitHub version release the file was validated with. | [optional] 
**principal_dimension** | **str** | The principal dimension of the matrix. | [optional] 
**secondary_dimensions** | **List[str]** | The secondary, tertiary....n levels of dimensions of the matrix. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the matrix file. | [optional] 
**integrated_in** | **List[str]** | Construct library set(s) that this file was used for in insert design. | [optional] 
**input_file_for** | **List[str]** | The files which are derived from this file. | [optional] 
**gene_list_for** | **List[str]** | File Set(s) that this file is a gene list for. | [optional] 
**loci_list_for** | **List[str]** | File Set(s) that this file is a loci list for. | [optional] 
**quality_metrics** | **List[str]** | The quality metrics that are associated with this file. | [optional] 
**assay_titles** | **List[str]** | Title(s) of assay from the file set this file belongs to. | [optional] 
**workflow** | **str** | The workflow used to produce this file. | [optional] 
**href** | **str** | The download path to obtain file. | [optional] 
**s3_uri** | **str** | The S3 URI of public file object. | [optional] 
**upload_credentials** | **object** | The upload credentials for S3 to submit the file content. | [optional] 
**content_summary** | **str** | A summary of the data in the matrix file. | [optional] 
**transcriptome_annotation** | **str** | The annotation and version of the reference resource. | [optional] 
**assembly** | **str** | The assembly associated with the matrix file. | [optional] 

## Example

```python
from igvf_client.models.matrix_file import MatrixFile

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixFile from a JSON string
matrix_file_instance = MatrixFile.from_json(json)
# print the JSON string representation of the object
print(MatrixFile.to_json())

# convert the object into a dict
matrix_file_dict = matrix_file_instance.to_dict()
# create an instance of MatrixFile from a dict
matrix_file_from_dict = MatrixFile.from_dict(matrix_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


