from graphviz import Digraph

import json
import os

__all__ = [
    "DependencyVisualizer"
]


class DependencyVisualizer:
    """ Класс для создания графа зависимостей """
    def __init__(self, repo_name: str, repo_path: str, result_path: str):
        self.repo_name = repo_name
        self.repo_path = repo_path
        self.result_path = result_path
        self.graph = Digraph(comment=f'Граф зависимостей для {repo_name}')

    def build_graph(self, package_name: str, current_path: str, dependencies_path: str = None) -> None:
        """ Рекурсивное построение графа зависимостей """
        if not dependencies_path:
            dependencies_path = os.path.join(current_path, 'node_modules')

        package_json_path = os.path.join(current_path, 'package.json')
        if not os.path.exists(package_json_path):
            return

        # Чтение зависимостей из package.json
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)
        dependencies = package_data.get('dependencies', {})

        for dep_name, dep_version in dependencies.items():
            self.graph.edge(package_name, dep_name)
            dep_repo_path = os.path.join(dependencies_path, dep_name)
            self.build_graph(dep_name, dep_repo_path, dependencies_path)

    def save_graph(self) -> None:
        """ Сохранение графа в файл """
        self.graph.save(self.result_path)
        print(f'Граф зависимостей сохранён в {self.result_path}')
