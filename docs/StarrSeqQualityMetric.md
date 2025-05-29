# StarrSeqQualityMetric

Schema for submission of a STARR-seq uniform pipeline quality metric.

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
**coverage** | **float** | Coverage of the library. | [optional] 
**coverage_per_basepair** | **float** | Coverage at basepair level. | [optional] 
**rna_correlation_in_peaks** | **float** | Correlation of RNA only over regions called as peaks in DNA. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the quality metric. | [optional] 

## Example

```python
from igvf_client.models.starr_seq_quality_metric import StarrSeqQualityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of StarrSeqQualityMetric from a JSON string
starr_seq_quality_metric_instance = StarrSeqQualityMetric.from_json(json)
# print the JSON string representation of the object
print(StarrSeqQualityMetric.to_json())

# convert the object into a dict
starr_seq_quality_metric_dict = starr_seq_quality_metric_instance.to_dict()
# create an instance of StarrSeqQualityMetric from a dict
starr_seq_quality_metric_from_dict = StarrSeqQualityMetric.from_dict(starr_seq_quality_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


