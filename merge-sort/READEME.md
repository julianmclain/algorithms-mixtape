# Merge Sort

Merge Sort was known to John von Neumann as early as 1945. Despite being over 70 years old, it's still one of the choice sorting algorithms today. It's runtime requires less operations than selection, insertion, and bubble sort. 

## Approach

It's a canonical divide-and-conquer algorithm because it recusrively breaks the problem into subproblems and then combines the subproblem solutions into a final result.

Input: A list of n distinct elements
Output: A new list with the same elements, sorted from smallest to largest
Operations (ignoring base cases):
1. Recursively sort the first half of the input list.
2. Recursively sort the second half of the input list.
3. Merge the two sorted sub-lists into one sorted list.

## Analysis

At most, Merge Sort requires 6n * log<sub>2</sub>n + 6n operations where n is the number of elements in the list.