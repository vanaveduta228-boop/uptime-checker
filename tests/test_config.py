import pytest
import yaml
import subprocess
import sys
from uptime_checker.config import load_config

def test_invalid_url_type(tmp_path):
    test_file= tmp_path / "bad_config.yaml"
    bad_data = {
        "targets" : [
            {
                "name": "Test",
                "url": 123,  
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            }
        ]
    }

    with open(test_file, "w", encoding= "utf-8") as f:
        yaml.dump(bad_data, f)

    with pytest.raises(SystemExit) as excinfo:
        load_config(test_file)

    assert excinfo.value.code == 2

def test_json_write_error(tmp_path):
    fake_file = tmp_path / "im_a_file.txt"
    fake_file.write_text("Я файл, а не папка!")
    config_file = tmp_path / "config.yaml"
    bad_data2 = {
        "targets" : [
            {
                "name": "Test",
                "url": "http://127.0.0.1",  
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            }
        ]
    }

    with open(config_file, "w", encoding= "utf-8") as f:
        yaml.dump(bad_data2, f)

    impossible_path = fake_file / "report.json"
    result = subprocess.run(
        ["python", "-m", "uptime_checker", "--config", str(config_file), "--output", str(impossible_path)])

    assert result.returncode == 1

def smoke_successful_run_and_continue(tmp_path):
    config_file = tmp_path / "config.yaml"
    output_file = tmp_path / "report.json"
    test_data = {
        "targets": [
            {
                "name": "Good Site",
                "url": "https://example.com",
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            },
            {
                "name": "Bad Site",
                "url": "https://this-site-does-not-exist.com",
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            }
        ]
    }

    with open(config_file, "w", encoding="utf-8") as f:
        yaml.dump(test_data, f)

    result = subprocess.run(
        [sys.executable, "-m", "uptime_checker", "--config", str(config_file), "--output", str(output_file)],
        capture_output=True, text=True
    )
    # Выводим скрытую ошибку на экран, чтобы мы могли ее прочитать
    print("\n--- ОШИБКА ВНУТРИ СКРИПТА ---")
    print(result.stderr)
    print("-----------------------------\n")
    
    assert output_file.exists(), "Файл отчета не был создан!"
    assert result.returncode == 1

def smoke_perfect_run(tmp_path):
    config_file = tmp_path / "config.yaml"
    output_file = tmp_path / "report.json"
    test_data = {
        "targets": [
            {
                "name": "Good Site",
                "url": "https://example.com",
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            }
        ]
    }

    with open(config_file, "w", encoding="utf-8") as f:
        yaml.dump(test_data, f)

    result = subprocess.run(
        [sys.executable, "-m", "uptime_checker", "--config", str(config_file), "--output", str(output_file)],
        capture_output=True, text=True
    )

    assert output_file.exists()
    assert result.returncode == 0


def test_multiple_targets_validation(tmp_path):
    config_file = tmp_path / "config.yaml"
    test_data = {
        "targets": [
            {
                "name": "Good Site",
                "url": "https://example.com",
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            },
            {
                "name": "Bad Site",
                "url": 123,
                "expected_status": 200,
                "timeout_seconds": 10,
                "slow_threshold_ms": 1000
            }
        ]  
    }

    with open (config_file, "w", encoding="utf-8") as f:
        yaml.dump(test_data, f)

    with pytest.raises(SystemExit) as excinfo:
        load_config(config_file)

    assert excinfo.value.code == 2