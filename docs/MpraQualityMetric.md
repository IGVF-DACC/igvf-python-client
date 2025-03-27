# MpraQualityMetric

Schema for submission of a MPRA uniform pipeline quality metric.

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
**pearson_correlation** | **float** | The correlation of log2 RNA/DNA ratios across tested sequences as a measure of replicable activity signal. Value is the median of replicate comparisons using only oligos with &gt;&#x3D; 10 barcodes. | [optional] 
**median_barcodes_passing_filtering** | **float** | Median number of barcodes across tested sequences that passed filtering to determine if there was sufficient barcode to oligo coverage. Value is the median of all replicates. | [optional] 
**median_rna_read_count** | **float** | Median of RNA read count for oligos that passed filtering to determine sufficient coverage in terms of read count. Value is the median of all replicates. | [optional] 
**fraction_oligos_passing** | **float** | Fraction of tested sequences that passed filtering of the mappable sequences to determine if the designed library was sufficiently recovered. Value is the median of all replicates. | [optional] 
**median_assigned_barcodes** | **float** | Median number of barcodes assigned to tested sequences in mapping as a quality control measure for the assignment step, whether there is sufficient barcode to oligo coverage. | [optional] 
**fraction_assigned_oligos** | **float** | Fraction of assigned tested sequences in mapping to determine if the library during the assignment step was sufficiently recovered. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the quality metric. | [optional] 

## Example

```python
from igvf_client.models.mpra_quality_metric import MpraQualityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of MpraQualityMetric from a JSON string
mpra_quality_metric_instance = MpraQualityMetric.from_json(json)
# print the JSON string representation of the object
print(MpraQualityMetric.to_json())

# convert the object into a dict
mpra_quality_metric_dict = mpra_quality_metric_instance.to_dict()
# create an instance of MpraQualityMetric from a dict
mpra_quality_metric_from_dict = MpraQualityMetric.from_dict(mpra_quality_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


