import src.templates.oop.mapping as mapa
import src.templates.oop.human as human



NIVEL = mapa.Level(25, 80)
MATEO = human.Human('Mateo', NIVEL.find_free_tile())
NIVEL.render(MATEO)






