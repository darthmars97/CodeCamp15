"""
This is where the Math/graph numbers should be happening.
"""
import randomizer

class Song(object):
    """docstring for Song"""
    def __init__(self, name, popularity, value):
        super(Song, self).__init__()
        self.name = name
        self.popularity = popularity
        self.value = value

    def pop_formula(self):
        pass



song1 = Song("Hello - Adele", 25, randomizer.songs['Hello -Adele'])
song2 = Song("Hotline Bling - Drake", 25, randomizer.songs['Hello -Adele'])
song3 = Song("The Hills - The Weeknd", 25, randomizer.songs['Hello -Adele'])
song4 = Song("Sorry - Justin Beiber", 25, randomizer.songs['Hello -Adele'])
song5 = Song("What Do You Mean? - Justin Beiber", 25, randomizer.songs['Hello -Adele'])
song6 = Song("Stiches - Shawn Mendes", 25, randomizer.songs['Hello -Adele'])
song7 = Song("Focus - Ariana Grande", 25, randomizer.songs['Hello -Adele'])
song8 = Song("Wildest Dreams - Taylor Swift", 25, randomizer.songs['Hello -Adele'])
song9 = Song("679 - Fetty Wap", 25, randomizer.songs['Hello -Adele'])
song10 = Song("Like Im Gonna Lose You - Meghan Trainor", 25, randomizer.songs['Hello -Adele'])
song11 = Song("Locked Away - R. City", 25, randomizer.songs['Hello -Adele'])
song12 = Song("Exs & Ohs - Elle King", 25, randomizer.songs['Hello -Adele'])
song13 = Song("Here - Alessia Cara", 25, randomizer.songs['Hello -Adele'])
song14 = Song("Cant Feel My Face - The Weeknd", 25, randomizer.songs['Hello -Adele'])
song15 = Song("Watch Me - Silento", 25, randomizer.songs['Hello -Adele'])
song16 = Song("Jumpman - Drake & Future", 25, randomizer.songs['Hello -Adele'])
song17 = Song("Same Old Love - Selena Gomez", 25, randomizer.songs['Hello -Adele'])
song18 = Song("On My Mind - Ellie Goulding", 25, randomizer.songs['Hello -Adele'])
song19 = Song("Lean On - Major Lazer & DJ Snake", 25, randomizer.songs['Hello -Adele'])
song20 = Song("Renegades - X Ambassadors", 25, randomizer.songs['Hello -Adele'])
song21 = Song("Downtown - Mackelmore", 25, randomizer.songs['Hello -Adele'])
song22 = Song("Hit The Quan - iLoveMemphis", 25, randomizer.songs['Hello -Adele'])
song23 = Song("Tennessee Whiskey - Chris Stapleton", 25, randomizer.songs['Hello -Adele'])
song24 = Song("Trap Queen - Fetty Wap", 25, randomizer.songs['Hello -Adele'])
song25 = Song("Good For You - Selena Gomez", 25, randomizer.songs['Hello -Adele'])
song26 = Song("Drag Me Down - One Direction", 25, randomizer.songs['Hello -Adele'])
song27 = Song("Antidote - Travi$ Scott", 25, randomizer.songs['Hello -Adele'])
song28 = Song("Die A Happy Man - Thomas Rhett", 25, randomizer.songs['Hello -Adele'])
song29 = Song("How Deep Is Your Love - Calvin Harris", 25, randomizer.songs['Hello -Adele'])
song30 = Song("Where Ya At - Future feat Drake", 25, randomizer.songs['Hello -Adele'])


print song1.popularity, song1.name, song1.value
