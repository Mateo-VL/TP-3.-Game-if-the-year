import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
import src.templates.oop.player as player


'''NIVEL = mapa.Level(25, 80)
MATEO = human.Human('Mateo', NIVEL.find_free_tile())
NIVEL.render(MATEO)
actions.move_up(NIVEL, MATEO)
NIVEL.render(MATEO)
actions.move_down(NIVEL, MATEO)
NIVEL.render(MATEO)
actions.move_left(NIVEL, MATEO)
NIVEL.render(MATEO)
actions.move_right(NIVEL, MATEO)
NIVEL.render(MATEO)'''
NIVEL = mapa.Level(25, 80)   #pedir parametros para ver longitud y ver que no pase limites
MATEO = human.Human('Mateo', NIVEL.find_free_tile())
'''capo = True
while capo:
    if keyboard.read_key() == "w":
        actions.move_up(NIVEL, MATEO)
    if keyboard.read_key() == "a":
        actions.move_left(NIVEL, MATEO)
    if keyboard.read_key() == "s":
        actions.move_down(NIVEL, MATEO)
    if keyboard.read_key() == "d":
        actions.move_right(NIVEL, MATEO)
    if keyboard.read_key() == "e":
        capo = False
    NIVEL.render(MATEO)
'''
import msvcrt
#GNOME= player.Gnome(NIVEL.find_free_tile())
rows= NIVEL.rows
columns= NIVEL.columns
capo = True 
NIVEL.render(MATEO)  #smar arg gnomo
while capo:
    key = msvcrt.getch()
    if key == b'w':
        actions.move_up(NIVEL, MATEO)
    elif key == b'a':
        actions.move_left(NIVEL, MATEO)
    elif key == b's':
        actions.move_down(NIVEL, MATEO, rows)  #recibe cant filas
    elif key == b'd':
        actions.move_right(NIVEL, MATEO, columns)  #recibe cant columnas
    else:
        capo = False
    NIVEL.render(MATEO)

 


