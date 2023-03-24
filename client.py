import socket

# create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connect to the server
clientsocket.connect((host, port))

# send data to the server
data = 10
message = str(data).encode('utf-8')
clientsocket.sendall(message)

# receive data from the server
data = clientsocket.recv(1024)
result = int(data.decode('utf-8'))

print("Result: {}".format(result))

# close the client socket
clientsocket.close()