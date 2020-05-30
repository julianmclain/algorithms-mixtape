
def main():
    test = [5, 10, 11, 4, 1, 8, 7, 2, 6, 3, 9]
    sorted = merge_sort(test)
    print(sorted)


def merge_sort(list):
    """
    Input: A list of n elements.
    Output: Returns a new list containing the same elements in sorted order.
    """

    # Base case
    if len(list) <= 1:
        return list[:]  # Return a new list with the same elements

    split = len(list) // 2
    left = merge_sort(list[:split])  # Recursively sort left
    right = merge_sort(list[split:])  # Recursively sort right
    return merge_v2(left, right)


def merge(l, r):
    index_l = 0
    index_r = 0
    output = []
    for k in range(len(l) + len(r)):
        if index_r >= len(r) or (index_l < len(l) and l[index_l] < r[index_r]):
            output.append(l[index_l])
            index_l += 1
        else:
            output.append(r[index_r])
            index_r += 1
    return output


def merge_v2(l, r):
    """
    You can decrease the max number of iterations needed with an optimization.
    If you get to the end of one of the lists, add the remaining elements of both lists
    to the end of the output list. One will be empty, the other will contain 0 to it's
    length number of elements.

    Reference: https://www.cs.cmu.edu/~15110-n15/lectures/unit05-3-MergeSort.pdf
    """
    index_l = 0
    index_r = 0
    output = []
    while index_l < len(l) and index_r < len(r):
        if l[index_l] <= r[index_r]:
            output.append(l[index_l])
            index_l += 1
        else:
            output.append(r[index_r])
            index_r += 1
    # When we exit the loop, we know at least 1 list is empty.
    # Since we don't know which one is empty, just append the remaining
    # elements in both l and r to the output list.
    output.extend(l[index_l:])
    output.extend(r[index_r:])
    return output


if __name__ == '__main__':
    main()
