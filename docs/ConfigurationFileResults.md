# ConfigurationFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[ConfigurationFile]**](ConfigurationFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.configuration_file_results import ConfigurationFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationFileResults from a JSON string
configuration_file_results_instance = ConfigurationFileResults.from_json(json)
# print the JSON string representation of the object
print(ConfigurationFileResults.to_json())

# convert the object into a dict
configuration_file_results_dict = configuration_file_results_instance.to_dict()
# create an instance of ConfigurationFileResults from a dict
configuration_file_results_from_dict = ConfigurationFileResults.from_dict(configuration_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


