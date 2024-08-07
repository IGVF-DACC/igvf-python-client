# DocumentResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Document]**](Document.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.document_results import DocumentResults

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResults from a JSON string
document_results_instance = DocumentResults.from_json(json)
# print the JSON string representation of the object
print(DocumentResults.to_json())

# convert the object into a dict
document_results_dict = document_results_instance.to_dict()
# create an instance of DocumentResults from a dict
document_results_from_dict = DocumentResults.from_dict(document_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


