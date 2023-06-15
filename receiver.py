import socket
import sys

if len(sys.argv) == 3:
    # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (ip, port)
s.bind(server_address)

while True:
    print("Server is listening....")
    data, address = s.recvfrom(4096)
    print("\nServer received: ", data.decode('utf-8'), "\n")
    send_data = input("Type message => ")
    s.sendto(send_data.encode('utf-8'), address)
    print("\nServer sent : ", send_data,"\n")