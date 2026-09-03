from uptime_checker.reporting import evaluate_result

def test_evaluate_result_ok():
    target = {"expected_status": 200, "slow_threshold_ms": 1000}
    result = {"status_code": 200, "duration_ms": 200, "error": None}
    status = evaluate_result(target, result)
    assert status == "OK"

def test_evaluate_result_warn():
    target = {"expected_status": 200, "slow_threshold_ms": 1000}
    result = {"status_code": 200, "duration_ms": 1500, "error": None}
    status = evaluate_result(target, result)
    assert status == "WARN"

def test_evaluate_result_fail():
    target = {"expected_status": 200, "slow_threshold_ms": 1000}
    result = {"status_code": 404, "duration_ms": 200, "error": None}
    status = evaluate_result(target, result)
    assert status == "FAIL"