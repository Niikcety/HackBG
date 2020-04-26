from big_positive_pow import big_possitive_pow
from unittest.mock import patch
import unittest


class TestBigPositivePow(unittest.TestCase):
    @patch('big_positive_pow.randint')
    def test_if_y_is_less_than_one_should_raise_error(self, mock_randint):
        mock_randint.return_value = -1
        exc = None

        try:
            big_possitive_pow()
        except ValueError as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Try again.')

    @patch('big_positive_pow.randint')
    def test_with_correct_values(self, mock_randint):
        mock_randint.return_value = 2
        result = big_possitive_pow()

        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
