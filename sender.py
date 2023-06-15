import socket
import sys

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

while True:
    send_data = input("Type message =>")
    s.sendto(send_data.encode('utf-8'), (ip, port))
    print("\nClient Sent : ", send_data, "\n")
    data, address = s.recvfrom(4096)
    print("\nClient received: ", data.decode('utf-8'), "\n")
s.close()