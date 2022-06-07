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
    rows = dungeon.get_rows()
    cols = dungeon.get_columns()
    
    if key == b'e':
        game = False
        return game
    
    new_location = _get_new_location(character, key)
    #gnome_new_location = _get_new_location(gnome, random.choice(list_letters))
    gnome_new_location = gnome.loc()
    
    if dungeon.is_inside_map(new_location):
        _move_to(dungeon, character, new_location)
        attack(character, gnome)
    
    if character.loc() in gnome.search_area(rows, cols):
        gnome_new_location = gnome_gets_angry(gnome, character, dungeon, rows, cols)
        
    if dungeon.is_inside_map(gnome_new_location):
        _move_to(dungeon, gnome, gnome_new_location)
        attack(gnome, character)
        
    
    if dungeon.level < 2 and character.loc() == dungeon.dungeon[dungeon.level].index(mapping.STAIR_DOWN):
        descend_stair(dungeon, character)
    
    elif character.loc()== dungeon.dungeon[dungeon.level].index(mapping.STAIR_UP):
        game = climb_stair(dungeon, character, game)
        
    return game

def _get_new_location(player: player.Player, key: bytes) -> Location:
    """
    The _get_new_location function takes a player and a key as parameters. 
    It returns the new location of the player after moving in the direction specified by key.
    
    :param player:player.Player: Get the current location of the player
    :param key:bytes: Get the key that was pressed
    :return: The new location of the player
    """
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

def gnome_gets_angry(gnome: player.Gnome,player: human.Human, dungeon: mapping.Dungeon, rows, cols) -> Location:
    """
    The gnome_gets_angry function allows the gnome to move towards the player if the player is 
    within detection range of the gnome.
    
    :param gnome:player.Gnome: Access the gnome's location
    :param dungeon:mapping.Dungeon: Access the dungeon's map
    :return: the location the gnome would move to.
    """
    new_location = dungeon.get_path(gnome.search_area(rows, cols),player.loc(), gnome.loc())
    return new_location

                 
def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(player: human.Human, gnome: player.Gnome): # completar
    """
    The attack function allows the player to attack a gnome if they are in the same location.
    The function takes two parameters, player and gnome. The function checks if the player is in 
    the same location as a gnome, and then allows for damage to be done to that specific 
    gnome.
    
    :param player:human.Human: Access the player's location and damage
    :param gnome:player.Gnome: Access the gnome's location and damage functions
    :return: A boolean value
    """
    if player.loc()== gnome.loc(): 
            gnome.take_damage(player.damage())
            player.take_damage(gnome.damage())

def _move_to (dungeon: mapping.Dungeon, player: player.Player, location: Location):
    """
    Moves the player to a new location. If the location is walkable, then it moves the player there. 
    Otherwise, if they have a tool in their inventory, it allows them to move there anyway.
    
    :param dungeon:mapping.Dungeon: Check if the location is walkable
    :param player:player.Player: Access the player's current location
    :param location:Location: Determine the location of the player
    :return: None

    """
    if dungeon.is_walkable(location):
        player.move_to(location)
        
    elif dungeon.is_walkable(location)== False and player.tool== True:
        player.move_to(location)
        dungeon.dig(location)

def _move_up (player: player.Player) -> Location:
        """
        Moves the player up one space on the grid.
        
        :param player:player.Player: Pass the player object to the function
        :return: The new location of the player after moving up
    
        """
        return player.loc()[0], player.loc()[1]-1

def _move_down (player: player.Player) -> Location: 
    """    
    Moves the player down one space on the grid.
        
    :param player:player.Player: Pass the player object to the function
    :return: The new location of the player after moving up"""
    return player.loc()[0], player.loc()[1] + 1

def _move_left(player: player.Player) -> Location:
    """  
    Moves the player to left one space on the grid.
        
    :param player:player.Player: Pass the player object to the function
    :return: The new location of the player after moving up
    """
    return player.loc()[0] - 1, player.loc()[1]

def _move_right(player: player.Player) -> Location:
    """
    Moves the player right one space on the grid.
        
    :param player:player.Player: Pass the player object to the function
    :return: The new location of the player after moving up
    """
    return player.loc()[0] + 1, player.loc()[1]

def climb_stair(dungeon: mapping.Dungeon, human: human.Human, game: bool) -> bool:
    """
    The descend_stair function moves the player down one level in the dungeon.
    
    :param dungeon:mapping.Dungeon: Access the dungeon's level.
    :param human:human.Human: Refer to the human object that is created in the main function.
    :return: where player appears in other level.
    """
    if dungeon.level == 0:         
        game = False 
        return game
    else:
        dungeon.level -= 1
        human.move_to(dungeon.dungeon[dungeon.level].index(mapping.STAIR_DOWN)) 
    return game

def descend_stair(dungeon: mapping.Dungeon, human: human.Human) -> bool:
    """
    The descend_stair function moves the player down one level in the dungeon.
    
    :param dungeon:mapping.Dungeon: Access the dungeon's level.
    :param human:human.Human: Refer to the human object that is created in the main function.
    """
    dungeon.level += 1
    human.move_to(dungeon.dungeon[dungeon.level].index(mapping.STAIR_UP))

    