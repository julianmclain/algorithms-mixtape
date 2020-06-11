# MergeSort

MergeSort was known to John von Neumann as early as 1945. Despite being over 70
years old, it's still one of the choice sorting algorithms today. For large
input sizes, it's runtime is faster than other sorting algorithms like
selection, insertion, and bubble sort. 

## Approach

MergeSort is a canonical "divide-and-conquer" algorithm. It splits the input list
into two halves, recursively sorts each half, and combines the sorted results
with a Merge subroutine.

**Input**: A list of n distinct elements.

**Output**: A new list with the same elements, sorted from smallest to largest.

**Operations** (ignoring base cases):
1. Recursively sort the first half of the input list.
2. Recursively sort the second half of the input list.
3. Merge the two sorted sub-lists into one sorted list.

## Analysis

Using the Master Method:

*T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

*a* = 2

*b* = 2

*d* = 1

Case 1: *T*(*n*) <= *O*(*n* log *n*)