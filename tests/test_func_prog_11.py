from funcs.funcs_11 import is_power_n


def test_for_is_power_true():
    result = is_power_n(8, 2)
    assert result == True


def test_for_is_power_false():
    result = is_power_n(7, 2)
    assert result == False
