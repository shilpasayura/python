import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" # server address
port =12345 #server port
ctr=0
max=10
print("Client Connecting to ", host, port)
s.connect((host, port))
print(s.recv(1024))
print("Sending Messages")
while (ctr < max):
    time.sleep(2)# 2 seconds   
    ctr=ctr + 1
    msg="Hello Server " + str(ctr)
    print(msg)
    s.send(msg.encode())
    print(s.recv(1024))
   
msg=""
s.send(msg.encode())
s.close()
print("Sending Finished : Connection Closed")



