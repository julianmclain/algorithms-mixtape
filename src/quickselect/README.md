# Quickselect

Quickselect, also know as [Hoare's Selection
Algorithm](https://en.wikipedia.org/wiki/Quickselect), is a solution to the
[selection problem](https://en.wikipedia.org/wiki/Selection_algorithm) where the
goal is to select the *kth* smallest element from an unsorted array. A naive approach
to solving this problem is to first sort the array in *O*(*n* log *n*) time and
then access the *kth* element. This isn't an effective approach (hint: we can do
better than *O*(*n* log *n*) runtime), but it's important to note because it
demonstrates that the problem of selection can be *reduced* to sorting.
Reduction enables you to solve new problems using known solutions to similar
problems. It's an important concept in computer science.

Quickselect starts with the same approach as Quicksort. It chooses a pivot
element and partitions the data around the pivot. However, instead of recursing
on the elements smaller and larger than the pivot, Quickselect only needs to recurse on the half of the data
containing the *kth* element. By ignoring the unnecessary elements, it achieves
better performance than Quicksort.

Quickselect is usually implemented with in-place operations, so it has the
side-effect of partially sorting the input data.

## Implementation

### Input

An array of *n* >= 1 elements in arbitrary order and an integer *k* between 1 and *n* (inclusive).

### Output

The *kth* smallest element of the array.

### Description

`quickselect(array A, integer k)` subroutine:
- If the array contains 1 element, return the element.
- Choose a pivot uniformly at random from array `A`
- Partition the array around the pivot.
- If the index of the pivot equals `k`, return the pivot element.
- If the index of the pivot is less than `k`, recurse on all elements with an index less than `k`
- If the index of the pivot is greater than `k`, recurse on all elements with an index greater than `k` 

## Analysis

### Asymptotic runtime