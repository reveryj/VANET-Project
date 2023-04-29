import socket
import time
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9991
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
    total=0.000
    clientsocket, addr = serversocket.accept()

    print("Got a connection from {}".format(addr))

    # receive data from the client
    micro_data = clientsocket.recv(1024)
    # add 5 to the data
    result1 = int(micro_data.decode('utf-8'))
    # send the result back to the client
    message1 = str(result1).encode('utf-8')
    clientsocket.sendall(message1)

    macro_data = clientsocket.recv(1024)
    # add 7 to the data
    result2 = int(macro_data.decode('utf-8'))
    # send the result back to the client
    message2 = str(result2).encode('utf-8')
    clientsocket.sendall(message2)

    time1 = clientsocket.recv(1024)
    time1 = time1.decode('utf-8')
    print(time1)
    total=float(time1)+total
    clientsocket.close()
    start_time1=time.time()
    Bridgesocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Bridgesocket.connect((host2,port2))

    # send data to the server
    micro_data1 = 10
    message3 = str(micro_data1).encode('utf-8')
    Bridgesocket.sendall(message3)


    # receive data from the server
    micro_data1 = Bridgesocket.recv(1024)
    result4 = int(micro_data1.decode('utf-8'))
    print("Result1: {}".format(result1))
    macro_data1 = 5
    message4 = str(macro_data1).encode('utf-8')
    Bridgesocket.sendall(message2)


    # receive data from the server
    macro_data1 = Bridgesocket.recv(1024)
    result2 = int(macro_data1.decode('utf-8'))
    print("Result2: {}".format(result2))
    end_time1 = time.time()
    elapsed_time1=end_time1 -start_time1
    elapsed_time1=elapsed_time1*1000
    x=round(elapsed_time1,3)
    print("Elapsed time: ", x, " ms")
    total=float(x)+total
    total = str(total).encode('utf-8')
    Bridgesocket.sendall(total)

    # close the client socket
    Bridgesocket.close()