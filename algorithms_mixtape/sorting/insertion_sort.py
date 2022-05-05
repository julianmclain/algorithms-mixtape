def insertion_sort(arr):
    """Sort a list using the insertion sort algorithm.

    The main idea of insertion sort is to iterate forward through the list and
    keep the list in sorted order behind the current position.

    Sorting process:

    Assume that a list of length < 1 is trivially sorted. Starting at element 1,
    iterate forward through the list and compare the current element against the
    largest element seen so far (which will be stored at the previous index). If
    the current element is smaller, swap positions. Repeate this process until
    the current element is bigger than the previous element or the front of the
    list is reached.
    """
    if arr is None or len(arr) <= 1:
        return

    for i, num in enumerate(arr[1:], 1):
        while i > 0 and num < arr[i - 1]:
            arr[i] = arr[i - 1]
            arr[i - 1] = num
            i -= 1
