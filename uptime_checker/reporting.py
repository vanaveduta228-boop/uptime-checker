def evaluate_result(target, result):
    if result['error'] is not None or result['status_code'] != target['expected_status']:
        return "FAIL"
    elif result['duration_ms'] > target['slow_threshold_ms']:
        return "WARN"
    else:
        return "OK"