# MeasurementSetResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[MeasurementSet]**](MeasurementSet.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.measurement_set_results import MeasurementSetResults

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSetResults from a JSON string
measurement_set_results_instance = MeasurementSetResults.from_json(json)
# print the JSON string representation of the object
print(MeasurementSetResults.to_json())

# convert the object into a dict
measurement_set_results_dict = measurement_set_results_instance.to_dict()
# create an instance of MeasurementSetResults from a dict
measurement_set_results_from_dict = MeasurementSetResults.from_dict(measurement_set_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


