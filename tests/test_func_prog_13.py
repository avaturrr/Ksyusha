from funcs.funcs_13 import my_funcs


def test_for_my_func_1():
    result = my_funcs(1, "1")
    assert result == 2.54


def test_for_my_func_2():
    result = my_funcs(1, "2")
    assert result == 0.393701


def test_for_my_func_3():
    result = my_funcs(1, "3")
    assert result == 1.852


def test_for_my_func_4():
    result = my_funcs(1, "4")
    assert result == 0.539957
