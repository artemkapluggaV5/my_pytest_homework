import pytest
from utils import arrs


@pytest.fixture
def array_data():
    return [1, 2, 3]


def test_get(array_data):
    assert arrs.get(array_data, 1, "test") == 2
    assert arrs.get(array_data, -1, "test") == "test"
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_data):
    assert arrs.my_slice(array_data, 1, 3) == [2, 3]
    assert arrs.my_slice(array_data, 1) == [2, 3]
    assert arrs.my_slice(array_data, end=2) == [1, 2]

    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]