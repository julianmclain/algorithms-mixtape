def remove_element(nums, val) -> int:
    """Remove all occurences of a value from an array.

    The idea is to use 2 pointers to traverse the array. One pointer `j` scans
    the entire list while the second pointer `i` keeps track of the next index
    where a non-"val" should be copied.

    Parameters
    ----------
    nums : list val : int

    Returns
    -------
    int The resulting length of the array.
    """
    i = 0
    for j, num in enumerate(nums):
        if num != val:
            nums[i] = num
            i += 1
    return i


def duplicate_element(arr, val):
    """Duplicate all occurences of a value in an array.

    The duplicates are inserted 1 position to the right of the value. All
    elements after the value are shifted to the right 1 position. The length of
    the array is not increased, so inserting the duplicate elements will slice
    off any elements that are shifted beyond the end of the array.

    The idea is to iterate from the end of the array to the front. That way you
    only modify elements that have already been seen. If the current number is
    equal to "val", skip 1 index for the duplicate and start copying all
    elements until the end of the array. Then insert the duplicate in the
    position 1 index to the right of "val."

    TODO: This doesn't run in O(n) time. A better approach would be to make 2
    linear scans. The first to identify duplicates, and the second to overwrite
    the entire array.

    Parameters
    ----------
    arr : list
    val : int
    """
    arr_length = len(arr)
    for i in reversed(range(arr_length)):
        if arr[i] == val and i != arr_length - 1:
            prev = arr[i + 1]
            for j in range(i + 2, arr_length):
                if j >= arr_length:
                    break
                tmp = arr[j]
                arr[j] = prev
                prev = tmp
            arr[i + 1] = val


def remove_duplicates(nums) -> int:
    """Remove all duplicate values from an array.

    The idea is very similar to `remove_element` above. The only difference is the
    condition that must be satisfied before an element is copied.

    This could be done in a slick 1-liner using a for-comprehension but the goal is
    to do the modification in place.

    Returns
    -------
    int The resulting length of the array.
    """
    i = 0
    for j, num in enumerate(nums):
        if num not in nums[:i]:
            nums[i] = num
            i += 1
    return i
