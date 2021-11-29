class Room:

    def __init__(self, name, capacity, entry_fee):
        self.name = name 
        self.guest_list = []
        self.playlist = []
        self.capacity = capacity 
        self.entry_fee = entry_fee
        self.till = 100.00

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

    def find_song_by_title(self, title):
        for song in self.playlist:
            if title == song.title:
                return song 
    
    def find_song_by_artist(self, artist):
        for song in self.playlist:
            if artist == song.artist:
                return song 
    
    def can_guest_enter_room(self, guest):
        # amount = guest.group_size
        # if amount <= self.capacity:
        #     return True 
        return guest.group_size <= self.capacity
    
    def remaining_capacity(self, guest):
        self.capacity -= guest.group_size
    
    def guest_can_afford_room(self, guest):
        return guest.wallet >= self.entry_fee

    def guest_pays_entry_fee(self, guest):
        if self.can_guest_enter_room(guest) and self.guest_can_afford_room(guest):
            guest.wallet -= self.entry_fee
            self.till += self.entry_fee

    def favourite_song_in_playlist(self, guest, song):
        if guest.favourite_song == song.title:
            return "Whoo!!!"