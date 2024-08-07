# MatrixFileResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[MatrixFile]**](MatrixFile.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.matrix_file_results import MatrixFileResults

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixFileResults from a JSON string
matrix_file_results_instance = MatrixFileResults.from_json(json)
# print the JSON string representation of the object
print(MatrixFileResults.to_json())

# convert the object into a dict
matrix_file_results_dict = matrix_file_results_instance.to_dict()
# create an instance of MatrixFileResults from a dict
matrix_file_results_from_dict = MatrixFileResults.from_dict(matrix_file_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


