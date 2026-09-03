import yaml
import sys

def load_config(file_path):
    try:
        with open(file_path, "r", encoding="UTF-8") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Помилка: Файл конфігурації '{file_path}' не знайдено.")
        sys.exit(2)
    except yaml.YAMLError as exc:
        print(f"Помилка парсингу YAML: {exc}")
        sys.exit(2)

    if not config or 'targets' not in config:
        print("Помилка: Конфігурація порожня або відсутній список 'targets'.")
        sys.exit(2)

    targets = config['targets']
    if not targets or not isinstance(targets, list):
        print("Помилка: Список 'targets' порожній або має невірний формат.")
        sys.exit(2)

    required_keys = {'name', 'url', 'expected_status', 'timeout_seconds', 'slow_threshold_ms'}
    for target in targets:
        if not required_keys.issubset(target.keys()):
            print(f"Помилка: У цілі {target.get('name', 'Unknown')} відсутні обов'язкові поля.")
            sys.exit(2)

        url = target['url']
        if not (url.startswith('http://') or url.startswith('https://')):
            print(f"Помилка: URL '{url}' має починатися з http:// або https://")
            sys.exit(2)

        if target['timeout_seconds'] <=0 or target['slow_threshold_ms'] <=0:
            print(f"Помилка: Таймаут або поріг для '{url}' має бути більшим за 0.")
            sys.exit(2)
    return targets