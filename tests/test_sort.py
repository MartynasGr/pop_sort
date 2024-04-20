import pytest
from pop_sort.selection_sort import selection_sort
from pop_sort.bubble_sort import bubble_sort

sorted_array_1 = [1, 1, 4, 5, 5, 8, 10, 15, 22, 111]
sorted_array_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def array_fixture():
    original_array_1 = [5, 8, 4, 15, 111, 1, 22, 1, 5, 10]
    original_array_2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    return original_array_1.copy(), original_array_2.copy()


def test_selection_sort(array_fixture):
    array_1, array_2 = array_fixture
    assert selection_sort(array_1) == sorted_array_1
    assert selection_sort(array_2) == sorted_array_2


def test_bubble_sort(array_fixture):
    array_1, array_2 = array_fixture
    assert bubble_sort(array_1) == sorted_array_1
    assert bubble_sort(array_2) == sorted_array_2
