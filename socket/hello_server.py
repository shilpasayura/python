import socket

host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 12345  # Port to listen on (non-privileged ports are > 1023)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #bind server
s.listen(2)
print("Server Listening at", host, port)
conn, addr = s.accept()

print(addr, "Now Connected")
msg="Thank you for connecting"
conn.send(msg.encode())
conn.close()

'''
while True:
    data = conn.recv(1024)
    if not data:
        break
        conn.sendall(data)
    else:
        print(data)

print("Dis connecting")
conn.close()
'''
