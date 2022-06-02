from typing import Union, Tuple

import src.templates.oop.mapping as mapping
import src.templates.oop.player as player 
import src.templates.oop.items as items  #lo importo
import msvcrt

numeric = Union[int, float]
key = msvcrt.getch()

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
def move_to(dungeon: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    # completar
    if dungeon.is_walkable(location):
        player.move_to(location)
    #raise NotImplementedError
    elif dungeon.is_walkable(location)== False and player.tool== True:
        player.move_to(location)
        dungeon.dig(location)

def move_up(dungeon: mapping.Dungeon, player: player.Player):
    #if dungeon.is_walkable([player.x, player.y-1]) or player.tool==True:   # con pico atraviese pared. Ver de que desaparezca
    if player.y>0:  #no pasar limite
        move_to(dungeon, player, [player.x, player.y -1])
            #player.move_to((player.x, player.y - 1))
    
def move_down(dungeon: mapping.Dungeon, player: player.Player):  #recibe cant de filas
    #if dungeon.is_walkable([player.x, player.y+1]) or player.tool==True:
    if player.y< dungeon.get_rows() -1:    #objeto.valor
        move_to(dungeon, player,[player.x, player.y +1])
    #llamar a dig

def move_left(dungeon: mapping.Dungeon, player: player.Player):
    #if dungeon.is_walkable([player.x - 1, player.y]) or player.tool==True:
    if player.x>0:
        move_to(dungeon, player,[player.x - 1, player.y])

def move_right(dungeon: mapping.Dungeon, player: player.Player):  #recibe cant de columnas
    #if dungeon.is_walkable([player.x + 1, player.y]) or player.tool==True:
    if player.x< dungeon.get_columns() -1:
        move_to(dungeon, player,[player.x + 1, player.y])

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player, pickaxe: items.PickAxe, sword: items.Sword, amulet: items.Amulet):
    # completar
    if player.loc()== pickaxe.loc():
        player.tool= True
    elif player.loc()== sword.loc():
        player.weapon= True
    elif player.loc()== amulet.loc():
        player.treasure= True
    



#def gnome_action(dungeon: mapping.Dungeon, player: player.Player):
    #random entre lugares disponibles