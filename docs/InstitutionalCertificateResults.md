# InstitutionalCertificateResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[InstitutionalCertificate]**](InstitutionalCertificate.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.institutional_certificate_results import InstitutionalCertificateResults

# TODO update the JSON string below
json = "{}"
# create an instance of InstitutionalCertificateResults from a JSON string
institutional_certificate_results_instance = InstitutionalCertificateResults.from_json(json)
# print the JSON string representation of the object
print(InstitutionalCertificateResults.to_json())

# convert the object into a dict
institutional_certificate_results_dict = institutional_certificate_results_instance.to_dict()
# create an instance of InstitutionalCertificateResults from a dict
institutional_certificate_results_from_dict = InstitutionalCertificateResults.from_dict(institutional_certificate_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


