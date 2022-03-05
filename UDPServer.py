import socket
import os
from socket import* 
from _thread import *

ServerSocket = socket.socket()
host = '10.120.70.106'
port = 16001
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
            player = decodeddata.split(' ')
            player.remove('register')
            player.append('0') # this number will represent 1 if in game 2 if dealer and 0 if not in game
            
            if player[2] in players:
               reply = 'FAILURE'
            elif player[0] in players:
               reply = 'FAILURE'
            else:
               players.append(player)
               reply = 'SUCCESS'
        elif decodeddata[0:12] == 'de-register ':#checks if command used was de-register
            reply = 'FAILURE'
            initialLength = len(players)
            players = [i for i in players if i[0] != decodeddata[12:]]
            resultLength = len(players)
            if initialLength != resultLength:
                reply = 'SUCCESS'
            break
        elif decodeddata[0:4] == 'end ':#checks if command used was end game
            reply = 'FAILURE'
            initialLength = len(games)
            games = [i for i in games if i[0] != decodeddata[12:]]
            if initialLength != len(games):
                reply = 'SUCCESS'
        elif decodeddata[0:11] == 'start game':
            reply = 'FAILURE'

            game = decodeddata.split(' ')
            game.remove('start')
            game.remove('game')
            gameStart = False

            if 1<= game[1] <= 3:
                if game[0] in players:# check if user is in player
                    j = 0
                    for i in players:#check if there are sufficient players available
                        if i[3] == 0:
                            j = j + 1
                        if i[0] == game[0]:
                            gameStart = True
                    
                    if j >= game[1]:
                        if gameStart == True: #start a new thread and begin game
                            games.append(game)
                            reply = 'SUCESS'

        else:
            reply = 'error'
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ServerSocket.close()