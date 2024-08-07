# PageLayout

Hierarchical description of the page layout.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocks** | [**List[PageLayoutComponents]**](PageLayoutComponents.md) |  | [optional] 

## Example

```python
from igvf_client.models.page_layout import PageLayout

# TODO update the JSON string below
json = "{}"
# create an instance of PageLayout from a JSON string
page_layout_instance = PageLayout.from_json(json)
# print the JSON string representation of the object
print(PageLayout.to_json())

# convert the object into a dict
page_layout_dict = page_layout_instance.to_dict()
# create an instance of PageLayout from a dict
page_layout_from_dict = PageLayout.from_dict(page_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


