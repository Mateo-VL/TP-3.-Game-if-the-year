#!/usr/bin/env python3

from regex import P
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
DUNGEON = mapa.Dungeon(ROWS, COLUMNS)   #pedir parametros para ver longitud y ver que no pase limites
PLAYER = human.Human('Mateo', DUNGEON.find_free_tile())
GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]

SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.find_free_tile())
AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())

rows= DUNGEON.rows
columns= DUNGEON.columns
def insameplace(player, gnome):

    if player.loc()== gnome.loc():   #ver que con 2do gnomo no hay ataque
            if player.has_sword()== True:
            #actions.attack()
                gnome.kill()
            else:
                player.hp -=1 
def movements(character, dungeon: mapa.Dungeon, letter: str) -> None:
        #while character[dungeon.level].alive == True:
            #list_number=[1,2,3,4]
            #random_num= random.choice(list_number)
            if letter == "w":
                 actions.move_up(dungeon, character)
            elif letter == "a":
                 actions.move_left(dungeon, character)
            elif letter == "s":
                 actions.move_down(dungeon, character)
            elif letter == "d":
                 actions.move_right(dungeon, character)
if __name__ == "__main__":
   
    game = True 
    DUNGEON.add_item(PICKAXE, 1, PICKAXE.loc())   #ya imprime mapa  #podemos hacer random
    DUNGEON.add_item(SWORD, 1, SWORD.loc())
    DUNGEON.add_item(AMULET, 3, AMULET.loc())
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level])

    turns=0
    while game and PLAYER.alive==True:  #MATEO.alive?
        turns +=1
        key = msvcrt.getch()
        letter= key
        movements(PLAYER, DUNGEON, letter)
        insameplace(PLAYER, GNOMES[DUNGEON.level])

        list_letters=["w", "a", "s", "d"]
        gnome_movement= random.choice(list_letters)
        movements(GNOMES[DUNGEON.level], DUNGEON, gnome_movement)
        insameplace(PLAYER, GNOMES[DUNGEON.level])
        actions.pickup(DUNGEON, PLAYER, PICKAXE, SWORD, AMULET)
    #DUNGEON.add_item(GNOME, 1, GNOME.loc())
        DUNGEON.get_items(PLAYER.loc()) 
        DUNGEON.dig(PLAYER.loc())
        
    
    if DUNGEON.level < 2:
        stair_down = DUNGEON.dungeon[DUNGEON.level].index(mapa.STAIR_DOWN)
    stair_up = DUNGEON.dungeon[DUNGEON.level].index(mapa.STAIR_UP)
    #if MATEO.loc() == DUNGEON.dungeon[DUNGEON.level].index(stair_down):
    
    if PLAYER.loc()== stair_down:
        DUNGEON.level += 1
        #MATEO.loc()== 
        GNOMES[DUNGEON.level].loc()== DUNGEON.find_free_tile()  #gnomo aparece en cada nivel 
        #GNOME.loc()== DUNGEON.level.get_random_location()
    if PLAYER.loc() == stair_up:
        if DUNGEON.level == 0:
           
            if PLAYER.treasure== True:
                print("Congratulations! You accomplished with the mision.")
            else:
                print("The game ended. You abandoned the mission")
            capo = False

            
        else:
            DUNGEON.level -= 1   
    
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level])

        
    # initial parameters
    #level = 0
    

    # initial locations may be random generated
    #gnomes =

    #dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

   # turns = 0
    #while dungeon.level >= 0:
        #turns += 1
        # render map
        #dungeon.render()

        # read key
       # key = 

        # Hacer algo con keys:
        # move player and/or gnomes

    # Salió del loop principal, termina el juego


   