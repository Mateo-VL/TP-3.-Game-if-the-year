import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
import src.templates.oop.player as player
import msvcrt

DUNGEON = mapa.Dungeon(25, 80)   #pedir parametros para ver longitud y ver que no pase limites
MATEO = human.Human('Mateo', DUNGEON.find_free_tile())


#GNOME= player.Gnome(DUNGEON.find_free_tile())
rows= DUNGEON.rows
columns= DUNGEON.columns
capo = True 
DUNGEON.render(MATEO)  #sumar arg gnomo
while capo:
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
    
    DUNGEON.render(MATEO)







