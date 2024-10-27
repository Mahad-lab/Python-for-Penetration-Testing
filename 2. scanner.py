# pip install python-nmap
# apt install namp

import nmap

scanner = nmap.PortScanner()

def syn_ack_scan(ip_address):
    print(f'namp version: {scanner.nmap_version()}')
    scanner.scan(ip_address, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open ports: ', scanner[ip_address]['tcp'].keys())

def udp_scan(ip_address):
    print(f'namp version: {scanner.nmap_version()}')
    scanner.scan(ip_address, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open ports: ', scanner[ip_address]['udp'].keys())


def comp_scan(ip_address):
    print(f'namp version: {scanner.nmap_version()}')
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O') # -O or -0
    print(scanner.scaninfo())
    print('IP status: ', scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print('Open ports: ', scanner[ip_address]['tcp'].keys())


def main():
    print("Welcome to a simple nmap automation tool")
    print("<"+ ("-"*40) +">")

    ip_address = input("Enter IP Address to scan: ")

    resp = input("""\n Enter the type of scan \n
1) SYN ACK scan
2) UDP scan
3) Comprehensive scan
""")

    if resp == '1':
        syn_ack_scan(ip_address=ip_address)
    elif resp == '2':
        udp_scan(ip_address=ip_address)
    elif resp == '3':
        comp_scan(ip_address=ip_address)
    else:
        print('invalid option selected')

if __name__ == '__main__':
    main()