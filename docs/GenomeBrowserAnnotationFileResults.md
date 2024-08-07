# GenomeBrowserAnnotationFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[GenomeBrowserAnnotationFile]**](GenomeBrowserAnnotationFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.genome_browser_annotation_file_results import GenomeBrowserAnnotationFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of GenomeBrowserAnnotationFileResults from a JSON string
genome_browser_annotation_file_results_instance = GenomeBrowserAnnotationFileResults.from_json(json)
# print the JSON string representation of the object
print(GenomeBrowserAnnotationFileResults.to_json())

# convert the object into a dict
genome_browser_annotation_file_results_dict = genome_browser_annotation_file_results_instance.to_dict()
# create an instance of GenomeBrowserAnnotationFileResults from a dict
genome_browser_annotation_file_results_from_dict = GenomeBrowserAnnotationFileResults.from_dict(genome_browser_annotation_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


