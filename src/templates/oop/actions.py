from typing import Union, Tuple

import mapping
import player 
import items  #lo importo
import msvcrt

numeric = Union[int, float]
key = msvcrt.getch()

def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

'''def attack(dungeon, player, ...): # completar
     #completar
    raise NotImplementedError'''

def move_to (dungeon: mapping.Dungeon, player: player.Player, location: Tuple[numeric, numeric]):
    """
    The move_to function moves the player to a new location.
    If the location is walkable, then it moves there.
    Otherwise, if the player has a tool equipped and can break things, then it breaks them and moves there.
    
    :param dungeon:mapping.Dungeon: Access the dungeon map
    :param player:player.Player: Access the player's current location
    :param location:Tuple[numeric: Set the location of the player
    :param numeric]: Determine the location of the player
    :return: The player
    """
    if dungeon.is_walkable(location):
        player.move_to(location)
        
    elif dungeon.is_walkable(location)== False and player.tool== True:
        player.move_to(location)
        dungeon.dig(location)

def move_up (dungeon: mapping.Dungeon, player: player.Player):
    """
    The move_up function moves the player up one space.
    
    
    
    :param dungeon:mapping.Dungeon: Access the dungeon map
    :param player:player.Player: Access the player's y coordinate
    :return: The value of the dungeon tile above the player
    :doc-author: Trelent
    """
    if player.y>0:
        move_to(dungeon, player, [player.x, player.y -1])

def move_down (dungeon: mapping.Dungeon, player: player.Player): 
    """
    The move_down function moves the player down one square.
        Args:
            dungeon (mapping.Dungeon): The dungeon object to move the player in.
            player (player.Player): The Player object to move down.
    
    :param dungeon:mapping.Dungeon: Access the dungeon object
    :param player:player.Player: Access the player's y coordinate
    :return: A new player object with the y position incremented by 1
    :doc-author: Trelent
    """
    if player.y< dungeon.get_rows() -1:
        move_to(dungeon, player,[player.x, player.y +1])

def move_left(dungeon: mapping.Dungeon, player: player.Player):
    """
    The move_left function moves the player left one tile.
    
    
    
    :param dungeon:mapping.Dungeon: Access the dungeon map
    :param player:player.Player: Access the player's x and y coordinates
    :return: The player's new x coordinate
    :doc-author: Trelent
    """
    if player.x>0:
        move_to(dungeon, player,[player.x - 1, player.y])

def move_right(dungeon: mapping.Dungeon, player: player.Player):
    """
    The move_right function moves the player right one column.
    
    
    
    :param dungeon:mapping.Dungeon: Access the dungeon
    :param player:player.Player: Get the player's current position
    :return: The player object
    :doc-author: Trelent
    """
    if player.x< dungeon.get_columns() -1:
        move_to(dungeon, player,[player.x + 1, player.y])

def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):
    # completar
    raise NotImplementedError


def pickup(dungeon: mapping.Dungeon, player: player.Player, pickaxe: items.PickAxe, sword: items.Sword, amulet: items.Amulet):
    """
    The pickup function allows the player to pick up items. If the player is on a tile with an item, it will be added to their inventory.
    
    
    :param dungeon:mapping.Dungeon: Access the dungeon map
    :param player:player.Player: Access the player's inventory
    :param pickaxe:items.PickAxe: Determine if the player is currently in the same location as a pickaxe
    :param sword:items.Sword: Check if the player is on the sword location
    :param amulet:items.Amulet: Check if the player is in the same location as an amulet
    :return: The player's tool, weapon and amulet
    :doc-author: Trelent
    """
    if player.loc()== pickaxe.loc():
        player.tool= True
    elif player.loc()== sword.loc():
        player.weapon= True
    elif player.loc()== amulet.loc():
        player.treasure= True
    return
    
