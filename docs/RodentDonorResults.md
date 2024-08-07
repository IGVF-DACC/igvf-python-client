# RodentDonorResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[RodentDonor]**](RodentDonor.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.rodent_donor_results import RodentDonorResults

# TODO update the JSON string below
json = "{}"
# create an instance of RodentDonorResults from a JSON string
rodent_donor_results_instance = RodentDonorResults.from_json(json)
# print the JSON string representation of the object
print(RodentDonorResults.to_json())

# convert the object into a dict
rodent_donor_results_dict = rodent_donor_results_instance.to_dict()
# create an instance of RodentDonorResults from a dict
rodent_donor_results_from_dict = RodentDonorResults.from_dict(rodent_donor_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


