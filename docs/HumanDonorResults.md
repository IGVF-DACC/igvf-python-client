# HumanDonorResults


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**graph** | [**List[HumanDonor]**](HumanDonor.md) |  | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**total** | **int** |  | [optional] 
**facets** | [**List[SearchFacet]**](SearchFacet.md) |  | [optional] 

## Example

```python
from igvf_client.models.human_donor_results import HumanDonorResults

# TODO update the JSON string below
json = "{}"
# create an instance of HumanDonorResults from a JSON string
human_donor_results_instance = HumanDonorResults.from_json(json)
# print the JSON string representation of the object
print(HumanDonorResults.to_json())

# convert the object into a dict
human_donor_results_dict = human_donor_results_instance.to_dict()
# create an instance of HumanDonorResults from a dict
human_donor_results_from_dict = HumanDonorResults.from_dict(human_donor_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


