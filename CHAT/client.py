import socket
from tkinter import *
import threading

def send():
    message = entry.get()
    listbox.insert('end', "Client: " + message)
    entry.delete(0, END)
    s.send(bytes(message, "utf-8"))

def receive():
    while True:
        try:
            message = s.recv(50)
            if not message:
                break
            listbox.insert('end', "Server: " + message.decode('utf-8'))
        except:
            break

# GUI setup
root = Tk()
root.title("Chat Client")

entry = Entry(root)
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

send_button = Button(root, text="Send", command=send)
send_button.pack(side=BOTTOM)

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.connect((HOST_NAME, PORT))

# Start thread for receiving messages
receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

root.mainloop()
