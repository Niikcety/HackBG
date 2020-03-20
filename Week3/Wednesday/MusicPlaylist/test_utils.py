import unittest
from utils import is_length_valid, length_to_seconds, length_to_minutes, length_to_hours, from_seconds_to_string

class TestIsLengthValid(unittest.TestCase):
	def test_with_invalid_length_should_raise_error(self):
		length = '1:2:3:4'
		exc = None

		try:
			is_length_valid(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_length_containing_characters_different_than_integers(self):
		length = '1:b'
		exc = None

		try:
			is_length_valid(length)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_length_bigger_than_sixty_should_raise_error(self):
		length1 = '1:62:15'
		length2 = '2:59:63'
		length3 = '-1:12:14'
		exc1 = None
		exc2 = None
		exc3 = None

		try:
			is_length_valid(length1)
		except Exception as err:
			exc1 = err

		try:
			is_length_valid(length2)
		except Exception as err:
			exc2 = err

		try:
			is_length_valid(length3)
		except Exception as err:
			exc3 = err

		self.assertIsNotNone(exc1)
		self.assertIsNotNone(exc2)
		self.assertIsNotNone(exc3)

	def test_with_valid_length_should_return_true(self):
		length1 = '1:03:15'
		length2 = '32:14'

		self.assertTrue(is_length_valid(length1))
		self.assertTrue(is_length_valid(length2))

class TestLengthToSeconds(unittest.TestCase):
	def test_all_avaliable(self):
		input1 = '2:32'
		input2 = '1:0:5'
		wanted_result1 = 152
		wanted_result2 = 3605

		result1 = length_to_seconds(input1)
		result2 = length_to_seconds(input2)

		self.assertTrue(result1 == wanted_result1)
		self.assertTrue(result2 == wanted_result2)

class TestLengthToMinutes(unittest.TestCase):
	def test_all_avaliable(self):
		input1 = '2:32'
		input2 = '1:0:5'
		wanted_result1 = 2
		wanted_result2 = 60

		result1 = length_to_minutes(input1)
		result2 = length_to_minutes(input2)

		self.assertTrue(result1 == wanted_result1)
		self.assertTrue(result2 == wanted_result2)

class TestLengthToHours(unittest.TestCase):
	def test_all_avaliable(self):
		input1 = '2:32'
		input2 = '1:0:5'
		wanted_result1 = 0
		wanted_result2 = 1

		result1 = length_to_hours(input1)
		result2 = length_to_hours(input2)

		self.assertTrue(result1 == wanted_result1)
		self.assertTrue(result2 == wanted_result2)

class TestFromSecondsToString(unittest.TestCase):
	def test_all(self):
		input1 = 0
		input2 = 3800
		input3 = 65

		self.assertTrue(from_seconds_to_string(input1) == "0:0:0")
		self.assertTrue(from_seconds_to_string(input2) == "1:3:20")
		self.assertTrue(from_seconds_to_string(input3) == "0:1:5")
cd 
if __name__ == '__main__':
	unittest.main()