from funcs.funcs_08 import my_function


def test_for_mean_type_0():
    result = my_function(1, 2, 3, 4, 5, mean_type=0)
    assert result == 3


def test_for_mean_type_1():
    result = round(my_function(4, 4, 4, mean_type=1))
    assert result == 4
