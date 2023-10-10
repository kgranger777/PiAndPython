# File: isLeapYear.py
# Description: Repeatedly takes integer input and determines if the number is a leap year
# Inputs: An integer value
# Output: A string telling the user if the year entered is a leap year
# Limitations: Only handles integer years, returns program when non-integer is entered

def isLeapYear():
    while True:
        year = input("Enter a year: ")
        try:
            year = int(year)
        except ValueError:
            print("Non-integer entered")
            return

        if compute(year):
            print("Yes, that's a leap year")
        else:
            print("Not a leap year")


def compute(year):
    # A year is a leap year if divisible by 4, except if divisible by 100, except if divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True


if __name__ == '__main__':
    isLeapYear()
    print("Exiting program")
