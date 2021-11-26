import unittest 

from src.room import Room
from src.guest import Guest 

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Jay Pritchard", 4, 200.00)
        self.guest2 = Guest("Cameron Tucker", 3, 100.00)
        self.room1 = Room("Cheviot", 10)

    def test_room_has_name(self):
        self.assertEqual("Cheviot", self.room1.name) 
    
    def test_room_has_capacity(self):
        self.assertEqual(10, self.room1.capacity) 

    # def test_room_has_entry_fee(self):
    #     self.assertEqual(5, self.room.entry_fee) 

    def test_guest_list_starts_off_empty(self):
        self.assertEqual([], self.room1.guest_list)
    
    def test_playlist_starts_off_empty(self):
        self.assertEqual([], self.room1.playlist)

    def test_can_add_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)
        self.assertEqual(2, len(self.room1.guest_list))

    def test_room_find_guest(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)        
        self.assertEqual(self.guest2, self.room1.find_guest_by_name("Cameron Tucker"))
        self.assertEqual(None, self.room1.find_guest_by_name("Homer Simpson"))

    def test_can_remove_guests(self):
        self.room1.add_guest(self.guest1)
        self.room1.add_guest(self.guest2)  
        self.room1.remove_guest(self.guest2)
        self.assertEqual(1, len(self.room1.guest_list))
        self.assertEqual(False, self.guest2 in self.room1.guest_list)