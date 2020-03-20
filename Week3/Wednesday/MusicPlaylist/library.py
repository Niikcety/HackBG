from utils import is_length_valid, length_to_seconds, length_to_minutes, length_to_hours
import random
import json


class Song:
    def __init__(self, title="Not stated", artist="Not stated", album="Not stated", length="0:0:0"):
        self.title = title
        self.artist = artist
        self.album = album
        if is_length_valid(length):
            self.length = length

    def __str__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __repr__(self):
        return f'{self.artist} - {self.title} from {self.album} - {self.length}'

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self.length == other.length

    def __hash__(self):
        return hash((self.title, self.artist, self.album, self.length))

    def length(seconds=None, minutes=None, hours=None):
        if seconds == None and minutes == None and hours == None:
            return self.length
        if seconds == True:
            return utils.length_to_seconds(self.length)
        elif minutes == True:
            return utils.length_to_minutes(self.length)
        else:
            return utils.length_to_hours(self.length)


class Playlist:
    def __init__(self, name=None, repeat=True, shuffle=True, songs=[], not_played_songs=[], queue=0):
        number = 1

        if name == None:
            self.name = "Auto generated playlist #" + str(number)
            number += 1
        else:
            self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.songs = songs
        self.not_played_songs = not_played_songs
        self.queue = queue



    def add_song(self, song):
        if isinstance(song, Song):
            self.songs.append(song)
            self.not_played_songs.append(song)
        else:
            raise Exception('Argument is not instance of the Song class')

    def remove_song(self, song):
        if isinstance(song, Song):
            self.songs.remove(song)
        else:
            raise Exception('Argument is not instance of the Song class')

    def add_songs(self, songs):
        if not isinstance(songs, list):
            raise Exceptions('Given argument is not a list')
        elif songs == []:
        	self.songs = []
        	self.not_played_songs = []
        else:
            for song in songs:
                self.add_song(song)

    def count_songs_of_an_artist(self, artist):
        counter = 0
        for song in self.songs:
            if song.artist == artist:
                counter += 1
        return counter

    def artists(self):
        artists = {}
        for song in self.songs:
            artists[song.artist] = self.count_songs_of_an_artist(song.artist)

        return artists

    def total_length(self):
        seconds = 0
        for song in self.songs:
            seconds += song.length_to_seconds()
        return from_seconds_to_string(seconds)

    def __getitem__(self, index):
        return self.songs[index]

    def next_song(self):
        if self.repeat == True and self.shuffle == False:
            if self.queue == len(self.songs) - 1:
                self.queue = 0
                return self.songs[len(self.songs) - 1]
            else:
                self.queue += 1
                return self.songs[self.queue - 1]
        elif self.repeat == False and self.shuffle == False:
            self.queue += 1
            return self.songs[self.queue - 1]
        elif self.repeat == False and self.shuffle == True:
            chosen = random.choice(self.not_played_songs)
            self.not_played_songs.remove(chosen)
            return chosen
        else:
            if self.not_played_songs == []:
                self.not_played_songs = self.songs[::]
            chosen = random.choice(self.not_played_songs)
            self.not_played_songs.remove(chosen)

        return chosen

    
    def from_list_to_list_of_ditionaries(self,lst):
        dicti = []
        for i in lst:
            dicti.append(i.__dict__)

        return dicti

    def save(self):
        self.__dict__['songs'] = self.from_list_to_list_of_ditionaries(self.songs)
        self.__dict__['not_played_songs'] = self.from_list_to_list_of_ditionaries(self.not_played_songs)
        
        splitted_name = self.name.split(' ')
        new_name = '-'.join(splitted_name)
        new_name += '.json'

        with open(new_name,'w') as f:
        	json.dump(self.__dict__, f)

    @classmethod
    def load(cls, path):
    	with open(path, 'r') as f:
    		dicti = json.load(f)
    	
    	not_played_songs = []
    	songs = []
    	for i in dicti['songs']:
    		songs.append(Song(i['title'],i['artist'],i['album'],i['length']))
    	for i in dicti['not_played_songs']:
    		not_played_songs.append(Song(i['title'],i['artist'],i['album'],i['length']))

    	return cls(dicti['name'],dicti['repeat'],dicti['shuffle'],songs,not_played_songs,dicti['queue'])
