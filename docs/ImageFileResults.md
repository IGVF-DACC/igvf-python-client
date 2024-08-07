# ImageFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ImageFile]**](ImageFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.image_file_results import ImageFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of ImageFileResults from a JSON string
image_file_results_instance = ImageFileResults.from_json(json)
# print the JSON string representation of the object
print(ImageFileResults.to_json())

# convert the object into a dict
image_file_results_dict = image_file_results_instance.to_dict()
# create an instance of ImageFileResults from a dict
image_file_results_from_dict = ImageFileResults.from_dict(image_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


