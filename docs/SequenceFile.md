# SequenceFile

A file containing sequencing results in bam, fastq, or pod5 formats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controlled_access** | **bool** | Boolean value, indicating the file being controlled access, if true. | [optional] 
**anvil_url** | **str** | URL linking to the controlled access file that has been deposited at AnVIL workspace. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
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
**flowcell_id** | **str** | The alphanumeric identifier for the flowcell of a sequencing machine. | [optional] 
**lane** | **int** | An integer identifying the lane of a sequencing machine. | [optional] 
**read_count** | **int** | Number of reads in a fastq file. | [optional] 
**minimum_read_length** | **int** | For high-throughput sequencing, the minimum number of contiguous nucleotides determined by sequencing. | [optional] 
**maximum_read_length** | **int** | For high-throughput sequencing, the maximum number of contiguous nucleotides determined by sequencing. | [optional] 
**mean_read_length** | **float** | For high-throughput sequencing, the mean number of contiguous nucleotides determined by sequencing. | [optional] 
**sequencing_platform** | **str** | The measurement device used to produce sequencing data. | [optional] 
**sequencing_kit** | **str** | A reagent kit used with a library to prepare it for sequencing. | [optional] 
**sequencing_run** | **int** | An ordinal number indicating which sequencing run of the associated library that the file belongs to. | [optional] 
**illumina_read_type** | **str** | The read type of the file. Relevant only for files produced using an Illumina sequencing platform. | [optional] 
**index** | **str** | An Illumina index associated with the file. | [optional] 
**base_modifications** | **List[str]** | The chemical modifications to bases in a DNA sequence that are detected in this file. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the sequence file. | [optional] 
**integrated_in** | **List[str]** | Construct library set(s) that this file was used for in insert design. | [optional] 
**input_file_for** | **List[str]** | The files which are derived from this file. | [optional] 
**gene_list_for** | **List[str]** | File Set(s) that this file is a gene list for. | [optional] 
**loci_list_for** | **List[str]** | File Set(s) that this file is a loci list for. | [optional] 
**href** | **str** | The download path to obtain file. | [optional] 
**s3_uri** | **str** | The S3 URI of public file object. | [optional] 
**upload_credentials** | **object** | The upload credentials for S3 to submit the file content. | [optional] 
**seqspecs** | **List[str]** | Link(s) to the associated seqspec YAML configuration file(s). | [optional] 

## Example

```python
from igvf_client.models.sequence_file import SequenceFile

# TODO update the JSON string below
json = "{}"
# create an instance of SequenceFile from a JSON string
sequence_file_instance = SequenceFile.from_json(json)
# print the JSON string representation of the object
print(SequenceFile.to_json())

# convert the object into a dict
sequence_file_dict = sequence_file_instance.to_dict()
# create an instance of SequenceFile from a dict
sequence_file_from_dict = SequenceFile.from_dict(sequence_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


