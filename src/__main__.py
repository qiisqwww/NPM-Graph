from src.config_loader import ConfigLoader
from src.repository_manager import RepositoryManager
from src.dependency_visualizer import DependencyVisualizer


def main() -> None:
    config = ConfigLoader('config.toml').load_config()

    repo_url = config['repository']['repo_url']
    repo_name = config['repository']['name']
    result_file = config['output']['result_file']

    # Управление репозиторием (установит зависимости и удалит их после выхода из блока with)
    repo_manager = RepositoryManager(repo_url, repo_name)
    with repo_manager:
        # Визуализация зависимостей
        visualizer = DependencyVisualizer(repo_name, repo_manager.repo_path, result_file)
        visualizer.build_graph(repo_name, repo_manager.repo_path)
        visualizer.save_graph()


if __name__ == "__main__":
    main()
