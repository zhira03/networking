import threading
import socket

nick_name = input("Enter your username:: ")
port = 2010

clientSide = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSide.connect(("127.0.0.1", port))

def client_recv():
    while True:
        try:
            mssge = clientSide.recv(1024).decode("utf-8")
            if mssge == " nick_name?":
                clientSide.send(nick_name.encode("utf-8"))
            else:
                print(mssge)
        except:
            print("Connection Error!")
            clientSide.close()
            break

def client_send():
    while True:
        textToSend = input("")
        mssge = (f"{nick_name} : {textToSend}")
        clientSide.send(mssge.encode("utf-8"))


recvngThread = threading.Thread(target=client_recv)
recvngThread.start()

sendingThread = threading.Thread(target= client_send)
sendingThread.start()

