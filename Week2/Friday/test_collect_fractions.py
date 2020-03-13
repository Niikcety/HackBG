import unittest
from collect_fractions import check_if_list_is_legit, find_the_total_denominator, expand_the_fractions, collect_fractions

class TestIfListIsLegit(unittest.TestCase):
	def test_with_tuples_of_len_diffent_than_two_should_raise_error(self):
		input = [(1,2,3)]
		exc = None

		try:
			check_if_list_is_legit(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuples different than two items')

	def test_with_tuples_with_one_element_should_raise_error(self):
		input = [(1)]
		exc = None

		try:
			check_if_list_is_legit(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with one element')

	def test_with_empty_list_should_raise_error(self):
		input = []
		exc = None

		try:
			check_if_list_is_legit(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Empty list')

	def test_with_tuples_different_than_int_should_raise_error(self):
		input = [('a','b')]
		exc = None

		try:
			check_if_list_is_legit(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Tuple with different elements than int')

	def test_with_correct_input_should_return_true(self):
		input = [(1, 7), (2, 6)]

		result = check_if_list_is_legit([(1, 7), (2, 6)])

		self.assertEqual(result, True)

class TestFindTheTotalDenominator(unittest.TestCase):
	def test_with_nominator_equal_to_zero_should_put_it_out_of_the_equation(self):
		input = [(0,6),(3,5),(4,2)]
		wanted_result = 10

		result = find_the_total_denominator(input)

		self.assertEqual(wanted_result,result)

	def test_with_denomminator_equal_to_zero_should_raise_error(self):
		input = [(5,0),(3,5),(4,2)]
		exc = None

		try:
			find_the_total_denominator(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),'Forbidden division of zero')
	

	def test_with_correct_input_should_return_integer(self):
		input = [(1, 7), (2,6)]
		wanted_result = 42

		result = find_the_total_denominator(input)

		self.assertEqual(wanted_result,result)


class TestExpandTheFractions(unittest.TestCase):
	def test_with_nominator_equal_to_zero_should_put_it_out_of_the_list(self):
		input = [(1,7),(2,6),(0,5)]
		wanted_result = [(6,42),(14,42)]

		result = expand_the_fractions(input)

		self.assertEqual(wanted_result,result)

	def test_with_correct_input_should_return_list(self):
		input = [(1,7),(2,6)]
		wanted_result = [(6,42),(14,42)]

		result = expand_the_fractions(input)

		self.assertEqual(wanted_result,result)

class TestCollectFractions(unittest.TestCase):
	def test_with_correct_input_should_return_simplified_tuple(self):
		input = [(1,7),(2,6)]
		wanted_result = (10,21)

		result = collect_fractions(input)

		self.assertEqual(wanted_result,result)

if __name__ == '__main__':
	unittest.main()