# client.py

import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Choose a username
username = input("Enter your username: ")

def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            if msg == "USERNAME":
                client.send(username.encode('utf-8'))
            else:
                print(msg)
        except:
            print("An error occurred. Connection closed.")
            client.close()
            break

def send_messages():
    while True:
        message = f"{username}: {input()}"
        client.send(message.encode('utf-8'))

# Start threads
recv_thread = threading.Thread(target=receive_messages)
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
