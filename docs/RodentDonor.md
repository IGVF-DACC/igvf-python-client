# RodentDonor

A rodent donor of a biosample. Submission of any sample originating from a rodent donor requires submission of information about the relevant donor. The rodent donor can be a generic representative of an inbred strain, or a unique, individual mouse. For example, submission of a B6 mouse donor is a prerequisite for submission of any B6 mouse samples.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_timestamp** | **str** | The date the object was released. | [optional] 
**taxa** | **str** | The species of the organism. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
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
**dbxrefs** | **List[str]** | Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF donors. | [optional] 
**sex** | **str** | Sex of the donor. | [optional] 
**phenotypic_features** | **List[str]** | A list of associated phenotypic features of the donor. | [optional] 
**virtual** | **bool** | Virtual donors are not representing actual human or model organism donors, samples coming from which were used in experiments, but rather capturing metadata about hypothetical donors that the reported analysis results are relevant for. | [optional] 
**strain_background** | **str** | The specific parent strain designation of a non-human donor. | [optional] 
**strain** | **str** | The specific strain designation of a non-human donor. | [optional] 
**genotype** | **str** | The genotype of the strain according to accepted nomenclature conventions. | [optional] 
**individual_rodent** | **bool** | This rodent donor represents an individual rodent. | [optional] 
**rodent_identifier** | **str** | The identifier for this individual rodent donor. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the rodent donor. | [optional] 

## Example

```python
from igvf_client.models.rodent_donor import RodentDonor

# TODO update the JSON string below
json = "{}"
# create an instance of RodentDonor from a JSON string
rodent_donor_instance = RodentDonor.from_json(json)
# print the JSON string representation of the object
print(RodentDonor.to_json())

# convert the object into a dict
rodent_donor_dict = rodent_donor_instance.to_dict()
# create an instance of RodentDonor from a dict
rodent_donor_from_dict = RodentDonor.from_dict(rodent_donor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


