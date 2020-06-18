# Counting Inversions of an Array

An inversion of an array is a pair of elements that are "out of order," meaning
that an element that occurs earlier in the array is bigger than one that
occurs later. Mathematically, that is to say that an inversion is a pair of 
array indicies `(i, j)` such that `i < j` and `A[i] > A[j]`.

Inversions can be used to objectively measure the similarity of 2 ranked lists.
For example, imagine you rank your 10 favorite movies. You then ask your friend
to take your 10 favorite movies and provide their own rank list. If your friend
ranks the same movies 1 - 10, there will be no inversions. If he / she provides the
exact opposite rankings (i.e. 1 become 10, 9 becomes 2, etc...), there will be
10 choose 2 inversions (the maximum possible).

The concept of generating a measure of similarity between rankings is core to
*collaborative filtering*, a technique used to make recommendations.

There are 3 types of inversions
- Left inversion: when `i, j <= n/2`
- Right inversion: when `i, j > n/2` 
- Split inversion: when `i <= n/2 < j`

where `n` = the array length

## Implementation 

### Input

An array containing the numbers 1 through `n` in an arbitrary order.

### Output

The number of inversions of the array. 

### Description 

A naive approach is to use brute-force to solve:
1. If `n = 1`, return 0
2. Loop through all indices `i`
3. For each index `i`, Loop through indicies `j` (each index bigger than `i`)
4. If `A[i] > A[j]`, count an inversion

This has a runtime of *O(n<sup>2</sup>)*... not great :(

A better approach is to use the Divide and Conquer Paradigm. If you split the
array in half, you can recusively compute the left and right inversions. Then
you just need to solve for the split inversions and sum the counts.

The key to making this approach work is to see that counting inversions
intersects directly with sorting. Remember that an inversion is essentially
just an element that's "out of order."

The Divide and Conquer approach:
1. If `n = 1`, return the array unmodified and 0.
2. B, x = recursive call with the first half of the array. Returns a sorted array and the number of inversions.
3. C, y = recursive call with the left half of the array. Returns a sorted array and the number of inversions.
4. D, z = merge x and y while counting all split inversions. If you have a sorted left array, B, and a sorted right array, C, then you have a split inversion any time you copy an element from C into the output array while B is not empty. More specifically, if you have indicies `i` of `B` and `j` of `C`, then the number of inversions created when `C[j]` is copied to the output array is equal to the number of remaining elements in `B`. This is because B is already sorted. If `C[j]` is less than `B[i]`, it must also be less than every element after `B[i]`.
5. return x + y + z

## Analysis

The runtime of the entire function will be equal to the runtime of the 'merge and count split inversions' subroutine multiplied by the number of times it's called. 

The 'merge and count inversions' must loop through `n` elements while building the ouput array. For each index of the ouptput array, the subroutine copies an element from the sub-array and possibly adding to the inversion count. As a result, copying the elements from the sub-arrays to the output array requires `0(n)` work. Adding to the inversion count requires at most `1/2n` additions since in the 'worst-case-scenario', every element in the second sub-array will be copied before the first sub-array. However, in this scenario, once the second sub-array is copied, there will be no more additions. `0(n)` runtime for copying the elements plus `0(n)` for counting inversions (drop the 1/2 constant) equals `0(n)` for the entire subroutine.

The main function makes 2 recursive calls, each with half of the input array. This results in `log n` runtime. Combining the main function and the subroutine, you get `0(n log n)` for the entire algorithm.

Confirmed using the Master Method:

*T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

*a* = 2

*b* = 2

*d* = 1

*T*(*n*) <= *O*(*n* log *n*)