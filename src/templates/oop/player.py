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

#ver q pico este en ubicacion alcanzable. disponible desde nivel 1?
import random 

class Gnome(Player):
    def __init__(self, name,  xy):
        super().__init__(name, xy, 1)
        #self.name= name
        #self.x, self.y = xy
        self.alive= True
        self.face = "G"
        self.tool= False  

    def get_face(self):
        return self.face
"""
def gnome_movement():
    list_number=[1,2,3,4]
    random_num= random.choice(list_number)
    if random_num==1:
        actions.

"""
