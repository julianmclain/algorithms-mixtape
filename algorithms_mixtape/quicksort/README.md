# Quicksort

Tony Hoare developed the Quicksort algorithm in 1959 when he was only 25! It was
published 2 years later in 1961. Eventually he went on to win an ACM Turing
award.

## Implementation

### Input

An array of `n` elements.

### Postcondition

The elements in the input array are sorted from smallest to largest.

### Description

Subroutine `quicksort(A, left_index, right_index)`
- Return if the array `A` contains 1 element or less. In this case it's already sorted.
- Choose a pivot index between `left_index` and `right_index` uniformly at random
- Make the pivot element the left-most element (i.e. swap `A[left_index]` with
  `A[pivot_index]`)
- Partition the array `A` around the pivot element
- Recursively sort elements to the left of the pivot element
- Recursively sort elements to the right of the pivot element

Subroutine `choose_pivot(A, left_index, right_index)`
- Return a random index between `left_index` and `right_index`

Subroutine `partition(A, left_index, right_index)`
- Take the left-most element as the pivot element (i.e `A[left_index]`)
- Store a pointer `i` to the index after the pivot element (i.e. `A[left_index +
  1]`). It will be used to keep track of the bounary between processed elements
  that are less than and processed elements greater than the pivot. For example, the element at
  `A[i]` should be leftmost element greater than the pivot.
- Range over all indicies `j` between `left_index + 1` and `right_index`. Note
  that the index `j` will track progress as elements are processed.
- For each element `A[j]`:
    - If it's greater than the pivot, no work needs to be performed.
    - If it's less than the pivot element:
      - Swap the position of the current element `A[j]` with the left-most
        processed element greater than the pivot `A[i]`.
      - Increment `i`
- Once every index has been visited, place the pivot element currently sitting
  at `A[left_index]` in it's sorted position. This can be done by swapping the
  pivot element `A[left_index]` and the right-most element less than the pivot
  `A[pointer - 1]`.
- Return the final position of the pivot `pointer - 1`.

![partition diagram](https://www.dropbox.com/s/bl5u5477wp9d9dm/Partition%20in%20place.jpg?raw=1)

## Analysis

One key idea in Quicksort is partitioning the array around a pivot element. In
the first step of the process, the element at index `i` is selected from the
array `A`. Then the array is modified in place such that all elements less than
`A[i]` are positioned before it and all elements greater than `A[i]` are
positioned after it. While the operation doesn't gaurantee that the elements to
the "left" and "right" are sorted relative to each other, it does gaurantee that
the pivot element is in it's "correct" sorted position. For example:
```
Array A = [3, 8, 2, 5, 1, 4, 7, 6]
```
Now let's select the first element as the pivot and partition the array.
```
[2, 1, 3, 6, 7, 4, 5, 8]
```
After partitioning, note the result:
- The pivot element is in it's ultimate sorted position
- Elements left of pivot are less than the pivot element
- Elements right of pivot greater than the pivot element

While partitioning doesn't completely sort an array, it's the key to mergesort
because it enables a "divide and conquer" approach. After partitioning an array,
the sorting problem can be broken down into 2 sub-problems: sorting the left elements and sorting the right elements. The pivot element can be excluded from the sub-problems
since partitioning already places it in the final sorted position.

Finally, with a small constant of memory usage, all of the operations can be done in-place.

### Asymptotic runtime

The run time of Quicksort hinges completely on the quality of the pivot chosen.

#### Worst case scenario

The worst case scenario occurs when the chosen pivot is always the smallest
element of the array. In this case, the `partition` subroutine will scan the
array and never find any elements less than the pivot. As a result, the
subsequent left recursive call will receive an empty sub-array and the right
recursive call will receive a sub-array containing all remaining elements minus
the pivot. Over the entire execution of `quicksort`, the `partition` subroutine
will be called with sub-arrays of length *n*, *n* - 1, *n* - 2, ... 1. Since the
work done in `partition` is equal to the length of the sub-array, `partition`
will perform *n* + (*n* - 1) + (*n* - 2) ... + 1 or 

> *O*(*n*<sup>2</sup>)

While this exact scenario sounds unlikely, it will occur if quicksort is passed
an already sorted array, and the `choose_pivot` subroutine is implemented to
always select the first element as the pivot.

#### Best case scenario

On the other hand, if the chosen pivot happens to always be the median element,
then the array will be evenly split into 2 sub-arrays of `n/2` length. Each
recursive call decreases the input by a constant factor indepenent of *n* which
is great because it allows us to use the Master Method to determine the runtime.

Let's assume that `choose_pivot` can identify the median in *O*(*n*) time,
and `partition` also operates in *O*(*n*) time.

The [Master
Method](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
states that the runtine of a divide-and-conquer algorithm denoted *T(n)* can be
expressed by the recurrence relation:

> *T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

Where *a* is the number of recrusive calls, *b* is the factor by which the input
size shrinks in every subproblem, and *d* is the exponent in the running time of
the "combine" step.

For quicksort, we fill in the following constants:
- *a* = 2
- *b* = 2
- *d* = 1

This puts quicksort's runtime in category 1 of 3 since *a* = *b<sup>d</sup>*.
Category 3 run times are defined as *T*(*n*) = *O*(*n*<sup>*d*</sup> log *n*).
Filling in the *d* parameter, we end up with a run time of:

> *O*(*n* log *n*)

Note that this is the same recurrence relation observed in mergesort.

#### Randomization

The performance disparity between the worst case and best case scenario is
pretty big. Knowing that it's possible to implement `choose_pivot` such that
quicksort runs in *O*(*n* log *n*) time, why would any other implementations
exist?

As it turns out, simply selecting the pivot at random will produce an *average*
runtime of *O*(*n* log *n*). I won't give the full-blown mathematical proof of
that fact, but intuitively it seems plausible. If we define an "approximate
median" as any number between the 25th percentile and the 75th percentile, then
there's a 50% chance that a randomly selected pivot will be an "approximate
median." Randomization is a second key idea in quicksort. There are many
computational problems for which randomized algorithms are faster, more
effective, and easier to code than deterministic counterparts.