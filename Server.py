import socket
#import os
from _thread import *

def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server\n'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    print('Connection Closed')
    connection.close()

ServerSocket = socket.socket()
host = '192.168.1.150'
port = 5556
ThreadCount = 0

try:
    ServerSocket.bind((host, port))
    print('Waiting for a Connection..')
    ServerSocket.listen(5)

    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSocket.close()

except socket.error as e:
    print(str(e))
