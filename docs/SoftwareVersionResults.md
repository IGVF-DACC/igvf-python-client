# SoftwareVersionResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[SoftwareVersion]**](SoftwareVersion.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.software_version_results import SoftwareVersionResults

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareVersionResults from a JSON string
software_version_results_instance = SoftwareVersionResults.from_json(json)
# print the JSON string representation of the object
print(SoftwareVersionResults.to_json())

# convert the object into a dict
software_version_results_dict = software_version_results_instance.to_dict()
# create an instance of SoftwareVersionResults from a dict
software_version_results_from_dict = SoftwareVersionResults.from_dict(software_version_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


