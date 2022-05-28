import random
from src.templates.oop.player import Player


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

    def take_tool(self):
        self.tool= True
        return self.tool

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

    #def has_sword(self):
        # completar
