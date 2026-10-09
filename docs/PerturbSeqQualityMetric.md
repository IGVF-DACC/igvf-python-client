# PerturbSeqQualityMetric

Schema for submission of a Perturb-seq uniform pipeline quality metric.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
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
**total_cells_passing_filters** | **float** | Total Cells Passing Filters | [optional] 
**frac_cells_with_guide** | **float** | Fraction of cells with at least one assigned guide. | [optional] 
**avg_cells_per_guide** | **float** | Average number of cells assigned to each guide. | [optional] 
**observed_moi** | **float** | The multiplicity of infection (MOI) derived from the Perturb-seq pipeline output. This property is distinct from the experimentally reported &#x60;moi&#x60; property on the sample. | [optional] 
**avg_umis_per_cell** | **float** | Average UMIs Per Cell | [optional] 
**total_guides** | **float** | Total Guides | [optional] 
**umi_median** | **float** | Median total gene UMIs per cell after filtering. | [optional] 
**genes_median** | **float** | Median number of expressed genes per cell after filtering. | [optional] 
**n_cells_with_guide** | **float** | Number of cells with at least one assigned guide. | [optional] 
**n_cells_exactly_1_guide** | **float** | Number of cells with exactly one assigned guide. | [optional] 
**guide_umi_mean** | **float** | Mean total guide UMIs per cell after filtering. | [optional] 
**mean_percent_mitochondrial** | **float** | Mean percent mitochondrial UMIs per cell. | [optional] 
**n_targets** | **float** | Total number of target sequences (e.g., transcripts) in the index. | [optional] 
**total_reads** | **float** | Total reads (n_processed) reported by Kallisto. | [optional] 
**paired_reads_mapped** | **float** | Paired reads mapped (n_pseudoaligned) reported by Kallisto. | [optional] 
**alignment_percentage** | **float** | Alignment percentage (p_pseudoaligned) reported by Kallisto. | [optional] 
**total_detected_scrna_barcodes** | **float** | Unfiltered total detected scRNA barcodes (numBarcodes) reported by Kallisto. | [optional] 
**n_unique** | **float** | Number of reads that could be pseudoaligned to a unique target sequence. | [optional] 
**p_unique** | **float** | Percentage of reads that could be pseudoaligned to a unique target sequence. | [optional] 
**percentage_barcodes_on_onlist** | **float** | Percentage of cell barcodes matching an expected list of barcodes (onlist). | [optional] 
**percentage_reads_on_onlist** | **float** | Percentage of reads associated with barcodes on the onlist. | [optional] 
**mean_umis_per_barcode** | **float** | Mean number of UMIs per cell barcode. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the quality metric. | [optional] 

## Example

```python
from igvf_client.models.perturb_seq_quality_metric import PerturbSeqQualityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of PerturbSeqQualityMetric from a JSON string
perturb_seq_quality_metric_instance = PerturbSeqQualityMetric.from_json(json)
# print the JSON string representation of the object
print(PerturbSeqQualityMetric.to_json())

# convert the object into a dict
perturb_seq_quality_metric_dict = perturb_seq_quality_metric_instance.to_dict()
# create an instance of PerturbSeqQualityMetric from a dict
perturb_seq_quality_metric_from_dict = PerturbSeqQualityMetric.from_dict(perturb_seq_quality_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


