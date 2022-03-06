from pickle import TRUE
import socket
import random

ClientSocket = socket.socket()
host = '10.120.70.106'
port = 16001
inGame = 0 #0 for not in game, 1 for player, 2 for dealer
cards = []
visibleCards = 2
stock = ['A D','2 D','3 D','4 D','5 D','6 D','7 D','8 D','9 D','10 D','J D','Q D','K D',
    'A H','2 H','3 H','4 H','5 H','6 H','7 H','8 H','9 H','10 H','J H','Q H','K H',
    'A S','2 S','3 S','4 S','5 S','6 S','7 S','8 S','9 S','10 S','J S','Q S','K S',
    'A C','2 C','3 C','4 C','5 C','6 C','7 C','8 C','9 C','10 C','J C','Q C','K C']
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
        while inGame == 1:
            
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