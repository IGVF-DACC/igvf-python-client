# AccessKeyResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[AccessKey]**](AccessKey.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.access_key_results import AccessKeyResults

# TODO update the JSON string below
json = "{}"
# create an instance of AccessKeyResults from a JSON string
access_key_results_instance = AccessKeyResults.from_json(json)
# print the JSON string representation of the object
print(AccessKeyResults.to_json())

# convert the object into a dict
access_key_results_dict = access_key_results_instance.to_dict()
# create an instance of AccessKeyResults from a dict
access_key_results_from_dict = AccessKeyResults.from_dict(access_key_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


