import msvcrt
import src.templates.oop.actions as actions
key= msvcrt.getch().decode("UTF-8")

def hola():
    while True:
        pressedKey= msvcrt.getch()
        if pressedKey == "w":
            actions.move_to()

