class Song:
	def __init__(self, title = None, artist = None, album = None, length = '0:0:0'):
		if self.is_time_valid(length):
			self.title = title
			self.artist = artist
			self.album = album
			self.length = length

	@classmethod
	def is_time_valid(cls, time):
		x = time.split(':')
		if len(x) == 2 or len(x) == 3:
			for i in x:
				if not i.isdigit():
					raise TypeError('Negative value / Value different than integers')
		else:
			raise TypeError('Invalid song length')
		


if __name__ == '__main__':
	pass