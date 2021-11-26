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

    def test_guest_list_starts_off_empty(self):
        self.assertEqual([], self.room.guest_list)
    
    def test_playlist_starts_off_empty(self):
        self.assertEqual([], self.room.playlist)

    def test_can_add_customers(self):
        self.event.add_customer(self.customer)
        self.event.add_customer(self.customer2)
        self.assertEqual(2, len(self.event.customers))