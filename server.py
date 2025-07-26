# server.py

import socket
import threading

# Server config
HOST = '127.0.0.1'
PORT = 12345

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

# Broadcast messages to all clients
def broadcast(msg):
    for client in clients:
        client.send(msg)

# Handle each client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chat.".encode('utf-8'))
            usernames.remove(username)
            break

# Accept new connections
def receive():
    print(f"Server started on {HOST}:{PORT}")
    while True:
        client, addr = server.accept()
        print(f"Connected with {addr}")
        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)

        print(f"Username: {username}")
        broadcast(f"{username} joined the chat!".encode('utf-8'))
        client.send("Connected to chat server!".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive()
