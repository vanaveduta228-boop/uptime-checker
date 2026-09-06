# Uptime Checker 🔍

Простая и надежная утилита на Python для мониторинга доступности веб-сайтов. Программа читает список целей из YAML-конфигурации, проверяет их статус-коды и время отклика, а затем выводит результаты в консоль и сохраняет подробный JSON-отчет.

Полностью контейнеризована и готова к запуску через Docker.

## ⚙️ Требования
* **Docker** (для запуска утилиты в изолированной среде)
* **Git** (для клонирования репозитория)

## 🚀 Быстрый старт

**1. Клонирование репозитория**
```bash
git clone https://github.com/vanaveduta228-boop/uptime-checker
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

**4. Запуск проверки (збереження звіту на комп'ютері)**
Контейнер запускається з пробросом вашого локального файлу конфігурації всередину та монтуванням папки для збереження звіту назовні:

```powershell
docker run --rm -v ${PWD}\config.yaml:/app/config.yaml -v${PWD}:/app/out uptime-checker --config /app/config.yaml --output /app/out/report.json
(Для Linux/Mac використовуйте $(pwd) замість ${PWD})

## 📝 Пример файла config.yaml

```yaml
targets:
  - name: DTEU_Main
    url: https://example.com
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