# PageLayoutComponents


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for this blocUnique identifier for this block. | [optional] 
**type** | **str** | Indicates whether this block contains markdown or a component specification. | [optional] 
**body** | **str** | The text content of this block. | [optional] 
**direction** | **str** | The text language direction -- ltr or rtl. | [optional] 

## Example

```python
from igvf_client.models.page_layout_components import PageLayoutComponents

# TODO update the JSON string below
json = "{}"
# create an instance of PageLayoutComponents from a JSON string
page_layout_components_instance = PageLayoutComponents.from_json(json)
# print the JSON string representation of the object
print(PageLayoutComponents.to_json())

# convert the object into a dict
page_layout_components_dict = page_layout_components_instance.to_dict()
# create an instance of PageLayoutComponents from a dict
page_layout_components_from_dict = PageLayoutComponents.from_dict(page_layout_components_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


