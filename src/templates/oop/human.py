import random
from items import Item, Sword, Amulet, PickAxe
from player import Player
from typing import List, Tuple

Location = Tuple[int, int]

class Human(Player):
    def __init__(self, name: str, xy):
        super().__init__(name, xy, 50)
        self.weapon = None
        self.treasure = None
        self.tool = None
        self.alive = True
        self.face = '@'  

    def get_face(self):
        return self.face

    def take_object(self, list_items: List [Item]):
        for i in list_items:
            if i.type == "weapon":
                self.weapon= True
            elif i.type== "treasure":
                self.treasure= True
            elif i.type== "tool":
                self.tool= True
    
    def pickup(self, items: List[Item]):
        for item in items:
            if isinstance(item, Sword):
                self.weapon = item
            elif isinstance(item, Amulet):
                self.treasure = True
            elif isinstance(item, PickAxe):
                self.tool = True

    def damage(self):
        if self.weapon:
            return random.random() * 20 + 5
        return random.random() * 10 + 1      

    def has_sword(self):
        return self.weapon

