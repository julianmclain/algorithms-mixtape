import math


def k_multiply(x, y):
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

    a = x // 10 ** (nby2)
    b = x % 10 ** (nby2)
    c = y // 10 ** (nby2)
    d = y % 10 ** (nby2)

    ac = k_multiply(a, c)
    bd = k_multiply(b, d)

    ab_plus_bc = k_multiply(a + b, c + d) - ac - bd

    product = 10 ** (2 * nby2) * ac + (10 ** nby2 * ab_plus_bc) + bd

    return product


def num_digits(num):
    """Produce the number of digits in a positive integer.

    Parameters
    ----------
    num : int
        Must be a positive integer.

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
    elif num <= 999999999999997:
        return int(math.log10(num)) + 1
    else:
        counter = 15
        while num >= 10 ** counter:
            counter += 1
        return counter
