from random import randint


def quick_sort(input_list):
    """Sort a list using the Quicksort algorithm.

    Sorting is done in-place and this function doesn't return a value.

    Parameters
    ----------
    input_list : list
    """
    _quick_sort(input_list, 0, len(input_list) - 1)


def _quick_sort(input_list, left, right):
    if left >= right:
        return
    else:
        i = _choose_pivot(input_list, left, right)
        pivot_element = input_list[i]
        input_list[i] = input_list[left]
        input_list[left] = pivot_element

        j = _partition(input_list, left, right)
        _quick_sort(input_list, left, j - 1)
        _quick_sort(input_list, j + 1, right)


def _choose_pivot(input_list, left, right):
    return randint(left, right)


def _partition(input_list, left, right):
    pivot = input_list[left]
    index_after_pivot = left + 1
    for cur, num in enumerate(input_list[left + 1:right + 1], left + 1):
        if num < pivot:
            input_list[cur] = input_list[index_after_pivot]
            input_list[index_after_pivot] = num
            index_after_pivot += 1
    input_list[left] = input_list[index_after_pivot - 1]
    input_list[index_after_pivot - 1] = pivot
    return index_after_pivot - 1
