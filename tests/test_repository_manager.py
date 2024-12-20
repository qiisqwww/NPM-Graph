import os

from src.repository_manager import RepositoryManager


def test_repository_lifecycle(config: dict) -> None:
    repo_url = config['repository']['repo_url']
    repo_name = config['repository']['name']

    repository_manager = RepositoryManager(repo_url, repo_name)
    repository_manager._git_clone_cmd = ['mkdir', repo_name]
    repository_manager._npm_install_cmd = ['echo', '))']

    existed = os.path.exists(repository_manager.repo_path)

    with repository_manager:
        created = os.path.exists(repository_manager.repo_path)
    left = os.path.exists(repository_manager.repo_path)

    assert not existed and created and not left
