import msvcrt
import actions as actions
key= msvcrt.getch().decode("UTF-8")

def hola():
    while True:
        pressedKey= msvcrt.getch()
        if pressedKey == "w":
            print("w")
           # actions.move_up()
        if pressedKey == "s":
            print("s")
            #actions.move_down()
        if pressedKey == "d":
            print("d")
            #actions.move_right()
        if pressedKey == "a":
            print("a")
            #actions.move_left()


