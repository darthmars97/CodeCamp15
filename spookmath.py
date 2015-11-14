"""
This is where the Math/graph numbers should be happening.
"""


class Song(object):
    """docstring for Song"""
    def __init__(self, name, popularity, value):
        super(Song, self).__init__()
        self.name = name
        self.popularity = popularity
        self.value = value

    def pop_formula(self):
        value =



song = Song("Rolling in the deep - Adele", 50, 10)

print song.popularity, song.name, song.value
