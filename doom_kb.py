import keyboard
import time
import os


def run_doom():
    print("Launching Doom!")
    os.system("./ftp.sh")
    time.sleep(1)


keyboard.add_hotkey('ctrl+shift+k', run_doom)

while True:
    time.sleep(9999999)
