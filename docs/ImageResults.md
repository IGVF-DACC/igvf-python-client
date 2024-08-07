# ImageResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[Image]**](Image.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.image_results import ImageResults

# TODO update the JSON string below
json = "{}"
# create an instance of ImageResults from a JSON string
image_results_instance = ImageResults.from_json(json)
# print the JSON string representation of the object
print(ImageResults.to_json())

# convert the object into a dict
image_results_dict = image_results_instance.to_dict()
# create an instance of ImageResults from a dict
image_results_from_dict = ImageResults.from_dict(image_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


