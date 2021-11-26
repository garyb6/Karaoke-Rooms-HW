import unittest 

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("stolen dance", "milky chance")

    def test_song_has_title(self):
        self.assertEqual("stolen dance", self.song.title) 
    
    def test_song_has_artist(self):
        self.assertEqual("milky chance", self.song.artist) 