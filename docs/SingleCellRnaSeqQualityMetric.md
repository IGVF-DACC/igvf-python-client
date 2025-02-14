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
**n_records** | **float** |  | [optional] 
**n_reads** | **float** |  | [optional] 
**n_barcodes** | **float** |  | [optional] 
**frac_reads_in_genes_library** | **float** |  | [optional] 
**total_umis** | **float** |  | [optional] 
**n_barcode_umis** | **float** |  | [optional] 
**median_reads_per_barcode** | **float** |  | [optional] 
**mean_reads_per_barcode** | **float** |  | [optional] 
**median_genes_per_barcode** | **float** |  | [optional] 
**median_umis_per_barcode** | **float** |  | [optional] 
**mean_umis_per_barcode** | **float** |  | [optional] 
**pct_duplicates** | **float** |  | [optional] 
**n_genes** | **float** |  | [optional] 
**frac_dup** | **float** |  | [optional] 
**frac_mito** | **float** |  | [optional] 
**frac_mito_genes** | **float** |  | [optional] 
**frac_reads_in_genes_barcode** | **float** |  | [optional] 
**joint_barcodes_passing** | **float** |  | [optional] 
**gt_records** | **float** |  | [optional] 
**num_barcodes_on_onlist** | **float** |  | [optional] 
**percentage_barcodes_on_onlist** | **float** |  | [optional] 
**num_reads_on_onlist** | **float** |  | [optional] 
**percentage_reads_on_onlist** | **float** |  | [optional] 
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


