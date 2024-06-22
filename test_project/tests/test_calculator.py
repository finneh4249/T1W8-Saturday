import pytest # type: ignore
from src.calculator import add, subtract, multiply, divide


@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 0, 0),
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6),
        (4, 4, 8),
        (5, 5, 10),
        (6, 6, 12),
        (7, 7, 14),
        (8, 8, 16),
        (9, 9, 18),
    ],
)
def test_add(a, b, result):
    assert add(a, b) == result
    
@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 0, 0),
        (1, 1, 0),
        (2, 2, 0),
        (3, 3, 0),
        (4, 4, 0),
        (5, 5, 0),
        (6, 6, 0),
        (7, 7, 0),
        (8, 8, 0),
        (9, 9, 0),
    ],
)
def test_subtract(a, b, result):
    assert subtract(a, b) == result
    
@pytest.mark.parametrize(
    "a, b, result",
    [
        (0, 0, 0),
        (1, 1, 1),
        (2, 2, 4),
        (3, 3, 9),
        (4, 4, 16),
        (5, 5, 25),
        (6, 6, 36),
        (7, 7, 49),
        (8, 8, 64),
        (9, 9, 81),
    ],
)
def test_multiply(a, b, result):
    assert multiply(a, b) == result
    
@pytest.mark.parametrize(
    "a, b, result",
    [
        (1, 1, 1),
        (2, 2, 1),
        (3, 3, 1),
        (4, 4, 1),
        (5, 5, 1),
        (6, 6, 1),
        (7, 7, 1),
        (8, 8, 1),
        (9, 9, 1),
    ],
)   
def test_divide(a, b, result):
    assert divide(a, b) == result

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
        