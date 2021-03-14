import socket
from socket import AF_INET, SOCK_STREAM

clientSocket = socket.socket(AF_INET, SOCK_STREAM)
srv_addr = ("127.0.0.1", 12345)

print("[Client INFO] connect to {}".format(srv_addr))
clientSocket.connect(srv_addr)

message = bytes(input("Input lowercase message> "), encoding="utf-8")
clientSocket.send(message)

modifiedMessage = clientSocket.recv(1024).decode("utf-8")
print("[Client INFO] recv: '{}'".format(modifiedMessage))
clientSocket.close()
 
