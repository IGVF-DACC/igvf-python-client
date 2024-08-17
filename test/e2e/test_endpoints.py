import pytest


def test_endpoints_test_api():
    from igvf_client import IgvfApi
    from igvf_client.models.software import Software
    api = IgvfApi()
    r = api.search(query='abc')
    assert r.total > 2
    r = api.search(query='abc', limit=1)
    assert len(r.graph) == 1
    r = api.search(query='abc', type=['Software'], limit=1)
    assert len(r.graph) == 1
    assert isinstance(r.graph[0].actual_instance, Software)
