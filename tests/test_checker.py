import pytest
import requests
from unittest.mock import patch, Mock
from uptime_checker.checker import check_site

@patch('uptime_checker.checker.requests.get')
def test_check_site_success(mock_get):
    mock_get.return_value = Mock(status_code=200)
    target = {
        "url": "https://example.comhttps", 
        "timeout_seconds": 10
    }
    result = check_site(target)
    assert result['status_code'] == 200

@patch('uptime_checker.checker.requests.get')
def test_check_site_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    target = {
            "url": "https://example.com", 
            "timeout_seconds": 10
        }
    result = check_site(target)
    assert result['error'] == "Таймаут"
    assert result['status_code'] is None

@patch('uptime_checker.checker.requests.get')
def test_check_site_connection(mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    target = {
            "url": "https://example.com", 
            "timeout_seconds": 10
        }
    result = check_site(target)
    assert result['error'] == "Помилка з'єднання або DNS"
    assert result['status_code'] is None
