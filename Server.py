import socket
from _thread import *
import time
import random
import sys


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 50100        # Port to listen on (non-privileged ports are > 1023)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((HOST, PORT))
serversocket.listen(5)

contor = 0
reply = 'Acces Denied. Server not alive'
accept = True

def cnt():  
    global contor
    global accept
    while True:
        if contor == 0:
            accept = True
        time.sleep(1)
        contor += 1
        if contor > 5:
            accept = False



def fun(clientsocket, address):
    global contor
    global accept
    print('Connected by', address)

    while True:
        try:
            data = clientsocket.recv(1024)
            if not data:
                break       

            if data.decode() == 'KeepAlive':
                contor = 0
                accept = True

            if accept == True:
                print('Received', repr(data))

                if data.decode() == 'cmd1':
                    text = str(random.randrange(10,100))
                    clientsocket.sendall(text.encode())
                elif data.decode() == 'cmd2':
                    f = open("file.txt", "r")
                    string = f.read()
                    text = string.split(" ")[0]
                    clientsocket.sendall(text.encode())
                else:
                    text = 'Unknown command!'
                    clientsocket.sendall(text.encode())
            else:
                clientsocket.sendall(reply.encode())
        except:
            print('Disconnected!')
            # print(sys.exc_info()[0])
            return
    clientsocket.close()
    print('S-a terminat comunicarea cu ', address)




start_new_thread(cnt,())
while True:
    print ('#########################################################################')
    print ('Serverul asculta potentiali clienti.')
    print ('#########################################################################')

    (conn, addr) = serversocket.accept()
    start_new_thread(fun, (conn, addr))
