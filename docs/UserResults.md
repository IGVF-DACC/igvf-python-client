# UserResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[User]**](User.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.user_results import UserResults

# TODO update the JSON string below
json = "{}"
# create an instance of UserResults from a JSON string
user_results_instance = UserResults.from_json(json)
# print the JSON string representation of the object
print(UserResults.to_json())

# convert the object into a dict
user_results_dict = user_results_instance.to_dict()
# create an instance of UserResults from a dict
user_results_from_dict = UserResults.from_dict(user_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


