import socket
import datetime
import threading

serverSide = socket.socket()
date_now = datetime.datetime.now()

print("Server now up and Running")

port = 2010
serverSide.bind(("127.0.0.1", port))
print(f"Server running on port: {port}")
serverSide.listen(5)
print("Waiting for Client Connections.....")

clients = []
nick_names = []

def broadcasting(message):
    for client in clients:
        client.send(message)

def client_handler(client):
    while True:
        try:
            message = client.recv(1024)
            broadcasting(message)
        except:
            pointer1 = clients.index(client)
            clients.remove(client)
            client.close()
            nick_name = nick_names[pointer1]
            broadcasting(f" {nick_name} has left the chat".encode("utf-8"))
            nick_names.remove(nick_name)
            break

def recieveConnz():
    while True:
        client, addre = serverSide.accept()
        print(f"{str(addre)} has Connected at {date_now}")
        client.send("nick_names?".encode("utf-8"))
        nick_name = client.recv(1024)
        nick_names.append(nick_name)
        clients.append(client)
        print(f"The NIckname for this Client is {nick_name}")
        broadcasting(f" {nick_name} has joined the ChatRoom".encode("utf-8"))
        message = "Connection Successful"
        client.send(message.encode("utf-8"))
        client.close()
        thread = threading.Thread(target = client_handler, args= (client,))
        thread.start()
