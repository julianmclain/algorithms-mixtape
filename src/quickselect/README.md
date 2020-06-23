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

An array of *n* >= 1 elements in any order and an integer *k* between 1 and *n* (inclusive).

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

The runtime analysis of Quickselect is very similar to Quicksort. This should
make sense since Quickselect is basically a partial application of the Quicksort
algorithm.

Like Quicksort, the runtime of Quickselect hinges completely on the quality of
the pivot chosen. Also like Quicksort, it's fair to assume that a pivot chosen
uniformly at random will produce an "approximate median" on average. Using an
approximate median pivot, the input array will be split into 2 sub-arrays
of roughly *n/2* length. Then a recursive call is made with whichever sub-array
contains the *kth* element (ignoring the lucky case where the pivot is the *kth*
element).

This design is well-suited for the [Master
Method](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
since it recurses on a sub-problem that's reduced by a constant factor. The
Master Method states that the runtine of a divide-and-conquer algorithm denoted
*T(n)* can be expressed by the recurrence relation:

> *T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

Where *a* is the number of recrusive calls, *b* is the factor by which the input
size shrinks in every subproblem, and *d* is the exponent in the running time of
the "combine" step.

For Quickselect, we fill in the following constants:
- *a* = 1
- *b* = 2
- *d* = 1 

This puts quicksort's runtime in category 2 of 3 since *a* < *b<sup>d</sup>*.
Category 2 run times are defined as *T*(*n*) = *O*(*n*<sup>*d*</sup>).
Filling in the *d* parameter, we end up with a run time of:

> *O*(*n*)

Note that this is an *average* runtime because pivots are chosen randomly. It's
highly unlikely but possible that the randomly chosen pivot always produces a
subproblem of *n* - 1 length. In that case, the runtime would be quadratic. 