# Karatsuba Multiplication

The Karatsuba Multiplication algorithm was discovered by Anatoly Karatsuba in 1960 and published in 1962. It's an optimization of recursive multiplication.

## Implementation 

### Input

Two n-digit positive integers *x*, and `y`

### Output

The product of `x` and `y`

### Description 
1. If both operands are single digit numbers, compute and return the product
2. Split the first operand into two halves, `a` and `b`
3. Split the second operand into two halves, `c` and `d`
4. Recursively compute `a * c`
5. Recursively compute `b * d`
6. Recursively compute `(a + b) * (c + d)`
7. Subtract the results of step 4 and step 5 from step 6
8. Compute and return the final result by taking the sum of the results from steps 4, 5, and 7 after adding 10<super>n</super> trailing zeros to the result of step 4 and 10<super>n/2</super> zeros to the end of the result of step 7

## Analysis

How much better is Karatsuba's algorithm than straight-forward recursive multiplication?

#### Recursive multiplication

4 recursive calls, the operands have half as many digits in each recursive call, and outside the recusrive calls the additions and padding with 0s can be done in linear time.

Using the Master Method:

*T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

*a* = 4

*b* = 2

*d* = 1

Case 3: *T*(*n*) <= *O*(*n*<sup>log<sub>2</sub>4</sup>) or *O*(*n*<sup>2</sup>)

#### Karatsuba multiplication

The ingenuity of Karatsuba Multiplication is in the 6th step of the pseudocode. The typical approach to recursive multiplication requires 4 recursive calls. Though known to Gauss in the 19th century, Karatsuba formalized the idea that the 2 recursive calls computing `a * d` and `b * c`, can be condensed into one recursive call computing `(a + b) * (c + d)`. As a result, Karatsuba's algorithm only requires 3 recursive calls.

Using the Master Method:

*T*(*n*) <= *aT*(*n*/*b*) + *O*(*n*<sup>*d*</sup>)

*a* = 3

*b* = 2

*d* = 1

Case 3: *T*(*n*) <= *O*(*n*<sup>log<sub>2</sub>3</sup>) or roughly *O*(*n*<sup>1.59</sup>)