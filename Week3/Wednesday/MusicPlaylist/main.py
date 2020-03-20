from library import Song, Playlist

def main():
	playlist = Playlist(repeat = True, shuffle = True)
	playlist.add_song(Song(artist = "Someone1", title = "Something1"))
	playlist.add_song(Song(artist = "Someone1", title = "Something2"))


	code = Playlist.load('Auto-generated-playlist-#1.json')

	print(code.name)
	print(code.next_song())
	print(code.next_song())
	

if __name__ == '__main__':
	main()