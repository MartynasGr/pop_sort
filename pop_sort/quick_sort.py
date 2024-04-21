def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot, left, right = partition(arr)
    return quick_sort(left) + [pivot] + quick_sort(right)


def partition(arr):
    pivot = arr[len(arr) - 1]
    pivot_index = 0
    for i in range(len(arr) - 1):
        if pivot >= arr[i]:
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
            pivot_index += 1
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]
    return pivot, arr[:pivot_index], arr[pivot_index + 1:]
