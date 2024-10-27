import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print(f"Recieved connection from {address}")

    message = "Thank you for connecting to the server" + "\r\n"
    clientsocket.send(message.encode('ascii'))
    print("message sent")

    clientsocket.close()
