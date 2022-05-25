import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1" # server address
port =12345 #server port
print("Client Connecting to ", host, port)
s.connect((host, port))
print(s.recv(1024))
'''
msg="Hello Server"
s.send(msg.encode())
'''
s.close()
