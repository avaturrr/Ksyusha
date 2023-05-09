from funcs.funcs_05 import funcs_sum_args


def test_funcs_sum_args():
    result = funcs_sum_args(1, 2, 3, -1, -2)
    assert result == -3
