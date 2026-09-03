```markdown
# Uptime Checker 🔍

Простая и надежная утилита на Python для мониторинга доступности веб-сайтов. Программа читает список целей из YAML-конфигурации, проверяет их статус-коды и время отклика, а затем выводит результаты в консоль и сохраняет подробный JSON-отчет.

Полностью контейнеризована и готова к запуску через Docker.

## ⚙️ Требования
* **Docker** (для запуска утилиты в изолированной среде)
* **Git** (для клонирования репозитория)

## 🚀 Быстрый старт

**1. Клонирование репозитория**
```bash
git clone <ССЫЛКА_НА_ТВОЙ_РЕПОЗИТОРИЙ>
cd uptime-checker

```

**2. Настройка конфигурации**
Создайте файл `config.yaml` в корне проекта (можно использовать готовый пример):

```bash
cp config.example.yaml config.yaml

```

**3. Сборка Docker-образа**

```bash
docker build -t uptime-checker .

```

**4. Запуск проверки (в Windows PowerShell)**
Контейнер запускается с пробросом вашего локального файла конфигурации внутрь:

```powershell
docker run --rm -v ${PWD}\config.yaml:/app/config.yaml uptime-checker

```

*(Для Linux/Mac используйте `$(pwd)` вместо `${PWD}`)*

## 📝 Пример файла config.yaml

```yaml
targets:
  - name: DTEU_Main
    url: [https://knute.edu.ua](https://knute.edu.ua)
    expected_status: 200
    timeout_seconds: 10
    slow_threshold_ms: 3000

```

## 🧪 Локальное тестирование

Проект покрыт детерминированными тестами (моками) без привязки к реальной сети.
Для запуска тестов (если у вас установлен Python локально):

```bash
pip install -r requirements.txt
pytest

```

```

***
```