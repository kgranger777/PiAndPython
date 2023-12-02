#########
# Name: Kenneth Granger
# Assignment: Programming Assignment 04
# File: granger04.py
# Purpose: Python 3 code sets up GUI and TCP server to change colors of an LED via PWM. The color data is input via
# the GUI and sent to the server by pressing a hardware button.
#
#           NOTE: Works with COMMON ANODE LED (Positive long lead)
#
# Development Computer: Raspberry Pi 4B ARM-v8 64-bit 8GB
# Operating System: Raspbian (Debian) Linux 11 "Bullseye"
# Environment: Python 3.9.2
# IDE: Sublime Text
# Operational status: TODO UPDATE STATUS
#########

# Using the same circuit from assignment 3 (shown below for reference), create a server on port 9000 (NOT a web server)
# that listens for data from a GUI application to control the lights.
# In this case, since you're sending commands, you will need to have a button to send the data to the server.
# Control the colors of the LED like before, toggle the LED, blink the LED (make it blink five times, returning it to
# its previous state before you started blinking. This is actually the easier way to do it.)
# Don't worry about the "Door" button.
# Send the data in whatever format you want, but do not use an HTML server this time.
from socket import *
from threading import Thread
from time import sleep


class Server(Thread):
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        # Buffer size defined as 10k bytes
        self.buffer = 10000
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((self.addr, self.port))
        # Run thread initialization
        Thread.__init__(self)

    def run(self):
        # Backlog size defined as 10k
        self.socket.listen(10000)
        while True:
            client_connection, client_addr = self.socket.accept()
            print("Connected to", str(client_addr[0]) + ":" + str(client_addr[1]))

            data = client_connection.recv(10000)
            print("Server: Received", data.decode())

            # TODO do some data processing here...
            #  Data should influence lights in some way.
            # NOTE client makes requests from the GUI

            # Test data sending:
            send_data = data.decode()[::-1]
            print("Server: Sending", send_data)
            client_connection.send(send_data.encode())

            # TODO if some data value received indicating user wants to quit, close sockets
            if data:
                print("Shutting down Server")
                client_connection.close()
                break
        self.socket.close()

    # Close socket when done
    def close(self):
        print("Shutting down Server")
        self.socket.close()


class Client(Thread):
    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        # Buffer size defined as 10k bytes
        self.buffer = 10000
        self.socket = socket(AF_INET, SOCK_STREAM)
        Thread.__init__(self)

    def run(self):
        self.socket.connect((self.addr, self.port))
        # user_input = input("Input a string to be sent")
        user_input = "This is a test string"
        # user_input.encode()

        print("Client: Sending", user_input.encode())
        self.socket.send(user_input.encode())

        # Receive 10k bytes
        data = self.socket.recv(10000)
        print("Client: Received", data.decode())
        sleep(10)
        self.close()

    # Close socket when done
    def close(self):
        print("Shutting down Client")
        self.socket.close()


#########
# class Application:
#     def __init__(self):
#         print(self)
# app = Application()


def main():
    # Change address and port here
    addr = "localhost"
    port = 9000
    th_server = Server(addr, port)
    th_client = Client(addr, port)

    th_server.start()
    th_client.start()

    th_server.join()
    th_client.join()


if __name__ == '__main__':
    main()
