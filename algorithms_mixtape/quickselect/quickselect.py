import random


def quickselect(items_list, k):
    """Select the kth smallest element of a list.

    Parameters
    ----------
    items_list : list
    k : int

    Returns
    -------
    int
        The kth smallest element of the list.
    """
    return select(items_list, 0, len(items_list) - 1, k - 1)


def select(lst, l, r, index):
    if l == r:
        return lst[l]

    pivot_index = _choose_pivot(l, r)
    pivot_element = lst[pivot_index]
    lst[pivot_index] = lst[l]
    lst[l] = pivot_element

    j = _partition(lst, l, r)

    if j == index:
        return lst[j]
    elif j > index:
        return select(lst, l, j - 1, index)
    else:
        return select(lst, j + 1, r, index)


def _choose_pivot(l, r):
    return random.randint(l, r)


def _partition(items_list, l, r):
    # Assume first element is the pivot
    pivot = items_list[l]
    index_after_pivot = l + 1
    for cur, num in enumerate(items_list[index_after_pivot : r + 1], index_after_pivot):
        if num < pivot:
            items_list[cur] = items_list[index_after_pivot]
            items_list[index_after_pivot] = num
            index_after_pivot += 1
    items_list[l] = items_list[index_after_pivot - 1]
    items_list[index_after_pivot - 1] = pivot
    return index_after_pivot - 1
