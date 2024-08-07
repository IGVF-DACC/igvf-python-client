# SearchFacet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**terms** | **List[object]** |  | [optional] 

## Example

```python
from igvf_client.models.search_facet import SearchFacet

# TODO update the JSON string below
json = "{}"
# create an instance of SearchFacet from a JSON string
search_facet_instance = SearchFacet.from_json(json)
# print the JSON string representation of the object
print(SearchFacet.to_json())

# convert the object into a dict
search_facet_dict = search_facet_instance.to_dict()
# create an instance of SearchFacet from a dict
search_facet_from_dict = SearchFacet.from_dict(search_facet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


