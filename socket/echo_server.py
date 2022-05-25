import socket

host = "127.0.0.1"  # Standard loopback interface address (localhost)
port = 12345  # Port to listen on (non-privileged ports are > 1023)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) #bind server
s.listen(2)
print("Server Listening at", host, port)
ctr=0
connected=0
while True:
    if connected==0:
        conn, addr = s.accept()
        print(addr, "Now Connected")
        msg="You are Connected"
        conn.send(msg.encode())
        connected=1
    else:
        data = conn.recv(1024)
        if not data:
            break
            #conn.sendall(data)
        else:
            ctr=ctr + 1
            msg="Message  " + str(ctr) + " Received"
            conn.send(msg.encode())
            print(data)

connected=0
print("Dis connected")
conn.close()

