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
"""
class Gnome(Player):
    def __init__(self, xy):
        super().__init__(name= "Gnome", xy, hit_points= 1)
        self.alive = True
        self.face = 'G'  
#ver linea 120 de mapping
"""