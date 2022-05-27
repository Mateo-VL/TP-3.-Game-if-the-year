'''import keyboard
capo = True
while capo:
    if keyboard.read_key() == "p":
        print("You pressed p")
    if keyboard.read_key() == 'q':
        capo = False
    

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
        
keyboard.on_press_key("r", lambda _:print("You pressed r"))'''

import msvcrt
key = msvcrt.getch()
print (key)