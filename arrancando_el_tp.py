import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
#import src.templates.oop.player as player
import src.templates.oop.items as items
import msvcrt

DUNGEON = mapa.Dungeon(25, 80)   #pedir parametros para ver longitud y ver que no pase limites
MATEO = human.Human('Mateo', DUNGEON.find_free_tile())

SWORD= items.Sword("Sword", "/", 10, 20, DUNGEON.find_free_tile())

AMULET= items.Amulet("Amulet", '"', DUNGEON.dungeon[2].find_free_tile())

PICKAXE= items.PickAxe("Pickaxe", "(", DUNGEON.find_free_tile())


rows= DUNGEON.rows
columns= DUNGEON.columns
capo = True 
DUNGEON.add_item(PICKAXE, 1, PICKAXE.loc())   #ya imprime mapa  #podemos hacer random
DUNGEON.add_item(SWORD, 1, SWORD.loc())
DUNGEON.add_item(AMULET, 3, AMULET.loc())
DUNGEON.render(MATEO)
while capo:  #MATEO.alive?
    key = msvcrt.getch()
    if key == b'w':
        actions.move_up(DUNGEON, MATEO)
    elif key == b'a':
        actions.move_left(DUNGEON, MATEO)
    elif key == b's':
        actions.move_down(DUNGEON, MATEO, rows)  #recibe cant filas
    elif key == b'd':
        actions.move_right(DUNGEON, MATEO, columns)  #recibe cant columnas
    else:
        capo = False
    #ver
    if MATEO.loc() in DUNGEON.dungeon[DUNGEON.level].items:
        list_items= DUNGEON.dungeon[DUNGEON.level].items[MATEO.loc()]
        MATEO.take_object(list_items)
    
    if MATEO.loc()== PICKAXE.loc():
        MATEO.tool= True
    
    DUNGEON.get_items(MATEO.loc()) 
    DUNGEON.dig(MATEO.loc())
    
    stair_down = DUNGEON.dungeon[DUNGEON.level].index(mapa.STAIR_DOWN)
    stair_up = DUNGEON.dungeon[DUNGEON.level].index(mapa.STAIR_UP)
    if MATEO.loc() == stair_down:
        DUNGEON.level += 1
    
    if MATEO.loc() == stair_up:
        if DUNGEON.level == 0:
            capo = False
        else:
            DUNGEON.level -= 1   
    
    DUNGEON.render(MATEO)


#en nivel 3 apenas se mueve se termina el juego


"""
COSAS POR HACER:
-que cuando regrese al nivel anterior quede el mismo mapa (y que no cree otro nuevo)
- que cuando pase por items cambie estado de objeto = True (ver funcion take_object en human)
-completar funciones para ver si hay camino posible. ver mapping (al menos para el nivel 1, donde hay q fijarse que haya camino entre personaje y pico)
- que se pueda mover en nivel 3 (cuando se apreta tecla se termina el juego, ver error)
-pasar la funcion que se fija la tecla apretada al archivo game. lo mismo con lo de agarrar los items (funcion pick_up en actions)
- hacer que imprima HP del jugador, los turnos, que items tiene, el nivel en el que está.
- ver que hacer si jugador se queda sin vidas restantes.
- hacer funcion has_sword (en human). si está en = posicion que Gnomo, lo mata (y q aparezca nuevamente en siguiente nivel). fijarse que al volver al nivel anterior el gnomo
no aparezca (si se mató antes).
- hacer clase Gnome. que esté en cada nivel. hacer que desaparezca si se mata. Que se mueva con random
- pasar lo de las escaleras a archivo actions
- hacer que si está en una escalera tenga que volver a apretar la tecla para cambiar nivel?
- que imprima mensaje si gana o abandona mision?
- al comienzo del juego solicitar un nombre.

"""