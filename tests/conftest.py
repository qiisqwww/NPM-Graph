import pytest


@pytest.fixture()
def config():
    return {
        "repository": {
            "name": "demo-auth-website",
            "repo_url": "https://github.com/qiisqwww/demo-auth-website"
        },
        "output": {
            "result_file": "dependency_graph.dot"
        }
    }
