# PublicationResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Publication]**](Publication.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.publication_results import PublicationResults

# TODO update the JSON string below
json = "{}"
# create an instance of PublicationResults from a JSON string
publication_results_instance = PublicationResults.from_json(json)
# print the JSON string representation of the object
print(PublicationResults.to_json())

# convert the object into a dict
publication_results_dict = publication_results_instance.to_dict()
# create an instance of PublicationResults from a dict
publication_results_from_dict = PublicationResults.from_dict(publication_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


