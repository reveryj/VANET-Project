import socket

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

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
    data = clientsocket.recv(1024)

    # add 5 to the data
    result = int(data.decode('utf-8')) + 5

    # send the result back to the client
    message = str(result).encode('utf-8')
    clientsocket.sendall(message)

    # close the client socket
    clientsocket.close()