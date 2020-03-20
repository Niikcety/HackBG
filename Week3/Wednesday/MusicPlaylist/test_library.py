import unittest
from library import Song, Playlist

class TestSong(unittest.TestCase):
	def test_initialization_without_parameters(self):
		s = Song()

		self.assertTrue(s.title == "No title")
		self.assertTrue(s.artist == "No artist")
		self.assertTrue(s.album == "No album")
		self.assertTrue(s.length == "0:0:0")

	def test_initialization_with_parameters(self):
		s = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")

		self.assertTrue(s.title == "Odin")
		self.assertTrue(s.artist == "Manowar")
		self.assertTrue(s.album == "The sons of Odin")
		self.assertTrue(s.length == "3:44")

	def test_str_method(self):
		s = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")

		self.assertTrue(str(s) == 'Manowar - Odin from The sons of Odin - 3:44')

	def test_eq_method(self):
		s1 = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")
		s2 = Song(title = "Overture to Odin", artist = "Manowar", album = "The sons of Odin", length = "3:42")
		s3 = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")

		self.assertTrue(s1 == s3)
		self.assertFalse(s1 == s2)

	def test_hash_method(self):
		s1 = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")
		s2 = Song(title = "Overture to Odin", artist = "Manowar", album = "The sons of Odin", length = "3:42")
		s3 = Song(title = "Odin", artist = "Manowar", album = "The sons of Odin", length = "3:44")

		self.assertTrue(s1.__hash__() == s1.__hash__())
		self.assertTrue(s1.__hash__() == s3.__hash__())
		self.assertFalse(s1.__hash__() == s2.__hash__())

class TestPlaylist(unittest.TestCase):
	def test_add_song_with_not_song_instance_should_raise_error(self):
		playlist = Playlist()
		exc = None

		try:
			playlist.add_song('song')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_if_song_is_added(self):
		playlist = Playlist()
		song = Song()

		playlist.add_song(song)

		self.assertTrue(song in playlist.songs)

	def test_trying_to_delete_song_that_is_not_instance_of_song_class(self):
		playlist = Playlist()
		exc = None

		try:
			playlist.remove_song('song')
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_add_songs_adding_not_a_list_should_raise_error(self):
		playlist = Playlist()
		exc = None

		try:
			playlist.add_songs(('song1','song2'))
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_count_songs_of_an_artist(self):
		playlist = Playlist()
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		playlist.add_song(Song(artist = "Someone1", title = "Something2"))
		playlist.add_song(Song(artist = "Someone1", title = "Something3"))
		playlist.add_song(Song(artist = "Someone1", title = "Something4"))

		self.assertTrue(playlist.count_songs_of_an_artist("Someone1") == 4)

	def test_artists(self):
		playlist = Playlist()
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		playlist.add_song(Song(artist = "Someone1", title = "Something2"))
		playlist.add_song(Song(artist = "Someone2", title = "Something3"))
		playlist.add_song(Song(artist = "Someone3", title = "Something4"))


		self.assertTrue({'Someone1': 2, 'Someone2': 1, 'Someone3': 1} == playlist.artists())


if __name__ == '__main__':
	unittest.main()