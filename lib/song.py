class Song:

    count = 0

    def __init__(self, name, artist, genres):
        self.add_song_to_count()
        self.name = name
        self.artist = artist
        self.genre = genres

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment
