import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999
time =0.000
# bind the socket to a public host, and a port
serversocket.bind((host, port))

# become a server socket
serversocket.listen(1)

print('Server listening on {}:{}'.format(host, port))

while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from {}".format(addr))

    # receive data from the client

    x = clientsocket.recv(1024)
    x = x.decode('utf-8')
    print(x)
    time = time+float(x)
    print(time)
    # close the client socket
    clientsocket.close()