# Quicksort

Tony Hoare developed the Quicksort algorithm in 1959 when he was 25! It was
published 2 years later in 1961. Eventually he went on to win an ACM Turing
award.

## Implementation

### Input

An array of `n` distinct elements.

Note that the Quicksort algorithm is a general purpose algorithm that can
operate on arrays containing duplicate elements. My implmentation only operates
on arrays of distinct elements because handling ties correctly and efficiently
is tricky. 

### Postcondition

The original input array containing the same elements, sorted from smallest to
largest.

### Description

Main function `quicksort(array A, length n)`
- If n = 1, return
- Choose a pivot element
- Partition `A` around the pivot element
- Recursively sort elements to the left of the pivot element
- Recursively sort elements to the right of the pivot element

Subroutine `choose_pivot(...)`

Subroutine `partition(...)`
- Note the following invariant. As you traverse the array, at any given time
  there will be seen an unseen elements. Within the seen elements, everything
  less than the pivot element must come before all elements greater than the
  pivot.
- Define `p` as the pivot element `A[l]`
- Define `i` as the index of the position just to the right of the pivot `A[l +
  1]`
- Define `j` as the index of elements seen so far, `A[l + 1]`
- Loop through the indicies `j` to `r`, `r` being the right most index
  - (If `A[j]` > p, then the new element is bigger than the pivot. You don't
    have to do anything)
  - If `A[j]` < p, then swap this element with the left-most element that's
    greater than the pivot. The aforementioned element is located at `A[i]`.
    Finally, increment `i` since the location of the pivot boundary has just
    moved to the right one position.
- When you break out of the loop, swap the pivot element `A[l]` and the element
  1 space to the left of the pivot boundary `A[i - 1]`

## Analysis

The run time of Quicksort hinges completely on the quality of the pivot chosen.

If the chosen pivot happens to be the smallest number of the array, then 1 recursive
call will receive an empty subarray and the other recursive call will receive a
subarray containing all remaining elements minus the pivot. Hypothetically, if
this occurs with every partition, then the `partition` subroutine will be called
on subarrays of length `n`, `n - 1`, `n - 1`, ... `1` resulting in
*O(n<sup>2</sup>)* runtime. This exact scenario will occur if Quicksort is passed
an already sorted array, and the `choose_pivot` subroutine is implemented to
always select the first element as the pivot.

On the other hand, if the chosen pivot happens to be the median element, then
the array will be evenly split into 2 arrays of `n/2` length. This is the best
case scenario, and applying the Master Method you can see that it results in
*O(n log n)* runtime.

As it turns out, we can approximate finding the median element by simply
selecting the pivot at random.

### The `partition` subroutine

The `partition` subroutine running time is *O(n)* since it does a scan of the
entire input array and performs a constant number of operations per element.
What's more interesting is that it has *O(1)* memory usage.

It's easy to partition an array in linear time if you are allowed to use *O(n)*
memory (essentially another array of *n* size). With an extra array, you can
scan the original array with 2 pointers, using the first pointer to fill
elements less than the pivot from the beginning of the array and the 2nd pointer
to fill elements greater than the pivot from the end of the array. This
implementation performs the partition in place, so it's memory usage is a
constant factor.

## Notes

The key idea in Quicksort is partitioning the array around a pivot element. In
the first step of the process, the element at index `i` is selected from the array
`A`. Then the array is modified in place such that all elements less than `A[i]`
are positioned before it and all elements greater than `A[i]` are positioned
after it. While the outcome doesn't gaurantee that the elements to the "left"
and "right" are sorted relative to each other, it does gaurantee that the pivot
element is in it's "correct" sorted position. For example:
```
Array A = [3, 8, 2, 5, 1, 4, 7, 6]
```
Now let's select the first element as the pivot and partition the array.
```
[2, 1, 3, 6, 7, 4, 5, 8]
```
As a result: 
- Elements left of pivot < the pivot element
- Elements right of pivot > the pivot element
- The pivot element is in it's ultimate sorted position

Most importantly, partitioning the array enables a "divide and conquer"
approach. Now the problem can be broken down into 2 sub-problems, sorting the
left and the right elements.
