import unittest
from simplify_fractions import the_largest_common_divisor, simplify_fraction

class TestTheLargestCommonDivisor(unittest.TestCase):
	def test_if_denominator_equal_to_zero_should_should_return_zero(self):
		nominator,denominator = (1,0)
		exc = None
		
		try:
			the_largest_common_divisor(nominator,denominator)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), 'Forbidden division on zero')

	def test_if_nominator_equal_to_zero_should_return_one(self):
		nominator,denominator = (0,1)
		
		result = the_largest_common_divisor(nominator,denominator)

		self.assertEqual(result,1)

	def test_if_function_is_passed_no_arguments_should_return_one(self):
		wanted_result = 1

		result = the_largest_common_divisor()

		self.assertEqual(wanted_result,result)

	def test_with_correct_arguments_should_return_largest_commong_divisor(self):
		nominator,denominator = (9,3)
		wanted_result = 3

		result = the_largest_common_divisor(nominator,denominator)

		self.assertEqual(result,wanted_result)

class TestSimplifyFraction(unittest.TestCase):
	def test_with_tuple_with_more_than_two_elements_should_raise_exception(self):
		input = (2,3,4,5)
		exc = None

		try:
			simplify_fraction(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with more than two elements')

	def test_with_correct_arguments_should_return_reduced_tuple(self):
		input = (3,9)
		wanted_result = (1,3)

		result = simplify_fraction(input)

		self.assertEqual(result,wanted_result)

	def test_with_tuple_of_elements_different_than_integers_should_raise_error(self):
		input = (1,'a')
		exc = None

		try:
			simplify_fraction(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with elements different from integers')

	def test_with_tuple_with_elements_less_than_two(self):
		input = ('a')
		exc = None

		try:
			simplify_fraction(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with elements less than two')


	def test_with_tuple_with_one_integer_in_it_should_raise_error(self):
		input = (3)
		exc = None

		try:
			simplify_fraction(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with one element from type Integer')

	def test_with_integers_less_than_zero_should_return_tuple_with_their_absolute(self):
		input = (-3,9)
		wanted_result = (-1,3)

		result = simplify_fraction(input)

		self.assertEqual(result,wanted_result)


if __name__ == '__main__':
	unittest.main()