import unittest
from music_library import Song

class TestClassSong(unittest.TestCase):
	def test_constructor_of_song_with_no_parameters_should_return_none_of_all(self):
		song = Song()

		self.assertTrue(song.title == None)
		self.assertTrue(song.artist == None)
		self.assertTrue(song.album == None)
		self.assertTrue(song.length == None)

	def test_is_time_valid_should_raise_type_error(self):
		time = '1:32:15:23'
		exc = None

		try:
			Song.is_time_valid(time)
		except TypeError as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_is_time_valid_with_negative_values(self):
		time1 = '-1:32'
		time2 = 'a:b'
		
		exc1 = None
		exc2 = None

		try:
			Song.is_time_valid(time1)
		except TypeError as err:
			exc1 = err

		try:
			Song.is_time_valid(time2)
		except TypeError as err:
			exc2 = err
		
		self.assertIsNotNone(exc2)
		self.assertIsNotNone(exc2)
if __name__ == '__main__':
	unittest.main()