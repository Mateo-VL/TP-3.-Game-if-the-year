import src.templates.oop.mapping as mapa
import src.templates.oop.human as human 
import src.templates.oop.player as player
BRYAN = human.Human('Bryan', (0,0))  #modulo.clase(argumentos)

def printface():
    print(BRYAN.get_face()) #se fija si objeto tiene funcion en clase llamada getface

printface()




def f():
    print(BRYAN.alive)  #no hay q poner self. ya accede a atributo de human
f()

a= mapa.Level(20,40)
def mostrar():
    print(a.render)

mostrar()  

MAPA= mapa.Level(35,70)

def mostr():
    MAPA.render(BRYAN)
mostr()

if (j, i) == player.loc():
                    print(player.face, end='')