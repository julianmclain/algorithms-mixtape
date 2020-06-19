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

The elements in the input array are sorted from smallest to largest.

### Description

Main function `quicksort(A, left_index, right_index)`
- Return if the `left_index` is less than the `right_index`
- Randomly choose a pivot index between `left_index` and `right_index`
- Make the pivot element the left-most element (i.e. swap `A[left_index]` with
  `A[pivot_index]`)
- Partition `A` around the pivot element
- Recursively sort elements to the left of the pivot element
- Recursively sort elements to the right of the pivot element

Subroutine `choose_pivot(A, left_index, right_index)`
- Return a random index between `left_index` and `right_index`

Subroutine `partition(A, left_index, right_index)`
- Take the left-most element as the pivot element (i.e `A[left_index]`)
- Store a pointer to the index after the pivot element (i.e. `A[left_index +
  1]`). It will be used to keep track of the bounary between processed elements
  that are less than and and greater than the pivot. For example, the element at
  `A[pointer]` should be leftmost element greater than the pivot.
- Range over all indicies `j` between `left_index + 1` and `right_index`. Note
  that the index `j` will track progress as elements are processed.
- For each element `A[j]`:
    - If it's greater than the pivot, no work needs to be performed.
    - If it's less than the pivot element:
      - Swap the position of the current element `A[j]` with the left-most
        processed element greater than the pivot `A[pointer]`.
      - Increment the pointer
- Once every index has been visited, place the pivot element currently sitting
  at `A[left_index]` in it's sorted position. This can be done by swapping the
  pivot element `A[left_index]` and the right-most element less than the pivot
  `A[pointer - 1]`.
- Return the final position of the pivot `pointer - 1`.

## Analysis

The run time of Quicksort hinges completely on the quality of the pivot chosen.

If the chosen pivot happens to be the smallest number of the array, then 1
recursive call will receive an empty subarray and the other recursive call will
receive a subarray containing all remaining elements minus the pivot.
Hypothetically, if this occurs with every partition, then the `partition`
subroutine will be called on subarrays of length `n`, `n - 1`, `n - 1`, ... `1`
resulting in *O(n<sup>2</sup>)* runtime. This exact scenario will occur if
Quicksort is passed an already sorted array, and the `choose_pivot` subroutine
is implemented to always select the first element as the pivot.

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
the first step of the process, the element at index `i` is selected from the
array `A`. Then the array is modified in place such that all elements less than
`A[i]` are positioned before it and all elements greater than `A[i]` are
positioned after it. While the outcome doesn't gaurantee that the elements to
the "left" and "right" are sorted relative to each other, it does gaurantee that
the pivot element is in it's "correct" sorted position. For example:
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



TODO

Draw a picture to go with this description and put it in the notes
- Enforce the following invariant during this subroutine. As you traverse the
  array, at any given time there will be seen an unseen elements. Within the
  seen elements, everything less than the pivot element must come before all
  elements greater than the pivot.