import src.templates.oop.mapping as mapa

import src.templates.oop.mapping as mapa
import src.templates.oop.human as human



DUNGEON = mapa.Dungeon(25, 80)
MATEO = human.Human('Mateo', DUNGEON.find_free_tile())
DUNGEON.render(MATEO)




