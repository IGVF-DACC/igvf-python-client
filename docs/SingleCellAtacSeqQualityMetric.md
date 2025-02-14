# SingleCellAtacSeqQualityMetric

Schema for submission of a scATAC-seq uniform pipeline quality metric.

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
**tsse** | **float** |  | [optional] 
**n_fragments** | **float** |  | [optional] 
**n_barcodes** | **float** |  | [optional] 
**pct_duplicates** | **float** |  | [optional] 
**n_fragment** | **float** |  | [optional] 
**frac_dup** | **float** |  | [optional] 
**frac_mito** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**duplicate** | **float** |  | [optional] 
**unmapped** | **float** |  | [optional] 
**lowmapq** | **float** |  | [optional] 
**joint_barcodes_passing** | **float** |  | [optional] 
**n_reads** | **float** |  | [optional] 
**n_mapped_reads** | **float** |  | [optional] 
**n_uniquely_mapped_reads** | **float** |  | [optional] 
**n_reads_with_multi_mappings** | **float** |  | [optional] 
**n_candidates** | **float** |  | [optional] 
**n_mappings** | **float** |  | [optional] 
**n_uni_mappings** | **float** |  | [optional] 
**n_multi_mappings** | **float** |  | [optional] 
**n_barcodes_on_onlist** | **float** |  | [optional] 
**n_corrected_barcodes** | **float** |  | [optional] 
**n_output_mappings** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the quality metric. | [optional] 

## Example

```python
from igvf_client.models.single_cell_atac_seq_quality_metric import SingleCellAtacSeqQualityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SingleCellAtacSeqQualityMetric from a JSON string
single_cell_atac_seq_quality_metric_instance = SingleCellAtacSeqQualityMetric.from_json(json)
# print the JSON string representation of the object
print(SingleCellAtacSeqQualityMetric.to_json())

# convert the object into a dict
single_cell_atac_seq_quality_metric_dict = single_cell_atac_seq_quality_metric_instance.to_dict()
# create an instance of SingleCellAtacSeqQualityMetric from a dict
single_cell_atac_seq_quality_metric_from_dict = SingleCellAtacSeqQualityMetric.from_dict(single_cell_atac_seq_quality_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


