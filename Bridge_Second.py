import socket
import time
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9199
host1="Tower.VANET-Project.ch-geni-net.instageni.clemson.edu"
port1=9919
host2="Car-1.VANET-Final.ch-geni-net.instageni.clemson.edu"
port2=9999
total=0.000
num=0
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
    micro_data = clientsocket.recv(1024)
    # add 5 to the data
    result1 = int(micro_data.decode('utf-8')) + 5
    # send the result back to the client
    message1 = str(result1).encode('utf-8')
    clientsocket.sendall(message1)

    macro_data = clientsocket.recv(1024)
    # add 7 to the data
    result2 = int(macro_data.decode('utf-8')) + 7
    # send the result back to the client
    message2 = str(result2).encode('utf-8')
    clientsocket.sendall(message2)

    time1 = clientsocket.recv(1024)
    time1 = time1.decode('utf-8')
    print(time1)
    total=float(time1)+total
    num=num+1
    clientsocket.close()

    Bridgesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Bridgesocket.connect((host2,port2))

    # close the client socket