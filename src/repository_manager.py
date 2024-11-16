import os
import subprocess
import shutil


__all__ = [
    "RepositoryManager",
]


class RepositoryManager:
    """ Класс для загрузки и удаления репозитория """
    def __init__(self, repo_url: str, repo_name: str):
        self.repo_url = repo_url
        self.repo_name = repo_name
        self.repo_path = os.path.join(os.getcwd(), repo_name)

    def __enter__(self) -> None:
        self._load_repo_with_dependencies()

    def _load_repo_with_dependencies(self) -> None:
        """ Клонирование репозитория с GitHub """
        print(f"Загружаю репозиторий {self.repo_name} с его зависимостями...")
        if not os.path.exists(self.repo_path):
            subprocess.run(['git', 'clone', self.repo_url, self.repo_path],
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        subprocess.run(['C:/Program Files/nodejs/npm.cmd', 'install'],
                       cwd=self.repo_path, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def __exit__(self, exc_type, *_):
        if exc_type is not None:
            print("Возникла ошибка во время загрузки репозитория или его зависимостей. Завершение программы.")
            exit()

        self._delete_repo_with_dependencies()

    def _delete_repo_with_dependencies(self) -> None:
        """ Удаляет директорию с клонированным репозиторием """
        if os.path.exists(self.repo_path) and os.path.isdir(self.repo_path):
            try:
                shutil.rmtree(self.repo_path, onerror=self._remove_readonly)
            except Exception as e:
                print(f"Ошибка при удалении репозитория: {e}")

    @staticmethod
    def _remove_readonly(func, path, _) -> None:
        """ Снимает атрибут 'только для чтения' и повторно вызывает функцию удаления """
        os.chmod(path, 0o777)
        func(path)
