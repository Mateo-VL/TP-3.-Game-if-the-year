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

    def damage(self):
        if self.sword:
            return random.random() * 20 + 5
        return random.random() * 10 + 1

    def kill(self):
        self.hp = 0
        self.alive = False

<<<<<<< Updated upstream
#def has_sword(self):
# completar
=======
    #def has_sword(self):
        # completar
    def has_sword(self):
        self.weapon= True

class Gnome:
    def __init__(self, name, xy):
        super().__init__("Gnome", xy, 1)
        self.alive= True
        self.face= "G"
  
    def get_face(self):
        return self.face
    
    def kill(self):
        self.hp=0
        self.alive= False
#cuando cambie nivel resucita
>>>>>>> Stashed changes
