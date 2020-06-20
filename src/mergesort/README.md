# mergesort

mergesort was known to John von Neumann as early as 1945. Despite being over 70
years old, it's still one of the choice sorting algorithms today. For large
input sizes, it's run time is faster than other sorting algorithms such as
selection, insertion, and bubble sort.

## Implementation 

### Input

an array of *n* elements.

### Output

A new array with the same elements, sorted from smallest to largest.

### Description:
Main function `mergesort(array)`
- If the array has length 1 or less, return a copy. It's already sorted.
- Recursively sort the first half of the input array.
- Recursively sort the second half of the input array.
- Merge the two sorted sub-arrays into one sorted array.

Subroutine `merge(left, right)`
- Create an output array of length `left` + `right`
- Store a pointer to the first element in left `i`
- Store a pointer to the first element in right `j`
- Traverse the indicies of the output array as `k`
   - If the current left element `left[i]` is less than the current right
     element `right[j]`, copy the left element `left[i]` to the output array at
     position `k`. Increment the pointer `i`.
   - If the current right element `right[j]` is less than the current left
     element `left[i]`, copy the right element `right[i]` to the output array at
     position `k`. Increment the pointer `j`.

## Analysis

mergesort is a canonical "divide-and-conquer" algorithm. It splits the input
array into two sub-problems, recursively solves each sub-problem, and then combines the solutions to the sub-problems.

### Asymptotic run time

The [Master
Method](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
states that the runtine of a divide-and-conquer algorithm denoted *T(n)* can be
expressed by the recurrence relation:

> *T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

Where *a* is the number of recrusive calls, *b* is the factor by which the input
size shrinks in every subproblem, and *d* is the exponent in the running time of
the "combine" step.

For mergesort, we fill in the following constants:
- *a* = 2
- *b* = 2
- *d* = 1

This puts the run time in category 1 of 3 since *a* = *b<sup>d</sup>*. Category 3 run
times are defined as *T*(*n*) = *O*(*n*<sup>*d*</sup> log *n*). Filling in the
*d* parameter, we end up with a run time of:

> *O*(*n* log *n*)

Ok, the Master Method is a cool party trick, but the die-hard skeptic in me
wasn't convinced after I ran that black box analysis. mergesort is a hall of fame
algorithm, and I wanted better proof that it can sort an array in *O*(*n* log *n*)
time.

Intuitively, we can confirm the Master Method by analyzing the algorithm as a
recursion tree. The root node of the tree corresponds to the outermost call with
the original input *n* (level 0). Except in the base case, each call to
`mergesort` produces two recursive calls modeled as child nodes. 

![recursion-tree](https://www.dropbox.com/s/18hvfyg61rlt3dc/recursion-tree.jpg?raw=1)

The diagram makes it clear that the total work performed equals the work done
per level multiplied by the number of levels. Ultimately, what we need is:

> *Total work* = *total work per level* * *number of levels*

Let's start by determining the amount of work done per level:

> *Total work per level* = *work per sub-problem* * *number of sub-problems*

Returning to the high-level description of `mergesort` above, there are 3 steps
(excluding the base case):
  1. recusively sort the left
  2. recursively sort the right
  3. `merge`

When analyzing the work done at a single level, we can ignore the recursive
calls. The work performed in recursive calls will be accounted for when we
multiply by the number of levels in the recursion tree. As a result, the total
work done in a given call to `mergesort` is equal to the amount of work done in
the `merge` subroutine. `merge` has to examine every element in the left and
right input arrays, so the work performed by merge is proportional to the input
size. Return to our recursion tree diagram and notice the relationship between
the size of *n* and the number of sub-problems at a given level. Mergesort has an
especially satisfying design because the amount of work done in each sub-problem
decreases at the same rate that the number of sub-problems increases. They
operate in perfect equalibrium. No matter the level, the aggregate input size is
*n*. Given that the aggregate input size at every level equals *n* and
that `merge` must visit every element in the input, we can confidently say that
`merge`, and consequently `mergesort`, will perform *O(n)* work at every level.

Now for the number of levels. Looking at the recursion tree, you can see that
the input size shirnks by a factor of 2 with each level (e.g. n, n/2, n/4, n/8,
n/16...). Eventually, the input size will be equal or less than 1. At that
point, the base case kicks in and the recursion ends. To determine the number of
levels, what we need is an operation that will tell us how many times we need to
divide *n* by 2 until we reach a number that is 1 or less. Luckly, this is the
exact definition of log<sub>2</sub>. For example:

> log<sub>2</sub>16 = 4
>
>4 is the number of times you need to divide 16 by 2 until you reach 1 or less

Equipped with this info, we know that number of levels in the recursion tree is
log<sub>2</sub> *n*. Let's return to our original forumla and fill in the *total
work per level* and the *number of levels*.

> *Total work* = *O*(*n*) * log<sub>2</sub> *n*

Logarithms of a different base differ by a constant factor so we can eliminate
the base: O(*n* log *n*). There it is! The Master Method holds up, and we have an
intuitive understanding for why mergesort runs in O(*n* log *n*) time.
