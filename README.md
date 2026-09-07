# Uptime Checker 🔍

Проста та надійна утиліта на Python для моніторингу доступності веб-сайтів. Програма читає список цілей з YAML-конфігурації, перевіряє їх статус-коди та час відгуку, а потім виводить результати в консоль і зберігає детальний JSON-звіт.

Повністю контейнеризована та готова до запуску через Docker.

## ⚙️ Вимоги
* **Docker** (для запуску утиліти в ізольованому середовищі)
* **Git** (для клонування репозиторію)

## 🚀 Швидкий старт

**1. Клонування репозиторію**
```bash
git clone https://github.com/vanaveduta228-boop/uptime-checker
cd uptime-checker

```

**2. Налаштування конфігурації**
Створіть файл config.yaml у корені проєкту (можна використати готовий приклад):

```bash
cp config.example.yaml config.yaml

```

**3. Збірка Docker-образу**

```bash
docker build -t uptime-checker .

```

**4. Запуск перевірки (збереження звіту на комп'ютері)**
Контейнер запускається з пробросом вашого локального файлу конфігурації всередину та монтуванням папки для збереження звіту назовні:

```powershell
docker run --rm -v ${PWD}\config.yaml:/app/config.yaml -v ${PWD}:/app/out uptime-checker --config /app/config.yaml --output /app/out/report.json
```
(Для Linux/Mac використовуйте $(pwd) замість ${PWD})

## 📝 Приклад файлу config.yaml

```yaml
targets:
  - name: DTEU_Main
    url: https://example.com
    expected_status: 200
    timeout_seconds: 10
    slow_threshold_ms: 3000

```

## 🧪 Локальне тестування

Проект покритий детермінованими тестами (моками) без прив'язки до реальної мережі.
Для запуску тестів (якщо у вас встановлений Python локально):

```bash
pip install -r requirements.txt
pytest

```