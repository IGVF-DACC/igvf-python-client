# igvf_client.IgvfApi

All URIs are relative to *https://api.data.igvf.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_keys**](IgvfApi.md#access_keys) | **GET** /access-keys/@@listing | List items in the AccessKey collection.
[**alignment_files**](IgvfApi.md#alignment_files) | **GET** /alignment-files/@@listing | List items in the AlignmentFile collection.
[**analysis_sets**](IgvfApi.md#analysis_sets) | **GET** /analysis-sets/@@listing | List items in the AnalysisSet collection.
[**analysis_step_versions**](IgvfApi.md#analysis_step_versions) | **GET** /analysis-step-versions/@@listing | List items in the AnalysisStepVersion collection.
[**analysis_steps**](IgvfApi.md#analysis_steps) | **GET** /analysis-steps/@@listing | List items in the AnalysisStep collection.
[**assay_terms**](IgvfApi.md#assay_terms) | **GET** /assay-terms/@@listing | List items in the AssayTerm collection.
[**auxiliary_sets**](IgvfApi.md#auxiliary_sets) | **GET** /auxiliary-sets/@@listing | List items in the AuxiliarySet collection.
[**awards**](IgvfApi.md#awards) | **GET** /awards/@@listing | List items in the Award collection.
[**batch_download**](IgvfApi.md#batch_download) | **GET** /batch-download | List files to download based on search query. All results are returned.
[**biomarkers**](IgvfApi.md#biomarkers) | **GET** /biomarkers/@@listing | List items in the Biomarker collection.
[**configuration_files**](IgvfApi.md#configuration_files) | **GET** /configuration-files/@@listing | List items in the ConfigurationFile collection.
[**construct_library_sets**](IgvfApi.md#construct_library_sets) | **GET** /construct-library-sets/@@listing | List items in the ConstructLibrarySet collection.
[**crispr_modifications**](IgvfApi.md#crispr_modifications) | **GET** /crispr-modifications/@@listing | List items in the CrisprModification collection.
[**curated_sets**](IgvfApi.md#curated_sets) | **GET** /curated-sets/@@listing | List items in the CuratedSet collection.
[**degron_modifications**](IgvfApi.md#degron_modifications) | **GET** /degron-modifications/@@listing | List items in the DegronModification collection.
[**documents**](IgvfApi.md#documents) | **GET** /documents/@@listing | List items in the Document collection.
[**download**](IgvfApi.md#download) | **GET** /{file_id}/@@download | Download file.
[**genes**](IgvfApi.md#genes) | **GET** /genes/@@listing | List items in the Gene collection.
[**genome_browser_annotation_files**](IgvfApi.md#genome_browser_annotation_files) | **GET** /genome-browser-annotation-files/@@listing | List items in the GenomeBrowserAnnotationFile collection.
[**get_by_id**](IgvfApi.md#get_by_id) | **GET** /{resource_id} | Get item information
[**human_donors**](IgvfApi.md#human_donors) | **GET** /human-donors/@@listing | List items in the HumanDonor collection.
[**image_files**](IgvfApi.md#image_files) | **GET** /image-files/@@listing | List items in the ImageFile collection.
[**images**](IgvfApi.md#images) | **GET** /images/@@listing | List items in the Image collection.
[**in_vitro_systems**](IgvfApi.md#in_vitro_systems) | **GET** /in-vitro-systems/@@listing | List items in the InVitroSystem collection.
[**index_files**](IgvfApi.md#index_files) | **GET** /index-files/@@listing | List items in the IndexFile collection.
[**institutional_certificates**](IgvfApi.md#institutional_certificates) | **GET** /institutional-certificates/@@listing | List items in the InstitutionalCertificate collection.
[**labs**](IgvfApi.md#labs) | **GET** /labs/@@listing | List items in the Lab collection.
[**matrix_files**](IgvfApi.md#matrix_files) | **GET** /matrix-files/@@listing | List items in the MatrixFile collection.
[**measurement_sets**](IgvfApi.md#measurement_sets) | **GET** /measurement-sets/@@listing | List items in the MeasurementSet collection.
[**model_files**](IgvfApi.md#model_files) | **GET** /model-files/@@listing | List items in the ModelFile collection.
[**model_sets**](IgvfApi.md#model_sets) | **GET** /model-sets/@@listing | List items in the ModelSet collection.
[**multiplexed_samples**](IgvfApi.md#multiplexed_samples) | **GET** /multiplexed-samples/@@listing | List items in the MultiplexedSample collection.
[**open_reading_frames**](IgvfApi.md#open_reading_frames) | **GET** /open-reading-frames/@@listing | List items in the OpenReadingFrame collection.
[**pages**](IgvfApi.md#pages) | **GET** /pages/@@listing | List items in the Page collection.
[**phenotype_terms**](IgvfApi.md#phenotype_terms) | **GET** /phenotype-terms/@@listing | List items in the PhenotypeTerm collection.
[**phenotypic_features**](IgvfApi.md#phenotypic_features) | **GET** /phenotypic-features/@@listing | List items in the PhenotypicFeature collection.
[**platform_terms**](IgvfApi.md#platform_terms) | **GET** /platform-terms/@@listing | List items in the PlatformTerm collection.
[**prediction_sets**](IgvfApi.md#prediction_sets) | **GET** /prediction-sets/@@listing | List items in the PredictionSet collection.
[**primary_cells**](IgvfApi.md#primary_cells) | **GET** /primary-cells/@@listing | List items in the PrimaryCell collection.
[**publications**](IgvfApi.md#publications) | **GET** /publications/@@listing | List items in the Publication collection.
[**reference_files**](IgvfApi.md#reference_files) | **GET** /reference-files/@@listing | List items in the ReferenceFile collection.
[**report**](IgvfApi.md#report) | **GET** /multireport.tsv | Generate a TSV file report based on search query. All results are returned.
[**rodent_donors**](IgvfApi.md#rodent_donors) | **GET** /rodent-donors/@@listing | List items in the RodentDonor collection.
[**sample_terms**](IgvfApi.md#sample_terms) | **GET** /sample-terms/@@listing | List items in the SampleTerm collection.
[**schema_for_item_type**](IgvfApi.md#schema_for_item_type) | **GET** /profiles/{item_type} | Retrieve JSON schema for item type
[**schemas**](IgvfApi.md#schemas) | **GET** /profiles | Retrieve JSON schemas for all item types
[**search**](IgvfApi.md#search) | **GET** /search | Search for items on the IGVF Data Portal.
[**sequence_files**](IgvfApi.md#sequence_files) | **GET** /sequence-files/@@listing | List items in the SequenceFile collection.
[**signal_files**](IgvfApi.md#signal_files) | **GET** /signal-files/@@listing | List items in the SignalFile collection.
[**software**](IgvfApi.md#software) | **GET** /software/@@listing | List items in the Software collection.
[**software_versions**](IgvfApi.md#software_versions) | **GET** /software-versions/@@listing | List items in the SoftwareVersion collection.
[**sources**](IgvfApi.md#sources) | **GET** /sources/@@listing | List items in the Source collection.
[**tabular_files**](IgvfApi.md#tabular_files) | **GET** /tabular-files/@@listing | List items in the TabularFile collection.
[**technical_samples**](IgvfApi.md#technical_samples) | **GET** /technical-samples/@@listing | List items in the TechnicalSample collection.
[**tissues**](IgvfApi.md#tissues) | **GET** /tissues/@@listing | List items in the Tissue collection.
[**treatments**](IgvfApi.md#treatments) | **GET** /treatments/@@listing | List items in the Treatment collection.
[**users**](IgvfApi.md#users) | **GET** /users/@@listing | List items in the User collection.
[**whole_organisms**](IgvfApi.md#whole_organisms) | **GET** /whole-organisms/@@listing | List items in the WholeOrganism collection.
[**workflows**](IgvfApi.md#workflows) | **GET** /workflows/@@listing | List items in the Workflow collection.


# **access_keys**
> AccessKeyResults access_keys(query=query, limit=limit, sort=sort, id=id, access_key_id=access_key_id, aliases=aliases, creation_timestamp=creation_timestamp, description=description, notes=notes, secret_access_key_hash=secret_access_key_hash, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, user=user, uuid=uuid)

List items in the AccessKey collection.

Collection endpoint that accepts various query parameters to filter and sort AccessKey items. Supports filtering on fields within AccessKey items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.access_keys(**parameters) # List items in the AccessKey collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **access_key_id** | **List[str]**| Filter by access_key_id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **secret_access_key_hash** | **List[str]**| Filter by secret_access_key_hash | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **user** | **List[str]**| Filter by user | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**AccessKeyResults**](AccessKeyResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **alignment_files**
> AlignmentFileResults alignment_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_summary=content_summary, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, filtered=filtered, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, read_count=read_count, redacted=redacted, reference_files=reference_files, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the AlignmentFile collection.

Collection endpoint that accepts various query parameters to filter and sort AlignmentFile items. Supports filtering on fields within AlignmentFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.alignment_files(**parameters) # List items in the AlignmentFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_summary** | **List[str]**| Filter by content_summary | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **filtered** | **List[bool]**| Filter by filtered | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **read_count** | **List[int]**| Filter by read_count | [optional] 
 **redacted** | **List[bool]**| Filter by redacted | [optional] 
 **reference_files** | **List[str]**| Filter by reference_files | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**AlignmentFileResults**](AlignmentFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_sets**
> AnalysisSetResults analysis_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, assay_titles=assay_titles, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, collections=collections, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, demultiplexed_sample=demultiplexed_sample, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, external_image_data_url=external_image_data_url, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform=files_sequencing_platform, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, functional_assay_mechanisms_id=functional_assay_mechanisms_id, functional_assay_mechanisms_term_id=functional_assay_mechanisms_term_id, functional_assay_mechanisms_term_name=functional_assay_mechanisms_term_name, input_file_sets_id=input_file_sets_id, input_file_sets_accession=input_file_sets_accession, input_file_sets_aliases=input_file_sets_aliases, input_file_sets_file_set_type=input_file_sets_file_set_type, input_for=input_for, lab_id=lab_id, lab_title=lab_title, notes=notes, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_summary=sample_summary, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments=samples_cell_fate_change_treatments, samples_classifications=samples_classifications, samples_construct_library_sets=samples_construct_library_sets, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, uuid=uuid, workflows_id=workflows_id, workflows_accession=workflows_accession, workflows_name=workflows_name, workflows_uniform_pipeline=workflows_uniform_pipeline)

List items in the AnalysisSet collection.

Collection endpoint that accepts various query parameters to filter and sort AnalysisSet items. Supports filtering on fields within AnalysisSet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.analysis_sets(**parameters) # List items in the AnalysisSet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **demultiplexed_sample** | **List[str]**| Filter by demultiplexed_sample | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **external_image_data_url** | **List[str]**| Filter by external_image_data_url | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform** | **List[str]**| Filter by files.sequencing_platform | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **functional_assay_mechanisms_id** | **List[str]**| Filter by functional_assay_mechanisms.@id | [optional] 
 **functional_assay_mechanisms_term_id** | **List[str]**| Filter by functional_assay_mechanisms.term_id | [optional] 
 **functional_assay_mechanisms_term_name** | **List[str]**| Filter by functional_assay_mechanisms.term_name | [optional] 
 **input_file_sets_id** | **List[str]**| Filter by input_file_sets.@id | [optional] 
 **input_file_sets_accession** | **List[str]**| Filter by input_file_sets.accession | [optional] 
 **input_file_sets_aliases** | **List[str]**| Filter by input_file_sets.aliases | [optional] 
 **input_file_sets_file_set_type** | **List[str]**| Filter by input_file_sets.file_set_type | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_summary** | **List[str]**| Filter by sample_summary | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments** | **List[str]**| Filter by samples.cell_fate_change_treatments | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets** | **List[str]**| Filter by samples.construct_library_sets | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **workflows_id** | **List[str]**| Filter by workflows.@id | [optional] 
 **workflows_accession** | **List[str]**| Filter by workflows.accession | [optional] 
 **workflows_name** | **List[str]**| Filter by workflows.name | [optional] 
 **workflows_uniform_pipeline** | **List[bool]**| Filter by workflows.uniform_pipeline | [optional] 

### Return type

[**AnalysisSetResults**](AnalysisSetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_step_versions**
> AnalysisStepVersionResults analysis_step_versions(query=query, limit=limit, sort=sort, id=id, aliases=aliases, analysis_step_id=analysis_step_id, analysis_step_name=analysis_step_name, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, description=description, lab_id=lab_id, lab_title=lab_title, notes=notes, release_timestamp=release_timestamp, software_versions_id=software_versions_id, software_versions_name=software_versions_name, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, uuid=uuid)

List items in the AnalysisStepVersion collection.

Collection endpoint that accepts various query parameters to filter and sort AnalysisStepVersion items. Supports filtering on fields within AnalysisStepVersion items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.analysis_step_versions(**parameters) # List items in the AnalysisStepVersion collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **analysis_step_id** | **List[str]**| Filter by analysis_step.@id | [optional] 
 **analysis_step_name** | **List[str]**| Filter by analysis_step.name | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **software_versions_id** | **List[str]**| Filter by software_versions.@id | [optional] 
 **software_versions_name** | **List[str]**| Filter by software_versions.name | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**AnalysisStepVersionResults**](AnalysisStepVersionResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analysis_steps**
> AnalysisStepResults analysis_steps(query=query, limit=limit, sort=sort, id=id, aliases=aliases, analysis_step_types=analysis_step_types, analysis_step_versions=analysis_step_versions, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, description=description, input_content_types=input_content_types, lab_id=lab_id, lab_title=lab_title, name=name, notes=notes, output_content_types=output_content_types, parents_id=parents_id, parents_title=parents_title, release_timestamp=release_timestamp, status=status, step_label=step_label, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, uuid=uuid, workflow_id=workflow_id, workflow_accession=workflow_accession)

List items in the AnalysisStep collection.

Collection endpoint that accepts various query parameters to filter and sort AnalysisStep items. Supports filtering on fields within AnalysisStep items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.analysis_steps(**parameters) # List items in the AnalysisStep collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **analysis_step_types** | **List[str]**| Filter by analysis_step_types | [optional] 
 **analysis_step_versions** | **List[str]**| Filter by analysis_step_versions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **input_content_types** | **List[str]**| Filter by input_content_types | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **output_content_types** | **List[str]**| Filter by output_content_types | [optional] 
 **parents_id** | **List[str]**| Filter by parents.@id | [optional] 
 **parents_title** | **List[str]**| Filter by parents.title | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **step_label** | **List[str]**| Filter by step_label | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **workflow_id** | **List[str]**| Filter by workflow.@id | [optional] 
 **workflow_accession** | **List[str]**| Filter by workflow.accession | [optional] 

### Return type

[**AnalysisStepResults**](AnalysisStepResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assay_terms**
> AssayTermResults assay_terms(query=query, limit=limit, sort=sort, id=id, aliases=aliases, ancestors=ancestors, assay_slims=assay_slims, category_slims=category_slims, creation_timestamp=creation_timestamp, deprecated_ntr_terms=deprecated_ntr_terms, description=description, is_a=is_a, name=name, notes=notes, objective_slims=objective_slims, ontology=ontology, preferred_assay_titles=preferred_assay_titles, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, synonyms=synonyms, term_id=term_id, term_name=term_name, uuid=uuid)

List items in the AssayTerm collection.

Collection endpoint that accepts various query parameters to filter and sort AssayTerm items. Supports filtering on fields within AssayTerm items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.assay_terms(**parameters) # List items in the AssayTerm collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **ancestors** | **List[str]**| Filter by ancestors | [optional] 
 **assay_slims** | **List[str]**| Filter by assay_slims | [optional] 
 **category_slims** | **List[str]**| Filter by category_slims | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **deprecated_ntr_terms** | **List[str]**| Filter by deprecated_ntr_terms | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **is_a** | **List[str]**| Filter by is_a | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **objective_slims** | **List[str]**| Filter by objective_slims | [optional] 
 **ontology** | **List[str]**| Filter by ontology | [optional] 
 **preferred_assay_titles** | **List[str]**| Filter by preferred_assay_titles | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **term_id** | **List[str]**| Filter by term_id | [optional] 
 **term_name** | **List[str]**| Filter by term_name | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**AssayTermResults**](AssayTermResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auxiliary_sets**
> AuxiliarySetResults auxiliary_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, barcode_map=barcode_map, collections=collections, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform=files_sequencing_platform, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, input_for=input_for, lab_id=lab_id, lab_title=lab_title, measurement_sets_id=measurement_sets_id, measurement_sets_accession=measurement_sets_accession, measurement_sets_aliases=measurement_sets_aliases, measurement_sets_preferred_assay_title=measurement_sets_preferred_assay_title, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments=samples_cell_fate_change_treatments, samples_classifications=samples_classifications, samples_construct_library_sets=samples_construct_library_sets, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, url=url, uuid=uuid)

List items in the AuxiliarySet collection.

Collection endpoint that accepts various query parameters to filter and sort AuxiliarySet items. Supports filtering on fields within AuxiliarySet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.auxiliary_sets(**parameters) # List items in the AuxiliarySet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **barcode_map** | **List[str]**| Filter by barcode_map | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform** | **List[str]**| Filter by files.sequencing_platform | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **measurement_sets_id** | **List[str]**| Filter by measurement_sets.@id | [optional] 
 **measurement_sets_accession** | **List[str]**| Filter by measurement_sets.accession | [optional] 
 **measurement_sets_aliases** | **List[str]**| Filter by measurement_sets.aliases | [optional] 
 **measurement_sets_preferred_assay_title** | **List[str]**| Filter by measurement_sets.preferred_assay_title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments** | **List[str]**| Filter by samples.cell_fate_change_treatments | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets** | **List[str]**| Filter by samples.construct_library_sets | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**AuxiliarySetResults**](AuxiliarySetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **awards**
> AwardResults awards(query=query, limit=limit, sort=sort, id=id, aliases=aliases, component=component, contact_pi=contact_pi, creation_timestamp=creation_timestamp, description=description, end_date=end_date, name=name, notes=notes, pis=pis, project=project, start_date=start_date, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, url=url, uuid=uuid, viewing_group=viewing_group)

List items in the Award collection.

Collection endpoint that accepts various query parameters to filter and sort Award items. Supports filtering on fields within Award items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.awards(**parameters) # List items in the Award collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **component** | **List[str]**| Filter by component | [optional] 
 **contact_pi** | **List[str]**| Filter by contact_pi | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **end_date** | **List[str]**| Filter by end_date | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **pis** | **List[str]**| Filter by pis | [optional] 
 **project** | **List[str]**| Filter by project | [optional] 
 **start_date** | **List[str]**| Filter by start_date | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **viewing_group** | **List[str]**| Filter by viewing_group | [optional] 

### Return type

[**AwardResults**](AwardResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_download**
> str batch_download(type, query=query, field_filters=field_filters)

List files to download based on search query. All results are returned.

Generates TSV of files contained in FileSets in search results.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.batch_download(**parameters) # List files to download based on search query. All results are returned. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **List[str]**| Type of objects to return. Can be repeated for multiple types. | 
 **query** | **str**| Query string for searching. | [optional] 
 **field_filters** | **object**| Any field from any object type can be used as a filter. Use &#39;!&#39; for negation, &#39;*&#39; as a wildcard, and &#39;lt:&#39;, &#39;lte:&#39;, &#39;gt:&#39;, &#39;gte:&#39; for range queries on numeric fields. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/tab-separated-values, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **biomarkers**
> BiomarkerResults biomarkers(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, award_name=award_name, biomarker_for=biomarker_for, classification=classification, creation_timestamp=creation_timestamp, description=description, gene=gene, lab_id=lab_id, lab_title=lab_title, name=name, name_quantification=name_quantification, notes=notes, quantification=quantification, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, synonyms=synonyms, uuid=uuid)

List items in the Biomarker collection.

Collection endpoint that accepts various query parameters to filter and sort Biomarker items. Supports filtering on fields within Biomarker items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.biomarkers(**parameters) # List items in the Biomarker collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_name** | **List[str]**| Filter by award.name | [optional] 
 **biomarker_for** | **List[str]**| Filter by biomarker_for | [optional] 
 **classification** | **List[str]**| Filter by classification | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **gene** | **List[str]**| Filter by gene | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **name_quantification** | **List[str]**| Filter by name_quantification | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **quantification** | **List[str]**| Filter by quantification | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**BiomarkerResults**](BiomarkerResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_files**
> ConfigurationFileResults configuration_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, assay_titles=assay_titles, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_type=content_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, seqspec_of=seqspec_of, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the ConfigurationFile collection.

Collection endpoint that accepts various query parameters to filter and sort ConfigurationFile items. Supports filtering on fields within ConfigurationFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.configuration_files(**parameters) # List items in the ConfigurationFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **seqspec_of** | **List[str]**| Filter by seqspec_of | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**ConfigurationFileResults**](ConfigurationFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **construct_library_sets**
> ConstructLibrarySetResults construct_library_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, applied_to_samples_id=applied_to_samples_id, applied_to_samples_accession=applied_to_samples_accession, applied_to_samples_aliases=applied_to_samples_aliases, applied_to_samples_classifications=applied_to_samples_classifications, applied_to_samples_disease_terms_id=applied_to_samples_disease_terms_id, applied_to_samples_disease_terms_term_name=applied_to_samples_disease_terms_term_name, applied_to_samples_donors_id=applied_to_samples_donors_id, applied_to_samples_donors_taxa=applied_to_samples_donors_taxa, applied_to_samples_modifications_id=applied_to_samples_modifications_id, applied_to_samples_modifications_modality=applied_to_samples_modifications_modality, applied_to_samples_modifications_summary=applied_to_samples_modifications_summary, applied_to_samples_sample_terms_id=applied_to_samples_sample_terms_id, applied_to_samples_sample_terms_term_name=applied_to_samples_sample_terms_term_name, applied_to_samples_status=applied_to_samples_status, applied_to_samples_summary=applied_to_samples_summary, applied_to_samples_targeted_sample_term_id=applied_to_samples_targeted_sample_term_id, applied_to_samples_targeted_sample_term_term_name=applied_to_samples_targeted_sample_term_term_name, applied_to_samples_taxa=applied_to_samples_taxa, applied_to_samples_treatments_id=applied_to_samples_treatments_id, applied_to_samples_treatments_summary=applied_to_samples_treatments_summary, applied_to_samples_treatments_treatment_term_name=applied_to_samples_treatments_treatment_term_name, associated_phenotypes_id=associated_phenotypes_id, associated_phenotypes_term_id=associated_phenotypes_term_id, associated_phenotypes_term_name=associated_phenotypes_term_name, average_guide_coverage=average_guide_coverage, average_insert_size=average_insert_size, award_id=award_id, award_component=award_component, collections=collections, control_file_sets=control_file_sets, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, description=description, documents=documents, exon=exon, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_content_type=files_content_type, files_file_format=files_file_format, files_upload_status=files_upload_status, guide_type=guide_type, input_for=input_for, integrated_content_files_id=integrated_content_files_id, integrated_content_files_accession=integrated_content_files_accession, integrated_content_files_aliases=integrated_content_files_aliases, integrated_content_files_upload_status=integrated_content_files_upload_status, lab_id=lab_id, lab_title=lab_title, large_scale_gene_list_id=large_scale_gene_list_id, large_scale_gene_list_accession=large_scale_gene_list_accession, large_scale_gene_list_aliases=large_scale_gene_list_aliases, large_scale_loci_list_id=large_scale_loci_list_id, large_scale_loci_list_accession=large_scale_loci_list_accession, large_scale_loci_list_aliases=large_scale_loci_list_aliases, lot_id=lot_id, lower_bound_guide_coverage=lower_bound_guide_coverage, lower_bound_insert_size=lower_bound_insert_size, notes=notes, orf_list_id=orf_list_id, orf_list_aliases=orf_list_aliases, orf_list_genes_id=orf_list_genes_id, orf_list_genes_symbol=orf_list_genes_symbol, orf_list_orf_id=orf_list_orf_id, product_id=product_id, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, scope=scope, selection_criteria=selection_criteria, small_scale_gene_list_id=small_scale_gene_list_id, small_scale_gene_list_geneid=small_scale_gene_list_geneid, small_scale_gene_list_name=small_scale_gene_list_name, small_scale_gene_list_symbol=small_scale_gene_list_symbol, small_scale_gene_list_synonyms=small_scale_gene_list_synonyms, small_scale_loci_list=small_scale_loci_list, sources=sources, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, targeton=targeton, tiling_modality=tiling_modality, upper_bound_guide_coverage=upper_bound_guide_coverage, upper_bound_insert_size=upper_bound_insert_size, uuid=uuid)

List items in the ConstructLibrarySet collection.

Collection endpoint that accepts various query parameters to filter and sort ConstructLibrarySet items. Supports filtering on fields within ConstructLibrarySet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.construct_library_sets(**parameters) # List items in the ConstructLibrarySet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **applied_to_samples_id** | **List[str]**| Filter by applied_to_samples.@id | [optional] 
 **applied_to_samples_accession** | **List[str]**| Filter by applied_to_samples.accession | [optional] 
 **applied_to_samples_aliases** | **List[str]**| Filter by applied_to_samples.aliases | [optional] 
 **applied_to_samples_classifications** | **List[str]**| Filter by applied_to_samples.classifications | [optional] 
 **applied_to_samples_disease_terms_id** | **List[str]**| Filter by applied_to_samples.disease_terms.@id | [optional] 
 **applied_to_samples_disease_terms_term_name** | **List[str]**| Filter by applied_to_samples.disease_terms.term_name | [optional] 
 **applied_to_samples_donors_id** | **List[str]**| Filter by applied_to_samples.donors.@id | [optional] 
 **applied_to_samples_donors_taxa** | **List[str]**| Filter by applied_to_samples.donors.taxa | [optional] 
 **applied_to_samples_modifications_id** | **List[str]**| Filter by applied_to_samples.modifications.@id | [optional] 
 **applied_to_samples_modifications_modality** | **List[str]**| Filter by applied_to_samples.modifications.modality | [optional] 
 **applied_to_samples_modifications_summary** | **List[str]**| Filter by applied_to_samples.modifications.summary | [optional] 
 **applied_to_samples_sample_terms_id** | **List[str]**| Filter by applied_to_samples.sample_terms.@id | [optional] 
 **applied_to_samples_sample_terms_term_name** | **List[str]**| Filter by applied_to_samples.sample_terms.term_name | [optional] 
 **applied_to_samples_status** | **List[str]**| Filter by applied_to_samples.status | [optional] 
 **applied_to_samples_summary** | **List[str]**| Filter by applied_to_samples.summary | [optional] 
 **applied_to_samples_targeted_sample_term_id** | **List[str]**| Filter by applied_to_samples.targeted_sample_term.@id | [optional] 
 **applied_to_samples_targeted_sample_term_term_name** | **List[str]**| Filter by applied_to_samples.targeted_sample_term.term_name | [optional] 
 **applied_to_samples_taxa** | **List[str]**| Filter by applied_to_samples.taxa | [optional] 
 **applied_to_samples_treatments_id** | **List[str]**| Filter by applied_to_samples.treatments.@id | [optional] 
 **applied_to_samples_treatments_summary** | **List[str]**| Filter by applied_to_samples.treatments.summary | [optional] 
 **applied_to_samples_treatments_treatment_term_name** | **List[str]**| Filter by applied_to_samples.treatments.treatment_term_name | [optional] 
 **associated_phenotypes_id** | **List[str]**| Filter by associated_phenotypes.@id | [optional] 
 **associated_phenotypes_term_id** | **List[str]**| Filter by associated_phenotypes.term_id | [optional] 
 **associated_phenotypes_term_name** | **List[str]**| Filter by associated_phenotypes.term_name | [optional] 
 **average_guide_coverage** | **List[float]**| Filter by average_guide_coverage | [optional] 
 **average_insert_size** | **List[float]**| Filter by average_insert_size | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_file_sets** | **List[str]**| Filter by control_file_sets | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **exon** | **List[str]**| Filter by exon | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **guide_type** | **List[str]**| Filter by guide_type | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **integrated_content_files_id** | **List[str]**| Filter by integrated_content_files.@id | [optional] 
 **integrated_content_files_accession** | **List[str]**| Filter by integrated_content_files.accession | [optional] 
 **integrated_content_files_aliases** | **List[str]**| Filter by integrated_content_files.aliases | [optional] 
 **integrated_content_files_upload_status** | **List[str]**| Filter by integrated_content_files.upload_status | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **large_scale_gene_list_id** | **List[str]**| Filter by large_scale_gene_list.@id | [optional] 
 **large_scale_gene_list_accession** | **List[str]**| Filter by large_scale_gene_list.accession | [optional] 
 **large_scale_gene_list_aliases** | **List[str]**| Filter by large_scale_gene_list.aliases | [optional] 
 **large_scale_loci_list_id** | **List[str]**| Filter by large_scale_loci_list.@id | [optional] 
 **large_scale_loci_list_accession** | **List[str]**| Filter by large_scale_loci_list.accession | [optional] 
 **large_scale_loci_list_aliases** | **List[str]**| Filter by large_scale_loci_list.aliases | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **lower_bound_guide_coverage** | **List[int]**| Filter by lower_bound_guide_coverage | [optional] 
 **lower_bound_insert_size** | **List[int]**| Filter by lower_bound_insert_size | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **orf_list_id** | **List[str]**| Filter by orf_list.@id | [optional] 
 **orf_list_aliases** | **List[str]**| Filter by orf_list.aliases | [optional] 
 **orf_list_genes_id** | **List[str]**| Filter by orf_list.genes.@id | [optional] 
 **orf_list_genes_symbol** | **List[str]**| Filter by orf_list.genes.symbol | [optional] 
 **orf_list_orf_id** | **List[str]**| Filter by orf_list.orf_id | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **scope** | **List[str]**| Filter by scope | [optional] 
 **selection_criteria** | **List[str]**| Filter by selection_criteria | [optional] 
 **small_scale_gene_list_id** | **List[str]**| Filter by small_scale_gene_list.@id | [optional] 
 **small_scale_gene_list_geneid** | **List[str]**| Filter by small_scale_gene_list.geneid | [optional] 
 **small_scale_gene_list_name** | **List[str]**| Filter by small_scale_gene_list.name | [optional] 
 **small_scale_gene_list_symbol** | **List[str]**| Filter by small_scale_gene_list.symbol | [optional] 
 **small_scale_gene_list_synonyms** | **List[str]**| Filter by small_scale_gene_list.synonyms | [optional] 
 **small_scale_loci_list** | **List[Locus]**| Filter by small_scale_loci_list | [optional] 
 **sources** | **List[str]**| Filter by sources | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **targeton** | **List[str]**| Filter by targeton | [optional] 
 **tiling_modality** | **List[str]**| Filter by tiling_modality | [optional] 
 **upper_bound_guide_coverage** | **List[int]**| Filter by upper_bound_guide_coverage | [optional] 
 **upper_bound_insert_size** | **List[int]**| Filter by upper_bound_insert_size | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**ConstructLibrarySetResults**](ConstructLibrarySetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **crispr_modifications**
> CrisprModificationResults crispr_modifications(query=query, limit=limit, sort=sort, id=id, activated=activated, activating_agent_term_id=activating_agent_term_id, activating_agent_term_name=activating_agent_term_name, aliases=aliases, award_id=award_id, award_component=award_component, biosamples_modified=biosamples_modified, cas=cas, cas_species=cas_species, creation_timestamp=creation_timestamp, description=description, documents=documents, fused_domain=fused_domain, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, modality=modality, notes=notes, product_id=product_id, release_timestamp=release_timestamp, sources=sources, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, tagged_proteins=tagged_proteins, uuid=uuid)

List items in the CrisprModification collection.

Collection endpoint that accepts various query parameters to filter and sort CrisprModification items. Supports filtering on fields within CrisprModification items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.crispr_modifications(**parameters) # List items in the CrisprModification collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **activated** | **List[bool]**| Filter by activated | [optional] 
 **activating_agent_term_id** | **List[str]**| Filter by activating_agent_term_id | [optional] 
 **activating_agent_term_name** | **List[str]**| Filter by activating_agent_term_name | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biosamples_modified** | **List[str]**| Filter by biosamples_modified | [optional] 
 **cas** | **List[str]**| Filter by cas | [optional] 
 **cas_species** | **List[str]**| Filter by cas_species | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **fused_domain** | **List[str]**| Filter by fused_domain | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **modality** | **List[str]**| Filter by modality | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **sources** | **List[str]**| Filter by sources | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **tagged_proteins** | **List[str]**| Filter by tagged_proteins | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**CrisprModificationResults**](CrisprModificationResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **curated_sets**
> CuratedSetResults curated_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, assemblies=assemblies, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, collections=collections, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform=files_sequencing_platform, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, input_for=input_for, lab_id=lab_id, lab_title=lab_title, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments=samples_cell_fate_change_treatments, samples_classifications=samples_classifications, samples_construct_library_sets=samples_construct_library_sets, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, taxa=taxa, transcriptome_annotations=transcriptome_annotations, url=url, uuid=uuid)

List items in the CuratedSet collection.

Collection endpoint that accepts various query parameters to filter and sort CuratedSet items. Supports filtering on fields within CuratedSet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.curated_sets(**parameters) # List items in the CuratedSet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **assemblies** | **List[str]**| Filter by assemblies | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform** | **List[str]**| Filter by files.sequencing_platform | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments** | **List[str]**| Filter by samples.cell_fate_change_treatments | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets** | **List[str]**| Filter by samples.construct_library_sets | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **transcriptome_annotations** | **List[str]**| Filter by transcriptome_annotations | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**CuratedSetResults**](CuratedSetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **degron_modifications**
> DegronModificationResults degron_modifications(query=query, limit=limit, sort=sort, id=id, activated=activated, activating_agent_term_id=activating_agent_term_id, activating_agent_term_name=activating_agent_term_name, aliases=aliases, award_id=award_id, award_component=award_component, biosamples_modified=biosamples_modified, creation_timestamp=creation_timestamp, degron_system=degron_system, description=description, documents=documents, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, modality=modality, notes=notes, product_id=product_id, release_timestamp=release_timestamp, sources=sources, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, tagged_proteins=tagged_proteins, uuid=uuid)

List items in the DegronModification collection.

Collection endpoint that accepts various query parameters to filter and sort DegronModification items. Supports filtering on fields within DegronModification items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.degron_modifications(**parameters) # List items in the DegronModification collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **activated** | **List[bool]**| Filter by activated | [optional] 
 **activating_agent_term_id** | **List[str]**| Filter by activating_agent_term_id | [optional] 
 **activating_agent_term_name** | **List[str]**| Filter by activating_agent_term_name | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biosamples_modified** | **List[str]**| Filter by biosamples_modified | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **degron_system** | **List[str]**| Filter by degron_system | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **modality** | **List[str]**| Filter by modality | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **sources** | **List[str]**| Filter by sources | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **tagged_proteins** | **List[str]**| Filter by tagged_proteins | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**DegronModificationResults**](DegronModificationResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents**
> DocumentResults documents(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, characterization_method=characterization_method, creation_timestamp=creation_timestamp, description=description, document_type=document_type, lab_id=lab_id, lab_title=lab_title, notes=notes, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, urls=urls, uuid=uuid)

List items in the Document collection.

Collection endpoint that accepts various query parameters to filter and sort Document items. Supports filtering on fields within Document items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.documents(**parameters) # List items in the Document collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **characterization_method** | **List[str]**| Filter by characterization_method | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **document_type** | **List[str]**| Filter by document_type | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **urls** | **List[str]**| Filter by urls | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**DocumentResults**](DocumentResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download**
> bytearray download(file_id)

Download file.

Returns underlying file associated with file metadata

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.download(**parameters) # Download file. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier for the file to download, e.g. @id (/tabular-files/IGVFFI8092FZKL/), accession (IGVFFI8092FZKL), or UUID (fdbdc159-e5b9-40a8-b788-3f72c9886b03). | 

### Return type

**bytearray**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Item not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genes**
> GeneResults genes(query=query, limit=limit, sort=sort, id=id, aliases=aliases, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, geneid=geneid, geneid_with_version=geneid_with_version, locations=locations, name=name, notes=notes, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, symbol=symbol, synonyms=synonyms, taxa=taxa, title=title, transcriptome_annotation=transcriptome_annotation, uuid=uuid, version_number=version_number)

List items in the Gene collection.

Collection endpoint that accepts various query parameters to filter and sort Gene items. Supports filtering on fields within Gene items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.genes(**parameters) # List items in the Gene collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **geneid** | **List[str]**| Filter by geneid | [optional] 
 **geneid_with_version** | **List[str]**| Filter by geneid_with_version | [optional] 
 **locations** | **List[GeneLocation]**| Filter by locations | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **symbol** | **List[str]**| Filter by symbol | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **version_number** | **List[str]**| Filter by version_number | [optional] 

### Return type

[**GeneResults**](GeneResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **genome_browser_annotation_files**
> GenomeBrowserAnnotationFileResults genome_browser_annotation_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, cell_type_annotation_id=cell_type_annotation_id, cell_type_annotation_term_name=cell_type_annotation_term_name, collections=collections, content_md5sum=content_md5sum, content_type=content_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_format_type=file_format_type, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the GenomeBrowserAnnotationFile collection.

Collection endpoint that accepts various query parameters to filter and sort GenomeBrowserAnnotationFile items. Supports filtering on fields within GenomeBrowserAnnotationFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.genome_browser_annotation_files(**parameters) # List items in the GenomeBrowserAnnotationFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **cell_type_annotation_id** | **List[str]**| Filter by cell_type_annotation.@id | [optional] 
 **cell_type_annotation_term_name** | **List[str]**| Filter by cell_type_annotation.term_name | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_format_type** | **List[str]**| Filter by file_format_type | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**GenomeBrowserAnnotationFileResults**](GenomeBrowserAnnotationFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_id**
> Item get_by_id(resource_id)

Get item information

Retrieve detailed information about a specific item using its @id or uuid.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.get_by_id(**parameters) # Get item information 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | **str**| The unique identifier for the resource i.e. @id (&#x60;/sequence-files/IGVFFI1165AJSO/&#x60;), accession (&#x60;IGVFFI1165AJSO&#x60;) or UUID (&#x60;fffcd64e-af02-4675-8953-7352459ee06a&#x60;). | 

### Return type

[**Item**](Item.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | Object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **human_donors**
> HumanDonorResults human_donors(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, collections=collections, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, ethnicities=ethnicities, human_donor_identifiers=human_donor_identifiers, lab_id=lab_id, lab_title=lab_title, notes=notes, phenotypic_features_id=phenotypic_features_id, phenotypic_features_feature_id=phenotypic_features_feature_id, phenotypic_features_feature_term_id=phenotypic_features_feature_term_id, phenotypic_features_feature_term_name=phenotypic_features_feature_term_name, phenotypic_features_observation_date=phenotypic_features_observation_date, phenotypic_features_quantity_units=phenotypic_features_quantity_units, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, related_donors_donor_id=related_donors_donor_id, related_donors_donor_accession=related_donors_donor_accession, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sex=sex, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, url=url, uuid=uuid, virtual=virtual)

List items in the HumanDonor collection.

Collection endpoint that accepts various query parameters to filter and sort HumanDonor items. Supports filtering on fields within HumanDonor items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.human_donors(**parameters) # List items in the HumanDonor collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **ethnicities** | **List[str]**| Filter by ethnicities | [optional] 
 **human_donor_identifiers** | **List[str]**| Filter by human_donor_identifiers | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **phenotypic_features_id** | **List[str]**| Filter by phenotypic_features.@id | [optional] 
 **phenotypic_features_feature_id** | **List[str]**| Filter by phenotypic_features.feature.@id | [optional] 
 **phenotypic_features_feature_term_id** | **List[str]**| Filter by phenotypic_features.feature.term_id | [optional] 
 **phenotypic_features_feature_term_name** | **List[str]**| Filter by phenotypic_features.feature.term_name | [optional] 
 **phenotypic_features_observation_date** | **List[str]**| Filter by phenotypic_features.observation_date | [optional] 
 **phenotypic_features_quantity_units** | **List[str]**| Filter by phenotypic_features.quantity_units | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **related_donors_donor_id** | **List[str]**| Filter by related_donors.donor.@id | [optional] 
 **related_donors_donor_accession** | **List[str]**| Filter by related_donors.donor.accession | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**HumanDonorResults**](HumanDonorResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_files**
> ImageFileResults image_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, assay_titles=assay_titles, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_type=content_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the ImageFile collection.

Collection endpoint that accepts various query parameters to filter and sort ImageFile items. Supports filtering on fields within ImageFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.image_files(**parameters) # List items in the ImageFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**ImageFileResults**](ImageFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **images**
> ImageResults images(query=query, limit=limit, sort=sort, id=id, aliases=aliases, caption=caption, creation_timestamp=creation_timestamp, description=description, download_url=download_url, notes=notes, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, thumb_nail=thumb_nail, uuid=uuid)

List items in the Image collection.

Collection endpoint that accepts various query parameters to filter and sort Image items. Supports filtering on fields within Image items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.images(**parameters) # List items in the Image collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **caption** | **List[str]**| Filter by caption | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **download_url** | **List[str]**| Filter by download_url | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **thumb_nail** | **List[str]**| Filter by thumb_nail | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**ImageResults**](ImageResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **in_vitro_systems**
> InVitroSystemResults in_vitro_systems(query=query, limit=limit, sort=sort, id=id, accession=accession, age=age, age_units=age_units, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, biomarkers_id=biomarkers_id, biomarkers_classification=biomarkers_classification, biomarkers_gene_id=biomarkers_gene_id, biomarkers_gene_symbol=biomarkers_gene_symbol, biomarkers_name_quantification=biomarkers_name_quantification, biosample_qualifiers=biosample_qualifiers, cell_fate_change_protocol=cell_fate_change_protocol, cell_fate_change_treatments_id=cell_fate_change_treatments_id, cell_fate_change_treatments_purpose=cell_fate_change_treatments_purpose, cell_fate_change_treatments_status=cell_fate_change_treatments_status, cell_fate_change_treatments_summary=cell_fate_change_treatments_summary, cell_fate_change_treatments_treatment_type=cell_fate_change_treatments_treatment_type, cellular_sub_pool=cellular_sub_pool, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, demultiplexed_from=demultiplexed_from, demultiplexed_to=demultiplexed_to, description=description, disease_terms_id=disease_terms_id, disease_terms_term_name=disease_terms_term_name, documents=documents, donors=donors, embryonic=embryonic, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, growth_medium=growth_medium, institutional_certificates_id=institutional_certificates_id, institutional_certificates_certificate_identifier=institutional_certificates_certificate_identifier, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, lower_bound_age=lower_bound_age, lower_bound_age_in_hours=lower_bound_age_in_hours, modifications_id=modifications_id, modifications_cas_species=modifications_cas_species, modifications_degron_system=modifications_degron_system, modifications_fused_domain=modifications_fused_domain, modifications_modality=modifications_modality, modifications_status=modifications_status, modifications_summary=modifications_summary, modifications_tagged_proteins_id=modifications_tagged_proteins_id, modifications_tagged_proteins_status=modifications_tagged_proteins_status, modifications_tagged_proteins_summary=modifications_tagged_proteins_summary, modifications_tagged_proteins_symbol=modifications_tagged_proteins_symbol, moi=moi, multiplexed_in_id=multiplexed_in_id, multiplexed_in_accession=multiplexed_in_accession, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, originated_from_id=originated_from_id, originated_from_accession=originated_from_accession, part_of=part_of, parts=parts, passage_number=passage_number, pooled_from=pooled_from, pooled_in=pooled_in, product_id=product_id, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sex=sex, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, targeted_sample_term_id=targeted_sample_term_id, targeted_sample_term_term_name=targeted_sample_term_term_name, taxa=taxa, time_post_change=time_post_change, time_post_change_units=time_post_change_units, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, treatments_id=treatments_id, treatments_depletion=treatments_depletion, treatments_purpose=treatments_purpose, treatments_status=treatments_status, treatments_treatment_term_name=treatments_treatment_term_name, treatments_treatment_type=treatments_treatment_type, upper_bound_age=upper_bound_age, upper_bound_age_in_hours=upper_bound_age_in_hours, url=url, uuid=uuid, virtual=virtual)

List items in the InVitroSystem collection.

Collection endpoint that accepts various query parameters to filter and sort InVitroSystem items. Supports filtering on fields within InVitroSystem items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.in_vitro_systems(**parameters) # List items in the InVitroSystem collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **age** | **List[str]**| Filter by age | [optional] 
 **age_units** | **List[str]**| Filter by age_units | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biomarkers_id** | **List[str]**| Filter by biomarkers.@id | [optional] 
 **biomarkers_classification** | **List[str]**| Filter by biomarkers.classification | [optional] 
 **biomarkers_gene_id** | **List[str]**| Filter by biomarkers.gene.@id | [optional] 
 **biomarkers_gene_symbol** | **List[str]**| Filter by biomarkers.gene.symbol | [optional] 
 **biomarkers_name_quantification** | **List[str]**| Filter by biomarkers.name_quantification | [optional] 
 **biosample_qualifiers** | **List[str]**| Filter by biosample_qualifiers | [optional] 
 **cell_fate_change_protocol** | **List[str]**| Filter by cell_fate_change_protocol | [optional] 
 **cell_fate_change_treatments_id** | **List[str]**| Filter by cell_fate_change_treatments.@id | [optional] 
 **cell_fate_change_treatments_purpose** | **List[str]**| Filter by cell_fate_change_treatments.purpose | [optional] 
 **cell_fate_change_treatments_status** | **List[str]**| Filter by cell_fate_change_treatments.status | [optional] 
 **cell_fate_change_treatments_summary** | **List[str]**| Filter by cell_fate_change_treatments.summary | [optional] 
 **cell_fate_change_treatments_treatment_type** | **List[str]**| Filter by cell_fate_change_treatments.treatment_type | [optional] 
 **cellular_sub_pool** | **List[str]**| Filter by cellular_sub_pool | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **demultiplexed_from** | **List[str]**| Filter by demultiplexed_from | [optional] 
 **demultiplexed_to** | **List[str]**| Filter by demultiplexed_to | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **disease_terms_id** | **List[str]**| Filter by disease_terms.@id | [optional] 
 **disease_terms_term_name** | **List[str]**| Filter by disease_terms.term_name | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **embryonic** | **List[bool]**| Filter by embryonic | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **growth_medium** | **List[str]**| Filter by growth_medium | [optional] 
 **institutional_certificates_id** | **List[str]**| Filter by institutional_certificates.@id | [optional] 
 **institutional_certificates_certificate_identifier** | **List[str]**| Filter by institutional_certificates.certificate_identifier | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **lower_bound_age** | **List[float]**| Filter by lower_bound_age | [optional] 
 **lower_bound_age_in_hours** | **List[float]**| Filter by lower_bound_age_in_hours | [optional] 
 **modifications_id** | **List[str]**| Filter by modifications.@id | [optional] 
 **modifications_cas_species** | **List[str]**| Filter by modifications.cas_species | [optional] 
 **modifications_degron_system** | **List[str]**| Filter by modifications.degron_system | [optional] 
 **modifications_fused_domain** | **List[str]**| Filter by modifications.fused_domain | [optional] 
 **modifications_modality** | **List[str]**| Filter by modifications.modality | [optional] 
 **modifications_status** | **List[str]**| Filter by modifications.status | [optional] 
 **modifications_summary** | **List[str]**| Filter by modifications.summary | [optional] 
 **modifications_tagged_proteins_id** | **List[str]**| Filter by modifications.tagged_proteins.@id | [optional] 
 **modifications_tagged_proteins_status** | **List[str]**| Filter by modifications.tagged_proteins.status | [optional] 
 **modifications_tagged_proteins_summary** | **List[str]**| Filter by modifications.tagged_proteins.summary | [optional] 
 **modifications_tagged_proteins_symbol** | **List[str]**| Filter by modifications.tagged_proteins.symbol | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in_id** | **List[str]**| Filter by multiplexed_in.@id | [optional] 
 **multiplexed_in_accession** | **List[str]**| Filter by multiplexed_in.accession | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **originated_from_id** | **List[str]**| Filter by originated_from.@id | [optional] 
 **originated_from_accession** | **List[str]**| Filter by originated_from.accession | [optional] 
 **part_of** | **List[str]**| Filter by part_of | [optional] 
 **parts** | **List[str]**| Filter by parts | [optional] 
 **passage_number** | **List[int]**| Filter by passage_number | [optional] 
 **pooled_from** | **List[str]**| Filter by pooled_from | [optional] 
 **pooled_in** | **List[str]**| Filter by pooled_in | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **targeted_sample_term_id** | **List[str]**| Filter by targeted_sample_term.@id | [optional] 
 **targeted_sample_term_term_name** | **List[str]**| Filter by targeted_sample_term.term_name | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_change** | **List[float]**| Filter by time_post_change | [optional] 
 **time_post_change_units** | **List[str]**| Filter by time_post_change_units | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **treatments_id** | **List[str]**| Filter by treatments.@id | [optional] 
 **treatments_depletion** | **List[bool]**| Filter by treatments.depletion | [optional] 
 **treatments_purpose** | **List[str]**| Filter by treatments.purpose | [optional] 
 **treatments_status** | **List[str]**| Filter by treatments.status | [optional] 
 **treatments_treatment_term_name** | **List[str]**| Filter by treatments.treatment_term_name | [optional] 
 **treatments_treatment_type** | **List[str]**| Filter by treatments.treatment_type | [optional] 
 **upper_bound_age** | **List[float]**| Filter by upper_bound_age | [optional] 
 **upper_bound_age_in_hours** | **List[float]**| Filter by upper_bound_age_in_hours | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**InVitroSystemResults**](InVitroSystemResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_files**
> IndexFileResults index_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, filtered=filtered, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, redacted=redacted, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the IndexFile collection.

Collection endpoint that accepts various query parameters to filter and sort IndexFile items. Supports filtering on fields within IndexFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.index_files(**parameters) # List items in the IndexFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **filtered** | **List[bool]**| Filter by filtered | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **redacted** | **List[bool]**| Filter by redacted | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**IndexFileResults**](IndexFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **institutional_certificates**
> InstitutionalCertificateResults institutional_certificates(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, certificate_identifier=certificate_identifier, controlled_access=controlled_access, creation_timestamp=creation_timestamp, data_use_limitation=data_use_limitation, data_use_limitation_modifiers=data_use_limitation_modifiers, description=description, lab_id=lab_id, lab_title=lab_title, notes=notes, release_timestamp=release_timestamp, samples=samples, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, urls=urls, uuid=uuid)

List items in the InstitutionalCertificate collection.

Collection endpoint that accepts various query parameters to filter and sort InstitutionalCertificate items. Supports filtering on fields within InstitutionalCertificate items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.institutional_certificates(**parameters) # List items in the InstitutionalCertificate collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **certificate_identifier** | **List[str]**| Filter by certificate_identifier | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **data_use_limitation** | **List[str]**| Filter by data_use_limitation | [optional] 
 **data_use_limitation_modifiers** | **List[str]**| Filter by data_use_limitation_modifiers | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **samples** | **List[str]**| Filter by samples | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **urls** | **List[str]**| Filter by urls | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**InstitutionalCertificateResults**](InstitutionalCertificateResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **labs**
> LabResults labs(query=query, limit=limit, sort=sort, id=id, aliases=aliases, awards_id=awards_id, awards_component=awards_component, awards_name=awards_name, creation_timestamp=creation_timestamp, description=description, institute_label=institute_label, name=name, notes=notes, pi=pi, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, url=url, uuid=uuid)

List items in the Lab collection.

Collection endpoint that accepts various query parameters to filter and sort Lab items. Supports filtering on fields within Lab items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.labs(**parameters) # List items in the Lab collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **awards_id** | **List[str]**| Filter by awards.@id | [optional] 
 **awards_component** | **List[str]**| Filter by awards.component | [optional] 
 **awards_name** | **List[str]**| Filter by awards.name | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **institute_label** | **List[str]**| Filter by institute_label | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **pi** | **List[str]**| Filter by pi | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**LabResults**](LabResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matrix_files**
> MatrixFileResults matrix_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, assay_titles=assay_titles, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_summary=content_summary, content_type=content_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, principal_dimension=principal_dimension, reference_files=reference_files, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, secondary_dimensions=secondary_dimensions, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the MatrixFile collection.

Collection endpoint that accepts various query parameters to filter and sort MatrixFile items. Supports filtering on fields within MatrixFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.matrix_files(**parameters) # List items in the MatrixFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_summary** | **List[str]**| Filter by content_summary | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **principal_dimension** | **List[str]**| Filter by principal_dimension | [optional] 
 **reference_files** | **List[str]**| Filter by reference_files | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **secondary_dimensions** | **List[str]**| Filter by secondary_dimensions | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**MatrixFileResults**](MatrixFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **measurement_sets**
> MeasurementSetResults measurement_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, assay_term_id=assay_term_id, assay_term_term_name=assay_term_term_name, auxiliary_sets_id=auxiliary_sets_id, auxiliary_sets_accession=auxiliary_sets_accession, auxiliary_sets_aliases=auxiliary_sets_aliases, auxiliary_sets_file_set_type=auxiliary_sets_file_set_type, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, collections=collections, control_file_sets_id=control_file_sets_id, control_file_sets_accession=control_file_sets_accession, control_file_sets_aliases=control_file_sets_aliases, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, external_image_url=external_image_url, externally_hosted=externally_hosted, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform_id=files_sequencing_platform_id, files_sequencing_platform_term_name=files_sequencing_platform_term_name, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, functional_assay_mechanisms_id=functional_assay_mechanisms_id, functional_assay_mechanisms_term_id=functional_assay_mechanisms_term_id, functional_assay_mechanisms_term_name=functional_assay_mechanisms_term_name, input_for=input_for, lab_id=lab_id, lab_title=lab_title, multiome_size=multiome_size, notes=notes, preferred_assay_title=preferred_assay_title, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, related_multiome_datasets_id=related_multiome_datasets_id, related_multiome_datasets_accession=related_multiome_datasets_accession, release_timestamp=release_timestamp, revoke_detail=revoke_detail, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments_id=samples_cell_fate_change_treatments_id, samples_cell_fate_change_treatments_purpose=samples_cell_fate_change_treatments_purpose, samples_cell_fate_change_treatments_summary=samples_cell_fate_change_treatments_summary, samples_cell_fate_change_treatments_treatment_type=samples_cell_fate_change_treatments_treatment_type, samples_classifications=samples_classifications, samples_construct_library_sets_id=samples_construct_library_sets_id, samples_construct_library_sets_accession=samples_construct_library_sets_accession, samples_construct_library_sets_file_set_type=samples_construct_library_sets_file_set_type, samples_construct_library_sets_small_scale_gene_list_id=samples_construct_library_sets_small_scale_gene_list_id, samples_construct_library_sets_small_scale_gene_list_geneid=samples_construct_library_sets_small_scale_gene_list_geneid, samples_construct_library_sets_small_scale_gene_list_name=samples_construct_library_sets_small_scale_gene_list_name, samples_construct_library_sets_small_scale_gene_list_summary=samples_construct_library_sets_small_scale_gene_list_summary, samples_construct_library_sets_small_scale_gene_list_symbol=samples_construct_library_sets_small_scale_gene_list_symbol, samples_construct_library_sets_summary=samples_construct_library_sets_summary, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_purpose=samples_treatments_purpose, samples_treatments_summary=samples_treatments_summary, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, samples_treatments_treatment_type=samples_treatments_treatment_type, sequencing_library_types=sequencing_library_types, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, targeted_genes_id=targeted_genes_id, targeted_genes_geneid=targeted_genes_geneid, targeted_genes_name=targeted_genes_name, targeted_genes_symbol=targeted_genes_symbol, targeted_genes_synonyms=targeted_genes_synonyms, uuid=uuid)

List items in the MeasurementSet collection.

Collection endpoint that accepts various query parameters to filter and sort MeasurementSet items. Supports filtering on fields within MeasurementSet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.measurement_sets(**parameters) # List items in the MeasurementSet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **assay_term_id** | **List[str]**| Filter by assay_term.@id | [optional] 
 **assay_term_term_name** | **List[str]**| Filter by assay_term.term_name | [optional] 
 **auxiliary_sets_id** | **List[str]**| Filter by auxiliary_sets.@id | [optional] 
 **auxiliary_sets_accession** | **List[str]**| Filter by auxiliary_sets.accession | [optional] 
 **auxiliary_sets_aliases** | **List[str]**| Filter by auxiliary_sets.aliases | [optional] 
 **auxiliary_sets_file_set_type** | **List[str]**| Filter by auxiliary_sets.file_set_type | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_file_sets_id** | **List[str]**| Filter by control_file_sets.@id | [optional] 
 **control_file_sets_accession** | **List[str]**| Filter by control_file_sets.accession | [optional] 
 **control_file_sets_aliases** | **List[str]**| Filter by control_file_sets.aliases | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **external_image_url** | **List[str]**| Filter by external_image_url | [optional] 
 **externally_hosted** | **List[bool]**| Filter by externally_hosted | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform_id** | **List[str]**| Filter by files.sequencing_platform.@id | [optional] 
 **files_sequencing_platform_term_name** | **List[str]**| Filter by files.sequencing_platform.term_name | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **functional_assay_mechanisms_id** | **List[str]**| Filter by functional_assay_mechanisms.@id | [optional] 
 **functional_assay_mechanisms_term_id** | **List[str]**| Filter by functional_assay_mechanisms.term_id | [optional] 
 **functional_assay_mechanisms_term_name** | **List[str]**| Filter by functional_assay_mechanisms.term_name | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **multiome_size** | **List[int]**| Filter by multiome_size | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **preferred_assay_title** | **List[str]**| Filter by preferred_assay_title | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **related_multiome_datasets_id** | **List[str]**| Filter by related_multiome_datasets.@id | [optional] 
 **related_multiome_datasets_accession** | **List[str]**| Filter by related_multiome_datasets.accession | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments_id** | **List[str]**| Filter by samples.cell_fate_change_treatments.@id | [optional] 
 **samples_cell_fate_change_treatments_purpose** | **List[str]**| Filter by samples.cell_fate_change_treatments.purpose | [optional] 
 **samples_cell_fate_change_treatments_summary** | **List[str]**| Filter by samples.cell_fate_change_treatments.summary | [optional] 
 **samples_cell_fate_change_treatments_treatment_type** | **List[str]**| Filter by samples.cell_fate_change_treatments.treatment_type | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets_id** | **List[str]**| Filter by samples.construct_library_sets.@id | [optional] 
 **samples_construct_library_sets_accession** | **List[str]**| Filter by samples.construct_library_sets.accession | [optional] 
 **samples_construct_library_sets_file_set_type** | **List[str]**| Filter by samples.construct_library_sets.file_set_type | [optional] 
 **samples_construct_library_sets_small_scale_gene_list_id** | **List[str]**| Filter by samples.construct_library_sets.small_scale_gene_list.@id | [optional] 
 **samples_construct_library_sets_small_scale_gene_list_geneid** | **List[str]**| Filter by samples.construct_library_sets.small_scale_gene_list.geneid | [optional] 
 **samples_construct_library_sets_small_scale_gene_list_name** | **List[str]**| Filter by samples.construct_library_sets.small_scale_gene_list.name | [optional] 
 **samples_construct_library_sets_small_scale_gene_list_summary** | **List[str]**| Filter by samples.construct_library_sets.small_scale_gene_list.summary | [optional] 
 **samples_construct_library_sets_small_scale_gene_list_symbol** | **List[str]**| Filter by samples.construct_library_sets.small_scale_gene_list.symbol | [optional] 
 **samples_construct_library_sets_summary** | **List[str]**| Filter by samples.construct_library_sets.summary | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_purpose** | **List[str]**| Filter by samples.treatments.purpose | [optional] 
 **samples_treatments_summary** | **List[str]**| Filter by samples.treatments.summary | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **samples_treatments_treatment_type** | **List[str]**| Filter by samples.treatments.treatment_type | [optional] 
 **sequencing_library_types** | **List[str]**| Filter by sequencing_library_types | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **targeted_genes_id** | **List[str]**| Filter by targeted_genes.@id | [optional] 
 **targeted_genes_geneid** | **List[str]**| Filter by targeted_genes.geneid | [optional] 
 **targeted_genes_name** | **List[str]**| Filter by targeted_genes.name | [optional] 
 **targeted_genes_symbol** | **List[str]**| Filter by targeted_genes.symbol | [optional] 
 **targeted_genes_synonyms** | **List[str]**| Filter by targeted_genes.synonyms | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**MeasurementSetResults**](MeasurementSetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_files**
> ModelFileResults model_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, external_host_url=external_host_url, externally_hosted=externally_hosted, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the ModelFile collection.

Collection endpoint that accepts various query parameters to filter and sort ModelFile items. Supports filtering on fields within ModelFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.model_files(**parameters) # List items in the ModelFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **external_host_url** | **List[str]**| Filter by external_host_url | [optional] 
 **externally_hosted** | **List[bool]**| Filter by externally_hosted | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**ModelFileResults**](ModelFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **model_sets**
> ModelSetResults model_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, assessed_genes_id=assessed_genes_id, assessed_genes_geneid=assessed_genes_geneid, assessed_genes_name=assessed_genes_name, assessed_genes_symbol=assessed_genes_symbol, assessed_genes_synonyms=assessed_genes_synonyms, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, collections=collections, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, external_input_data=external_input_data, externally_hosted=externally_hosted, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform=files_sequencing_platform, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, input_file_sets_id=input_file_sets_id, input_file_sets_accession=input_file_sets_accession, input_file_sets_aliases=input_file_sets_aliases, input_for=input_for, lab_id=lab_id, lab_title=lab_title, model_name=model_name, model_version=model_version, model_zoo_location=model_zoo_location, notes=notes, prediction_objects=prediction_objects, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments=samples_cell_fate_change_treatments, samples_classifications=samples_classifications, samples_construct_library_sets=samples_construct_library_sets, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, software_version=software_version, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, url=url, uuid=uuid)

List items in the ModelSet collection.

Collection endpoint that accepts various query parameters to filter and sort ModelSet items. Supports filtering on fields within ModelSet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.model_sets(**parameters) # List items in the ModelSet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **assessed_genes_id** | **List[str]**| Filter by assessed_genes.@id | [optional] 
 **assessed_genes_geneid** | **List[str]**| Filter by assessed_genes.geneid | [optional] 
 **assessed_genes_name** | **List[str]**| Filter by assessed_genes.name | [optional] 
 **assessed_genes_symbol** | **List[str]**| Filter by assessed_genes.symbol | [optional] 
 **assessed_genes_synonyms** | **List[str]**| Filter by assessed_genes.synonyms | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **external_input_data** | **List[str]**| Filter by external_input_data | [optional] 
 **externally_hosted** | **List[bool]**| Filter by externally_hosted | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform** | **List[str]**| Filter by files.sequencing_platform | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **input_file_sets_id** | **List[str]**| Filter by input_file_sets.@id | [optional] 
 **input_file_sets_accession** | **List[str]**| Filter by input_file_sets.accession | [optional] 
 **input_file_sets_aliases** | **List[str]**| Filter by input_file_sets.aliases | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **model_name** | **List[str]**| Filter by model_name | [optional] 
 **model_version** | **List[str]**| Filter by model_version | [optional] 
 **model_zoo_location** | **List[str]**| Filter by model_zoo_location | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **prediction_objects** | **List[str]**| Filter by prediction_objects | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments** | **List[str]**| Filter by samples.cell_fate_change_treatments | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets** | **List[str]**| Filter by samples.construct_library_sets | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **software_version** | **List[str]**| Filter by software_version | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**ModelSetResults**](ModelSetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **multiplexed_samples**
> MultiplexedSampleResults multiplexed_samples(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, barcode_map=barcode_map, biomarkers_id=biomarkers_id, biomarkers_classification=biomarkers_classification, biomarkers_gene_id=biomarkers_gene_id, biomarkers_gene_symbol=biomarkers_gene_symbol, biomarkers_name_quantification=biomarkers_name_quantification, cellular_sub_pool=cellular_sub_pool, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, description=description, disease_terms_id=disease_terms_id, disease_terms_term_name=disease_terms_term_name, documents=documents, donors=donors, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, institutional_certificates_id=institutional_certificates_id, institutional_certificates_certificate_identifier=institutional_certificates_certificate_identifier, lab_id=lab_id, lab_title=lab_title, modifications_id=modifications_id, modifications_cas_species=modifications_cas_species, modifications_degron_system=modifications_degron_system, modifications_fused_domain=modifications_fused_domain, modifications_status=modifications_status, modifications_summary=modifications_summary, moi=moi, multiplexed_in_id=multiplexed_in_id, multiplexed_in_accession=multiplexed_in_accession, multiplexed_samples_id=multiplexed_samples_id, multiplexed_samples_accession=multiplexed_samples_accession, multiplexed_samples_construct_library_sets=multiplexed_samples_construct_library_sets, multiplexed_samples_disease_terms_id=multiplexed_samples_disease_terms_id, multiplexed_samples_disease_terms_term_name=multiplexed_samples_disease_terms_term_name, multiplexed_samples_donors_id=multiplexed_samples_donors_id, multiplexed_samples_donors_accession=multiplexed_samples_donors_accession, multiplexed_samples_sample_terms_id=multiplexed_samples_sample_terms_id, multiplexed_samples_sample_terms_term_name=multiplexed_samples_sample_terms_term_name, multiplexed_samples_status=multiplexed_samples_status, multiplexed_samples_summary=multiplexed_samples_summary, multiplexing_methods=multiplexing_methods, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, treatments_id=treatments_id, treatments_depletion=treatments_depletion, treatments_purpose=treatments_purpose, treatments_status=treatments_status, treatments_treatment_term_name=treatments_treatment_term_name, treatments_treatment_type=treatments_treatment_type, url=url, uuid=uuid, virtual=virtual)

List items in the MultiplexedSample collection.

Collection endpoint that accepts various query parameters to filter and sort MultiplexedSample items. Supports filtering on fields within MultiplexedSample items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.multiplexed_samples(**parameters) # List items in the MultiplexedSample collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **barcode_map** | **List[str]**| Filter by barcode_map | [optional] 
 **biomarkers_id** | **List[str]**| Filter by biomarkers.@id | [optional] 
 **biomarkers_classification** | **List[str]**| Filter by biomarkers.classification | [optional] 
 **biomarkers_gene_id** | **List[str]**| Filter by biomarkers.gene.@id | [optional] 
 **biomarkers_gene_symbol** | **List[str]**| Filter by biomarkers.gene.symbol | [optional] 
 **biomarkers_name_quantification** | **List[str]**| Filter by biomarkers.name_quantification | [optional] 
 **cellular_sub_pool** | **List[str]**| Filter by cellular_sub_pool | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **disease_terms_id** | **List[str]**| Filter by disease_terms.@id | [optional] 
 **disease_terms_term_name** | **List[str]**| Filter by disease_terms.term_name | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **institutional_certificates_id** | **List[str]**| Filter by institutional_certificates.@id | [optional] 
 **institutional_certificates_certificate_identifier** | **List[str]**| Filter by institutional_certificates.certificate_identifier | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **modifications_id** | **List[str]**| Filter by modifications.@id | [optional] 
 **modifications_cas_species** | **List[str]**| Filter by modifications.cas_species | [optional] 
 **modifications_degron_system** | **List[str]**| Filter by modifications.degron_system | [optional] 
 **modifications_fused_domain** | **List[str]**| Filter by modifications.fused_domain | [optional] 
 **modifications_status** | **List[str]**| Filter by modifications.status | [optional] 
 **modifications_summary** | **List[str]**| Filter by modifications.summary | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in_id** | **List[str]**| Filter by multiplexed_in.@id | [optional] 
 **multiplexed_in_accession** | **List[str]**| Filter by multiplexed_in.accession | [optional] 
 **multiplexed_samples_id** | **List[str]**| Filter by multiplexed_samples.@id | [optional] 
 **multiplexed_samples_accession** | **List[str]**| Filter by multiplexed_samples.accession | [optional] 
 **multiplexed_samples_construct_library_sets** | **List[str]**| Filter by multiplexed_samples.construct_library_sets | [optional] 
 **multiplexed_samples_disease_terms_id** | **List[str]**| Filter by multiplexed_samples.disease_terms.@id | [optional] 
 **multiplexed_samples_disease_terms_term_name** | **List[str]**| Filter by multiplexed_samples.disease_terms.term_name | [optional] 
 **multiplexed_samples_donors_id** | **List[str]**| Filter by multiplexed_samples.donors.@id | [optional] 
 **multiplexed_samples_donors_accession** | **List[str]**| Filter by multiplexed_samples.donors.accession | [optional] 
 **multiplexed_samples_sample_terms_id** | **List[str]**| Filter by multiplexed_samples.sample_terms.@id | [optional] 
 **multiplexed_samples_sample_terms_term_name** | **List[str]**| Filter by multiplexed_samples.sample_terms.term_name | [optional] 
 **multiplexed_samples_status** | **List[str]**| Filter by multiplexed_samples.status | [optional] 
 **multiplexed_samples_summary** | **List[str]**| Filter by multiplexed_samples.summary | [optional] 
 **multiplexing_methods** | **List[str]**| Filter by multiplexing_methods | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **treatments_id** | **List[str]**| Filter by treatments.@id | [optional] 
 **treatments_depletion** | **List[bool]**| Filter by treatments.depletion | [optional] 
 **treatments_purpose** | **List[str]**| Filter by treatments.purpose | [optional] 
 **treatments_status** | **List[str]**| Filter by treatments.status | [optional] 
 **treatments_treatment_term_name** | **List[str]**| Filter by treatments.treatment_term_name | [optional] 
 **treatments_treatment_type** | **List[str]**| Filter by treatments.treatment_type | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**MultiplexedSampleResults**](MultiplexedSampleResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_reading_frames**
> OpenReadingFrameResults open_reading_frames(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award=award, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, genes_id=genes_id, genes_geneid=genes_geneid, genes_symbol=genes_symbol, lab=lab, notes=notes, orf_id=orf_id, pct_coverage_orf=pct_coverage_orf, pct_coverage_protein=pct_coverage_protein, pct_identical_protein=pct_identical_protein, protein_id=protein_id, release_timestamp=release_timestamp, status=status, submitted_by=submitted_by, submitter_comment=submitter_comment, summary=summary, uuid=uuid)

List items in the OpenReadingFrame collection.

Collection endpoint that accepts various query parameters to filter and sort OpenReadingFrame items. Supports filtering on fields within OpenReadingFrame items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.open_reading_frames(**parameters) # List items in the OpenReadingFrame collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award** | **List[str]**| Filter by award | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **genes_id** | **List[str]**| Filter by genes.@id | [optional] 
 **genes_geneid** | **List[str]**| Filter by genes.geneid | [optional] 
 **genes_symbol** | **List[str]**| Filter by genes.symbol | [optional] 
 **lab** | **List[str]**| Filter by lab | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **orf_id** | **List[str]**| Filter by orf_id | [optional] 
 **pct_coverage_orf** | **List[float]**| Filter by pct_coverage_orf | [optional] 
 **pct_coverage_protein** | **List[float]**| Filter by pct_coverage_protein | [optional] 
 **pct_identical_protein** | **List[float]**| Filter by pct_identical_protein | [optional] 
 **protein_id** | **List[str]**| Filter by protein_id | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by** | **List[str]**| Filter by submitted_by | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**OpenReadingFrameResults**](OpenReadingFrameResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pages**
> PageResults pages(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award=award, canonical_uri=canonical_uri, creation_timestamp=creation_timestamp, description=description, lab=lab, name=name, notes=notes, parent=parent, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, uuid=uuid)

List items in the Page collection.

Collection endpoint that accepts various query parameters to filter and sort Page items. Supports filtering on fields within Page items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.pages(**parameters) # List items in the Page collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award** | **List[str]**| Filter by award | [optional] 
 **canonical_uri** | **List[str]**| Filter by canonical_uri | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **lab** | **List[str]**| Filter by lab | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **parent** | **List[str]**| Filter by parent | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**PageResults**](PageResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phenotype_terms**
> PhenotypeTermResults phenotype_terms(query=query, limit=limit, sort=sort, id=id, aliases=aliases, ancestors=ancestors, creation_timestamp=creation_timestamp, deprecated_ntr_terms=deprecated_ntr_terms, description=description, is_a=is_a, name=name, notes=notes, ontology=ontology, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, synonyms=synonyms, term_id=term_id, term_name=term_name, uuid=uuid)

List items in the PhenotypeTerm collection.

Collection endpoint that accepts various query parameters to filter and sort PhenotypeTerm items. Supports filtering on fields within PhenotypeTerm items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.phenotype_terms(**parameters) # List items in the PhenotypeTerm collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **ancestors** | **List[str]**| Filter by ancestors | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **deprecated_ntr_terms** | **List[str]**| Filter by deprecated_ntr_terms | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **is_a** | **List[str]**| Filter by is_a | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **ontology** | **List[str]**| Filter by ontology | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **term_id** | **List[str]**| Filter by term_id | [optional] 
 **term_name** | **List[str]**| Filter by term_name | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**PhenotypeTermResults**](PhenotypeTermResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **phenotypic_features**
> PhenotypicFeatureResults phenotypic_features(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, description=description, feature_id=feature_id, feature_term_id=feature_term_id, feature_term_name=feature_term_name, lab_id=lab_id, lab_title=lab_title, notes=notes, observation_date=observation_date, quality=quality, quantity=quantity, quantity_units=quantity_units, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, uuid=uuid)

List items in the PhenotypicFeature collection.

Collection endpoint that accepts various query parameters to filter and sort PhenotypicFeature items. Supports filtering on fields within PhenotypicFeature items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.phenotypic_features(**parameters) # List items in the PhenotypicFeature collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **feature_id** | **List[str]**| Filter by feature.@id | [optional] 
 **feature_term_id** | **List[str]**| Filter by feature.term_id | [optional] 
 **feature_term_name** | **List[str]**| Filter by feature.term_name | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **observation_date** | **List[str]**| Filter by observation_date | [optional] 
 **quality** | **List[str]**| Filter by quality | [optional] 
 **quantity** | **List[float]**| Filter by quantity | [optional] 
 **quantity_units** | **List[str]**| Filter by quantity_units | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**PhenotypicFeatureResults**](PhenotypicFeatureResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **platform_terms**
> PlatformTermResults platform_terms(query=query, limit=limit, sort=sort, id=id, aliases=aliases, ancestors=ancestors, company=company, creation_timestamp=creation_timestamp, deprecated_ntr_terms=deprecated_ntr_terms, description=description, is_a=is_a, name=name, notes=notes, ontology=ontology, release_timestamp=release_timestamp, sequencing_kits=sequencing_kits, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, synonyms=synonyms, term_id=term_id, term_name=term_name, uuid=uuid)

List items in the PlatformTerm collection.

Collection endpoint that accepts various query parameters to filter and sort PlatformTerm items. Supports filtering on fields within PlatformTerm items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.platform_terms(**parameters) # List items in the PlatformTerm collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **ancestors** | **List[str]**| Filter by ancestors | [optional] 
 **company** | **List[str]**| Filter by company | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **deprecated_ntr_terms** | **List[str]**| Filter by deprecated_ntr_terms | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **is_a** | **List[str]**| Filter by is_a | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **ontology** | **List[str]**| Filter by ontology | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **sequencing_kits** | **List[str]**| Filter by sequencing_kits | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **term_id** | **List[str]**| Filter by term_id | [optional] 
 **term_name** | **List[str]**| Filter by term_name | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**PlatformTermResults**](PlatformTermResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prediction_sets**
> PredictionSetResults prediction_sets(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, assessed_genes_id=assessed_genes_id, assessed_genes_geneid=assessed_genes_geneid, assessed_genes_name=assessed_genes_name, assessed_genes_symbol=assessed_genes_symbol, assessed_genes_synonyms=assessed_genes_synonyms, award_id=award_id, award_component=award_component, award_contact_pi_id=award_contact_pi_id, award_contact_pi_title=award_contact_pi_title, award_title=award_title, collections=collections, control_for_id=control_for_id, control_for_accession=control_for_accession, control_for_aliases=control_for_aliases, control_type=control_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, donors_id=donors_id, donors_accession=donors_accession, donors_aliases=donors_aliases, donors_sex=donors_sex, donors_status=donors_status, donors_taxa=donors_taxa, file_set_type=file_set_type, files_id=files_id, files_accession=files_accession, files_aliases=files_aliases, files_assembly=files_assembly, files_content_type=files_content_type, files_creation_timestamp=files_creation_timestamp, files_file_format=files_file_format, files_file_size=files_file_size, files_href=files_href, files_s3_uri=files_s3_uri, files_sequencing_platform=files_sequencing_platform, files_submitted_file_name=files_submitted_file_name, files_transcriptome_annotation=files_transcriptome_annotation, files_upload_status=files_upload_status, input_file_sets=input_file_sets, input_for=input_for, lab_id=lab_id, lab_title=lab_title, large_scale_gene_list_id=large_scale_gene_list_id, large_scale_gene_list_accession=large_scale_gene_list_accession, large_scale_gene_list_aliases=large_scale_gene_list_aliases, large_scale_loci_list_id=large_scale_loci_list_id, large_scale_loci_list_accession=large_scale_loci_list_accession, large_scale_loci_list_aliases=large_scale_loci_list_aliases, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, samples_id=samples_id, samples_accession=samples_accession, samples_aliases=samples_aliases, samples_cell_fate_change_treatments=samples_cell_fate_change_treatments, samples_classifications=samples_classifications, samples_construct_library_sets_id=samples_construct_library_sets_id, samples_construct_library_sets_accession=samples_construct_library_sets_accession, samples_construct_library_sets_summary=samples_construct_library_sets_summary, samples_disease_terms_id=samples_disease_terms_id, samples_disease_terms_term_name=samples_disease_terms_term_name, samples_modifications_id=samples_modifications_id, samples_modifications_modality=samples_modifications_modality, samples_sample_terms_id=samples_sample_terms_id, samples_sample_terms_aliases=samples_sample_terms_aliases, samples_sample_terms_status=samples_sample_terms_status, samples_sample_terms_summary=samples_sample_terms_summary, samples_sample_terms_term_name=samples_sample_terms_term_name, samples_status=samples_status, samples_summary=samples_summary, samples_targeted_sample_term_id=samples_targeted_sample_term_id, samples_targeted_sample_term_term_name=samples_targeted_sample_term_term_name, samples_taxa=samples_taxa, samples_treatments_id=samples_treatments_id, samples_treatments_treatment_term_name=samples_treatments_treatment_term_name, scope=scope, small_scale_gene_list_id=small_scale_gene_list_id, small_scale_gene_list_geneid=small_scale_gene_list_geneid, small_scale_gene_list_name=small_scale_gene_list_name, small_scale_gene_list_symbol=small_scale_gene_list_symbol, small_scale_gene_list_synonyms=small_scale_gene_list_synonyms, small_scale_loci_list=small_scale_loci_list, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_files_timestamp=submitted_files_timestamp, submitter_comment=submitter_comment, summary=summary, url=url, uuid=uuid)

List items in the PredictionSet collection.

Collection endpoint that accepts various query parameters to filter and sort PredictionSet items. Supports filtering on fields within PredictionSet items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.prediction_sets(**parameters) # List items in the PredictionSet collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **assessed_genes_id** | **List[str]**| Filter by assessed_genes.@id | [optional] 
 **assessed_genes_geneid** | **List[str]**| Filter by assessed_genes.geneid | [optional] 
 **assessed_genes_name** | **List[str]**| Filter by assessed_genes.name | [optional] 
 **assessed_genes_symbol** | **List[str]**| Filter by assessed_genes.symbol | [optional] 
 **assessed_genes_synonyms** | **List[str]**| Filter by assessed_genes.synonyms | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **award_contact_pi_id** | **List[str]**| Filter by award.contact_pi.@id | [optional] 
 **award_contact_pi_title** | **List[str]**| Filter by award.contact_pi.title | [optional] 
 **award_title** | **List[str]**| Filter by award.title | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **control_for_id** | **List[str]**| Filter by control_for.@id | [optional] 
 **control_for_accession** | **List[str]**| Filter by control_for.accession | [optional] 
 **control_for_aliases** | **List[str]**| Filter by control_for.aliases | [optional] 
 **control_type** | **List[str]**| Filter by control_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors_id** | **List[str]**| Filter by donors.@id | [optional] 
 **donors_accession** | **List[str]**| Filter by donors.accession | [optional] 
 **donors_aliases** | **List[str]**| Filter by donors.aliases | [optional] 
 **donors_sex** | **List[str]**| Filter by donors.sex | [optional] 
 **donors_status** | **List[str]**| Filter by donors.status | [optional] 
 **donors_taxa** | **List[str]**| Filter by donors.taxa | [optional] 
 **file_set_type** | **List[str]**| Filter by file_set_type | [optional] 
 **files_id** | **List[str]**| Filter by files.@id | [optional] 
 **files_accession** | **List[str]**| Filter by files.accession | [optional] 
 **files_aliases** | **List[str]**| Filter by files.aliases | [optional] 
 **files_assembly** | **List[str]**| Filter by files.assembly | [optional] 
 **files_content_type** | **List[str]**| Filter by files.content_type | [optional] 
 **files_creation_timestamp** | **List[str]**| Filter by files.creation_timestamp | [optional] 
 **files_file_format** | **List[str]**| Filter by files.file_format | [optional] 
 **files_file_size** | **List[int]**| Filter by files.file_size | [optional] 
 **files_href** | **List[str]**| Filter by files.href | [optional] 
 **files_s3_uri** | **List[str]**| Filter by files.s3_uri | [optional] 
 **files_sequencing_platform** | **List[str]**| Filter by files.sequencing_platform | [optional] 
 **files_submitted_file_name** | **List[str]**| Filter by files.submitted_file_name | [optional] 
 **files_transcriptome_annotation** | **List[str]**| Filter by files.transcriptome_annotation | [optional] 
 **files_upload_status** | **List[str]**| Filter by files.upload_status | [optional] 
 **input_file_sets** | **List[str]**| Filter by input_file_sets | [optional] 
 **input_for** | **List[str]**| Filter by input_for | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **large_scale_gene_list_id** | **List[str]**| Filter by large_scale_gene_list.@id | [optional] 
 **large_scale_gene_list_accession** | **List[str]**| Filter by large_scale_gene_list.accession | [optional] 
 **large_scale_gene_list_aliases** | **List[str]**| Filter by large_scale_gene_list.aliases | [optional] 
 **large_scale_loci_list_id** | **List[str]**| Filter by large_scale_loci_list.@id | [optional] 
 **large_scale_loci_list_accession** | **List[str]**| Filter by large_scale_loci_list.accession | [optional] 
 **large_scale_loci_list_aliases** | **List[str]**| Filter by large_scale_loci_list.aliases | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **samples_id** | **List[str]**| Filter by samples.@id | [optional] 
 **samples_accession** | **List[str]**| Filter by samples.accession | [optional] 
 **samples_aliases** | **List[str]**| Filter by samples.aliases | [optional] 
 **samples_cell_fate_change_treatments** | **List[str]**| Filter by samples.cell_fate_change_treatments | [optional] 
 **samples_classifications** | **List[str]**| Filter by samples.classifications | [optional] 
 **samples_construct_library_sets_id** | **List[str]**| Filter by samples.construct_library_sets.@id | [optional] 
 **samples_construct_library_sets_accession** | **List[str]**| Filter by samples.construct_library_sets.accession | [optional] 
 **samples_construct_library_sets_summary** | **List[str]**| Filter by samples.construct_library_sets.summary | [optional] 
 **samples_disease_terms_id** | **List[str]**| Filter by samples.disease_terms.@id | [optional] 
 **samples_disease_terms_term_name** | **List[str]**| Filter by samples.disease_terms.term_name | [optional] 
 **samples_modifications_id** | **List[str]**| Filter by samples.modifications.@id | [optional] 
 **samples_modifications_modality** | **List[str]**| Filter by samples.modifications.modality | [optional] 
 **samples_sample_terms_id** | **List[str]**| Filter by samples.sample_terms.@id | [optional] 
 **samples_sample_terms_aliases** | **List[str]**| Filter by samples.sample_terms.aliases | [optional] 
 **samples_sample_terms_status** | **List[str]**| Filter by samples.sample_terms.status | [optional] 
 **samples_sample_terms_summary** | **List[str]**| Filter by samples.sample_terms.summary | [optional] 
 **samples_sample_terms_term_name** | **List[str]**| Filter by samples.sample_terms.term_name | [optional] 
 **samples_status** | **List[str]**| Filter by samples.status | [optional] 
 **samples_summary** | **List[str]**| Filter by samples.summary | [optional] 
 **samples_targeted_sample_term_id** | **List[str]**| Filter by samples.targeted_sample_term.@id | [optional] 
 **samples_targeted_sample_term_term_name** | **List[str]**| Filter by samples.targeted_sample_term.term_name | [optional] 
 **samples_taxa** | **List[str]**| Filter by samples.taxa | [optional] 
 **samples_treatments_id** | **List[str]**| Filter by samples.treatments.@id | [optional] 
 **samples_treatments_treatment_term_name** | **List[str]**| Filter by samples.treatments.treatment_term_name | [optional] 
 **scope** | **List[str]**| Filter by scope | [optional] 
 **small_scale_gene_list_id** | **List[str]**| Filter by small_scale_gene_list.@id | [optional] 
 **small_scale_gene_list_geneid** | **List[str]**| Filter by small_scale_gene_list.geneid | [optional] 
 **small_scale_gene_list_name** | **List[str]**| Filter by small_scale_gene_list.name | [optional] 
 **small_scale_gene_list_symbol** | **List[str]**| Filter by small_scale_gene_list.symbol | [optional] 
 **small_scale_gene_list_synonyms** | **List[str]**| Filter by small_scale_gene_list.synonyms | [optional] 
 **small_scale_loci_list** | **List[Locus]**| Filter by small_scale_loci_list | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_files_timestamp** | **List[str]**| Filter by submitted_files_timestamp | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**PredictionSetResults**](PredictionSetResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **primary_cells**
> PrimaryCellResults primary_cells(query=query, limit=limit, sort=sort, id=id, accession=accession, age=age, age_units=age_units, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, biomarkers_id=biomarkers_id, biomarkers_classification=biomarkers_classification, biomarkers_gene_id=biomarkers_gene_id, biomarkers_gene_symbol=biomarkers_gene_symbol, biomarkers_name_quantification=biomarkers_name_quantification, biosample_qualifiers=biosample_qualifiers, cellular_sub_pool=cellular_sub_pool, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, description=description, disease_terms_id=disease_terms_id, disease_terms_term_name=disease_terms_term_name, documents=documents, donors=donors, embryonic=embryonic, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, institutional_certificates_id=institutional_certificates_id, institutional_certificates_certificate_identifier=institutional_certificates_certificate_identifier, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, lower_bound_age=lower_bound_age, lower_bound_age_in_hours=lower_bound_age_in_hours, modifications_id=modifications_id, modifications_cas_species=modifications_cas_species, modifications_degron_system=modifications_degron_system, modifications_fused_domain=modifications_fused_domain, modifications_modality=modifications_modality, modifications_status=modifications_status, modifications_summary=modifications_summary, modifications_tagged_proteins_id=modifications_tagged_proteins_id, modifications_tagged_proteins_status=modifications_tagged_proteins_status, modifications_tagged_proteins_summary=modifications_tagged_proteins_summary, modifications_tagged_proteins_symbol=modifications_tagged_proteins_symbol, moi=moi, multiplexed_in_id=multiplexed_in_id, multiplexed_in_accession=multiplexed_in_accession, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, originated_from=originated_from, part_of=part_of, parts=parts, passage_number=passage_number, pooled_from=pooled_from, pooled_in=pooled_in, product_id=product_id, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sex=sex, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, treatments_id=treatments_id, treatments_depletion=treatments_depletion, treatments_purpose=treatments_purpose, treatments_status=treatments_status, treatments_treatment_term_name=treatments_treatment_term_name, treatments_treatment_type=treatments_treatment_type, upper_bound_age=upper_bound_age, upper_bound_age_in_hours=upper_bound_age_in_hours, url=url, uuid=uuid, virtual=virtual)

List items in the PrimaryCell collection.

Collection endpoint that accepts various query parameters to filter and sort PrimaryCell items. Supports filtering on fields within PrimaryCell items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.primary_cells(**parameters) # List items in the PrimaryCell collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **age** | **List[str]**| Filter by age | [optional] 
 **age_units** | **List[str]**| Filter by age_units | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biomarkers_id** | **List[str]**| Filter by biomarkers.@id | [optional] 
 **biomarkers_classification** | **List[str]**| Filter by biomarkers.classification | [optional] 
 **biomarkers_gene_id** | **List[str]**| Filter by biomarkers.gene.@id | [optional] 
 **biomarkers_gene_symbol** | **List[str]**| Filter by biomarkers.gene.symbol | [optional] 
 **biomarkers_name_quantification** | **List[str]**| Filter by biomarkers.name_quantification | [optional] 
 **biosample_qualifiers** | **List[str]**| Filter by biosample_qualifiers | [optional] 
 **cellular_sub_pool** | **List[str]**| Filter by cellular_sub_pool | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **disease_terms_id** | **List[str]**| Filter by disease_terms.@id | [optional] 
 **disease_terms_term_name** | **List[str]**| Filter by disease_terms.term_name | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **embryonic** | **List[bool]**| Filter by embryonic | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **institutional_certificates_id** | **List[str]**| Filter by institutional_certificates.@id | [optional] 
 **institutional_certificates_certificate_identifier** | **List[str]**| Filter by institutional_certificates.certificate_identifier | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **lower_bound_age** | **List[float]**| Filter by lower_bound_age | [optional] 
 **lower_bound_age_in_hours** | **List[float]**| Filter by lower_bound_age_in_hours | [optional] 
 **modifications_id** | **List[str]**| Filter by modifications.@id | [optional] 
 **modifications_cas_species** | **List[str]**| Filter by modifications.cas_species | [optional] 
 **modifications_degron_system** | **List[str]**| Filter by modifications.degron_system | [optional] 
 **modifications_fused_domain** | **List[str]**| Filter by modifications.fused_domain | [optional] 
 **modifications_modality** | **List[str]**| Filter by modifications.modality | [optional] 
 **modifications_status** | **List[str]**| Filter by modifications.status | [optional] 
 **modifications_summary** | **List[str]**| Filter by modifications.summary | [optional] 
 **modifications_tagged_proteins_id** | **List[str]**| Filter by modifications.tagged_proteins.@id | [optional] 
 **modifications_tagged_proteins_status** | **List[str]**| Filter by modifications.tagged_proteins.status | [optional] 
 **modifications_tagged_proteins_summary** | **List[str]**| Filter by modifications.tagged_proteins.summary | [optional] 
 **modifications_tagged_proteins_symbol** | **List[str]**| Filter by modifications.tagged_proteins.symbol | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in_id** | **List[str]**| Filter by multiplexed_in.@id | [optional] 
 **multiplexed_in_accession** | **List[str]**| Filter by multiplexed_in.accession | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **originated_from** | **List[str]**| Filter by originated_from | [optional] 
 **part_of** | **List[str]**| Filter by part_of | [optional] 
 **parts** | **List[str]**| Filter by parts | [optional] 
 **passage_number** | **List[int]**| Filter by passage_number | [optional] 
 **pooled_from** | **List[str]**| Filter by pooled_from | [optional] 
 **pooled_in** | **List[str]**| Filter by pooled_in | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **treatments_id** | **List[str]**| Filter by treatments.@id | [optional] 
 **treatments_depletion** | **List[bool]**| Filter by treatments.depletion | [optional] 
 **treatments_purpose** | **List[str]**| Filter by treatments.purpose | [optional] 
 **treatments_status** | **List[str]**| Filter by treatments.status | [optional] 
 **treatments_treatment_term_name** | **List[str]**| Filter by treatments.treatment_term_name | [optional] 
 **treatments_treatment_type** | **List[str]**| Filter by treatments.treatment_type | [optional] 
 **upper_bound_age** | **List[float]**| Filter by upper_bound_age | [optional] 
 **upper_bound_age_in_hours** | **List[float]**| Filter by upper_bound_age_in_hours | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**PrimaryCellResults**](PrimaryCellResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publications**
> PublicationResults publications(query=query, limit=limit, sort=sort, id=id, abstract=abstract, aliases=aliases, authors=authors, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, date_published=date_published, date_revised=date_revised, description=description, donors=donors, file_sets=file_sets, issue=issue, journal=journal, lab_id=lab_id, lab_title=lab_title, notes=notes, page=page, publication_identifiers=publication_identifiers, publication_year=publication_year, published_by=published_by, release_timestamp=release_timestamp, samples=samples, software=software, software_versions=software_versions, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, uuid=uuid, volume=volume, workflows=workflows)

List items in the Publication collection.

Collection endpoint that accepts various query parameters to filter and sort Publication items. Supports filtering on fields within Publication items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.publications(**parameters) # List items in the Publication collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **abstract** | **List[str]**| Filter by abstract | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **authors** | **List[str]**| Filter by authors | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_published** | **List[str]**| Filter by date_published | [optional] 
 **date_revised** | **List[str]**| Filter by date_revised | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **file_sets** | **List[str]**| Filter by file_sets | [optional] 
 **issue** | **List[str]**| Filter by issue | [optional] 
 **journal** | **List[str]**| Filter by journal | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **page** | **List[str]**| Filter by page | [optional] 
 **publication_identifiers** | **List[str]**| Filter by publication_identifiers | [optional] 
 **publication_year** | **List[int]**| Filter by publication_year | [optional] 
 **published_by** | **List[str]**| Filter by published_by | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **samples** | **List[str]**| Filter by samples | [optional] 
 **software** | **List[str]**| Filter by software | [optional] 
 **software_versions** | **List[str]**| Filter by software_versions | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **volume** | **List[str]**| Filter by volume | [optional] 
 **workflows** | **List[str]**| Filter by workflows | [optional] 

### Return type

[**PublicationResults**](PublicationResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_files**
> ReferenceFileResults reference_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, collections=collections, content_md5sum=content_md5sum, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, external=external, file_format=file_format, file_format_specifications=file_format_specifications, file_format_type=file_format_type, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, source_url=source_url, sources=sources, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the ReferenceFile collection.

Collection endpoint that accepts various query parameters to filter and sort ReferenceFile items. Supports filtering on fields within ReferenceFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.reference_files(**parameters) # List items in the ReferenceFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **external** | **List[bool]**| Filter by external | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_format_type** | **List[str]**| Filter by file_format_type | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **source_url** | **List[str]**| Filter by source_url | [optional] 
 **sources** | **List[str]**| Filter by sources | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**ReferenceFileResults**](ReferenceFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report**
> str report(query=query, type=type, limit=limit, sort=sort, field_filters=field_filters, include_fields=include_fields, frame=frame)

Generate a TSV file report based on search query. All results are returned.

Like /search endpoint but returns a TSV file instead of JSON. Must specify item type(s).

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.report(**parameters) # Generate a TSV file report based on search query. All results are returned. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **type** | **List[str]**| Filter by item type. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Does not work with limit&#x3D;all. | [optional] 
 **field_filters** | **object**| Any field from any item type can be used as a filter. Use &#39;!&#39; at end of field name for negation and &#39;lt:&#39;, &#39;lte:&#39;, &#39;gt:&#39;, &#39;gte:&#39; with value for range queries on numeric fields. Examples: {&#39;status!&#39;: &#39;in progress&#39;, &#39;file_size&#39;: &#39;gte:30000&#39;} | [optional] 
 **include_fields** | **List[str]**| Fields to include in the response. Can be repeated for multiple fields. | [optional] 
 **frame** | **str**| Object with links, or object with some links embedded. | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/tab-separated-values, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rodent_donors**
> RodentDonorResults rodent_donors(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, collections=collections, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, description=description, documents=documents, genotype=genotype, individual_rodent=individual_rodent, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, notes=notes, phenotypic_features_id=phenotypic_features_id, phenotypic_features_feature_id=phenotypic_features_feature_id, phenotypic_features_feature_term_id=phenotypic_features_feature_term_id, phenotypic_features_feature_term_name=phenotypic_features_feature_term_name, phenotypic_features_observation_date=phenotypic_features_observation_date, phenotypic_features_quantity_units=phenotypic_features_quantity_units, product_id=product_id, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, rodent_identifier=rodent_identifier, sex=sex, sources_id=sources_id, status=status, strain=strain, strain_background=strain_background, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, url=url, uuid=uuid, virtual=virtual)

List items in the RodentDonor collection.

Collection endpoint that accepts various query parameters to filter and sort RodentDonor items. Supports filtering on fields within RodentDonor items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.rodent_donors(**parameters) # List items in the RodentDonor collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **genotype** | **List[str]**| Filter by genotype | [optional] 
 **individual_rodent** | **List[bool]**| Filter by individual_rodent | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **phenotypic_features_id** | **List[str]**| Filter by phenotypic_features.@id | [optional] 
 **phenotypic_features_feature_id** | **List[str]**| Filter by phenotypic_features.feature.@id | [optional] 
 **phenotypic_features_feature_term_id** | **List[str]**| Filter by phenotypic_features.feature.term_id | [optional] 
 **phenotypic_features_feature_term_name** | **List[str]**| Filter by phenotypic_features.feature.term_name | [optional] 
 **phenotypic_features_observation_date** | **List[str]**| Filter by phenotypic_features.observation_date | [optional] 
 **phenotypic_features_quantity_units** | **List[str]**| Filter by phenotypic_features.quantity_units | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **rodent_identifier** | **List[str]**| Filter by rodent_identifier | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **strain** | **List[str]**| Filter by strain | [optional] 
 **strain_background** | **List[str]**| Filter by strain_background | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**RodentDonorResults**](RodentDonorResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sample_terms**
> SampleTermResults sample_terms(query=query, limit=limit, sort=sort, id=id, aliases=aliases, ancestors=ancestors, cell_slims=cell_slims, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, deprecated_ntr_terms=deprecated_ntr_terms, description=description, developmental_slims=developmental_slims, is_a=is_a, name=name, notes=notes, ontology=ontology, organ_slims=organ_slims, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, synonyms=synonyms, system_slims=system_slims, term_id=term_id, term_name=term_name, uuid=uuid)

List items in the SampleTerm collection.

Collection endpoint that accepts various query parameters to filter and sort SampleTerm items. Supports filtering on fields within SampleTerm items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.sample_terms(**parameters) # List items in the SampleTerm collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **ancestors** | **List[str]**| Filter by ancestors | [optional] 
 **cell_slims** | **List[str]**| Filter by cell_slims | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **deprecated_ntr_terms** | **List[str]**| Filter by deprecated_ntr_terms | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **developmental_slims** | **List[str]**| Filter by developmental_slims | [optional] 
 **is_a** | **List[str]**| Filter by is_a | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **ontology** | **List[str]**| Filter by ontology | [optional] 
 **organ_slims** | **List[str]**| Filter by organ_slims | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **synonyms** | **List[str]**| Filter by synonyms | [optional] 
 **system_slims** | **List[str]**| Filter by system_slims | [optional] 
 **term_id** | **List[str]**| Filter by term_id | [optional] 
 **term_name** | **List[str]**| Filter by term_name | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**SampleTermResults**](SampleTermResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_for_item_type**
> object schema_for_item_type(item_type)

Retrieve JSON schema for item type

Returns JSON schemas of all the item types defined in IGVF

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.schema_for_item_type(**parameters) # Retrieve JSON schema for item type 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_type** | **ItemType**| The name of the item type | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schemas**
> object schemas()

Retrieve JSON schemas for all item types

Returns JSON schemas of all the item types defined in IGVF

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.schemas(**parameters) # Retrieve JSON schemas for all item types 
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> SearchResults search(query=query, type=type, limit=limit, sort=sort, field_filters=field_filters)

Search for items on the IGVF Data Portal.

Search endpoint that accepts various query parameters to filter and sort results. Supports complex filtering on item types and fields within items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.search(**parameters) # Search for items on the IGVF Data Portal. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **type** | **List[str]**| Filter by item type. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Does not work with limit&#x3D;all. | [optional] 
 **field_filters** | **object**| Any field from any item type can be used as a filter. Use &#39;!&#39; at end of field name for negation and &#39;lt:&#39;, &#39;lte:&#39;, &#39;gt:&#39;, &#39;gte:&#39; with value for range queries on numeric fields. Examples: {&#39;status!&#39;: &#39;in progress&#39;, &#39;file_size&#39;: &#39;gte:30000&#39;} | [optional] 

### Return type

[**SearchResults**](SearchResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**404** | No results found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sequence_files**
> SequenceFileResults sequence_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, award_id=award_id, award_component=award_component, base_modifications=base_modifications, collections=collections, content_md5sum=content_md5sum, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, external_host_url=external_host_url, externally_hosted=externally_hosted, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, flowcell_id=flowcell_id, gene_list_for=gene_list_for, href=href, illumina_read_type=illumina_read_type, index=index, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, lane=lane, loci_list_for=loci_list_for, maximum_read_length=maximum_read_length, md5sum=md5sum, mean_read_length=mean_read_length, minimum_read_length=minimum_read_length, notes=notes, read_count=read_count, read_names=read_names, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, seqspecs=seqspecs, sequencing_kit=sequencing_kit, sequencing_platform_id=sequencing_platform_id, sequencing_platform_term_name=sequencing_platform_term_name, sequencing_run=sequencing_run, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the SequenceFile collection.

Collection endpoint that accepts various query parameters to filter and sort SequenceFile items. Supports filtering on fields within SequenceFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.sequence_files(**parameters) # List items in the SequenceFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **base_modifications** | **List[str]**| Filter by base_modifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **external_host_url** | **List[str]**| Filter by external_host_url | [optional] 
 **externally_hosted** | **List[bool]**| Filter by externally_hosted | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **flowcell_id** | **List[str]**| Filter by flowcell_id | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **illumina_read_type** | **List[str]**| Filter by illumina_read_type | [optional] 
 **index** | **List[str]**| Filter by index | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lane** | **List[int]**| Filter by lane | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **maximum_read_length** | **List[int]**| Filter by maximum_read_length | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **mean_read_length** | **List[float]**| Filter by mean_read_length | [optional] 
 **minimum_read_length** | **List[int]**| Filter by minimum_read_length | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **read_count** | **List[int]**| Filter by read_count | [optional] 
 **read_names** | **List[str]**| Filter by read_names | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **seqspecs** | **List[str]**| Filter by seqspecs | [optional] 
 **sequencing_kit** | **List[str]**| Filter by sequencing_kit | [optional] 
 **sequencing_platform_id** | **List[str]**| Filter by sequencing_platform.@id | [optional] 
 **sequencing_platform_term_name** | **List[str]**| Filter by sequencing_platform.term_name | [optional] 
 **sequencing_run** | **List[int]**| Filter by sequencing_run | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**SequenceFileResults**](SequenceFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_files**
> SignalFileResults signal_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, cell_type_annotation_id=cell_type_annotation_id, cell_type_annotation_term_name=cell_type_annotation_term_name, collections=collections, content_md5sum=content_md5sum, content_summary=content_summary, content_type=content_type, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, filtered=filtered, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, normalized=normalized, notes=notes, reference_files=reference_files, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, start_view_position=start_view_position, status=status, strand_specificity=strand_specificity, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the SignalFile collection.

Collection endpoint that accepts various query parameters to filter and sort SignalFile items. Supports filtering on fields within SignalFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.signal_files(**parameters) # List items in the SignalFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **cell_type_annotation_id** | **List[str]**| Filter by cell_type_annotation.@id | [optional] 
 **cell_type_annotation_term_name** | **List[str]**| Filter by cell_type_annotation.term_name | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_summary** | **List[str]**| Filter by content_summary | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **filtered** | **List[bool]**| Filter by filtered | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **normalized** | **List[bool]**| Filter by normalized | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **reference_files** | **List[str]**| Filter by reference_files | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **start_view_position** | **List[str]**| Filter by start_view_position | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **strand_specificity** | **List[str]**| Filter by strand_specificity | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**SignalFileResults**](SignalFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software**
> SoftwareResults software(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, description=description, lab_id=lab_id, lab_title=lab_title, name=name, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, source_url=source_url, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, used_by=used_by, uuid=uuid, versions=versions)

List items in the Software collection.

Collection endpoint that accepts various query parameters to filter and sort Software items. Supports filtering on fields within Software items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.software(**parameters) # List items in the Software collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **source_url** | **List[str]**| Filter by source_url | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **used_by** | **List[str]**| Filter by used_by | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **versions** | **List[str]**| Filter by versions | [optional] 

### Return type

[**SoftwareResults**](SoftwareResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **software_versions**
> SoftwareVersionResults software_versions(query=query, limit=limit, sort=sort, id=id, aliases=aliases, award_id=award_id, award_component=award_component, creation_timestamp=creation_timestamp, description=description, download_id=download_id, lab_id=lab_id, lab_title=lab_title, name=name, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, software_id=software_id, software_title=software_title, source_url=source_url, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, uuid=uuid, version=version)

List items in the SoftwareVersion collection.

Collection endpoint that accepts various query parameters to filter and sort SoftwareVersion items. Supports filtering on fields within SoftwareVersion items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.software_versions(**parameters) # List items in the SoftwareVersion collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **download_id** | **List[str]**| Filter by download_id | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **software_id** | **List[str]**| Filter by software.@id | [optional] 
 **software_title** | **List[str]**| Filter by software.title | [optional] 
 **source_url** | **List[str]**| Filter by source_url | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **version** | **List[str]**| Filter by version | [optional] 

### Return type

[**SoftwareVersionResults**](SoftwareVersionResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources**
> SourceResults sources(query=query, limit=limit, sort=sort, id=id, aliases=aliases, creation_timestamp=creation_timestamp, description=description, name=name, notes=notes, release_timestamp=release_timestamp, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, url=url, uuid=uuid)

List items in the Source collection.

Collection endpoint that accepts various query parameters to filter and sort Source items. Supports filtering on fields within Source items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.sources(**parameters) # List items in the Source collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**SourceResults**](SourceResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tabular_files**
> TabularFileResults tabular_files(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_step_version=analysis_step_version, anvil_url=anvil_url, assay_titles=assay_titles, assembly=assembly, award_id=award_id, award_component=award_component, barcode_map_for=barcode_map_for, cell_type_annotation_id=cell_type_annotation_id, cell_type_annotation_term_name=cell_type_annotation_term_name, collections=collections, content_md5sum=content_md5sum, content_type=content_type, controlled_access=controlled_access, creation_timestamp=creation_timestamp, dbxrefs=dbxrefs, derived_from=derived_from, derived_manually=derived_manually, description=description, documents=documents, file_format=file_format, file_format_specifications=file_format_specifications, file_format_type=file_format_type, file_set_id=file_set_id, file_set_accession=file_set_accession, file_set_file_set_type=file_set_file_set_type, file_set_samples_id=file_set_samples_id, file_set_samples_accession=file_set_samples_accession, file_set_samples_classifications=file_set_samples_classifications, file_set_samples_disease_terms_id=file_set_samples_disease_terms_id, file_set_samples_disease_terms_summary=file_set_samples_disease_terms_summary, file_set_samples_disease_terms_term_name=file_set_samples_disease_terms_term_name, file_set_samples_modifications_id=file_set_samples_modifications_id, file_set_samples_modifications_modality=file_set_samples_modifications_modality, file_set_samples_modifications_summary=file_set_samples_modifications_summary, file_set_samples_sample_terms_id=file_set_samples_sample_terms_id, file_set_samples_sample_terms_term_name=file_set_samples_sample_terms_term_name, file_set_samples_summary=file_set_samples_summary, file_set_samples_targeted_sample_term_id=file_set_samples_targeted_sample_term_id, file_set_samples_targeted_sample_term_term_name=file_set_samples_targeted_sample_term_term_name, file_set_samples_taxa=file_set_samples_taxa, file_set_samples_treatments_id=file_set_samples_treatments_id, file_set_samples_treatments_purpose=file_set_samples_treatments_purpose, file_set_samples_treatments_summary=file_set_samples_treatments_summary, file_set_samples_treatments_treatment_term_name=file_set_samples_treatments_treatment_term_name, file_set_summary=file_set_summary, file_set_taxa=file_set_taxa, file_size=file_size, gene_list_for=gene_list_for, href=href, input_file_for=input_file_for, integrated_in_id=integrated_in_id, integrated_in_associated_phenotypes_id=integrated_in_associated_phenotypes_id, integrated_in_associated_phenotypes_summary=integrated_in_associated_phenotypes_summary, integrated_in_associated_phenotypes_term_name=integrated_in_associated_phenotypes_term_name, integrated_in_file_set_type=integrated_in_file_set_type, integrated_in_small_scale_gene_list_id=integrated_in_small_scale_gene_list_id, integrated_in_small_scale_gene_list_symbol=integrated_in_small_scale_gene_list_symbol, integrated_in_summary=integrated_in_summary, lab_id=lab_id, lab_title=lab_title, loci_list_for=loci_list_for, md5sum=md5sum, notes=notes, release_timestamp=release_timestamp, revoke_detail=revoke_detail, s3_uri=s3_uri, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitted_file_name=submitted_file_name, submitter_comment=submitter_comment, summary=summary, transcriptome_annotation=transcriptome_annotation, upload_status=upload_status, uuid=uuid, validation_error_detail=validation_error_detail)

List items in the TabularFile collection.

Collection endpoint that accepts various query parameters to filter and sort TabularFile items. Supports filtering on fields within TabularFile items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.tabular_files(**parameters) # List items in the TabularFile collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_step_version** | **List[str]**| Filter by analysis_step_version | [optional] 
 **anvil_url** | **List[str]**| Filter by anvil_url | [optional] 
 **assay_titles** | **List[str]**| Filter by assay_titles | [optional] 
 **assembly** | **List[str]**| Filter by assembly | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **barcode_map_for** | **List[str]**| Filter by barcode_map_for | [optional] 
 **cell_type_annotation_id** | **List[str]**| Filter by cell_type_annotation.@id | [optional] 
 **cell_type_annotation_term_name** | **List[str]**| Filter by cell_type_annotation.term_name | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **content_md5sum** | **List[str]**| Filter by content_md5sum | [optional] 
 **content_type** | **List[str]**| Filter by content_type | [optional] 
 **controlled_access** | **List[bool]**| Filter by controlled_access | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **derived_from** | **List[str]**| Filter by derived_from | [optional] 
 **derived_manually** | **List[bool]**| Filter by derived_manually | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_format** | **List[str]**| Filter by file_format | [optional] 
 **file_format_specifications** | **List[str]**| Filter by file_format_specifications | [optional] 
 **file_format_type** | **List[str]**| Filter by file_format_type | [optional] 
 **file_set_id** | **List[str]**| Filter by file_set.@id | [optional] 
 **file_set_accession** | **List[str]**| Filter by file_set.accession | [optional] 
 **file_set_file_set_type** | **List[str]**| Filter by file_set.file_set_type | [optional] 
 **file_set_samples_id** | **List[str]**| Filter by file_set.samples.@id | [optional] 
 **file_set_samples_accession** | **List[str]**| Filter by file_set.samples.accession | [optional] 
 **file_set_samples_classifications** | **List[str]**| Filter by file_set.samples.classifications | [optional] 
 **file_set_samples_disease_terms_id** | **List[str]**| Filter by file_set.samples.disease_terms.@id | [optional] 
 **file_set_samples_disease_terms_summary** | **List[str]**| Filter by file_set.samples.disease_terms.summary | [optional] 
 **file_set_samples_disease_terms_term_name** | **List[str]**| Filter by file_set.samples.disease_terms.term_name | [optional] 
 **file_set_samples_modifications_id** | **List[str]**| Filter by file_set.samples.modifications.@id | [optional] 
 **file_set_samples_modifications_modality** | **List[str]**| Filter by file_set.samples.modifications.modality | [optional] 
 **file_set_samples_modifications_summary** | **List[str]**| Filter by file_set.samples.modifications.summary | [optional] 
 **file_set_samples_sample_terms_id** | **List[str]**| Filter by file_set.samples.sample_terms.@id | [optional] 
 **file_set_samples_sample_terms_term_name** | **List[str]**| Filter by file_set.samples.sample_terms.term_name | [optional] 
 **file_set_samples_summary** | **List[str]**| Filter by file_set.samples.summary | [optional] 
 **file_set_samples_targeted_sample_term_id** | **List[str]**| Filter by file_set.samples.targeted_sample_term.@id | [optional] 
 **file_set_samples_targeted_sample_term_term_name** | **List[str]**| Filter by file_set.samples.targeted_sample_term.term_name | [optional] 
 **file_set_samples_taxa** | **List[str]**| Filter by file_set.samples.taxa | [optional] 
 **file_set_samples_treatments_id** | **List[str]**| Filter by file_set.samples.treatments.@id | [optional] 
 **file_set_samples_treatments_purpose** | **List[str]**| Filter by file_set.samples.treatments.purpose | [optional] 
 **file_set_samples_treatments_summary** | **List[str]**| Filter by file_set.samples.treatments.summary | [optional] 
 **file_set_samples_treatments_treatment_term_name** | **List[str]**| Filter by file_set.samples.treatments.treatment_term_name | [optional] 
 **file_set_summary** | **List[str]**| Filter by file_set.summary | [optional] 
 **file_set_taxa** | **List[str]**| Filter by file_set.taxa | [optional] 
 **file_size** | **List[int]**| Filter by file_size | [optional] 
 **gene_list_for** | **List[str]**| Filter by gene_list_for | [optional] 
 **href** | **List[str]**| Filter by href | [optional] 
 **input_file_for** | **List[str]**| Filter by input_file_for | [optional] 
 **integrated_in_id** | **List[str]**| Filter by integrated_in.@id | [optional] 
 **integrated_in_associated_phenotypes_id** | **List[str]**| Filter by integrated_in.associated_phenotypes.@id | [optional] 
 **integrated_in_associated_phenotypes_summary** | **List[str]**| Filter by integrated_in.associated_phenotypes.summary | [optional] 
 **integrated_in_associated_phenotypes_term_name** | **List[str]**| Filter by integrated_in.associated_phenotypes.term_name | [optional] 
 **integrated_in_file_set_type** | **List[str]**| Filter by integrated_in.file_set_type | [optional] 
 **integrated_in_small_scale_gene_list_id** | **List[str]**| Filter by integrated_in.small_scale_gene_list.@id | [optional] 
 **integrated_in_small_scale_gene_list_symbol** | **List[str]**| Filter by integrated_in.small_scale_gene_list.symbol | [optional] 
 **integrated_in_summary** | **List[str]**| Filter by integrated_in.summary | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **loci_list_for** | **List[str]**| Filter by loci_list_for | [optional] 
 **md5sum** | **List[str]**| Filter by md5sum | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **s3_uri** | **List[str]**| Filter by s3_uri | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitted_file_name** | **List[str]**| Filter by submitted_file_name | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **transcriptome_annotation** | **List[str]**| Filter by transcriptome_annotation | [optional] 
 **upload_status** | **List[str]**| Filter by upload_status | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **validation_error_detail** | **List[str]**| Filter by validation_error_detail | [optional] 

### Return type

[**TabularFileResults**](TabularFileResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **technical_samples**
> TechnicalSampleResults technical_samples(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, description=description, documents=documents, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, institutional_certificates=institutional_certificates, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, moi=moi, multiplexed_in=multiplexed_in, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, product_id=product_id, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_material=sample_material, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, url=url, uuid=uuid, virtual=virtual)

List items in the TechnicalSample collection.

Collection endpoint that accepts various query parameters to filter and sort TechnicalSample items. Supports filtering on fields within TechnicalSample items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.technical_samples(**parameters) # List items in the TechnicalSample collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **institutional_certificates** | **List[str]**| Filter by institutional_certificates | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in** | **List[str]**| Filter by multiplexed_in | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_material** | **List[str]**| Filter by sample_material | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**TechnicalSampleResults**](TechnicalSampleResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tissues**
> TissueResults tissues(query=query, limit=limit, sort=sort, id=id, accession=accession, age=age, age_units=age_units, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, biomarkers_id=biomarkers_id, biomarkers_classification=biomarkers_classification, biomarkers_gene_id=biomarkers_gene_id, biomarkers_gene_symbol=biomarkers_gene_symbol, biomarkers_name_quantification=biomarkers_name_quantification, ccf_id=ccf_id, cellular_sub_pool=cellular_sub_pool, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, description=description, disease_terms_id=disease_terms_id, disease_terms_term_name=disease_terms_term_name, documents=documents, donors=donors, embryonic=embryonic, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, institutional_certificates_id=institutional_certificates_id, institutional_certificates_certificate_identifier=institutional_certificates_certificate_identifier, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, lower_bound_age=lower_bound_age, lower_bound_age_in_hours=lower_bound_age_in_hours, modifications_id=modifications_id, modifications_cas_species=modifications_cas_species, modifications_degron_system=modifications_degron_system, modifications_fused_domain=modifications_fused_domain, modifications_modality=modifications_modality, modifications_status=modifications_status, modifications_summary=modifications_summary, modifications_tagged_proteins_id=modifications_tagged_proteins_id, modifications_tagged_proteins_status=modifications_tagged_proteins_status, modifications_tagged_proteins_summary=modifications_tagged_proteins_summary, modifications_tagged_proteins_symbol=modifications_tagged_proteins_symbol, moi=moi, multiplexed_in_id=multiplexed_in_id, multiplexed_in_accession=multiplexed_in_accession, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, originated_from=originated_from, part_of=part_of, parts=parts, pmi=pmi, pmi_units=pmi_units, pooled_from=pooled_from, pooled_in=pooled_in, preservation_method=preservation_method, product_id=product_id, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sex=sex, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, treatments_id=treatments_id, treatments_depletion=treatments_depletion, treatments_purpose=treatments_purpose, treatments_status=treatments_status, treatments_treatment_term_name=treatments_treatment_term_name, treatments_treatment_type=treatments_treatment_type, upper_bound_age=upper_bound_age, upper_bound_age_in_hours=upper_bound_age_in_hours, url=url, uuid=uuid, virtual=virtual)

List items in the Tissue collection.

Collection endpoint that accepts various query parameters to filter and sort Tissue items. Supports filtering on fields within Tissue items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.tissues(**parameters) # List items in the Tissue collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **age** | **List[str]**| Filter by age | [optional] 
 **age_units** | **List[str]**| Filter by age_units | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biomarkers_id** | **List[str]**| Filter by biomarkers.@id | [optional] 
 **biomarkers_classification** | **List[str]**| Filter by biomarkers.classification | [optional] 
 **biomarkers_gene_id** | **List[str]**| Filter by biomarkers.gene.@id | [optional] 
 **biomarkers_gene_symbol** | **List[str]**| Filter by biomarkers.gene.symbol | [optional] 
 **biomarkers_name_quantification** | **List[str]**| Filter by biomarkers.name_quantification | [optional] 
 **ccf_id** | **List[str]**| Filter by ccf_id | [optional] 
 **cellular_sub_pool** | **List[str]**| Filter by cellular_sub_pool | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **disease_terms_id** | **List[str]**| Filter by disease_terms.@id | [optional] 
 **disease_terms_term_name** | **List[str]**| Filter by disease_terms.term_name | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **embryonic** | **List[bool]**| Filter by embryonic | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **institutional_certificates_id** | **List[str]**| Filter by institutional_certificates.@id | [optional] 
 **institutional_certificates_certificate_identifier** | **List[str]**| Filter by institutional_certificates.certificate_identifier | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **lower_bound_age** | **List[float]**| Filter by lower_bound_age | [optional] 
 **lower_bound_age_in_hours** | **List[float]**| Filter by lower_bound_age_in_hours | [optional] 
 **modifications_id** | **List[str]**| Filter by modifications.@id | [optional] 
 **modifications_cas_species** | **List[str]**| Filter by modifications.cas_species | [optional] 
 **modifications_degron_system** | **List[str]**| Filter by modifications.degron_system | [optional] 
 **modifications_fused_domain** | **List[str]**| Filter by modifications.fused_domain | [optional] 
 **modifications_modality** | **List[str]**| Filter by modifications.modality | [optional] 
 **modifications_status** | **List[str]**| Filter by modifications.status | [optional] 
 **modifications_summary** | **List[str]**| Filter by modifications.summary | [optional] 
 **modifications_tagged_proteins_id** | **List[str]**| Filter by modifications.tagged_proteins.@id | [optional] 
 **modifications_tagged_proteins_status** | **List[str]**| Filter by modifications.tagged_proteins.status | [optional] 
 **modifications_tagged_proteins_summary** | **List[str]**| Filter by modifications.tagged_proteins.summary | [optional] 
 **modifications_tagged_proteins_symbol** | **List[str]**| Filter by modifications.tagged_proteins.symbol | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in_id** | **List[str]**| Filter by multiplexed_in.@id | [optional] 
 **multiplexed_in_accession** | **List[str]**| Filter by multiplexed_in.accession | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **originated_from** | **List[str]**| Filter by originated_from | [optional] 
 **part_of** | **List[str]**| Filter by part_of | [optional] 
 **parts** | **List[str]**| Filter by parts | [optional] 
 **pmi** | **List[int]**| Filter by pmi | [optional] 
 **pmi_units** | **List[str]**| Filter by pmi_units | [optional] 
 **pooled_from** | **List[str]**| Filter by pooled_from | [optional] 
 **pooled_in** | **List[str]**| Filter by pooled_in | [optional] 
 **preservation_method** | **List[str]**| Filter by preservation_method | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **treatments_id** | **List[str]**| Filter by treatments.@id | [optional] 
 **treatments_depletion** | **List[bool]**| Filter by treatments.depletion | [optional] 
 **treatments_purpose** | **List[str]**| Filter by treatments.purpose | [optional] 
 **treatments_status** | **List[str]**| Filter by treatments.status | [optional] 
 **treatments_treatment_term_name** | **List[str]**| Filter by treatments.treatment_term_name | [optional] 
 **treatments_treatment_type** | **List[str]**| Filter by treatments.treatment_type | [optional] 
 **upper_bound_age** | **List[float]**| Filter by upper_bound_age | [optional] 
 **upper_bound_age_in_hours** | **List[float]**| Filter by upper_bound_age_in_hours | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**TissueResults**](TissueResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **treatments**
> TreatmentResults treatments(query=query, limit=limit, sort=sort, id=id, aliases=aliases, amount=amount, amount_units=amount_units, award_id=award_id, award_component=award_component, biosamples_treated=biosamples_treated, creation_timestamp=creation_timestamp, depletion=depletion, description=description, documents=documents, duration=duration, duration_units=duration_units, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, notes=notes, p_h=p_h, post_treatment_time=post_treatment_time, post_treatment_time_units=post_treatment_time_units, product_id=product_id, purpose=purpose, release_timestamp=release_timestamp, sources_id=sources_id, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, temperature=temperature, temperature_units=temperature_units, treatment_term_id=treatment_term_id, treatment_term_name=treatment_term_name, treatment_type=treatment_type, uuid=uuid)

List items in the Treatment collection.

Collection endpoint that accepts various query parameters to filter and sort Treatment items. Supports filtering on fields within Treatment items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.treatments(**parameters) # List items in the Treatment collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **amount** | **List[float]**| Filter by amount | [optional] 
 **amount_units** | **List[str]**| Filter by amount_units | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biosamples_treated** | **List[str]**| Filter by biosamples_treated | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **depletion** | **List[bool]**| Filter by depletion | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **duration** | **List[float]**| Filter by duration | [optional] 
 **duration_units** | **List[str]**| Filter by duration_units | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **p_h** | **List[float]**| Filter by pH | [optional] 
 **post_treatment_time** | **List[float]**| Filter by post_treatment_time | [optional] 
 **post_treatment_time_units** | **List[str]**| Filter by post_treatment_time_units | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **purpose** | **List[str]**| Filter by purpose | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **temperature** | **List[float]**| Filter by temperature | [optional] 
 **temperature_units** | **List[str]**| Filter by temperature_units | [optional] 
 **treatment_term_id** | **List[str]**| Filter by treatment_term_id | [optional] 
 **treatment_term_name** | **List[str]**| Filter by treatment_term_name | [optional] 
 **treatment_type** | **List[str]**| Filter by treatment_type | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 

### Return type

[**TreatmentResults**](TreatmentResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users**
> UserResults users(query=query, limit=limit, sort=sort, id=id, aliases=aliases, creation_timestamp=creation_timestamp, description=description, email=email, first_name=first_name, groups=groups, job_title=job_title, lab=lab, last_name=last_name, notes=notes, status=status, submits_for=submits_for, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, title=title, uuid=uuid, viewing_groups=viewing_groups)

List items in the User collection.

Collection endpoint that accepts various query parameters to filter and sort User items. Supports filtering on fields within User items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.users(**parameters) # List items in the User collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **email** | **List[str]**| Filter by email | [optional] 
 **first_name** | **List[str]**| Filter by first_name | [optional] 
 **groups** | **List[str]**| Filter by groups | [optional] 
 **job_title** | **List[str]**| Filter by job_title | [optional] 
 **lab** | **List[str]**| Filter by lab | [optional] 
 **last_name** | **List[str]**| Filter by last_name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submits_for** | **List[str]**| Filter by submits_for | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **title** | **List[str]**| Filter by title | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **viewing_groups** | **List[str]**| Filter by viewing_groups | [optional] 

### Return type

[**UserResults**](UserResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whole_organisms**
> WholeOrganismResults whole_organisms(query=query, limit=limit, sort=sort, id=id, accession=accession, age=age, age_units=age_units, aliases=aliases, alternate_accessions=alternate_accessions, award_id=award_id, award_component=award_component, biomarkers_id=biomarkers_id, biomarkers_classification=biomarkers_classification, biomarkers_gene_id=biomarkers_gene_id, biomarkers_gene_symbol=biomarkers_gene_symbol, biomarkers_name_quantification=biomarkers_name_quantification, cellular_sub_pool=cellular_sub_pool, classifications=classifications, collections=collections, construct_library_sets_id=construct_library_sets_id, construct_library_sets_accession=construct_library_sets_accession, construct_library_sets_associated_phenotypes_id=construct_library_sets_associated_phenotypes_id, construct_library_sets_associated_phenotypes_term_name=construct_library_sets_associated_phenotypes_term_name, construct_library_sets_file_set_type=construct_library_sets_file_set_type, creation_timestamp=creation_timestamp, date_obtained=date_obtained, dbxrefs=dbxrefs, description=description, disease_terms_id=disease_terms_id, disease_terms_term_name=disease_terms_term_name, documents=documents, donors=donors, embryonic=embryonic, file_sets_id=file_sets_id, file_sets_accession=file_sets_accession, file_sets_aliases=file_sets_aliases, file_sets_file_set_type=file_sets_file_set_type, file_sets_lab_title=file_sets_lab_title, file_sets_preferred_assay_title=file_sets_preferred_assay_title, file_sets_status=file_sets_status, file_sets_summary=file_sets_summary, institutional_certificates_id=institutional_certificates_id, institutional_certificates_certificate_identifier=institutional_certificates_certificate_identifier, lab_id=lab_id, lab_title=lab_title, lot_id=lot_id, lower_bound_age=lower_bound_age, lower_bound_age_in_hours=lower_bound_age_in_hours, modifications_id=modifications_id, modifications_cas_species=modifications_cas_species, modifications_degron_system=modifications_degron_system, modifications_fused_domain=modifications_fused_domain, modifications_modality=modifications_modality, modifications_status=modifications_status, modifications_summary=modifications_summary, modifications_tagged_proteins_id=modifications_tagged_proteins_id, modifications_tagged_proteins_status=modifications_tagged_proteins_status, modifications_tagged_proteins_summary=modifications_tagged_proteins_summary, modifications_tagged_proteins_symbol=modifications_tagged_proteins_symbol, moi=moi, multiplexed_in_id=multiplexed_in_id, multiplexed_in_accession=multiplexed_in_accession, notes=notes, nucleic_acid_delivery=nucleic_acid_delivery, origin_of=origin_of, originated_from=originated_from, part_of=part_of, parts=parts, pooled_from=pooled_from, pooled_in=pooled_in, product_id=product_id, protocols=protocols, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, sample_terms_id=sample_terms_id, sample_terms_term_name=sample_terms_term_name, sex=sex, sorted_fractions=sorted_fractions, sorted_from_id=sorted_from_id, sorted_from_accession=sorted_from_accession, sorted_from_detail=sorted_from_detail, sources_id=sources_id, starting_amount=starting_amount, starting_amount_units=starting_amount_units, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, taxa=taxa, time_post_library_delivery=time_post_library_delivery, time_post_library_delivery_units=time_post_library_delivery_units, treatments_id=treatments_id, treatments_depletion=treatments_depletion, treatments_purpose=treatments_purpose, treatments_status=treatments_status, treatments_treatment_term_name=treatments_treatment_term_name, treatments_treatment_type=treatments_treatment_type, upper_bound_age=upper_bound_age, upper_bound_age_in_hours=upper_bound_age_in_hours, url=url, uuid=uuid, virtual=virtual)

List items in the WholeOrganism collection.

Collection endpoint that accepts various query parameters to filter and sort WholeOrganism items. Supports filtering on fields within WholeOrganism items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.whole_organisms(**parameters) # List items in the WholeOrganism collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **age** | **List[str]**| Filter by age | [optional] 
 **age_units** | **List[str]**| Filter by age_units | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **biomarkers_id** | **List[str]**| Filter by biomarkers.@id | [optional] 
 **biomarkers_classification** | **List[str]**| Filter by biomarkers.classification | [optional] 
 **biomarkers_gene_id** | **List[str]**| Filter by biomarkers.gene.@id | [optional] 
 **biomarkers_gene_symbol** | **List[str]**| Filter by biomarkers.gene.symbol | [optional] 
 **biomarkers_name_quantification** | **List[str]**| Filter by biomarkers.name_quantification | [optional] 
 **cellular_sub_pool** | **List[str]**| Filter by cellular_sub_pool | [optional] 
 **classifications** | **List[str]**| Filter by classifications | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **construct_library_sets_id** | **List[str]**| Filter by construct_library_sets.@id | [optional] 
 **construct_library_sets_accession** | **List[str]**| Filter by construct_library_sets.accession | [optional] 
 **construct_library_sets_associated_phenotypes_id** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.@id | [optional] 
 **construct_library_sets_associated_phenotypes_term_name** | **List[str]**| Filter by construct_library_sets.associated_phenotypes.term_name | [optional] 
 **construct_library_sets_file_set_type** | **List[str]**| Filter by construct_library_sets.file_set_type | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **date_obtained** | **List[str]**| Filter by date_obtained | [optional] 
 **dbxrefs** | **List[str]**| Filter by dbxrefs | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **disease_terms_id** | **List[str]**| Filter by disease_terms.@id | [optional] 
 **disease_terms_term_name** | **List[str]**| Filter by disease_terms.term_name | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **donors** | **List[str]**| Filter by donors | [optional] 
 **embryonic** | **List[bool]**| Filter by embryonic | [optional] 
 **file_sets_id** | **List[str]**| Filter by file_sets.@id | [optional] 
 **file_sets_accession** | **List[str]**| Filter by file_sets.accession | [optional] 
 **file_sets_aliases** | **List[str]**| Filter by file_sets.aliases | [optional] 
 **file_sets_file_set_type** | **List[str]**| Filter by file_sets.file_set_type | [optional] 
 **file_sets_lab_title** | **List[str]**| Filter by file_sets.lab.title | [optional] 
 **file_sets_preferred_assay_title** | **List[str]**| Filter by file_sets.preferred_assay_title | [optional] 
 **file_sets_status** | **List[str]**| Filter by file_sets.status | [optional] 
 **file_sets_summary** | **List[str]**| Filter by file_sets.summary | [optional] 
 **institutional_certificates_id** | **List[str]**| Filter by institutional_certificates.@id | [optional] 
 **institutional_certificates_certificate_identifier** | **List[str]**| Filter by institutional_certificates.certificate_identifier | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **lot_id** | **List[str]**| Filter by lot_id | [optional] 
 **lower_bound_age** | **List[float]**| Filter by lower_bound_age | [optional] 
 **lower_bound_age_in_hours** | **List[float]**| Filter by lower_bound_age_in_hours | [optional] 
 **modifications_id** | **List[str]**| Filter by modifications.@id | [optional] 
 **modifications_cas_species** | **List[str]**| Filter by modifications.cas_species | [optional] 
 **modifications_degron_system** | **List[str]**| Filter by modifications.degron_system | [optional] 
 **modifications_fused_domain** | **List[str]**| Filter by modifications.fused_domain | [optional] 
 **modifications_modality** | **List[str]**| Filter by modifications.modality | [optional] 
 **modifications_status** | **List[str]**| Filter by modifications.status | [optional] 
 **modifications_summary** | **List[str]**| Filter by modifications.summary | [optional] 
 **modifications_tagged_proteins_id** | **List[str]**| Filter by modifications.tagged_proteins.@id | [optional] 
 **modifications_tagged_proteins_status** | **List[str]**| Filter by modifications.tagged_proteins.status | [optional] 
 **modifications_tagged_proteins_summary** | **List[str]**| Filter by modifications.tagged_proteins.summary | [optional] 
 **modifications_tagged_proteins_symbol** | **List[str]**| Filter by modifications.tagged_proteins.symbol | [optional] 
 **moi** | **List[float]**| Filter by moi | [optional] 
 **multiplexed_in_id** | **List[str]**| Filter by multiplexed_in.@id | [optional] 
 **multiplexed_in_accession** | **List[str]**| Filter by multiplexed_in.accession | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **nucleic_acid_delivery** | **List[str]**| Filter by nucleic_acid_delivery | [optional] 
 **origin_of** | **List[str]**| Filter by origin_of | [optional] 
 **originated_from** | **List[str]**| Filter by originated_from | [optional] 
 **part_of** | **List[str]**| Filter by part_of | [optional] 
 **parts** | **List[str]**| Filter by parts | [optional] 
 **pooled_from** | **List[str]**| Filter by pooled_from | [optional] 
 **pooled_in** | **List[str]**| Filter by pooled_in | [optional] 
 **product_id** | **List[str]**| Filter by product_id | [optional] 
 **protocols** | **List[str]**| Filter by protocols | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **sample_terms_id** | **List[str]**| Filter by sample_terms.@id | [optional] 
 **sample_terms_term_name** | **List[str]**| Filter by sample_terms.term_name | [optional] 
 **sex** | **List[str]**| Filter by sex | [optional] 
 **sorted_fractions** | **List[str]**| Filter by sorted_fractions | [optional] 
 **sorted_from_id** | **List[str]**| Filter by sorted_from.@id | [optional] 
 **sorted_from_accession** | **List[str]**| Filter by sorted_from.accession | [optional] 
 **sorted_from_detail** | **List[str]**| Filter by sorted_from_detail | [optional] 
 **sources_id** | **List[str]**| Filter by sources.@id | [optional] 
 **starting_amount** | **List[float]**| Filter by starting_amount | [optional] 
 **starting_amount_units** | **List[str]**| Filter by starting_amount_units | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **taxa** | **List[str]**| Filter by taxa | [optional] 
 **time_post_library_delivery** | **List[float]**| Filter by time_post_library_delivery | [optional] 
 **time_post_library_delivery_units** | **List[str]**| Filter by time_post_library_delivery_units | [optional] 
 **treatments_id** | **List[str]**| Filter by treatments.@id | [optional] 
 **treatments_depletion** | **List[bool]**| Filter by treatments.depletion | [optional] 
 **treatments_purpose** | **List[str]**| Filter by treatments.purpose | [optional] 
 **treatments_status** | **List[str]**| Filter by treatments.status | [optional] 
 **treatments_treatment_term_name** | **List[str]**| Filter by treatments.treatment_term_name | [optional] 
 **treatments_treatment_type** | **List[str]**| Filter by treatments.treatment_type | [optional] 
 **upper_bound_age** | **List[float]**| Filter by upper_bound_age | [optional] 
 **upper_bound_age_in_hours** | **List[float]**| Filter by upper_bound_age_in_hours | [optional] 
 **url** | **List[str]**| Filter by url | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **virtual** | **List[bool]**| Filter by virtual | [optional] 

### Return type

[**WholeOrganismResults**](WholeOrganismResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **workflows**
> WorkflowResults workflows(query=query, limit=limit, sort=sort, id=id, accession=accession, aliases=aliases, alternate_accessions=alternate_accessions, analysis_steps_id=analysis_steps_id, analysis_steps_analysis_step_types=analysis_steps_analysis_step_types, analysis_steps_analysis_step_versions_id=analysis_steps_analysis_step_versions_id, analysis_steps_analysis_step_versions_software_versions_id=analysis_steps_analysis_step_versions_software_versions_id, analysis_steps_analysis_step_versions_software_versions_name=analysis_steps_analysis_step_versions_software_versions_name, analysis_steps_analysis_step_versions_software_versions_software_id=analysis_steps_analysis_step_versions_software_versions_software_id, analysis_steps_analysis_step_versions_software_versions_software_name=analysis_steps_analysis_step_versions_software_versions_software_name, analysis_steps_name=analysis_steps_name, analysis_steps_output_content_types=analysis_steps_output_content_types, award_id=award_id, award_component=award_component, collections=collections, creation_timestamp=creation_timestamp, description=description, documents=documents, lab_id=lab_id, lab_title=lab_title, name=name, notes=notes, publications_id=publications_id, publications_publication_identifiers=publications_publication_identifiers, release_timestamp=release_timestamp, revoke_detail=revoke_detail, source_url=source_url, standards_page_id=standards_page_id, standards_page_title=standards_page_title, status=status, submitted_by_id=submitted_by_id, submitted_by_title=submitted_by_title, submitter_comment=submitter_comment, summary=summary, uniform_pipeline=uniform_pipeline, uuid=uuid, workflow_repositories=workflow_repositories, workflow_version=workflow_version)

List items in the Workflow collection.

Collection endpoint that accepts various query parameters to filter and sort Workflow items. Supports filtering on fields within Workflow items.

### Example

```python
from igvf_client import IgvfApi

api = IgvfApi()

api.workflows(**parameters) # List items in the Workflow collection. 
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query string for searching. | [optional] 
 **limit** | **Limit**| Maximum number of results to return. Default is 25. Use &#39;all&#39; for all results. | [optional] 
 **sort** | **List[str]**| Fields to sort results by. Prefix with &#39;-&#39; for descending order. Can be repeated for multiple sort fields. Does not work with limit&#x3D;all. | [optional] 
 **id** | **List[str]**| Filter by @id | [optional] 
 **accession** | **List[str]**| Filter by accession | [optional] 
 **aliases** | **List[str]**| Filter by aliases | [optional] 
 **alternate_accessions** | **List[str]**| Filter by alternate_accessions | [optional] 
 **analysis_steps_id** | **List[str]**| Filter by analysis_steps.@id | [optional] 
 **analysis_steps_analysis_step_types** | **List[str]**| Filter by analysis_steps.analysis_step_types | [optional] 
 **analysis_steps_analysis_step_versions_id** | **List[str]**| Filter by analysis_steps.analysis_step_versions.@id | [optional] 
 **analysis_steps_analysis_step_versions_software_versions_id** | **List[str]**| Filter by analysis_steps.analysis_step_versions.software_versions.@id | [optional] 
 **analysis_steps_analysis_step_versions_software_versions_name** | **List[str]**| Filter by analysis_steps.analysis_step_versions.software_versions.name | [optional] 
 **analysis_steps_analysis_step_versions_software_versions_software_id** | **List[str]**| Filter by analysis_steps.analysis_step_versions.software_versions.software.@id | [optional] 
 **analysis_steps_analysis_step_versions_software_versions_software_name** | **List[str]**| Filter by analysis_steps.analysis_step_versions.software_versions.software.name | [optional] 
 **analysis_steps_name** | **List[str]**| Filter by analysis_steps.name | [optional] 
 **analysis_steps_output_content_types** | **List[str]**| Filter by analysis_steps.output_content_types | [optional] 
 **award_id** | **List[str]**| Filter by award.@id | [optional] 
 **award_component** | **List[str]**| Filter by award.component | [optional] 
 **collections** | **List[str]**| Filter by collections | [optional] 
 **creation_timestamp** | **List[str]**| Filter by creation_timestamp | [optional] 
 **description** | **List[str]**| Filter by description | [optional] 
 **documents** | **List[str]**| Filter by documents | [optional] 
 **lab_id** | **List[str]**| Filter by lab.@id | [optional] 
 **lab_title** | **List[str]**| Filter by lab.title | [optional] 
 **name** | **List[str]**| Filter by name | [optional] 
 **notes** | **List[str]**| Filter by notes | [optional] 
 **publications_id** | **List[str]**| Filter by publications.@id | [optional] 
 **publications_publication_identifiers** | **List[str]**| Filter by publications.publication_identifiers | [optional] 
 **release_timestamp** | **List[str]**| Filter by release_timestamp | [optional] 
 **revoke_detail** | **List[str]**| Filter by revoke_detail | [optional] 
 **source_url** | **List[str]**| Filter by source_url | [optional] 
 **standards_page_id** | **List[str]**| Filter by standards_page.@id | [optional] 
 **standards_page_title** | **List[str]**| Filter by standards_page.title | [optional] 
 **status** | **List[str]**| Filter by status | [optional] 
 **submitted_by_id** | **List[str]**| Filter by submitted_by.@id | [optional] 
 **submitted_by_title** | **List[str]**| Filter by submitted_by.title | [optional] 
 **submitter_comment** | **List[str]**| Filter by submitter_comment | [optional] 
 **summary** | **List[str]**| Filter by summary | [optional] 
 **uniform_pipeline** | **List[bool]**| Filter by uniform_pipeline | [optional] 
 **uuid** | **List[str]**| Filter by uuid | [optional] 
 **workflow_repositories** | **List[str]**| Filter by workflow_repositories | [optional] 
 **workflow_version** | **List[int]**| Filter by workflow_version | [optional] 

### Return type

[**WorkflowResults**](WorkflowResults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**404** | No results found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

