import unittest
from algorithms_mixtape.karatsuba_multiplication.karatsuba_multiplication import (
    k_multiply,
)


class TestKaratsubaMultiplication(unittest.TestCase):
    def test_k_multiply(self):
        x = 3141592653589793238462643383279502884197169399375105820974944592
        y = 2718281828459045235360287471352662497757247093699959574966967627
        result = k_multiply(x, y)
        self.assertEqual(x * y, result)


if __name__ == "__main__":
    unittest.main()
