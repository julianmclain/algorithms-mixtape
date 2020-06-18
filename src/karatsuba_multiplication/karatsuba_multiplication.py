import math


def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    result = karatsuba(x, y)
    assert x * y == result
    print(f'{x} times {y} is {result}')

    # Test num_digits
    assert num_digits(0) == 1
    assert num_digits(123) == 3
    assert num_digits(1234) == 4
    assert num_digits(
        3141592653589793238462643383279502884197169399375105820974944592) == 64


def karatsuba(x, y):
    """Calculate the product of 2 integers using Karatsuba Multiplication.

    This implementation assumes that only single digit multiplication can be used.

    Parameters
    ----------
    x : int
    y : int

    Returns
    -------
    int
        The product of x and y.

    Notes
    -----
    When splitting the inputs, if one operand has less digits then you need to
    left pad it with 0s to make the number of digits equal. Floor dividing the
    input by 10 to the power nby2 achieves this.

    nby2 represents the approximate middle point. If n is odd, nby2 == (n / 2) - 1
    """

    if x < 10 and y < 10:
        return x * y

    n = max(num_digits(x), num_digits(y))
    nby2 = n // 2

    a = x // 10**(nby2)
    b = x % 10**(nby2)
    c = y // 10**(nby2)
    d = y % 10**(nby2)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)

    ab_plus_bc = karatsuba(a+b, c+d) - ac - bd

    product = 10**(2*nby2) * ac + (10**nby2 * ab_plus_bc) + bd

    return product


def num_digits(num):
    """Produce the number of digits in a non-negative integer.

    Parameters
    ----------
    num : int

    Returns
    -------
    int
        The number of digits in the input number.

    Notes
    -----
    For small numbers, using math.log10 is faster than converting the number
    to a string. However, if the number is greater than 999999999999997
    there will be inaccuracies due to the limits of floating point precision.

    https://stackoverflow.com/a/28883802/5665518
    """
    if num == 0:
        return 1
    if num <= 999999999999997:
        return int(math.log10(num)) + 1
    else:
        counter = 15
        while num >= 10**counter:
            counter += 1
        return counter


if __name__ == '__main__':
    main()
