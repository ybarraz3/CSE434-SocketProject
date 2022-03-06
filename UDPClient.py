from pickle import TRUE
import socket
import random

ClientSocket = socket.socket()
host = '10.120.70.106'
port = 16001
inGame = 0 #0 for not in game, 1 for player, 2 for dealer
cards = []
visibleCards = 2
stock = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
random.shuffle(stock)
discard = []

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

ans = 'open'

Response = ClientSocket.recv(1024)
while ans != 'exit':
    ans = input('\nEnter a command:')
    #will check if any of the commands were used
    if ans == 'query games' or ans == 'query players':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    elif ans[0:12] == 'de-register ':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
        ClientSocket.close()
    elif ans[0:9] =='register ':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    elif ans[0:4] == 'end ':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    elif ans[0:11] == 'start game ':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    elif inGame == 1:#player
        print('Welcome to game')
        while inGame == 1 and ans != 'exit':
            ans = input('\nEnter either stock, steal <name>, or discard:')
            if ans == 'stock':
                #take card from stock


                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans == 'discard':
                #take card from discard


                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans[0:5] == 'steal ':
                #steal card from another player, only steal face down card


                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans == 'exit':
                inGame == 0
                ClientSocket.send(str.encode('game interupted'))
    elif inGame == 2:#dealer
        while inGame == 2 and ans != 'exit':
            if ans == 'stock':
                #take card from stock



                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans == 'discard':
                #take card from discard



                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans[0:5] == 'steal ':
                #steal card from another player, only steal face down card



                ClientSocket.send(str.encode(ans))
                Response = ClientSocket.recv(1024)
            elif ans == 'exit':
                inGame == 0
                ClientSocket.send(str.encode('game interupted'))
        
    elif ans != 'exit':
        print('not a valid command try again')

ClientSocket.close()