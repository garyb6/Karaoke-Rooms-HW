class Guest:

    def __init__(self, name, group_size, wallet):
        self.name = name 
        self.group_size = group_size
        self.wallet = wallet  
    
    def get_group_size(self):
        return self.group_size 