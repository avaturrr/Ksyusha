from funcs.funcs_15 import my_func

def test_for_my_func_true():
    result = my_func("asdsa")
    assert result == True

def test_for_my_func_false():
    result = my_func("asd")
    assert result == False