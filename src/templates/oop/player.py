from __future__ import annotations
import random
from typing import Tuple, List

class Player:
    def __init__(self, name, xy, hit_points=50):
        self.name = name
        self.x, self.y = xy
        self.hp = hit_points
        self.max_hp = hit_points
        self.search_range = 3

    def loc(self):
        """Return the location of character"""
        return self.x, self.y 

    def move_to(self, xy):
        """Set the new location of the character."""
        self.x, self.y = xy

    def __str__(self):
        """Retrun character name. """
        return self.name

    def __repr__(self):
        """Return character name, location and hit points."""
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
     
    def show_items(self):
        """Return state of the objects."""
        return f"Tool: {self.tool}     Weapon: {self.weapon}     Treasure: {self.treasure}"

    def get_hp(self):
        """Return the remaining life."""
        return self.hp
    
    def kill(self):
        """Set player is death, if there is no remaining life."""
        self.hp = 0
        self.alive = False
    
    def get_state(self):
        """The get_state function returns the state of the game. """
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
        self.tool= False  

    def damage(self):
        """
        The damage function takes a character as an argument and returns the amount of damage that character has. 
        If the character is dead, it returns 0.
        """
        if self.alive:
            return random.random() * 10 + 1
        return 0
    
    def kill(self):
        """
        If there is no remining hp, gnome is death. Gnome face change.
        """
        super().kill()
        self.face = "%"

    def get_face(self):
        """
        Returns the face of the gnome.
        """
        return self.face
    
    def search_area(self, rows: int, columns: int) -> List[Tuple[int, int]]:
        detection_area = []
        for x in range(self.x - self.search_range, self.x + self.search_range + 1):
            if not (x < 1 or x > columns - 1):
                for y in range(self.y - self.search_range, self.y + self.search_range + 1):
                    if not (y < 1 or y > rows - 1):
                        detection_area.append((x, y))
        return detection_area
    

