from src.config_loader import ConfigLoader


def test_config_loader() -> None:
    config_loader = ConfigLoader('config.toml')
    config = config_loader.load_config()

    assert (
            isinstance(config, dict) and config.get('repository') and config.get('output')
            and config['repository'].get('name') and config['repository'].get('repo_url')
            and config['output'].get('result_file')
            )
