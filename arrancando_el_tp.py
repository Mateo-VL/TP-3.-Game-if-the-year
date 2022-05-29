import src.templates.oop.mapping as mapa
import src.templates.oop.human as human
import src.templates.oop.actions as actions
import src.templates.oop.player as player
import src.templates.oop.items as items

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

elif (j,i)== sword.loc():
                    print(sword.face, end='')
                elif (j,i)== amulet.loc():
                    print(amulet.face, end='')
                elif (j,i)== pickaxe.loc():
                    print(pickaxe.face, end='')
'''
 
SWORD= items.Sword("Sword", "/", 10, 20, NIVEL.find_free_tile())

AMULET= items.Amulet("Amulet", "''", NIVEL.find_free_tile())

PICKAXE= items.PickAxe("Pickaxe", "(", NIVEL.find_free_tile())
print(type(PICKAXE))
import msvcrt
#GNOME= player.Gnome(NIVEL.find_free_tile())
rows= NIVEL.rows
columns= NIVEL.columns
capo = True 
#NIVEL.render(MATEO)  #sumar arg gnomo
#NIVEL.render(MATEO)
NIVEL.add_item(PICKAXE, PICKAXE.loc())   #ya imprime mapa
NIVEL.add_item(SWORD, SWORD.loc())
NIVEL.add_item(AMULET, AMULET.loc())
NIVEL.render(MATEO)
while capo:  #MATEO.alive?
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
    
    if MATEO.loc() in NIVEL.items:
     
        #if MATEO.loc() in NIVEL.items: #diccionario donde claves son ubic de items
        list_items= NIVEL.items[MATEO.loc()]
        MATEO.take_object(list_items)
    if MATEO.loc()== PICKAXE.loc():
        MATEO.tool= True
    NIVEL.get_items(MATEO.loc()) 
    NIVEL.dig(MATEO.loc())
    NIVEL.render(MATEO)
        #MATEO.take_tool()

            
#el dig reemp paredes x espacio

#capo=Fals

"""
if NIVEL.is_walkable== False and player.tool== True:
    NIVEL.dig(player.x, player.y)
    MATEO.take_tool()
if NIVEL.is_walkable== False and player.tool== True:
    NIVEL.dig(player.x, player.y)
"""





