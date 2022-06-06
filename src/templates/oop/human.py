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
        """
        Return player face.
        """
        return self.face


    
    def pickup(self, items: List[Item]):
        """Player grabs the object from where is stand over."""
        for item in items:
            if isinstance(item, Sword):
                self.weapon = item
            elif isinstance(item, Amulet):
                self.treasure = True
            elif isinstance(item, PickAxe):
                self.tool = True

    def damage(self):
        """
        Return a damage value that player cause.
        """
        if self.weapon:
            return random.random() * 20 + 5
        return random.random() * 10 + 1      

    def has_sword(self):
        """
        Return if player has the sword.
        """
        return self.weapon

