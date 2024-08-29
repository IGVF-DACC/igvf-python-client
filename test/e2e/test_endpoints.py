import pytest


def test_endpoints_test_search_simple():
    from igvf_client import IgvfApi
    from igvf_client.models.software import Software
    api = IgvfApi()
    r = api.search(query='abc')
    assert r.total > 2
    r = api.search(query='abc', limit=1)
    assert len(r.graph) == 1
    r = api.search(query='abc', type=['Software'], limit=1)
    assert len(r.graph) == 1
    item = r.graph[0].actual_instance
    assert isinstance(item, Software)
    assert item.type == ['Software', 'Item']
    assert 'software' in item.id
    assert 'lab' in item.lab
    assert 'award' in item.award
    assert item.status == 'released'
    assert item.uuid is not None
    assert item.title is not None


def test_endpoints_test_search_filters():
    from igvf_client import IgvfApi
    from igvf_client.models.software import Software
    api = IgvfApi()
    all_users = api.search(type=['User'], limit=0)
    cherry_lab_users = api.search(
        type=['User'],
        limit=0,
        field_filters={
            'lab': '/labs/j-michael-cherry/'
        }
    )
    assert cherry_lab_users.total > 10
    assert all_users.total > cherry_lab_users.total


def test_endpoints_test_collections():
    from igvf_client import IgvfApi
    api = IgvfApi()
    file_id = '/sequence-files/IGVFFI4531KBUU/'
    files = api.measurement_sets(files_id=[file_id]).graph[0].files
    assert len(files) >= 1
    assert file_id in files
    users = api.users(lab=['/labs/j-michael-cherry/'])
    assert users.total > 10
    assert users.graph[0].lab == '/labs/j-michael-cherry/'


def test_endpoints_test_schemas():
    from igvf_client import IgvfApi
    api = IgvfApi()
    schemas = api.schemas()
    assert len(schemas) > 50
    assert 'AccessKey' in schemas
    assert 'User' in schemas
    user_schema = api.schema_for_item_type('User')
    assert schemas['User'] == user_schema


def test_endpoints_test_user_collection():
    from igvf_client import IgvfApi
    api = IgvfApi()
    users = api.users(title=['Indexing Service'])
    assert users.total == 1
    assert users.id == '/users/@@listing?title=Indexing%20Service&frame=object'
    assert users.graph[0].id == '/users/1ac5c055-d3e8-4290-a4bb-d5e2f508e54a/'
    assert users.graph[0].uuid == '1ac5c055-d3e8-4290-a4bb-d5e2f508e54a'
    assert users.graph[0].lab == '/labs/j-michael-cherry/'
    assert users.graph[0].title == 'Indexing Service'
    assert users.graph[0].type == ['User', 'Item']
    user = api.get_by_id(users.graph[0].uuid)
    assert user.actual_instance == users.graph[0]


def test_endpoints_test_report():
    from igvf_client import IgvfApi
    api = IgvfApi()
    r = api.report(type=['User'], field_filters={'lab': '/labs/j-michael-cherry/'})
    assert 'Indexing Service' in r
    assert 'J. Michael Cherry' in r
    assert 'ID' in r
    assert 'UUID' in r
    assert 'Title' in r
    assert 'Lab' in r
    assert 'Status' in r


def test_endpoints_test_curated_set_collection():
    from igvf_client import IgvfApi
    api = IgvfApi()
    curated_sets = api.curated_sets(files_file_format=['tsv'])
    assert curated_sets.total > 10


def test_endpoints_test_download_tsv_file():
    from igvf_client import IgvfApi
    api = IgvfApi()
    r = api.search(field_filters={'file_format': 'tsv'})
    raw_tsv = api.download(r.graph[0].uuid)
    assert isinstance(raw_tsv, bytes)
    assert len(raw_tsv) > 1


def test_endpoints_test_search_facets():
    from igvf_client import IgvfApi
    api = IgvfApi()
    actual_types = [x['key'] for x in api.search(field_filters={'files.file_format': 'tsv'}).facets[0].terms]
    expected_types = ['FileSet', 'AuxiliarySet', 'CuratedSet']
    for type_ in expected_types:
        assert type_ in actual_types


def test_endpoints_test_search_field_filters():
    from igvf_client import IgvfApi
    api = IgvfApi()
    r = api.search(type=['Item'], field_filters={'status': 'current'})
    assert r.total > 100
    r2 = api.search(type=['Item'], field_filters={'status': ['current', 'released']})
    assert r2.total > r.total
