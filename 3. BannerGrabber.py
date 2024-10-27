import socket


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, port))
    print(s.recv(1024))

def main():
    ip = input('Please enter the ip: ')
    port = int(input('Please enter the port: '))
    banner(ip, port)

if __name__ == '__main__':
    main()
