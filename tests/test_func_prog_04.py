from funcs.funcs_04 import new_matrix


def test_new_matrix():
    result = new_matrix(3)
    assert len(result) == 3 and len(result[0]) == 3
