# Attachment1

The attached content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**download** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**md5sum** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**width** | **int** |  | [optional] 
**height** | **int** |  | [optional] 

## Example

```python
from igvf_client.models.attachment1 import Attachment1

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment1 from a JSON string
attachment1_instance = Attachment1.from_json(json)
# print the JSON string representation of the object
print(Attachment1.to_json())

# convert the object into a dict
attachment1_dict = attachment1_instance.to_dict()
# create an instance of Attachment1 from a dict
attachment1_from_dict = Attachment1.from_dict(attachment1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


