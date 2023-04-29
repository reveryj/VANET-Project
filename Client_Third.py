import socket
import time
# create a socket object
start_time1 = time.time()
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = "Car-1.VANET-Project.ch-geni-net.instageni.clemson.edu"

port = 9199

# connect to the server
clientsocket.connect((host, port))

# send data to the server
micro_data = 10
message1 = str(micro_data).encode('utf-8')
clientsocket.sendall(message1)


# receive data from the server
micro_data = clientsocket.recv(1024)
result1 = int(micro_data.decode('utf-8'))
print("Result1: {}".format(result1))
macro_data = 5
message2 = str(macro_data).encode('utf-8')
clientsocket.sendall(message2)


# receive data from the server
macro_data = clientsocket.recv(1024)
result2 = int(macro_data.decode('utf-8'))
print("Result2: {}".format(result2))
end_time1 = time.time()
elapsed_time1=end_time1 -start_time1
elapsed_time1=elapsed_time1*1000
x=round(elapsed_time1,3)
print("Elapsed time: ", x, " ms")
micro_data = 10
x = str(x).encode('utf-8')
clientsocket.sendall(x)

# close the client socket
clientsocket.close()