import socket
import time
# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999
host1="Tower.VANET-Project.ch-geni-net.instageni.clemson.edu"
port1=9919
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
    if num>= 5:
        start_time= time.time()
        clientsocketq = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocketq.connect((host1,port1))
        end_time= time.time()
        elapsed_time1=end_time-start_time
        elapsed_time1=elapsed_time1*1000
        x=round(elapsed_time1,3)
        total=total+x
        total = str(total).encode('utf-8')
        clientsocketq.sendall(total)

    # close the client socket