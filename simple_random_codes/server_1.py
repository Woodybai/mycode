import socket
from socket import AF_INET, SOCK_STREAM

serverSocket = socket.socket(AF_INET, SOCK_STREAM)
srv_addr = ("127.0.0.1", 8888)
serverSocket.bind(srv_addr)
serverSocket.listen()

print("[Server INFO] listening...")
while True:
    conn, cli_addr = serverSocket.accept()
    print("[Server INFO] connection from {}".format(cli_addr))
    message = conn.recv(1024)
    conn.send(message.upper())
    conn.close()
 
