# SingleCellRnaSeqQualityMetric

Schema for submission of a scRNA-seq uniform pipeline quality metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The status of the metadata object. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**attachment** | [**Attachment**](Attachment.md) |  | [optional] 
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
**quality_metric_of** | **List[str]** | The file(s) to which this quality metric applies. | [optional] 
**analysis_step_version** | **str** | The analysis step version of the quality metric. | [optional] 
**n_records** | **float** | Number of records in BUS file. | [optional] 
**n_reads** | **float** | Total number of input reads. | [optional] 
**n_barcodes** | **float** | Total number of valid cell barcodes detected. | [optional] 
**total_umis** | **float** | Total number of UMIs detected. | [optional] 
**n_barcode_umis** | **float** | Total number of UMIs associated with cell barcodes. | [optional] 
**median_reads_per_barcode** | **float** | Median number of reads per cell barcode. | [optional] 
**mean_reads_per_barcode** | **float** | Mean number of reads per cell barcode. | [optional] 
**median_umis_per_barcode** | **float** | Median number of UMIs per cell barcode. | [optional] 
**mean_umis_per_barcode** | **float** | Mean number of UMIs per cell barcode. | [optional] 
**gt_records** | **float** | Number of BUS records for Good-Toulmin estimation. | [optional] 
**num_barcodes_on_onlist** | **float** | Number of cell barcodes matching an expected list of barcodes (onlist). | [optional] 
**percentage_barcodes_on_onlist** | **float** | Percentage of cell barcodes matching an expected list of barcodes (onlist). | [optional] 
**num_reads_on_onlist** | **float** | Number of reads associated with barcodes on the onlist. | [optional] 
**percentage_reads_on_onlist** | **float** | Percentage of reads associated with barcodes on the onlist. | [optional] 
**rnaseq_kb_info** | [**RNASeqKBInfo**](RNASeqKBInfo.md) |  | [optional] 
**n_targets** | **float** | Total number of target sequences (e.g., transcripts) in the index. | [optional] 
**n_bootstraps** | **float** | Number of bootstrap iterations used to estimate expression uncertainty. | [optional] 
**n_processed** | **float** | Number of valid reads processed by Kallisto. | [optional] 
**n_pseudoaligned** | **float** | Number of reads that could be pseudoaligned to the transcriptome index. | [optional] 
**n_unique** | **float** | Number of reads that could be pseudoaligned to a unique target sequence. | [optional] 
**p_pseudoaligned** | **float** | Percentage of reads that could be pseudoaligned to the transcriptome index. | [optional] 
**p_unique** | **float** | Percentage of reads that could be pseudoaligned to a unique target sequence. | [optional] 
**index_version** | **float** | Version of Kallisto index command used for building the transcriptome index. | [optional] 
**kmer_length** | **float** | Length of k-mers used for building the transcriptome index. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the quality metric. | [optional] 

## Example

```python
from igvf_client.models.single_cell_rna_seq_quality_metric import SingleCellRnaSeqQualityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SingleCellRnaSeqQualityMetric from a JSON string
single_cell_rna_seq_quality_metric_instance = SingleCellRnaSeqQualityMetric.from_json(json)
# print the JSON string representation of the object
print(SingleCellRnaSeqQualityMetric.to_json())

# convert the object into a dict
single_cell_rna_seq_quality_metric_dict = single_cell_rna_seq_quality_metric_instance.to_dict()
# create an instance of SingleCellRnaSeqQualityMetric from a dict
single_cell_rna_seq_quality_metric_from_dict = SingleCellRnaSeqQualityMetric.from_dict(single_cell_rna_seq_quality_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


