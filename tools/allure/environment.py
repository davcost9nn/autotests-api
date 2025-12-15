import sys
import platform

from config import settings


def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    os_info = f"{platform.system()}, {platform.release()}"
    items.append(f"os_info={os_info}")


    python_version = sys.version.replace('\n', ' ')
    items.append(f"python_version={python_version}")
    properties = '\n'.join(items)


    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)