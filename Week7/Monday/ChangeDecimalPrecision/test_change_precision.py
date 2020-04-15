from change_precision import change_precision1
import unittest
from decimal import *


class TestClassChangePrecision(unittest.TestCase):
    def test_with_correct_precision(self):
        with change_precision1(2):
            x = Decimal(2.3500) + Decimal(3.2500)
            self.assertEqual(Decimal(5.6), x)

    # def test_the_exit_clause(self):
    #     with change_precision1(2):
    #         sum1 = Decimal(2.111) + Decimal(2.111)
    #     sum2 = Decimal(2.111) + Decimal(2.111)

    #     self.assertEqual(sum1, Decimal(5.2))
    #     self.assertNotEqual(sum1, sum2)
    #     self.assertEqual(sum2, Decimal(2.111) + Decimal(2.111))

class TestFunctionChangePrecision(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
