import socket
sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockets.bind((socket.gethostname(), 1234))
sockets.listen(5)
while True: # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = sockets.accept() 
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!爱","utf-8"))
    clientsocket.close()
