def main():
    """
    The test input file contains all of the 100,000 integers between 1 and 100,000 (inclusive)
    in some order, with no integer repeated.

    Your task is to compute the number of inversions in the file given, where the i^{th}
    row of the file indicates the i^{th} entry of an array.
    """
    test_file = 'test_input.txt'
    test1 = [1, 2, 3, 4, 5, 6]
    test2 = [1, 3, 5, 2, 4, 6]
    test3 = [6, 5, 4, 3, 2, 1]
    test4 = [int(line) for line in open(test_file)]

    count1 = count_inversions(test1)
    count2 = count_inversions(test2)
    count3 = count_inversions(test3)
    count4 = count_inversions(test4)
    print(
        f'count1: {count1}, count2: {count2}, count3: {count3}, count4: {count4}')
    assert count1 == 0
    assert count2 == 3
    assert count3 == 15


def count_inversions(num_list):
    """Count the number of inversions in a list of numbers.

    Parameters
    ----------
    num_list : list

    Returns
    -------
    int
        The number of inversions present in the list.
    """
    num_list, count = _count_and_sort(num_list)
    return count


def _count_and_sort(num_list):
    # Base case
    if len(num_list) < 2:
        return num_list, 0

    # Recursive case
    split = len(num_list) // 2

    left, left_count = _count_and_sort(num_list[:split])
    right, right_count = _count_and_sort(num_list[split:])
    sorted_list, split_count = _mergesort_and_count(left, right)

    total_count = left_count + right_count + split_count

    return sorted_list, total_count


def _mergesort_and_count(l, r):
    # Assumes l and r are already sorted
    l_index = 0
    r_index = 0
    sorted_list = []
    split_count = 0

    while l_index < len(l) and r_index < len(r):
        if l[l_index] <= r[r_index]:
            sorted_list.append(l[l_index])
            l_index += 1
        else:
            sorted_list.append(r[r_index])
            r_index += 1
            split_count += len(l) - l_index

    sorted_list.extend(l[l_index:])
    sorted_list.extend(r[r_index:])

    return sorted_list, split_count


if __name__ == '__main__':
    main()
