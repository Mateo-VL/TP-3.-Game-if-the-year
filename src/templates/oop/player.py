from __future__ import annotations


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
    
    #def movements(character, dungeon: mapa.Dungeon, letter: str) -> None:
        #while character[dungeon.level].alive == True:
            #list_number=[1,2,3,4]
            #random_num= random.choice(list_number)
            #if letter == "w":
                # actions.move_up(dungeon, character)
           # elif letter == "a":
           #      actions.move_left(dungeon, character)
           # elif letter == "s":
          #       actions.move_down(dungeon, character)
          #  elif letter == "d":
           #      actions.move_right(dungeon, character)
        
#ver q pico este en ubicacion alcanzable. disponible desde nivel 1?
import random 

class Gnome(Player):
    def __init__(self, name,  xy):
        super().__init__(name, xy, 1)
        #self.name= name
        #self.x, self.y = xy
        self.alive= True
        self.face = "G"
        self.tool= False  #lo agregué

    def kill(self):
        self.hp = 0
        self.alive = False
        self.face= "%"


    def get_face(self):
        return self.face


""""
    def gnome_movement(gnomes : List[Gnome], dungeon: mapa.Dungeon) -> None:
        while gnomes[dungeon.level].alive == True:
            list_number=[1,2,3,4]
            random_num= random.choice(list_number)
            if random_num==1:
                actions.move_up(dungeon, gnomes[dungeon.level])
            elif random_num==2:
                actions.move_left(dungeon, gnomes[dungeon.level])
            elif random_num==3:
                actions.move_down(dungeon, gnomes[dungeon.level], rows)
            elif random_num==4:
                actions.move_right(dungeon, gnomes[dungeon.level], columns)
            return

def gnome_movement():
    list_number=[1,2,3,4]
    random_num= random.choice(list_number)
    if random_num==1:
        actions.

"""
