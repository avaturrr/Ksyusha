from funcs.funcs_06 import funcs_sum_max


def tests_funcs_sum_max():
    my_sum, my_max = funcs_sum_max(1, 3, 4, 5)
    assert my_sum == 13 and my_max == 5
