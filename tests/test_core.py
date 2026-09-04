from restscope import duplicates, group_by_method, normalize_endpoint


def test_normalize_and_group():
    assert normalize_endpoint({"method": "post", "path": " /users "}) == {"method": "POST", "path": "/users"}
    groups = group_by_method([{"method": "get", "path": "/a"}, {"method": "post", "path": "/a"}])
    assert list(groups) == ["GET", "POST"]


def test_duplicates():
    items = [{"method": "GET", "path": "/a"}, {"method": "GET", "path": "/a"}]
    assert len(duplicates(items)) == 2
