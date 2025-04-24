# MeasurementSet

Measurement set is a file set that hosts raw data files (e.g. FASTQs) resulting from sequencing of a library prepared from the nucleic acids of the sample that is the main target of the assay. For example sequencing of accessible regions in the genome, or sequencing of the transcriptome of the sample. The assay can either be bulk or single cell type. The sample specific raw sequencing results will be captured in the measurement sets. The files in the measurement sets are specific to the sample being investigated. See auxiliary sets for files that are not a direct result of sequencing the sample under investigation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_file_sets** | **List[str]** | File sets that can serve as scientific controls for this file set. | [optional] 
**release_timestamp** | **str** | The date the object was released. | [optional] 
**publications** | **List[str]** | The publications associated with this object. | [optional] 
**documents** | **List[str]** | Documents that provide additional information (not data file). | [optional] 
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
**dbxrefs** | **List[str]** | Identifiers from external resources that may have 1-to-1 or 1-to-many relationships with IGVF file sets. | [optional] 
**control_type** | **str** | The type of control this file set represents. | [optional] 
**samples** | **List[str]** | The sample(s) associated with this file set. | [optional] 
**donors** | **List[str]** | The donors of the samples associated with this measurement set. | [optional] 
**file_set_type** | **str** | The category that best describes this measurement set. | [optional] 
**assay_term** | **str** | The assay used to produce data in this measurement set. | [optional] 
**protocols** | **List[str]** | Links to the protocol(s) for conducting the assay on Protocols.io. | [optional] 
**preferred_assay_title** | **str** | The custom lab preferred label for the experiment performed in this measurement set. | [optional] 
**multiome_size** | **int** | The number of datasets included in the multiome experiment this measurement set is a part of. | [optional] 
**sequencing_library_types** | **List[str]** | Description of the libraries sequenced in this measurement set. | [optional] 
**primer_designs** | **List[str]** | The primer designs used in this measurement set. | [optional] 
**strand_specificity** | **str** | The strand-specificity of the sequencing results within Perturb-seq, scCRISPR screen, TAP-seq, and CERES-seq assays. | [optional] 
**auxiliary_sets** | **List[str]** | The auxiliary sets of files produced alongside raw data from this measurement set. | [optional] 
**external_image_url** | **str** | Links to the external site where images produced by this measurement are stored. | [optional] 
**targeted_genes** | **List[str]** | A list of genes targeted in this assay. For example, TF ChIP-seq attempts to identify binding sites of a protein encoded by a specific gene. In CRISPR FlowFISH, the modified samples are sorted based on expression of a specific gene. This property differs from small_scale_gene_list in Construct Library Set, which describes genes targeted by the content integrated in the constructs (such as guide RNAs.) | [optional] 
**functional_assay_mechanisms** | **List[str]** | The biological processes measured by this functional assay. For example, a VAMP-seq (MultiSTEP) assay measures the effects of variants on protein carboxylation and secretion processes. | [optional] 
**onlist_method** | **str** | The method by which the onlist files will be combined by the seqspec onlist tool to generate the final barcode inclusion list for the single cell uniform pipeline. | [optional] 
**onlist_files** | **List[str]** | The barcode region onlist files listed in associated seqspec yaml files. | [optional] 
**barcode_replacement_file** | **str** | A file containing original barcodes and the new barcodes used to replace the original barcodes. One common application is to use in preprocessing Parse SPLiT-seq data with the single cell uniform pipeline. | [optional] 
**id** | **str** |  | [optional] 
**type** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**files** | **List[str]** | The files associated with this file set. | [optional] 
**control_for** | **List[str]** | The file sets for which this file set is a control. | [optional] 
**submitted_files_timestamp** | **str** | The timestamp the first file object in the file_set or associated auxiliary sets was created. | [optional] 
**input_for** | **List[str]** | The file sets that use this file set as an input. | [optional] 
**construct_library_sets** | **List[str]** | The construct library sets associated with the samples of this file set. | [optional] 
**data_use_limitation_summaries** | **List[str]** | The data use limitation summaries of institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**controlled_access** | **bool** | The controlled access of the institutional certificates covering the sample associated with this file set which are signed by the same lab (or their partner lab) as the lab that submitted this file set. | [optional] 
**related_multiome_datasets** | **List[str]** | Related datasets included in the multiome experiment this measurement set is a part of. | [optional] 
**externally_hosted** | **bool** |  | [optional] 

## Example

```python
from igvf_client.models.measurement_set import MeasurementSet

# TODO update the JSON string below
json = "{}"
# create an instance of MeasurementSet from a JSON string
measurement_set_instance = MeasurementSet.from_json(json)
# print the JSON string representation of the object
print(MeasurementSet.to_json())

# convert the object into a dict
measurement_set_dict = measurement_set_instance.to_dict()
# create an instance of MeasurementSet from a dict
measurement_set_from_dict = MeasurementSet.from_dict(measurement_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


