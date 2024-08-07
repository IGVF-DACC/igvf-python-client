# RelatedDonor

Familial relation of this donor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donor** | **str** | An identifier for the related donor. | 
**relationship_type** | **str** | A descriptive term for the related donor’s relationship to this donor. | 

## Example

```python
from igvf_client.models.related_donor import RelatedDonor

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedDonor from a JSON string
related_donor_instance = RelatedDonor.from_json(json)
# print the JSON string representation of the object
print(RelatedDonor.to_json())

# convert the object into a dict
related_donor_dict = related_donor_instance.to_dict()
# create an instance of RelatedDonor from a dict
related_donor_from_dict = RelatedDonor.from_dict(related_donor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


