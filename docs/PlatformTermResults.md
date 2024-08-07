# PlatformTermResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[PlatformTerm]**](PlatformTerm.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.platform_term_results import PlatformTermResults

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformTermResults from a JSON string
platform_term_results_instance = PlatformTermResults.from_json(json)
# print the JSON string representation of the object
print(PlatformTermResults.to_json())

# convert the object into a dict
platform_term_results_dict = platform_term_results_instance.to_dict()
# create an instance of PlatformTermResults from a dict
platform_term_results_from_dict = PlatformTermResults.from_dict(platform_term_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


