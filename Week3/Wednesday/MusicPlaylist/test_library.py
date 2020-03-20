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

				# Case of next_song method
				# 1 - Repeat = True and Shuffle = False
				# 2 - Repeat = False and Shuffle = False
				# 3 - repeat = False and shuffle = True
				# 4 - repeat = True and shuffle = True

	def test_next_song_in_case_one_with_not_empty_list(self):
		playlist = Playlist(repeat = True, shuffle = False)
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		playlist.add_song(Song(artist = "Someone1", title = "Something2"))
				# first next_song should return first song
				# second next_song should return third song
				# third should return first song

				
		self.assertTrue(playlist.next_song() == Song(artist = "Someone1", title = "Something1"))
		self.assertTrue(playlist.next_song() == Song(artist = "Someone1", title = "Something2"))
		self.assertTrue(playlist.next_song() == Song(artist = "Someone1", title = "Something1"))

	def test_next_song_in_case_two_with_not_empty_list(self):
		playlist = Playlist(repeat = False, shuffle = False)
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		playlist.add_song(Song(artist = "Someone1", title = "Something2"))
		exc = None
				# first next_song should return first song
				# second next_song should return third song
				# third should raise error

		self.assertTrue(playlist.next_song() == Song(artist = "Someone1", title = "Something1"))
		self.assertTrue(playlist.next_song() == Song(artist = "Someone1", title = "Something2"))
		try:
			playlist.next_song()
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)
		
	def test_next_song_in_case_three_with_not_empty_list(self):
		playlist = Playlist(repeat = False, shuffle = True)
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		exc = None

		self.assertTrue(isinstance(playlist.next_song(),Song))

		try:
			playlist.next_song()
		except Exception as err:
			exc = err

		self.assertIsNotNone(exc)

	def test_next_song_in_case_four_with_not_empty_list(self):
		playlist = Playlist(repeat = True, shuffle = True)
		playlist.add_song(Song(artist = "Someone1", title = "Something1"))
		playlist.add_song(Song(artist = "Someone1", title = "Something2"))

				# after two calls length of playlist.not_played_songs should be zero
				# in the third call length of playlist.not_playes_songs should be 1
				# because list is coppied and one song is played and removed from the list
		
		playlist.next_song()
		playlist.next_song()
		
		self.assertTrue(len(playlist.not_played_songs) == 0)

		playlist.next_song()

		self.assertTrue(len(playlist.not_played_songs) == 1)





if __name__ == '__main__':
	unittest.main()