from __future__ import annotations
import random

class Player:
    def __init__(self, name, xy, hit_points=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points

    def loc(self):
        return self.x, self.y 

    def move_to(self, xy):
        self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
    
    def kill(self):
        self.hp = 0
        self.alive = False
    
    def get_state(self):
        return self.alive
    
    def take_damage(self, damage: float) -> None:
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
    

class Gnome(Player):
    def __init__(self, name,  xy):
        super().__init__(name, xy, 50)
        self.alive= True
        self.face = "G"
        self.tool= False  #lo agregué

    def damage(self):
        if self.alive:
            return random.random() * 10 + 1
        return 0
    
    def kill(self):
        super().kill()
        self.face = "%"

    def get_face(self):
        return self.face
    
    

