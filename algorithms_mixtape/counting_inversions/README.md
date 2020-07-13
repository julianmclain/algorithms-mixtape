# Counting Inversions of an Array

An inversion of an array is a pair of elements that are "out of order." The
first element of the pair is bigger than the second element, yet it occurs
earlier in the array (assuming ascending sort order). Using some notation, we
can express an inversion as a pair of array indicies `(i, j)` such that `i < j`
and `A[i] > A[j]`.

Using the notation above, we can define 3 types of inversions:
- Left inversion: when `i, j <= n/2`
- Right inversion: when `i, j > n/2` 
- Split inversion: when `i <= n/2 < j`

**`n` = the array length

In practice, an interesting application of inversions is measuring the
similarity of 2 ranked lists. For example, imagine you rank your 10 favorite
movies. Then you ask your friend to take those same 10 favorite movies and
provide her own rank list. If your friend ranks the same movies 1 - 10, then
there will be no inversions. If she provides the exact opposite rankings (i.e. 1
becomes 10, 9 becomes 2, etc...), there will be 10 choose 2 inversions (the
maximum possible).

The concept of measuring the similarity between ranked lists is core to
*collaborative filtering*, a technique used to make recommendations.

## Implementation 

### Input

An array containing the numbers 1 through `n` in an arbitrary order.

### Output

The number of inversions in the array. 

### Description 

A naive approach is to use brute-force to solve:
1. If `n = 1`, return 0
2. Loop through all indices `i`
3. For each index `i`, Loop through all `j` indices bigger than `i`
4. If `A[i] > A[j]`, count an inversion

This has a runtime of *O(n<sup>2</sup>)*... not great!

A better approach is to use the Divide and Conquer Paradigm. If you split the
array in half, you can recusively compute the left and right inversions. Then
you just need to solve for the split inversions and sum the counts.

The key to making this approach work is to see that counting inversions
intersects directly with sorting. Remember that an inversion is essentially
just an element that's "out of order."

The Divide and Conquer approach:
- Have the function return the number of inversion *AND* the sorted array. That
  way, the `merge` function will receive 2 sorted lists.

`count_inversions(A: array) -> array, int`
1. If `n = 1`, return 0
2. *B*, *x* = make a recursive call with the first half of the array.
3. *C*, *y* = make recursive call with the left half of the array.
4. *D*, *z* = merge *B* and *C* while counting all split inversions. 


`merge(B: array, C: array) -> array, int`

Because *B* and *C* are already sorted, there's at least one split inversion any
time an element in *C* is less than an element in *B*. The exact number of split
inversions depends on the number of elements still in *B*.

For example, let *n* equal the length of *C*. If `C[j] < B[i]`, then the number
of split inversions equals `n - j`.

See [mergesort](/algorithms_mixtape/mergesort) for a full description of merging 2 sorted arrays.

## Analysis

### Asymptotic Runtime

Given the above implementation, you can see that algorithm for counting
inversions is mergesort with a small modification that keeps track of the number
of inversions. The relevant question is: if mergesort runs in *O*(*n* log *n*)
time, does keeping tracking track of the number of inversions impact the
asymptotic runtime?

The answer is a resounding *nope*. Initializing and incrementing a counter can be done
in constant time.

The runtime for computing inversions of an array is:

> *O*(*n* log *n*) 

If you're interested in more detail, I recommend checking out the analysis of
[mergesort](/algorithms_mixtape/mergesort).