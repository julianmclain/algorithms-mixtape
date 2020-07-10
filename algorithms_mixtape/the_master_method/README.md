# The Master Method

The 3 cases of the master method are governed by the relationship of a and b**d

*recursion tree
- at a given depth j = 0,1,2,log<sub>b</sub>n, there are a<sup>j</sup>
  subproblems, each of size n/b<sup>j</sup> 

look at mergesort analysis and Proof 1

Mergesort analysis
- the approach was to look at all the work performed at a given sublevel *j*
  while ignoring work done in recursive calls. Then multiply that amount of work
  times the number of recursive calls required.

## Interpretation of the 3 cases

In the Master Method there's a tug-of-war between 2 opposing forces.
- *a*, a force of "evil" that increases algorithm runtime.
- *b<sup>d</sup>*, a force of "good" that decreases it.

The impact of *a* and *b<sup>d</sup>* on algorithmic runtime become clear if you
really think about what each one represents:
- a = The number of recursive calls. As a result, it's the rate at which
  subproblems proliferate as the algorithm moves deeper in the recursion tree.
  We can refer to it as the rate of subproblem proliferation or RSP for short.
- b<sup>d</sup> = The rate at which the amount of work performed shrinks with
  each subproblem. We can refer to it as the rate of work shrinkage RWS for
  short. Note: you might be wondering why we care about b<sup>d</sup> and not
  simply b. Remember that b is the factor by which the input size decreases with
  each subproblem. We only really care about the size of the subproblem as it
  relates to how much work needs to be performed. d represents the amount of
  work performed, so b<sup>d</sup> represents the amount of work done in a
  subproblem.

The 3 cases of the Master Method correspond to the 3 possibilities in the
relationship between these 2 forces of "good" and "evil":
1. A tie between the 2 forces a = b<sup>d</sup>
2. A case when the forces of good win, a < b<sup>d</sup>
3. A case when the "forces of evil" win, a > b<sup>d</sup>

Note the following:
- If RSP = RWS, then the amount of work is constant at every recursion level. We
  can get the runtime of the entire algorithm by taking the amount of work done
  at the root, n<sup>d</sup> and multiplying it by the number of levels in the
  recursion tree, log n.This leaves us with O(n<sup>d</sup> * log n). Note we
  suppress the log base since it's a constant factor. 
- If RSP < RWS, then the amount of work is decreasing with the recursion level
  *j*. That means the recursion tree level with the most work is the root node.
  Although it's not obvious, we can assume that the work done in the root node
  dominates the amount of work in the lower levels of recursion. Thus, the
  runtime is the amount of work done in the root, n<sup>d</sup>.
- If RSP > TWS, then the amount of work is increasing with the recursion level
  *j*. That means the leaves of the recursion tree will perform the most work.
  Although it's not obvious, we can assume that the work done in the leaves
  dominates the amount of work in higher levels of the recursion tree. Thus, the
  runtime is equal to the amount of work done in the leaves which is O(a
  log<sub>b</sub>n). This is the same as O(n<sup>log<sub>b</sub>a</sup>) which
  is easier to apply, so that's the version that's used.