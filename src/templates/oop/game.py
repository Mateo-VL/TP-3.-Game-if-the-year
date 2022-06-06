import mapping
import human
import actions
import player
import items         
import hay_camino


if __name__ == "__main__":
    ROWS = 25
    COLUMNS = 80
    DUNGEON = mapping.Dungeon(ROWS, COLUMNS)   #pedir parametros para ver longitud y ver que no pase limites
    PLAYER = human.Human(DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_UP))
    GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]
    
    SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.dungeon[1].find_free_tile())
    AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
    PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())
    game = True 
    DUNGEON.add_item(PICKAXE, 1, PICKAXE.loc())
    DUNGEON.add_item(SWORD, 2, SWORD.loc())
    DUNGEON.add_item(AMULET, 3, AMULET.loc())
    turns=0
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level, turns)
    while game and PLAYER.alive==True:
        turns +=1
        
        game = actions.use_turn(PLAYER, GNOMES[DUNGEON.level], DUNGEON, game)
        PLAYER.pickup(DUNGEON.get_items(PLAYER.loc()))      
        DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level, turns)
        print(DUNGEON.dungeon[DUNGEON.level].are_connected(DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_UP), DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_DOWN)))
    if PLAYER.treasure == True:
        print('CONGRATULATIONS ', PLAYER, ', YOU HAVE FOUND THE TREASURE')
    else:
        print('YOU HAVE BEEN DEFEATED', PLAYER, 'BETTER LUCK NEXT TIME')


