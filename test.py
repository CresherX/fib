import pytest
from f import is_fib
massive = [ 3, 5, 8, 13, 21, 34, 55, 89, 6765, 10946, 17711, 46368]
@pytest.mark.parametrize('massive', massive)
def test_check(massive):
    assert is_fib(massive) is True

