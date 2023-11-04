# Receive a connection, take the string, reverse it, and send it back
import socket
from socket import *


def main():
    # set up socket and connect to localhost on port 9000
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(("localhost", 9000))
    s.listen(10000)
    sock_connect, addr = s.accept()

    while(True):
        # Receive up to 10k bytes
        data = sock_connect.recv(10000)
        print("Received", data.decode())

        # Reverse data and send back to address
        reversed_data = data.decode()[::-1]
        print("Sending", reversed_data)
        sock_connect.send(reversed_data.encode(), addr)


if __name__ == "__main__":
    main()
