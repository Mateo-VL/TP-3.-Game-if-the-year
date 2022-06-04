from typing import Union, Tuple

import human
import mapping
import player 
import items  #lo importo
import msvcrt

numeric = Union[int, float]
key = msvcrt.getch()


def do_something(character: player.Player, dungeon: mapping.Dungeon, letter: bytes) -> None:
    if character.get_state():
            if letter == b"w":
                move_up(dungeon, character)
            elif letter == b"a":
                move_left(dungeon, character)
            elif letter == b"s":
                move_down(dungeon, character)
            elif letter == b"d":
                move_right(dungeon, character)
                 
def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(player: human.Human, gnome: player.Gnome): # completar
    if player.loc()== gnome.loc(): 
            damage = player.damage()
            gnome.take_damage(damage)
            player.take_damage(gnome.damage())

def move_to (dungeon: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    if dungeon.is_walkable(location):
        player.move_to(location)
        
    elif dungeon.is_walkable(location)== False and player.tool== True:
        player.move_to(location)
        dungeon.dig(location)

def move_up (dungeon: mapping.Dungeon, player: player.Player):
    if player.y>0:
        move_to(dungeon, player, [player.x, player.y -1])

def move_down (dungeon: mapping.Dungeon, player: player.Player): 
    if player.y< dungeon.get_rows() -1:
        move_to(dungeon, player,[player.x, player.y +1])

def move_left(dungeon: mapping.Dungeon, player: player.Player):
    if player.x>0:
        move_to(dungeon, player,[player.x - 1, player.y])

def move_right(dungeon: mapping.Dungeon, player: player.Player):
    if player.x< dungeon.get_columns() -1:
        move_to(dungeon, player,[player.x + 1, player.y])

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player, pickaxe: items.PickAxe, sword: items.Sword, amulet: items.Amulet):
    if player.loc()== pickaxe.loc():
        player.tool= True
    elif player.loc()== sword.loc():
        player.weapon= True
    elif player.loc()== amulet.loc():
        player.treasure= True
    return
    
