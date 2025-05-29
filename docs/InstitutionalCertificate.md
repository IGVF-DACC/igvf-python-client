# InstitutionalCertificate

An institutional certificate defining the data sharing limitations for data authorized for submission to the IGVF portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
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
**certificate_identifier** | **str** | A unique identifier for the certificate. | [optional] 
**controlled_access** | **bool** | Indicator of whether the samples are under controlled access. | [optional] 
**data_use_limitation** | **str** | Code indicating the limitations on data use for data generated from the applicable samples. | [optional] 
**data_use_limitation_modifiers** | **List[str]** | Code indicating a modifier on the limitations on data use for data generated from the applicable samples. | [optional] 
**samples** | **List[str]** | Samples covered by this institutional certificate. | [optional] 
**urls** | **List[str]** | Link to the institutional certification form. | [optional] 
**partner_labs** | **List[str]** | Labs which belong to same institution as the signing PI and can share this institutional certificate. | [optional] 
**partner_awards** | **List[str]** | Awards granted to at least one lab that belongs to same institution as the signing PI and can share this institutional certificate. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** | A summary of the institutional certificate. | [optional] 
**data_use_limitation_summary** | **str** | A combination of the data use limitation and its modifiers | [optional] 

## Example

```python
from igvf_client.models.institutional_certificate import InstitutionalCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionalCertificate from a JSON string
institutional_certificate_instance = InstitutionalCertificate.from_json(json)
# print the JSON string representation of the object
print(InstitutionalCertificate.to_json())

# convert the object into a dict
institutional_certificate_dict = institutional_certificate_instance.to_dict()
# create an instance of InstitutionalCertificate from a dict
institutional_certificate_from_dict = InstitutionalCertificate.from_dict(institutional_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


