from typing import Union, Tuple


import src.templates.oop.mapping as mapping
<<<<<<< HEAD
import src.templates.oop.player as player
import src.templates.oop.human as human
=======
import src.templates.oop.player as player 

>>>>>>> main

numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


<<<<<<< HEAD
def attack(dungeon, player, ...): # completar xygnomo xyplayer
    # completar
    
    raise NotImplementedError
=======
#def attack(dungeon, player, ...): # completar
    # completar
   # raise NotImplementedError
>>>>>>> main


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    # completar
    raise NotImplementedError


def move_up(dungeon: mapping.Dungeon, player: player.Player):
    player.move_to((player.x, player.y - 1))
    
def move_down(dungeon: mapping.Dungeon, player: player.Player):
    player.move_to((player.x, player.y +1))

def move_left(dungeon: mapping.Dungeon, player: player.Player):
    player.move_to((player.x - 1, player.y))

def move_right(dungeon: mapping.Dungeon, player: player.Player):
    player.move_to((player.x + 1, player.y))

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    if xyplayer ==xyamulet
    raise NotImplementedError



def gnome_action(dungeon: mapping.Dungeon, player: player.Player):
    #random entre lugares disponibles