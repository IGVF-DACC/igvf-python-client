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
**pct_cells_assigned_guide** | **float** | Percent Cells Assigned Guide | [optional] 
**avg_cells_per_target** | **float** | Average Cells Per Target | [optional] 
**moi** | **float** | Multiplicity Of Infection | [optional] 
**avg_umis_per_cell** | **float** | Average UMIs Per Cell | [optional] 
**total_guides** | **float** | Total Guides | [optional] 
**total_targets** | **float** | Total Targets | [optional] 
**guide_diversity** | **float** | Guide diversity (Gini index) | [optional] 
**mean_mitochondrial_reads** | **float** | Mean mitochondrial reads. | [optional] 
**total_reads** | **float** | Total reads (n_processed) reported by Kallisto. | [optional] 
**paired_reads_mapped** | **float** | Paired reads mapped (n_pseudoaligned) reported by Kallisto. | [optional] 
**alignment_percentage** | **float** | Alignment percentage (p_pseudoaligned) reported by Kallisto. | [optional] 
**total_detected_scrna_barcodes** | **float** | Unfiltered total detected scRNA barcodes (numBarcodes) reported by Kallisto. | [optional] 
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


