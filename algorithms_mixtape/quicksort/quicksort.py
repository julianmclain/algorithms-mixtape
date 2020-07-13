from random import randint


def quicksort(input_list):
    """Sort a list using the Quicksort algorithm.

    Sorting is done in-place and this function doesn't return a value. Note that
    the Quicksort algorithm is a general purpose algorithm that can operate on
    arrays containing duplicate elements. My implmentation only operates on
    arrays of distinct elements because handling ties correctly and efficiently
    is tricky.

    Parameters
    ----------
    input_list : list
        A list of distinct integers
    """
    _quicksort(input_list, 0, len(input_list) - 1)


def _quicksort(input_list, left_index, right_index):
    if left_index >= right_index:
        return
    else:
        i = _choose_pivot(input_list, left_index, right_index)
        pivot_element = input_list[i]
        input_list[i] = input_list[left_index]
        input_list[left_index] = pivot_element

        j = _partition(input_list, left_index, right_index)
        _quicksort(input_list, left_index, j - 1)
        _quicksort(input_list, j + 1, right_index)


def _choose_pivot(input_list, left, right):
    return randint(left, right)


def _partition(input_list, left, right):
    pivot = input_list[left]
    index_after_pivot = left + 1
    for cur, num in enumerate(input_list[left + 1 : right + 1], left + 1):
        if num < pivot:
            input_list[cur] = input_list[index_after_pivot]
            input_list[index_after_pivot] = num
            index_after_pivot += 1
    input_list[left] = input_list[index_after_pivot - 1]
    input_list[index_after_pivot - 1] = pivot
    return index_after_pivot - 1
