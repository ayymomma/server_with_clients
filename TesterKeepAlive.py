import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 50100        # The port used by the server

reply = 'KeepAlive'
StateTracker = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(reply.encode())
        print('Send ', reply)
        time.sleep(1)
		