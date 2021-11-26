class Room:

    def __init__(self, name, capacity):
        self.name = name 
        self.guest_list = []
        self.playlist = []
        self.capacity = capacity 
        # self.entry_fee = entry_fee