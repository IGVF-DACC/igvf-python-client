# InVitroSystem

A biosample that is cultured, such as immortalized cell lines, organoids, or samples that have been differentiated or reprogrammed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**taxa** | **str** | The species of the organism. | [optional] 
**url** | **str** | An external resource with additional information. | [optional] 
**sources** | **List[str]** | The originating lab(s) or vendor(s). | [optional] 
**lot_id** | **str** | The lot identifier provided by the originating lab or vendor. | [optional] 
**product_id** | **str** | The product identifier provided by the originating lab or vendor. | [optional] 
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
**lower_bound_age** | **float** | Lower bound of age of the organism at the time of collection of the sample. | [optional] 
**upper_bound_age** | **float** | Upper bound of age of the organism at the time of collection of the sample. | [optional] 
**age_units** | **str** | The units of time associated with age of the biosample. | [optional] 
**sample_terms** | **List[str]** | Ontology terms identifying a biosample. | [optional] 
**disease_terms** | **List[str]** | Ontology term of the disease associated with the biosample. | [optional] 
**pooled_from** | **List[str]** | The biosamples this biosample is pooled from. | [optional] 
**part_of** | **str** | Links to a biosample which represents a larger sample from which this sample was taken regardless of whether it is a tissue taken from an organism or smaller slices of a piece of tissue or aliquots of a cell growth. | [optional] 
**originated_from** | **str** | Links to a biosample that was originated from due to differentiation, dedifferentiation, reprogramming, or the introduction of a genetic modification. | [optional] 
**treatments** | **List[str]** | A list of treatments applied to the biosample with the purpose of perturbation. | [optional] 
**donors** | **List[str]** | Donor(s) the sample was derived from. | [optional] 
**biomarkers** | **List[str]** | Biological markers that are associated with this sample. | [optional] 
**embryonic** | **bool** | Biosample is embryonic. | [optional] 
**modifications** | **List[str]** | Links to modifications applied to this biosample. | [optional] 
**cellular_sub_pool** | **str** | Cellular sub-pool fraction of the sample. Also known as PKR and sub-library. | [optional] 
**starting_amount** | **float** | The initial quantity of samples obtained. | [optional] 
**starting_amount_units** | **str** | The units used to quantify the amount of samples obtained. | [optional] 
**dbxrefs** | **List[str]** | Biosample identifiers from external resources, such as Biosample database or Cellosaurus. | [optional] 
**date_obtained** | **str** | The date the sample was harvested, dissected or created, depending on the type of the sample. | [optional] 
**sorted_from** | **str** | Links to a larger sample from which this sample was obtained through sorting. | [optional] 
**sorted_from_detail** | **str** | Detail for sample sorted into fractions capturing information about sorting. | [optional] 
**virtual** | **bool** | Virtual samples are not representing actual physical entities from experiments, but rather capturing metadata about hypothetical samples that the reported analysis results are relevant for. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets of vectors introduced to this sample prior to performing an assay. | [optional] 
**moi** | **float** | The actual multiplicity of infection (MOI) for vectors introduced to this sample. At least one construct library set must be specified in order to specify MOI. This property should capture the actual MOI, and not the targeted MOI. | [optional] 
**nucleic_acid_delivery** | **str** | Method of introduction of nucleic acid into the cell. | [optional] 
**time_post_library_delivery** | **float** | The time that elapsed past the time-point when the construct library sets were introduced. | [optional] 
**time_post_library_delivery_units** | **str** | The units of time that elapsed past the point when the construct library sets were introduced. | [optional] 
**protocols** | **List[str]** | Links to the protocol(s) for preparing the samples on Protocols.io. | [optional] 
**classifications** | **List[str]** | The general category of this type of in vitro system. | [optional] 
**time_post_change** | **float** | The time that elapsed past the time-point when the cell fate change treatments were introduced. | [optional] 
**time_post_change_units** | **str** | The units of time that elapsed past the point when the cell fate change treatments were introduced. | [optional] 
**cell_fate_change_treatments** | **List[str]** | A list of treatments applied to the biosample with the purpose of differentiation, dedifferentiation, or reprogramming. | [optional] 
**cell_fate_change_protocol** | **str** | A protocol applied to the biosample with the purpose of differentiation, dedifferentiation, or reprogramming. | [optional] 
**demultiplexed_from** | **str** | The biosample this in vitro system sample was demultiplexed from using computational methods. | [optional] 
**passage_number** | **int** | Number of passages including the passages from the source. | [optional] 
**targeted_sample_term** | **str** | Ontology term identifying the targeted endpoint biosample resulting from differentation or reprogramming. | [optional] 
**growth_medium** | **str** | A growth medium of the in vitro system. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the sample. | [optional] 
**file_sets** | **List[str]** | The file sets linked to this sample. | [optional] 
**multiplexed_in** | **List[str]** | The multiplexed samples in which this sample is included. | [optional] 
**sorted_fractions** | **List[str]** | The fractions into which this sample has been sorted. | [optional] 
**origin_of** | **List[str]** | The samples which originate from this sample, such as through a process of cell differentiation. | [optional] 
**institutional_certificates** | **List[str]** | The institutional certificates under which use of this sample is approved. | [optional] 
**sex** | **str** |  | [optional] 
**age** | **str** | Age of organism at the time of collection of the sample. | [optional] 
**upper_bound_age_in_hours** | **float** | Upper bound of age of organism in hours at the time of collection of the sample. | [optional] 
**lower_bound_age_in_hours** | **float** | Lower bound of age of organism in hours at the time of collection of the sample . | [optional] 
**parts** | **List[str]** | The parts into which this sample has been divided. | [optional] 
**pooled_in** | **List[str]** | The pooled samples in which this sample is included. | [optional] 
**demultiplexed_to** | **List[str]** | The parts into which this sample has been demultiplexed. | [optional] 

## Example

```python
from igvf_client.models.in_vitro_system import InVitroSystem

# TODO update the JSON string below
json = "{}"
# create an instance of InVitroSystem from a JSON string
in_vitro_system_instance = InVitroSystem.from_json(json)
# print the JSON string representation of the object
print(InVitroSystem.to_json())

# convert the object into a dict
in_vitro_system_dict = in_vitro_system_instance.to_dict()
# create an instance of InVitroSystem from a dict
in_vitro_system_from_dict = InVitroSystem.from_dict(in_vitro_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


