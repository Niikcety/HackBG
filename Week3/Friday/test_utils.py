import unittest
from utils import test_input, return_the_input_with_list_of_tuples,check_number_of_frames, frame_number_10, frame_number_11, frame_number_12, return_game

class TestTestInput(unittest.TestCase):
	def test_if_input_is_list_should_raise_error(self):
		input = (1,2)
		exc = None

		try:
			test_input(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_if_input_length_is_less_11_or_bigger_than_21_should_raise_error(self):
		input1 = [1,1,1,1,1,1,1]
		input2 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
		exc1 = None
		exc2 = None

		try:
			test_input(input1)
		except Exception as err:
			exc1 = err

		try:
			test_input(input2)
		except Exception as err:
			exc2 = err

		self.assertIsNotNone(exc1)
		self.assertIsNotNone(exc2)

	def test_if_there_is_invalid_score_in_input(self):
		input1 = [1,2,3,4,5,6,7,9,1,10,11,12]
		exc = None

		try:
			test_input(input1)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_correct_scores_should_return_the_list(self):
		input1 = [1,1,1,1,1,1,1,1,1,1,1,1]

		self.assertTrue(test_input(input1))

class TestReturnInputWithListOfTuples(unittest.TestCase):
	def test_if_there_is_strike_in_second_roll_and_first_roll_different_than_zero(self):
					# for example [5,10] is invalid roll
					# should raise error
			input = [5,10,6,3,4,3,2,1,1,1,1,1]
			exc = None

			try:
				return_the_input_with_list_of_tuples(input)
			except Exception as err:
				exc = err

			self.assertIsNotNone(exc)

	def test_if_there_are_odd_rolls(self):
				# for example [5,3,2]
				# should return [5,3],[2]

		input = [5,3,2,1,2,1,2,1,2,1,2]
		wanted_result = [[5,3],[2,1],[2,1],[2,1],[2,1],[2]]

		result = return_the_input_with_list_of_tuples(input)

		self.assertEqual(wanted_result, result)


	def test_if_strike_is_on_first_roll_should_omit_the_next_roll(self):
		input = [5,3,10,4,3,2,1,2,1,2,1]
		wanted_result = [[5,3],[10,0],[4,3],[2,1],[2,1],[2,1]]

		result = return_the_input_with_list_of_tuples(input)

		self.assertEqual(wanted_result, result)

	def test_with_only_strikes(self):
		input = [10,10,10,10,10,10,10,10,10,10,10]
		wanted_result = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0]]

		result = return_the_input_with_list_of_tuples(input)

		self.assertEqual(wanted_result, result)


class TestCheckNumberOfFrames(unittest.TestCase):
	def test_with_frames_less_than_10_and_more_than_12(self):
		input1 = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0]]
		input2 = [[10,0],[10,0],[10,0],[10,0]]
		exc1 = None
		exc2 = None

		try:
			check_number_of_frames(input1)
		except Exception as err:
			exc1 = err

		try:
			check_number_of_frames(input2)
		except Exception as err:
			exc2 = err

		self.assertIsNotNone(exc1)
		self.assertIsNotNone(exc2)

class TestFrameNumber10(unittest.TestCase):
	def test_if_tenth_frame_has_sum_more_than_10_should_raise_error(self):
		input = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[7,8]]
		exc = None

		try:
			frame_number_10(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_if_frames_has_more_than_10_pins(self):
		input = [[10,0],[10,0],[10,0],[10,0],[7,8],[10,0],[10,0],[10,0],[10,0],[10,0]]
		exc = None

		try:
			frame_number_10(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_correct_frames(self):
		input = [[2,3],[4,5],[6,2],[1,2],[1,2],[3,4],[2,1],[3,2],[9,0],[2,3]]
		result = frame_number_10(input)

		self.assertEqual(input,result)

class TestFrameNumber11(unittest.TestCase):
	def test_if_tenth_frame_is_equal_to_lt_or_gt_than_10(self):
		input1 = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[7,8],[10,0]]
		input2 = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[2,1],[10,0]]
		exc1 = None
		exc2 = None
		

		try:
			frame_number_11(input1)
		except Exception as err:
			exc1 = err

		try:
			frame_number_11(input2)
		except Exception as err:
			exc2 = err
		
		self.assertIsNotNone(exc1)
		self.assertIsNotNone(exc2)

	def test_with_invalid_frame(self):
		input = [[[7,8],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[3]]]
		exc = None

		try:
			frame_number_11(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_correct_frames(self):
		input = [[2,3],[4,5],[6,2],[1,2],[1,2],[3,4],[2,1],[3,2],[9,0],[4,6],[2]]
		result = frame_number_11(input)

		self.assertEqual(input,result)

class TestFrameNumber12(unittest.TestCase):
	def test_with_invalid_last_frames(self):
		input = [[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[10,0],[3,4]]
		exc = None
		try:
			frame_number_12(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_with_correct_frames(self):
		input = [[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[10,0],[10,0],[10,0]]
		result = frame_number_12(input)

		self.assertEqual(input,result)

class TestReturnGame(unittest.TestCase):
	def test_with_correct_input(self):
		input = [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
		wanted_result = [[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3],[3,3]]

		result = return_game(input)

		self.assertEqual(wanted_result,result)

if __name__ == '__main__':
	unittest.main()