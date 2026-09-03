import sys
import argparse
import json
from datetime import datetime, timezone
from .config import load_config
from .checker import check_site
from .reporting import evaluate_result

parser = argparse.ArgumentParser(description="Утиліта перевірки доступності сайтів")
parser.add_argument("--config", required=True, help="Шлях до файлу конфігурації")
parser.add_argument("--output", help="Шлях до файлу JSON-звіту")
args = parser.parse_args()

targets = load_config(args.config)
ok_count = warn_count = fail_count = 0
results_list = []

for target in targets:
    result = check_site(target)
    status = evaluate_result(target, result)
    if status == "OK":
        ok_count += 1
    elif status == "WARN":
        warn_count += 1
    elif status == "FAIL":
        fail_count += 1
    if result['error'] is None:
        print(f"[{status}] {target['name']} | HTTP {result['status_code']} | {result['duration_ms']} ms")
    else:
        print(f"[{status}] {target['name']} | {result['error']}")
    item = {
    "name": target['name'],
    "url": target['url'],
    "expected_status": target['expected_status'],
    "actual_status": result['status_code'],
    "duration_ms": result['duration_ms'],
    "result": status,
    "error": result['error']
    }
    results_list.append(item)

print()
print(f"Разом: {len(targets)} | OK: {ok_count} | WARN: {warn_count} | FAIL: {fail_count}")
if args.output:
    now_utc = datetime.now(timezone.utc).isoformat()
    report_data = {
        "timestamp_utc": now_utc,
        "results": results_list,
        "summary": {
            "total": len(targets),
            "ok": ok_count,
            "warn": warn_count,
            "fail": fail_count
        }
    }   
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)
        
if fail_count > 0:
    sys.exit(1)
else:
    sys.exit(0)

