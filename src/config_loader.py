import toml

__all__ = [
    "ConfigLoader",
]


class ConfigLoader:
    """ Класс для загрузки конфигурационного файла """
    _file_path: str

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path

    def load_config(self) -> dict:
        """ Загрузка конфигурационного файла TOML """
        with open(self._file_path, 'r') as f:
            return toml.load(f)
