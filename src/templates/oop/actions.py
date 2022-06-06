from typing import Union, Tuple

import human
import mapping
import player 
import msvcrt
import random
import human

numeric = Union[int, float]
Location = Tuple[int, int]


def use_turn(character: human.Human, gnome:player.Gnome, dungeon: mapping.Dungeon, game: bool) -> bool:
    key = msvcrt.getch()
    list_letters=[b"w", b"a", b"s", b"d"]
    
    if key == b'e':
        game = False
        return game
    gnome_new_location = _get_new_location(gnome, random.choice(list_letters))
    new_location = _get_new_location(character, key)
    if dungeon.is_inside_map(new_location):
        _move_to(dungeon, character, new_location)
        attack(character, gnome)
    
    if dungeon.is_inside_map(gnome_new_location):
        _move_to(dungeon, gnome, gnome_new_location)
        attack(gnome, character)
    
    if dungeon.level < 2 and character.loc() == dungeon.dungeon[dungeon.level].index(mapping.STAIR_DOWN):
        descend_stair(dungeon, character)
    
    elif character.loc()== dungeon.dungeon[dungeon.level].index(mapping.STAIR_UP):
        game = climb_stair(dungeon, character, game)
        
    return game

def _get_new_location(player: player.Player, key: bytes) -> Location:
    new_location = player.loc()
    if player.get_state():
        if key == b"w":
            new_location= _move_up(player)
        elif key == b"a":
            new_location= _move_left(player)
        elif key == b"s":
            new_location= _move_down(player)
        elif key == b"d":
            new_location= _move_right(player)
    return new_location

                 
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

def _move_to (dungeon: mapping.Dungeon, player: player.Player, location: Location):
    if dungeon.is_walkable(location):
        player.move_to(location)
        
    elif dungeon.is_walkable(location)== False and player.tool== True:
        player.move_to(location)
        dungeon.dig(location)

def _move_up (player: player.Player) -> Location:
        return player.loc()[0], player.loc()[1]-1

def _move_down (player: player.Player) -> Location: 
        return player.loc()[0], player.loc()[1] + 1

def _move_left(player: player.Player) -> Location:
    return player.loc()[0] - 1, player.loc()[1]

def _move_right(player: player.Player) -> Location:
    return player.loc()[0] + 1, player.loc()[1]

def climb_stair(dungeon: mapping.Dungeon, human: human.Human, game: bool) -> bool:
    if dungeon.level == 0:         
        game = False 
        return game
    else:
        dungeon.level -= 1
        human.move_to(dungeon.dungeon[dungeon.level].index(mapping.STAIR_DOWN)) 
    return game

def descend_stair(dungeon: mapping.Dungeon, human: human.Human) -> bool:
    dungeon.level += 1
    human.move_to(dungeon.dungeon[dungeon.level].index(mapping.STAIR_UP))

    