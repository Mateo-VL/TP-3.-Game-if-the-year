import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
import keyboard



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
NIVEL = mapa.Level(25, 80)
MATEO = human.Human('Mateo', NIVEL.find_free_tile())
capo = True
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






