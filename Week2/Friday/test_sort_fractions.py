import unittest
from sort_fractions import list_checker, sort_list_of_tuples_ascending, sort_list_of_tuples_descending, test_if_boolean_is_correct

class TestListChecker(unittest.TestCase):
	def test_if_given_object_is_list_should_raise_error(self):
		input = 5
		exc = None

		try:
			list_checker(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),"Given argument is not a list")

	def test_if_elements_of_the_list_are_only_tuples_should_raise_error(self):
		input = [(1,2),(2,3),2]
		exc = None

		try:
			list_checker(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),"There is an element that is not tuple")

	def test_if_tuple_from_the_list_have_different_size_than_two_should_raise_error(self):
		input = [(1,2),(2,3,3)]
		exc = None

		try:
			list_checker(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),"There is an tuple with size different than two")

	def test_if_elements_from_the_tuple_are_only_integers_should_raise_error(self):
		input = [(2,'b'),(1,2)]
		exc = None

		try:
			list_checker(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc),"There is an tuple with elements different than int")

	def test_with_correct_input_should_return_true(self):
		input = [(2,3),(4,5)]

		result = list_checker(input)

		self.assertEqual(result,True)

class TestSortListOfTuplesAscending(unittest.TestCase):
	def test_if_its_given_list_with_one_element_should_return_same_list(self):
		input = [(2,3)]

		result = sort_list_of_tuples_ascending(input)

		self.assertEqual(input,result)

	def test_with_empty_list_should_return_empty_list(self):
		input = []

		result = sort_list_of_tuples_ascending(input)

		self.assertEqual(input,result)

	def test_with_correct_values(self):
		input = [(2, 3), (1, 2)]
		wanted_output = [(1,2),(2,3)]
		
		result = sort_list_of_tuples_ascending(input)

		self.assertEqual(result,input)

class TestSortOfTuplesAscending(unittest.TestCase):
	def test_with_correct_values(self):
		input = [(1,2),(2,3)]
		wanted_output = [(2,3),(1,2)]

		result = sort_list_of_tuples_descending(input)

		self.assertEqual(wanted_output,result)

class TestIfBooleanIsCorrect(unittest.TestCase):
	def test_with_wrong_value_should_raise_error(self):
		input = 2
		exc = None

		try:
			test_if_boolean_is_correct(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		self.assertEqual(str(exc), "Value different from Boolean")

	def test_with_correct_value_should_return_true(self):
		input = False 

		result = test_if_boolean_is_correct(input)

		self.assertEqual(result,True)


if __name__ == '__main__':
	unittest.main()