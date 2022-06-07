import mapping
import human
import actions
import player
<<<<<<< HEAD
import items         #cambiar los imports para entrega final
=======
import items         


>>>>>>> dr

if __name__ == "__main__":
    """
    Principal function that runs the game.
    """
    ROWS = 25
    COLUMNS = 80
    DUNGEON = mapping.Dungeon(ROWS, COLUMNS)   
    PLAYER = human.Human(DUNGEON.dungeon[DUNGEON.level].index(mapping.STAIR_UP))
    GNOMES = [player.Gnome('Gnome', DUNGEON.find_free_tile()) for _ in range(len(DUNGEON.dungeon))]
    
    SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.dungeon[1].find_free_tile())
    AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())
    PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())
    game = True 
    DUNGEON.add_item(PICKAXE, 1)
    DUNGEON.add_item(SWORD, 2, SWORD.loc())
    DUNGEON.add_item(AMULET, 3, AMULET.loc())
    turns=0
    DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level, turns)
    while game and PLAYER.alive==True:
        turns +=1
        game = actions.use_turn(PLAYER, GNOMES[DUNGEON.level], DUNGEON, game)
        PLAYER.pickup(DUNGEON.get_items(PLAYER.loc()))      
        DUNGEON.render(PLAYER, GNOMES[DUNGEON.level], DUNGEON.level, turns)
    if PLAYER.treasure == True:
        print('CONGRATULATIONS ', PLAYER, ', YOU HAVE FOUND THE TREASURE')
    else:
        print('YOU LOST', PLAYER, 'BETTER LUCK NEXT TIME')


