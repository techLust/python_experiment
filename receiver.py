import socket

# ip = "192.168.1.50"
# port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 1234))

while True:
    print("Server is listening....")
    data, address = s.recvfrom(1024)
    print("\nServer received: ", data.decode('utf-8'), "\n")

