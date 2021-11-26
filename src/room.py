class Room:

    def __init__(self, name, capacity):
        self.name = name 
        self.guest_list = []
        self.playlist = []
        self.capacity = capacity 
        # self.entry_fee = entry_fee

    def add_guest(self, guest):
        self.guest_list.append(guest)
    
    def find_guest_by_name(self, name):
        for guest in self.guest_list:
            if name == guest.name:
                return guest
    
    def remove_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.playlist.append(song)
