from typing import Union, Tuple

import human
import mapping
import player 
import items  #lo importo
import msvcrt

numeric = Union[int, float]
Location = Tuple[int, int]

def get_key(character: player.Player, dungeon: mapping.Dungeon, letter: bytes) -> None:
    key = msvcrt.getch()
    move_to(dungeon, character, key)

                 
def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(player: human.Human, gnome: player.Gnome): # completar
    if player.loc()== gnome.loc(): 
            gnome.take_damage(player.damage())
            player.take_damage(gnome.damage())

def move_to (dungeon: mapping.Dungeon, player: player.Player, key: bytes):
    if player.get_state():
            if key == b"w":
                new_location= move_up(dungeon, player)
            elif key == b"a":
                new_location= move_left(dungeon, player)
            elif key == b"s":
                new_location= move_down(dungeon, player)
            elif key == b"d":
                new_location= move_right(dungeon, player)
    if dungeon.is_walkable(new_location):
        player.move_to(new_location)
        
    elif dungeon.is_walkable(new_location)== False and player.tool== True:
        player.move_to(new_location)
        dungeon.dig(new_location)
    else:
        pass

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
    
