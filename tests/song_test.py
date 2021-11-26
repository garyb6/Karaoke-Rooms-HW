import unittest 

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("stolen_dance", "Milky Chance")

    def test_song_has_title(self):
        self.assertEqual("stolen_dance", self.song.title) 