import random

class Character:

    def __init__(self,name,description,current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs

    def __str__(self):
        return str((str(self.name) +" : " + str(self.description)))

    def move(self):
        move = random.choice([True, False])
        
        if not move:
            return False
        
        rooms = self.current_room.exits.values()
        
        if not rooms:
            return False 
        
        new_room = random.choice(rooms)
        self.current_room = new_room
        return True
    
    def get_msg(self):
        if not self.msgs:
            return " {self.name} n'a rien a vous dire "
        msg = self.msgs.pop(0)
        self.append.msgs(msg)
        return msg