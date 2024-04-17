from pop_sort.selection_sort  import selection_sort


def test_selection_sort():
    original_array = [5, 8, 4, 15, 111, 1]
    sorted_array = [1, 4, 5, 8, 15, 111]
    assert selection_sort(original_array) == sorted_array
