# Karatsuba Multiplication

The Karatsuba Multiplication algorithm was discovered by Anatoly Karatsuba in
1960 and published in 1962. At the time, Andrey Kolmogorov claimed that the
traditional grade-school algorithm was asymptotically optimal, meaning that any
algorithm for that task would require Ω(*n*<sup>2</sup>) operations.

## Implementation 

### Input

Two n-digit positive integers *x*, and *y*.

### Output

The product of *x* and *y*.

### Description 
1. If both operands are single digit numbers, compute and return the product
2. Split the first operand into two halves, `a` and `b`
3. Split the second operand into two halves, `c` and `d`
4. Recursively compute `a * c`
5. Recursively compute `b * d`
6. Recursively compute `(a + b) * (c + d)`
7. Subtract the results of step 4 and step 5 from step 6
8. Compute and return the final result by taking the sum of the results from
   steps 4, 5, and 7 after adding 10<super>n</super> trailing zeros to the
   result of step 4 and 10<super>n/2</super> zeros to the end of the result of
   step 7

## Analysis

This one was tricky to implement for 2 reasons:
  1. On first glance, the operations seem completely random. It was tough to
     develop an intuition for how the algorithm solves the problem.
  2. It took me a while to figure out the best way to split the operands in
     half. I ended up left padding one operand with 0s if it has less digits than
     the other. Floor dividing each input by 10 to the power nby2 achieves this.

Does the additional complexity pay off? How much better is Karatsuba's algorithm
than straight-forward recursive multiplication?

Intuitively, we have to believe that the answer is yes. Karatsuba shaves a full
recursive call off the traditional algorithm. Is it possible to quantify how much
faster it is?

### Asymptotic runtime

Let's compare standard recursive multiplication with Karatsuba multiplication.

#### Recursive multiplication

There are 4 recursive calls, the operands have half as many digits in each
recursive call, and outside the recusrive calls the additions and padding with
0s can be done in linear time.

The [Master
Method](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms))
states that the runtine of a divide-and-conquer algorithm denoted *T(n)* can be
expressed by the recurrence relation:

> *T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

Where *a* is the number of recrusive calls, *b* is the factor by which the input
size shrinks in every subproblem, and *d* is the exponent in the running time of
the "combine" step.

For standard recursive multiplication, we fill in the following parameters:
- *a* = 4
- *b* = 2
- *d* = 1

This puts the runtime in category 3 of 3 since *a* > *b<sup>d</sup>*. Category 3 run
times are defined as *T*(*n*) = *O*(*n*<sup>log<sub>*b*</sub>*a*</sup>). Filling in the
parameters, we end up with a runtime of:

> *O*(*n*<sup>log<sub>2</sub>4</sup>) which simplifies to *O*(*n*<sup>2</sup>)

#### Karatsuba multiplication

The ingenuity of Karatsuba Multiplication is in the 6th step of the description.
The typical approach to recursive multiplication requires 4 recursive calls.
Karatsuba performs it with 3. Although it was known to Gauss in the 19th
century, Karatsuba took advantage of the idea that the 2 recursive calls
computing `a * d` and `b * c`, can be condensed into one recursive call
computing `(a + b) * (c + d)`.

Again, using the Master Method, we fill in the following parameters:
- *a* = 3
- *b* = 2
- *d* = 1

This also puts the runtime in category 3 of 3 since *a* > *b<sup>d</sup>*. Category 3 run
times are defined as *T*(*n*) = *O*(*n*<sup>log<sub>*b*</sub>*a*</sup>). Filling in the
parameters, we end up with a runtime of:

> *O*(*n*<sup>log<sub>2</sub>3</sup>) or approximately *O*(*n*<sup>1.59</sup>)

There's the quantitative proof, it's a significant improvement for lage input sizes.