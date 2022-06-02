#!/usr/bin/env python3

import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
import src.templates.oop.player as player
import src.templates.oop.items as items         #cambiar los imports para entrega final
import msvcrt
from typing import List
import random
#from src.templates.oop.human import Human
#from src.templates.oop.items import Item
#import src.templates.oop.actions as actions


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    DUNGEON = mapa.Dungeon(ROWS, COLUMNS)   #pedir parametros para ver longitud y ver que no pase limites
    PLAYER = human.Human('Mateo', DUNGEON.find_free_tile())
    GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]
    SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.find_free_tile())
    AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
    PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())
    # initial parameters
    level = 0
    

    # initial locations may be random generated
    gnomes =

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    turns = 0
    while dungeon.level >= 0:
        turns += 1
        # render map
        dungeon.render()

        # read key
       # key = 

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego
