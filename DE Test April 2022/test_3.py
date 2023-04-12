from task_3 import sum_current_time_1, sum_current_time_2


def test_1():
    """Tests each sum time function returns 
    the expected value for given input."""
    time_str = "00:00:00"
    assert sum_current_time_1(time_str) == 0
    assert sum_current_time_2(time_str) == 0

def test_2():
    """Tests each sum time function returns 
    the expected value for given input."""
    time_str = "01:02:03"
    assert sum_current_time_1(time_str) == 6
    assert sum_current_time_2(time_str) == 6

def test_3():
    """Tests each sum time function returns 
    the expected value for given input."""
    time_str = "23:59:59"
    assert sum_current_time_1(time_str) == 141
    assert sum_current_time_2(time_str) == 33

def test_4():
    """Tests each sum time function returns 
    the expected value for given input."""
    time_str = "13:44:20"
    assert sum_current_time_1(time_str) == 77
    assert sum_current_time_2(time_str) == 14

def test_5():
    """Tests each sum time function returns 
    the expected value for given input."""
    time_str = "11:16:45"
    assert sum_current_time_1(time_str) == 72
    assert sum_current_time_2(time_str) == 18