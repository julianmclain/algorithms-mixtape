# MergeSort

MergeSort was known to John von Neumann as early as 1945. Despite being over 70
years old, it's still one of the choice sorting algorithms today. For large
input sizes, it's runtime is faster than other sorting algorithms such as
selection, insertion, and bubble sort.

## Implementation 

### Input

A list of *n* distinct elements.

### Output

A new list with the same elements, sorted from smallest to largest.

### Description:
1. Base case: if the list has length 1 or less, it's already sorted. Return a
   new copy of the list.
1. Recursively sort the first half of the input list.
2. Recursively sort the second half of the input list.
3. Merge the two sorted sub-lists into one sorted list.

## Analysis

MergeSort is a canonical "divide-and-conquer" algorithm. It splits the input
list into two halves, recursively sorts each half, and combines the sorted
results with a Merge subroutine.

### Asymptotic runtime

We can derive the big-O runtime using the Master Method which states:

*T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

Where *a* is the number of recrusive calls, *b* is the factor by which the input
size shrinks in every subproblem, and *d* is the exponent in the running time of
the "combine" step.

For MergeSort, we fill in the following constants:
- *a* = 2
- *b* = 2
- *d* = 1

This puts the runtime in category 1 of 3 where *a* = *b<sup>d</sup>*.

Category 3 runtimes are equal to *T*(*n*) = *O*(*n*<sup>*d*</sup> log *n*).

Filling in the *d* parameter, we end up with a runtime of *O*(*n* log *n*).