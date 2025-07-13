from hello import square_root

def test_square_root():
    assert square_root(4) == 2
    assert square_root(-1) == ValueError