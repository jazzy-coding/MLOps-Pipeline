from hello import square_root
import pytest

def test_square_root():
    assert square_root(4) == 2

    with pytest.raises(ValueError, match="Cannot compute square root of a negative number"):
        square_root(-1)