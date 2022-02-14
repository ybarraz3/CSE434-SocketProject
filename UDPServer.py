import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '10.120.70.106'
port = 1233
players = []
games = []

try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server!'))
    while True:
        data = connection.recv(2048)
        decodeddata = data.decode('utf-8')
        reply = 'Server Says: ' + data.decode('utf-8')
        if decodeddata == 'query games':#checks if command used was query games
            if games:
                reply = str(len(games)) + '\n' #the ammount of players
                reply += str(games)#returns list
            else:
                reply = '0\n[]'#no games
        elif decodeddata == 'query players':#checks if command used was query players
            global players
            if players:
                reply = str(len(players)) + '\n' #the ammount of players
                reply += str(players)#returns list
            else:
                reply = '0\n[]'#no players
        elif decodeddata[0:9] == 'register ':#checks if command used was register
            reply = 'FAILURE'
            
            player = decodeddata.split(' ')
            player.remove('register')

            players.append(player)
            reply = 'SUCCESS'
        elif decodeddata[0:12] == 'de-register ':#checks if command used was de-register
            reply = 'FAILURE'
            initialLength = len(players)
            players = [i for i in players if i[0] != decodeddata[12:]]
            resultLength = len(players)
            if initialLength != resultLength:
                reply = 'SUCCESS'
        else:
            reply = 'error'
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))

ServerSocket.close()