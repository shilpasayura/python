import socket
import time

addr     = "127.0.0.1"
port   = 20001
bufferSize  = 1024
# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((addr, port))
print("UDP server up and listening")
# Listen for incoming datagrams
ctr=0;
while(True):
    t=time.ctime(time.time())
    msgFromServer       = "Hello UDP Client : " + str(t) 
    bytesToSend         = str.encode(msgFromServer)
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
