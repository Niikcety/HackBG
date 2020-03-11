import unittest
from my_sort import sort_list_integers

class TestSortListeIntegers(unittest.TestCase):
	def test_if_there_are_no_arguments_should_return_empty_list(self):
		output = []

		result = sort_list_integers()

		self.assertEqual(result ,output)

	def test_if_there_is_one_element(self):
		input = [1]

		result = sort_list_integers(input)

		self.assertEqual(result,input),1,2

	def test_if_there_are_only_equal_integers(self):
		input = [3,3,3]

		result = sort_list_integers(input)

		self.assertEqual(input,result)

	# def test_should_raise_error_when_list_is_not_only_from_integers(self):
	# 	input = [1,2.3]
	# 	exc = None

	# 	try:
	# 		sort_list_integers(input)
	# 	except Exception as err:
	# 		exc = err

	# 	self.assertIsNotNone(exc)
	# 	self.assertEqual(str(exc),'List elements different from integers')


	# def test_should_raise_error_when_list_is_not_only_from_float(self):
	# 	input = [1.2,2.0,1]
	# 	exc = None

	# 	try:
	# 		sort_list_integers(input)
	# 	except Exception as err:
	# 		exc = err

	# 	self.assertIsNotNone(exc)
	# 	self.assertEqual(str(exc),'List elements different from floats')


if __name__ == '__main__':
	unittest.main()