def count_inversions(arr):
    """Count the number of inversions in a list of numbers.

    Parameters
    ----------
    num_list : list

    Returns
    -------
    int
        The number of inversions present in the list.
    """
    arr, count = _count_and_sort(arr)
    return count


def _count_and_sort(arr) -> tuple:
    # Base case
    if len(arr) < 2:
        return arr, 0

    # Recursive case
    split = len(arr) // 2

    left, left_count = _count_and_sort(arr[:split])
    right, right_count = _count_and_sort(arr[split:])
    sorted_list, split_count = _merge_and_count(left, right)

    total_count = left_count + right_count + split_count

    return sorted_list, total_count


def _merge_and_count(arr1, arr2):
    # Assumes l and r are already sorted
    i = 0
    j = 0
    sorted_list = []
    split_count = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_list.append(arr1[i])
            i += 1
        else:
            sorted_list.append(arr2[j])
            j += 1
            split_count += len(arr1) - i

    sorted_list.extend(arr1[i:])
    sorted_list.extend(arr2[j:])

    return sorted_list, split_count
