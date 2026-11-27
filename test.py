import pytest
from f import is_fib
massive = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]
@pytest.mark.parametrize('massive', massive)
def test_check(massive):
    assert is_fib(massive) is True

