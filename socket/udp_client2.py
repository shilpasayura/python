import socket
import time

addr="127.0.0.1"
port=20001
bufferSize          = 1024
# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Send to server using created UDP socket
ctr=0
while (ctr < 10):
    ctr=ctr+1
    msgFromClient       = "Hello UDP Server " + str(ctr)
    bytesToSend         = str.encode(msgFromClient)

    UDPClientSocket.sendto(bytesToSend, (addr, port))
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    time.sleep(2)

print("Transmission End")
UDPClientSocket.close()

