# Using the same circuit from assignment 3 (shown below for reference), create a server on port 9000 (NOT a web server)
# that listens for data from a GUI application to control the lights.
# In this case, since you're sending commands, you will need to have a button to send the data to the server.
# Control the colors of the LED like before, toggle the LED, blink the LED (make it blink five times, returning it to
# its previous state before you started blinking. This is actually the easier way to do it.)
# Don't worry about the "Door" button.
# Send the data in whatever format you want, but do not use an HTML server this time.


class Application:
    def __init__(self):
        print(self)


app = Application()


def main():
    print("Hello world")


if __name__ == '__main__':
    main()
