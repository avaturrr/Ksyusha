from funcs.funcs_14 import my_func

def test_for_odd():
    result = my_func(5)
    assert result == 15

def test_for_even():
    result = my_func(6)
    assert result == 48