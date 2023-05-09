from funcs.funcs_09 import my_func


def test_my_func():
    result = my_func(1, 2, 3, 4, 5, 3, 5, 4, 4, 4)
    assert result == {1: 1, 2: 1, 3: 2, 4: 4, 5: 2}
