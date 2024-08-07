# SourceResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Source]**](Source.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.source_results import SourceResults

# TODO update the JSON string below
json = "{}"
# create an instance of SourceResults from a JSON string
source_results_instance = SourceResults.from_json(json)
# print the JSON string representation of the object
print(SourceResults.to_json())

# convert the object into a dict
source_results_dict = source_results_instance.to_dict()
# create an instance of SourceResults from a dict
source_results_from_dict = SourceResults.from_dict(source_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


