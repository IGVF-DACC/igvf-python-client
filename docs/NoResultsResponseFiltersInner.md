# NoResultsResponseFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**term** | **str** |  | [optional] 
**remove** | **str** |  | [optional] 

## Example

```python
from igvf_client.models.no_results_response_filters_inner import NoResultsResponseFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of NoResultsResponseFiltersInner from a JSON string
no_results_response_filters_inner_instance = NoResultsResponseFiltersInner.from_json(json)
# print the JSON string representation of the object
print(NoResultsResponseFiltersInner.to_json())

# convert the object into a dict
no_results_response_filters_inner_dict = no_results_response_filters_inner_instance.to_dict()
# create an instance of NoResultsResponseFiltersInner from a dict
no_results_response_filters_inner_from_dict = NoResultsResponseFiltersInner.from_dict(no_results_response_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


