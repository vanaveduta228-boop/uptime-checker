import requests
import time

def check_site(target):
    url = target['url']
    timeout = target['timeout_seconds']
    start_time = time.perf_counter()
    
    try:
        response = requests.get(url, timeout=timeout, allow_redirects=True)
        end_time = time.perf_counter()
        duration_ms = int((end_time - start_time) * 1000)
        return {"status_code": response.status_code, "duration_ms": duration_ms, "error": None}
    
    except requests.exceptions.Timeout:
        return {"status_code": None, "duration_ms": None, "error": "Таймаут"}

    except requests.exceptions.SSLError:
        return {"status_code": None, "duration_ms": None, "error": "Помилка TLS-сертифіката"}

    except requests.exceptions.ConnectionError:
        return {"status_code": None, "duration_ms": None, "error":"Помилка з'єднання або DNS"}

    except requests.exceptions.RequestException as e:
        return {"status_code": None, "duration_ms": None, "error":"Невідома мережева помилка"}