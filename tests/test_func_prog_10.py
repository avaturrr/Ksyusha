from funcs.funcs_10 import my_func


def test_greater_0():
    result = my_func(1, -2, -3)
    assert result == (3, -1)


def test_less_0():
    result = my_func(5, 3, 7)
    assert result == None


def test_equal_0():
    result = my_func(1, 12, 36)
    assert result == -6
