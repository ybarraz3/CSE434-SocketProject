import socket

ClientSocket = socket.socket()
host = '10.120.70.106'
port = 1233

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
    elif ans[0:9] =='register ':
        ClientSocket.send(str.encode(ans))
        Response = ClientSocket.recv(1024)
        print(Response.decode('utf-8'))
    elif ans != 'exit':
        print('not a valid command try again')

ClientSocket.close()