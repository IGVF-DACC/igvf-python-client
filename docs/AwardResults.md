# AwardResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Award]**](Award.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.award_results import AwardResults

# TODO update the JSON string below
json = "{}"
# create an instance of AwardResults from a JSON string
award_results_instance = AwardResults.from_json(json)
# print the JSON string representation of the object
print(AwardResults.to_json())

# convert the object into a dict
award_results_dict = award_results_instance.to_dict()
# create an instance of AwardResults from a dict
award_results_from_dict = AwardResults.from_dict(award_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


