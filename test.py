import pytest

@pytest.fixture
def sample_data():
    # Setup code creating some sample data
    data = {"name": "John Doe", "age": 30}
    return data

def test_sample_data(sample_data):
    assert sample_data["name"] == "John Doe"
    assert sample_data["age"] == 30

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5)
])
def test_increment(input, expected):
    assert input + 1 == expected

def is_even(n):
    return n % 2 == 0

@pytest.mark.parametrize("num,expected", [
    (1, False),
    (2, True),
    (3, False),
    (4, True),
    (0, True),
    (-2, True),
    (-1, False)
])
def test_is_even(num, expected):
    assert is_even(num) == expected

@pytest.mark.parametrize("a,b,c,expected", [
    (1, 2, 3, 6),
    (2, 4, 8, 14),
    (4, 5, 9, 18)
])
def test_addition(a, b, c, expected):
    assert a + b + c == expected

@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5)
], ids=["increment_1", "increment_2", "increment_3", "increment_4"])
def test_increment(input, expected):
    assert input + 1 == expected