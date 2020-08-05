from random import randint


def quicksort(num_list):
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
    _quicksort(num_list, 0, len(num_list) - 1)


def _quicksort(num_list, left_index, right_index):
    if left_index >= right_index:
        return
    else:
        i = choose_pivot(left_index, right_index)
        pivot_element = num_list[i]
        num_list[i] = num_list[left_index]
        num_list[left_index] = pivot_element

        j = partition(num_list, left_index, right_index)
        _quicksort(num_list, left_index, j - 1)
        _quicksort(num_list, j + 1, right_index)


def choose_pivot(left, right):
    return randint(left, right)


def partition(num_list, left, right):
    pivot = num_list[left]
    index_after_pivot = left + 1
    for cur, num in enumerate(num_list[left + 1 : right + 1], left + 1):
        if num < pivot:
            num_list[cur] = num_list[index_after_pivot]
            num_list[index_after_pivot] = num
            index_after_pivot += 1
    num_list[left] = num_list[index_after_pivot - 1]
    num_list[index_after_pivot - 1] = pivot
    return index_after_pivot - 1
