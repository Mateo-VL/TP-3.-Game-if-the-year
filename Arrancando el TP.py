import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions



NIVEL = mapa.Level(25, 80)
MATEO = human.Human('Mateo', NIVEL.find_free_tile())
NIVEL.render(MATEO)
actions.move_up(NIVEL, MATEO)
NIVEL.render(MATEO)






