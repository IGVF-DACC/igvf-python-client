# RelatedMeasurementSetGroup

A group of related measurement sets of a given series type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measurement_sets** | **List[str]** | Measurement sets related by this relationship. | 
**series_type** | **str** | Type of relationship between this measurement set and the related measurement sets. | 

## Example

```python
from igvf_client.models.related_measurement_set_group import RelatedMeasurementSetGroup

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedMeasurementSetGroup from a JSON string
related_measurement_set_group_instance = RelatedMeasurementSetGroup.from_json(json)
# print the JSON string representation of the object
print(RelatedMeasurementSetGroup.to_json())

# convert the object into a dict
related_measurement_set_group_dict = related_measurement_set_group_instance.to_dict()
# create an instance of RelatedMeasurementSetGroup from a dict
related_measurement_set_group_from_dict = RelatedMeasurementSetGroup.from_dict(related_measurement_set_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


