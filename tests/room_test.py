import unittest 

from src.room import Room

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room = Room("Cheviot", 10)

    def test_room_has_name(self):
        self.assertEqual("Cheviot", self.room.name) 
    
    def test_room_has_capacity(self):
        self.assertEqual(10, self.room.capacity) 

    # def test_room_has_entry_fee(self):
    #     self.assertEqual(5, self.room.entry_fee) 