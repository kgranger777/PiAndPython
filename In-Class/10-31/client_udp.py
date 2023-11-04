# Ask user for string, send to server, receive reply, print reply, then exit
import socket
from socket import *


def main():
    # set up socket and connect to localhost on port 9000
    s = socket(AF_INET, SOCK_DGRAM)

    user_input = input("Input a string to be sent: ").encode()
    s.sendto(user_input, ("localhost", 9000))

    # Receive up to the length of the user input
    data, address = s.recvfrom(len(user_input))
    print("Received", data.decode())
    s.close()


if __name__ == "__main__":
    main()
