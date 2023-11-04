# Ask user for string, send to server, receive reply, print reply, then exit on blank line
import socket
from socket import *


def main():
    # set up socket and connect to localhost on port 9000
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(("localhost", 9000))

    user_input = input("Input a string to be sent: ").encode()
    s.send(user_input)

    # Receive up to the length of the user input
    data, address = s.recv(len(user_input))
    print("Received", data.decode())
    s.close()


if __name__ == "__main__":
    main()
