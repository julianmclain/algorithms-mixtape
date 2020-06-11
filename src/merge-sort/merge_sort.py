
def main():
    input = [5, 10, 11, 4, 1, 8, 7, 2, 6, 3, 9]
    sorted = merge_sort(input)
    print(sorted)


def merge_sort(num_list):
    """Sort a list of numbers using the MergeSort algorithm.

    Parameters
    ----------
    list : list

    Returns
    -------
    list
        A new list containing the same elements in sorted order.
    """

    # Base case
    if len(num_list) <= 1:
        return num_list[:]  # Return a new list with the same elements

    # Recursive case
    split = len(num_list) // 2
    left = merge_sort(num_list[:split])
    right = merge_sort(num_list[split:])
    return merge(left, right)


def merge(l, r):
    """Merge two sorted lists into a single sorted list.

    Parameters
    ----------
    l : list
    r : list

    Returns
    -------
    list
        A new list containing all of the elments from l and r in sorted order.

    Notes
    -----
    After doing some research, I found a way to improve my original implementation. The
    max number of iterations required in a "worst-case-scneario" can be decreased with the
    following optimization. After reaching end of one of the list, immediately add the
    remaining elements of both lists to the end of the output list. One will be empty,
    the other will contain between 0 and all of its elements.

    Reference: https://www.cs.cmu.edu/~15110-n15/lectures/unit05-3-MergeSort.pdf
    """
    index_l = 0
    index_r = 0
    sorted_list = []
    while index_l < len(l) and index_r < len(r):
        if l[index_l] <= r[index_r]:
            sorted_list.append(l[index_l])
            index_l += 1
        else:
            sorted_list.append(r[index_r])
            index_r += 1

    sorted_list.extend(l[index_l:])
    sorted_list.extend(r[index_r:])
    return sorted_list


if __name__ == '__main__':
    main()
