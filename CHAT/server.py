import socket
from tkinter import *
import threading

def send():
    message = entry.get()
    listbox.insert('end', "Server: " + message)
    entry.delete(0, END)
    client.send(bytes(message, "utf-8"))

def receive():
    while True:
        try:
            message_from_client = client.recv(50)
            if not message_from_client:
                break
            listbox.insert('end', "Client: " + message_from_client.decode('utf-8'))
        except:
            break

# Set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(1)
print("Server is waiting for connection...")
client, address = s.accept()
print(f"Connected to {address}")

# GUI setup
root = Tk()
root.title("Chat Server")

entry = Entry(root)
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

send_button = Button(root, text="Send", command=send)
send_button.pack(side=BOTTOM)

# Start thread for receiving messages
receive_thread = threading.Thread(target=receive, daemon=True)
receive_thread.start()

root.mainloop()
