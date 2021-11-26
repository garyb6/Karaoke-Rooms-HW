import unittest 

from src.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Jay Pritchard", 4, 200.00)

    def test_guest_has_name(self):
        self.assertEqual("Jay Pritchard", self.guest.name) 
    
    def test_guest_has_group_size(self):
        self.assertEqual(4, self.guest.group_size) 

    def test_guest_has_wallet(self):
        self.assertEqual(200.00, self.guest.wallet) 