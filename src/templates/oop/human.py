import random
from src.templates.oop.items import Item
from src.templates.oop.player import Player
from typing import List


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
            


    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):  #si gnomo= lugar que jugador (y no tienes espada) hp -1.  if hp==0: player.kill
        self.hp = 0
        self.alive = False

    #def has_sword(self):
        # completar
