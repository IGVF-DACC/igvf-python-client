# MultiplexedSample

A sample that is made by multiplexing multiple distinct samples.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**url** | **str** | An external resource with additional information. | [optional] 
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
**starting_amount** | **float** | The initial quantity of samples obtained. | [optional] 
**starting_amount_units** | **str** | The units used to quantify the amount of samples obtained. | [optional] 
**dbxrefs** | **List[str]** | Biosample identifiers from external resources, such as Biosample database or Cellosaurus. | [optional] 
**date_obtained** | **str** | The date the sample was harvested, dissected or created, depending on the type of the sample. | [optional] 
**sorted_from** | **str** | Links to a larger sample from which this sample was obtained through sorting. | [optional] 
**sorted_from_detail** | **str** | Detail for sample sorted into fractions capturing information about sorting. | [optional] 
**virtual** | **bool** | Virtual samples are not representing actual physical entities from experiments, but rather capturing metadata about hypothetical samples that the reported analysis results are relevant for. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets of the samples included in this multiplexed sample. | [optional] 
**moi** | **float** | The actual multiplicity of infection (MOI) for vectors introduced to this sample. At least one construct library set must be specified in order to specify MOI. This property should capture the actual MOI, and not the targeted MOI. | [optional] 
**nucleic_acid_delivery** | **str** | Method of introduction of nucleic acid into the cell. | [optional] 
**time_post_library_delivery** | **float** | The time that elapsed past the time-point when the construct library sets were introduced. | [optional] 
**time_post_library_delivery_units** | **str** | The units of time that elapsed past the point when the construct library sets were introduced. | [optional] 
**protocols** | **List[str]** | Links to the protocol(s) for preparing the samples on Protocols.io. | [optional] 
**supersedes** | **List[str]** | The sample(s) that this sample supersedes by virtue of being newer, better, or a fixed version of etc. than the one(s) it supersedes. | [optional] 
**multiplexed_samples** | **List[str]** | The samples multiplexed together to produce this sample. | [optional] 
**multiplexing_methods** | **List[str]** | The methods used for multiplexing and demultiplexing. | [optional] 
**cellular_sub_pool** | **str** | Cellular sub-pool fraction of the sample. Also known as PKR and sub-library. | [optional] 
**barcode_map** | **str** | The link to the barcode mapping tabular file. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of this sample. | [optional] 
**file_sets** | **List[str]** | The file sets linked to this sample. | [optional] 
**multiplexed_in** | **List[str]** | The multiplexed samples in which this sample is included. | [optional] 
**sorted_fractions** | **List[str]** | The fractions into which this sample has been sorted. | [optional] 
**origin_of** | **List[str]** | The samples which originate from this sample, such as through a process of cell differentiation. | [optional] 
**institutional_certificates** | **List[str]** | The institutional certificates of the samples included in this multiplexed sample. | [optional] 
**superseded_by** | **List[str]** | Sample(s) this sample is superseded by virtue of those sample(s) being newer, better, or a fixed version of etc. than this one. | [optional] 
**sample_terms** | **List[str]** | The sample terms of the samples included in this multiplexed sample. | [optional] 
**taxa** | **str** | The species of the organism. | [optional] 
**disease_terms** | **List[str]** | The disease terms of the samples included in this multiplexed sample. | [optional] 
**treatments** | **List[str]** | The treatments of the samples included in this multiplexed sample. | [optional] 
**modifications** | **List[str]** | The modifications of the samples included in this multiplexed sample. | [optional] 
**donors** | **List[str]** | The donors of the samples included in this multiplexed sample. | [optional] 
**biomarkers** | **List[str]** | The biomarkers of the samples included in this multiplexed sample. | [optional] 
**sources** | **List[str]** | The sources of the samples included in this multiplexed sample. | [optional] 
**classifications** | **List[str]** | The general category of this type of sample. | [optional] 

## Example

```python
from igvf_client.models.multiplexed_sample import MultiplexedSample

# TODO update the JSON string below
json = "{}"
# create an instance of MultiplexedSample from a JSON string
multiplexed_sample_instance = MultiplexedSample.from_json(json)
# print the JSON string representation of the object
print(MultiplexedSample.to_json())

# convert the object into a dict
multiplexed_sample_dict = multiplexed_sample_instance.to_dict()
# create an instance of MultiplexedSample from a dict
multiplexed_sample_from_dict = MultiplexedSample.from_dict(multiplexed_sample_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


