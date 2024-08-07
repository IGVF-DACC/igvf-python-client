# Tile

The coordinates and an identifier in plain text for the specific tile of a protein region cloned in an expression vector library. The associated gene for this protein must be listed in the small_scale_gene_list or large_scale_gene_list property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tile_id** | **str** | An identifier in plain text for the specific tile of a protein region cloned in an expression vector library. | [optional] 
**tile_start** | **int** | The 1-based, closed (inclusive) starting coordinate. | [optional] 
**tile_end** | **int** | The 1-based, closed (inclusive) ending coordinate. | [optional] 

## Example

```python
from igvf_client.models.tile import Tile

# TODO update the JSON string below
json = "{}"
# create an instance of Tile from a JSON string
tile_instance = Tile.from_json(json)
# print the JSON string representation of the object
print(Tile.to_json())

# convert the object into a dict
tile_dict = tile_instance.to_dict()
# create an instance of Tile from a dict
tile_from_dict = Tile.from_dict(tile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


