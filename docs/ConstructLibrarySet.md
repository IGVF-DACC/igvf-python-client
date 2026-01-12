# ConstructLibrarySet

Construct library set is a file set that hosts raw data files (e.g. FASTQs) resulting from sequencing of a library prior to its delivery into the samples being investigated. For example sequencing results of guide RNAs after cloning them but prior to their delivery to the actual samples under investigation. The results thus represent the sequencing output of the guides that are then introduced into cells, but may not always correspond to what exact guides ended up being delivered or expressed. Not all construct library sets will end up having FASTQs or any other files in them. For example if the lab chooses not to sequence their guide library prior to delivery, no FASTQs will be required in that case. Construct library sets should not be associated with any samples because they are designed to capture the library prior to its delivery and hence, has no relation to the sample that will get the plasmids eventually.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_timestamp** | **str** | The date the object was previewed. | [optional] 
**control_file_sets** | **List[str]** | File sets that can serve as scientific controls for this file set. | [optional] 
**small_scale_loci_list** | [**List[Locus1]**](Locus1.md) | A small scale (&lt;&#x3D;100) list of specific chromosomal region(s). | [optional] 
**large_scale_loci_list** | **str** | A large scale list (&gt;100) of specific chromosomal regions. | [optional] 
**small_scale_gene_list** | **List[str]** | The specific, small scale list of (&lt;&#x3D;100) gene(s) this construct library was designed to target. This property differs from targeted_genes in Measurement Set, which describes genes targeted for binding sites or used for sorting by expression. | [optional] 
**large_scale_gene_list** | **str** | The large scale list of (&gt;100 genes) this construct library was designed to target. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
**sources** | **List[str]** | The originating lab(s) or vendor(s). | [optional] 
**lot_id** | **str** | The lot identifier provided by the originating lab or vendor. | [optional] 
**product_id** | **str** | The product or catalog identifier provided following deposition to addgene.org. | [optional] 
**lab** | **str** | Lab associated with the submission. | [optional] 
**award** | **str** | Grant associated with the submission. | [optional] 
**accession** | **str** | A unique identifier to be used to reference the object prefixed with IGVF. | [optional] 
**alternate_accessions** | **List[str]** | Accessions previously assigned to objects that have been merged with this object. | [optional] 
**collections** | **List[str]** | Some samples are part of particular data collections. | [optional] 
**status** | **str** | The status of the metadata object. | [optional] 
**revoke_detail** | **str** | Explanation of why an object was transitioned to the revoked status. | [optional] 
**schema_version** | **str** | The version of the JSON schema that the server uses to validate the object. | [optional] 
**uuid** | **str** | The unique identifier associated with every object. | [optional] 
**notes** | **str** | DACC internal notes. | [optional] 
**aliases** | **List[str]** | Lab specific identifiers to reference an object. | [optional] 
**creation_timestamp** | **str** | The date the object was created. | [optional] 
**submitted_by** | **str** | The user who submitted the object. | [optional] 
**submitter_comment** | **str** | Additional information specified by the submitter to be displayed as a comment on the portal. | [optional] 
**description** | **str** | A plain text description of the object. | [optional] 
**file_set_type** | **str** | The type or category of this construct library set. | [optional] 
**control_types** | **List[str]** | The types of control this construct library set set represents. | [optional] 
**scope** | **str** | The scope or scale that this construct library is designed to target. | [optional] 
**selection_criteria** | **List[str]** | The criteria used to select the sequence material cloned into the library. | [optional] 
**integrated_content_files** | **List[str]** | The files containing sequence material of interest either used for insert design or directly cloned into vectors in this library. | [optional] 
**associated_phenotypes** | **List[str]** | Ontological terms for diseases or phenotypes associated with the sequence material cloned in this construct library. | [optional] 
**orf_list** | **List[str]** | List of Open Reading Frame this construct library was designed to target. | [optional] 
**exon** | **str** | An identifier in plain text for the specific exon in an expression vector library. The associated gene must be listed in the small_scale_gene_list property. | [optional] 
**tile** | [**Tile**](Tile.md) |  | [optional] 
**guide_type** | **str** | The design of guides used in a CRISPR library, paired-guide (pgRNA) or single-guide (sgRNA). | [optional] 
**tiling_modality** | **str** | The tiling modality of guides across elements or loci in a CRISPR library. | [optional] 
**average_guide_coverage** | **float** | The average number of guides targeting each element of interest in the library. | [optional] 
**lower_bound_guide_coverage** | **int** | Lower bound of the number of guides targeting each element of interest in the library. | [optional] 
**upper_bound_guide_coverage** | **int** | Upper bound of the number of guides targeting each element of interest in the library. | [optional] 
**average_insert_size** | **float** | The average size of the inserts cloned into vectors in the library. | [optional] 
**lower_bound_insert_size** | **int** | Lower bound of the size of the inserts cloned in vectors in the library. | [optional] 
**upper_bound_insert_size** | **int** | Upper bound of the size of the inserts cloned in vectors in the library. | [optional] 
**targeton** | **str** | An identifier in plain text for the specific targeton in an editing template library. The associated gene must be listed in the small_scale_gene_list property. | [optional] 
**supersedes** | **List[str]** | The file set(s) that this file set supersedes by virtue of being newer, better, or a fixed version of etc. than the one(s) it supersedes. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**superseded_by** | **List[str]** | File set(s) this file set is superseded by virtue of those file set(s) being newer, better, or a fixed version of etc. than this one. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets associated with the samples of this file set. | [optional] 
**data_use_limitation_summaries** | **List[str]** | The data use limitation summaries of institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**controlled_access** | **bool** | The controlled access of the institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**is_on_anvil** | **bool** | Indicates whether this file set has been submitted to AnVIL. | [optional] 
**samples** | **List[str]** | The samples this construct library set was applied to. | [optional] 
**file_sets** | **List[str]** | The file sets that used this construct library set. | [optional] 
**preferred_assay_titles** | **List[str]** | The preferred assay titles of the file sets that used this construct library set. | [optional] 
**assay_titles** | **List[str]** | Ontology term names from Ontology of Biomedical Investigations (OBI) for assays. | [optional] 
**donors** | **List[str]** | The donors of the samples associated with this auxiliary set. | [optional] 

## Example

```python
from igvf_client.models.construct_library_set import ConstructLibrarySet

# TODO update the JSON string below
json = "{}"
# create an instance of ConstructLibrarySet from a JSON string
construct_library_set_instance = ConstructLibrarySet.from_json(json)
# print the JSON string representation of the object
print(ConstructLibrarySet.to_json())

# convert the object into a dict
construct_library_set_dict = construct_library_set_instance.to_dict()
# create an instance of ConstructLibrarySet from a dict
construct_library_set_from_dict = ConstructLibrarySet.from_dict(construct_library_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


