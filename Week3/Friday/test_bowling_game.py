import unittest

from bowling_game import BowlingGame 

class TestBowlingGame(unittest.TestCase):
	def test_initialization_with_correct_values(self):
		input = [3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,10,10,10]
		wanted_result = [[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[3,4],[10,0],[10,0],[10,0]]
		bowling_game = BowlingGame(input)

		result = bowling_game.frames
		
		self.assertEqual(wanted_result, result)

	def test_initialization_with_incorrect_values(self):
		input = [3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,3,4,7,8]
		exc = None

		try:
			BowlingGame(input)
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		
if __name__ == '__main__':
	unittest.main()