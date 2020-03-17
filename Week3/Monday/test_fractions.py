import unittest
from fractions import Fraction, simplify_fraction, collect_fractions

class TestFraction(unittest.TestCase):
	def test_init_functions_if_values_different_than_integers_are_given_should_raise_error(self):
		exc = None

		try:
			Fraction('a',2)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Arguments different than integers')

	def test_init_function_if_denominator_equal_to_zero_should_raise_error(self):
		exc = None

		try:
			Fraction(1,0)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Denominator cannot be zero')
		

# class TestSimplifyFractions(unittest.TestCase):
# 	def test_if_argument_different_than_tuple_should_raise_error(self):
# 		input = [1,2]
# 		exc = None

# 		try:
# 			simplify_fraction(input)
# 		except Exception as err:
# 			exc = err

# 		self.assertIsNotNone(exc)
# 		self.assertEqual(str(exc),'Argument is not tuple')

# 	def test_if_argument_has_more_than_two_elements_should_raise_error(self):
# 		input = (1,2,3)
# 		exc = None

# 		try:
# 			simplify_fraction(input)
# 		except Exception as err:
# 			exc = err

# 		self.assertIsNotNone(exc)
# 		self.assertEqual(str(exc),'Argument is not with two parameters')

# 	def test_with_correct_values(self):
# 		a = Fraction(3,9)
# 		b = Fraction(1,3)

# 		a.simplify()

# 		self.assertEqual(a,b)


# class TestCollectFractions(unittest.TestCase):
# 	def test_if_argument_is_not_a_list_should_raise_error(self):
# 		input = (1,2)
# 		exc = None

# 		try:
# 			collect_fractions(input)
# 		except Exception as err:
# 			exc = err

# 		self.assertIsNotNone(exc)
# 		self.assertEqual(str(exc),'Argument is not a list')


# 	def test_if_list_is_not_from_tuples_should_raise_error(self):
# 		input = [(1,2),2]
# 		exc = None

# 		try:
# 			collect_fractions(input)
# 		except Exception as err:
# 			exc = err

# 		self.assertIsNotNone(exc)
# 		self.assertEqual(str(exc),'There is an element ')



if __name__ == '__main__':
	unittest.main()