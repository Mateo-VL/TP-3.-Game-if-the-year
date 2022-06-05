import mapping
import human
import actions
import player
import items         #cambiar los imports para entrega final
#from src.templates.oop.human import Human
#from src.templates.oop.items import Item
#import src.templates.oop.actions as actions


ROWS = 25
COLUMNS = 80
DUNGEON = mapping.Dungeon(ROWS, COLUMNS)   #pedir parametros para ver longitud y ver que no pase limites
PLAYER = human.Human('Mateo', DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_UP))
GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]

SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.find_free_tile())
AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())

rows= DUNGEON.rows
columns= DUNGEON.columns

if __name__ == "__main__":
   
    game = True 
    DUNGEON.add_item(PICKAXE, 1, PICKAXE.loc())
    DUNGEON.add_item(SWORD, 1, SWORD.loc())
    DUNGEON.add_item(AMULET, 3, AMULET.loc())
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level)

    turns=0
    while game and PLAYER.alive==True:
        turns +=1
        
        game = actions.use_turn(PLAYER, GNOMES[DUNGEON.level], DUNGEON, game)
        PLAYER.pickup(DUNGEON.get_items(PLAYER.loc()))      
        DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level)
    if PLAYER.treasure == True:
        print("You won in {} turns".format(turns))
    else:
        print("You lost in {} turns".format(turns))