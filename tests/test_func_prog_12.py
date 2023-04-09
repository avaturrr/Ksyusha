from funcs.funcs_12 import f_sum


def test_for():
    result = f_sum([[1, -2, 3], [-4, -5, 6]])
    assert result == (10, -11)
