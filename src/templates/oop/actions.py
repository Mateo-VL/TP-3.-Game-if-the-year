from typing import Union, Tuple


import src.templates.oop.mapping as mapping
import src.templates.oop.player as player 


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


#def attack(dungeon, player, ...): # completar
    # completar
   # raise NotImplementedError

#locacion= [player.x, player.y]
def move_to(NIVEL: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    # completar
    if NIVEL.is_walkable(location):
        player.move_to(location)
    #raise NotImplementedError
    elif NIVEL.is_walkable(location)== False and player.tool== True: 
        player.move_to(location)
        NIVEL.dig(location)

def move_up(NIVEL: mapping.Dungeon, player: player.Player):
    #if NIVEL.is_walkable([player.x, player.y-1]) or player.tool==True:   # con pico atraviese pared. Ver de que desaparezca
    if player.y>0:  #no pasar limite
        move_to(NIVEL, player, [player.x, player.y -1])
            #player.move_to((player.x, player.y - 1))
    
def move_down(NIVEL: mapping.Dungeon, player: player.Player, rows: int):  #recibe cant de filas
    #if NIVEL.is_walkable([player.x, player.y+1]) or player.tool==True:
    if player.y< rows -1:    #objeto.valor
        move_to(NIVEL, player,(player.x, player.y +1))
    #llamar a dig

def move_left(NIVEL: mapping.Dungeon, player: player.Player):
    #if NIVEL.is_walkable([player.x - 1, player.y]) or player.tool==True:
    if player.x>0:
        move_to(NIVEL, player,(player.x - 1, player.y))

def move_right(NIVEL: mapping.Dungeon, player: player.Player, columns: int):  #recibe cant de columnas
    #if NIVEL.is_walkable([player.x + 1, player.y]) or player.tool==True:
    if player.x< columns -1:
        move_to(NIVEL, player,(player.x + 1, player.y))

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    
    raise NotImplementedError



#def gnome_action(dungeon: mapping.Dungeon, player: player.Player):
    #random entre lugares disponibles