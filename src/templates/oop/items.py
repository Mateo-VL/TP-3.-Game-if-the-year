from typing import Union


numeric = Union[float, int]


class Item:
    def __init__(self, name, fc, type, xy):
        self.name = name
        self.face = fc
        self.type = type
        self.x, self.y = xy
    
    def loc(self):
        return self.x, self.y 

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Item('{self.name}', '{self.face}')"


class Sword(Item):
    def __init__(self, name: str, fc: str, min_dmg: numeric, max_dmg: numeric, xy):
        super().__init__(name, fc, 'weapon', xy)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        

class Amulet(Item):
    def __init__(self, name: str, fc: str, xy):
        super().__init__(name, fc, 'treasure', xy)


class PickAxe(Item):
    def __init__(self, name: str, fc: str, xy):
        super().__init__(name, fc, 'tool', xy)
