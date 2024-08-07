# OpenReadingFrameResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[OpenReadingFrame]**](OpenReadingFrame.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.open_reading_frame_results import OpenReadingFrameResults

# TODO update the JSON string below
json = "{}"
# create an instance of OpenReadingFrameResults from a JSON string
open_reading_frame_results_instance = OpenReadingFrameResults.from_json(json)
# print the JSON string representation of the object
print(OpenReadingFrameResults.to_json())

# convert the object into a dict
open_reading_frame_results_dict = open_reading_frame_results_instance.to_dict()
# create an instance of OpenReadingFrameResults from a dict
open_reading_frame_results_from_dict = OpenReadingFrameResults.from_dict(open_reading_frame_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


