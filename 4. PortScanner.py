import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input('Enter IP to scan: ')
port = int(input('Enter port: '))

def portScanner(host, port):
    if s.connect_ex((host, port)):
        print('The port is closed')
    else:
        print('The port is open')

portScanner(host, port)